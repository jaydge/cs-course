"""
Convert handouts/week-NN-homework.md files into Google Docs inside a
Drive folder, so sync_classroom.py can attach each one to students as
their own editable copy.

Only files under handouts/ are ever touched. Teacher guides under
lessons/ are never uploaded anywhere by this tool set; they are your
prep material, not student-facing.

Usage:
    python publish_handouts_to_docs.py --repo /path/to/cs-course \
        --folder-name "CS Course - Student Handouts"

    # Re-run any time a handout changes; existing Docs with the same
    # title are updated in place rather than duplicated.

Requires: pip install -r requirements.txt
"""

import argparse
import html as html_lib
import re
import sys
from pathlib import Path

from googleapiclient.http import MediaInMemoryUpload

from classroom_auth import get_docs_service, get_services

WEEK_FILE_RE = re.compile(r"week-(\d{2})-homework\.md$")

# Each "## " section renders as a two-column table: a checkbox column the
# student ticks off, and the content. Drive's HTML import keeps table cell
# background colors, which plain paragraphs cannot express, so tables are
# what give the handouts their vertical structure and color.
CHECKBOX_COL_WIDTH = "38px"   # import-time hint; the real width is set below
CHECKBOX_COL_PT = 32.0        # narrow column holding just the checkbox

# Page setup, applied through the Docs API after import. 1 inch = 72pt;
# the default 1" side margins waste width these handouts want.
PAGE_MARGIN_SIDE_PT = 43.2   # 0.6"
PAGE_MARGIN_VERT_PT = 54.0   # 0.75"

# Indents for the checkbox bullets, tightened so the box sits neatly in
# its narrow column instead of wrapping.
BULLET_INDENT_FIRST_PT = 0.0
BULLET_INDENT_START_PT = 18.0

# Course name used in the document's own title line.
COURSE_NAME = "Computer Science"

# Sections whose heading matches this get the "optional/bonus" palette
# instead of the default one, so the AP work reads as clearly separate.
EXTRA_CREDIT_RE = re.compile(r"extra credit|ap track", re.IGNORECASE)

# A line containing only this marker becomes blank writing space, for
# reflection prompts students answer on paper or by typing in their copy.
WRITING_SPACE_RE = re.compile(r"^\{\{\s*writing-space\s*\}\}$")
WRITING_SPACE_LINES = 6

# {{question: ...}} is addressed to sync_classroom.py, which turns it into
# a Classroom short-answer Question. It is not part of the handout text, so
# this tool skips it.
QUESTION_RE = re.compile(r"^\{\{\s*question:\s*(.+?)\s*\}\}$")

THEMES = {
    "default": {
        "border": "#b8cce4",
        "header_bg": "#dbe5f1",
        "header_fg": "#1f3864",
    },
    "extra": {
        "border": "#f0c992",
        "header_bg": "#fbe4cd",
        "header_fg": "#7f4f24",
    },
}

CALLOUT_BG = "#f4f4f4"
CALLOUT_BORDER = "#d0d0d0"
CODE_BG = "#f6f8fa"
GRID_BORDER = "#9aa0a6"
GRID_HEADER_BG = "#eef1f4"
BODY_FG = "#3c4043"
SPACER = '<p>&nbsp;</p>'


def _inline(text: str) -> str:
    """Escape HTML, then apply the inline markdown we actually use."""
    text = html_lib.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2" style="color:#1155cc;">\1</a>', text)
    return text


def _parse_blocks(md_text: str):
    """
    Turn markdown into a flat list of blocks. A "section" block collects the
    rows that belong under one "## " heading, which is what lets us render
    the whole section as a single table.
    """
    blocks = []
    section = None
    code_lines = None      # collecting a ``` fenced block
    table_rows = None      # collecting consecutive | pipe | rows

    def emit(row):
        if section is not None:
            section["rows"].append(row)
        else:
            blocks.append(row)

    def flush_table():
        nonlocal table_rows
        if table_rows:
            emit(("mdtable", table_rows))
            table_rows = None

    for raw in md_text.splitlines():
        line = raw.strip()

        # Inside a fence, keep the line verbatim. Indentation is the
        # meaning of the code in a Python course, so it must survive.
        if code_lines is not None:
            if line.startswith("```"):
                emit(("code", "\n".join(code_lines)))
                code_lines = None
            else:
                code_lines.append(raw.rstrip().expandtabs(4))
            continue

        if line.startswith("```"):
            flush_table()
            code_lines = []
            continue

        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            # The |---|---| separator carries no content.
            if not all(set(c) <= set("-: ") and c for c in cells):
                if table_rows is None:
                    table_rows = []
                table_rows.append(cells)
            continue
        flush_table()

        if not line:
            continue

        if line == "---":
            section = None
            continue

        if QUESTION_RE.match(line):
            continue

        if WRITING_SPACE_RE.match(line):
            if section is not None:
                section["rows"].append(("space", ""))
            else:
                blocks.append(("space", ""))
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level, text = len(heading.group(1)), heading.group(2)
            if level == 1:
                section = None
                blocks.append(("title", text))
            else:
                section = {"heading": text, "rows": []}
                blocks.append(("section", section))
            continue

        quote = re.match(r"^>\s?(.*)$", line)
        if quote:
            section = None
            if blocks and blocks[-1][0] == "callout":
                blocks[-1] = ("callout", blocks[-1][1] + " " + quote.group(1))
            else:
                blocks.append(("callout", quote.group(1)))
            continue

        item = re.match(r"^[-*]\s+(.*)$", line)
        if item:
            emit(("task", item.group(1)))
            continue

        # "1. ", "2. " ... are numbered questions to work through. They get
        # a checkbox like any other task, with the number kept so it can
        # still be referred to in class.
        numbered = re.match(r"^(\d+)\.\s+(.*)$", line)
        if numbered:
            emit(("task", f"{numbered.group(1)}. {numbered.group(2)}"))
            continue

        emit(("prose", line) if section is not None else ("paragraph", line))

    if code_lines:
        emit(("code", "\n".join(code_lines)))
    flush_table()

    return blocks


def _code_html(code_text: str) -> str:
    """
    Monospaced code with its indentation intact.

    Leading spaces become non-breaking spaces, because HTML collapses runs
    of whitespace and Python code without indentation is wrong code.
    """
    lines = []
    for raw in code_text.split("\n"):
        indent = len(raw) - len(raw.lstrip(" "))
        lines.append("&nbsp;" * indent + html_lib.escape(raw.lstrip(" "), quote=False))
    return (
        f'<span style="font-family:\'Courier New\',monospace;font-size:10pt;'
        f'color:#202124;">' + "<br>".join(lines) + "</span>"
    )


def _render_mdtable(rows) -> str:
    """
    A real bordered grid, for things like the truth tables students fill
    in. Grid lines are wanted here, unlike the section tables.

    Google Docs has no nested tables, so callers must close the section
    table before emitting one of these.
    """
    cell = f"border:1px solid {GRID_BORDER};padding:7px 9px;vertical-align:top;"
    out = [f'<table style="border-collapse:collapse;width:100%;'
           f'border:1px solid {GRID_BORDER};">']
    for index, cells in enumerate(rows):
        out.append("<tr>")
        for text in cells:
            body = _inline(text) if text else "&nbsp;"
            if index == 0:
                out.append(f'<td style="{cell}background-color:{GRID_HEADER_BG};">'
                           f"<b>{body}</b></td>")
            else:
                out.append(f'<td style="{cell}">{body}</td>')
        out.append("</tr>")
    out.append("</table>")
    return "".join(out)


def handout_intro(md_text: str) -> str:
    """
    The handout's opening paragraph -- the text between the title and the
    first "## " section. Used as the Classroom assignment description, so
    students see what the week is about without opening the Doc.
    """
    for kind, payload in _parse_blocks(md_text):
        if kind == "paragraph":
            return payload
    return ""


def _render_section(section: dict) -> str:
    """
    Two-column table: a narrow checkbox column and the content. The
    checkbox cells are left EMPTY on purpose -- apply_doc_formatting()
    fills them with real Docs checkbox bullets afterwards, which is the
    only way to get a box the student can actually click.

    Grid lines are deliberately absent; the only rule is under the header
    row. Structure comes from the tinted bands instead, which keeps the
    vertical flow clean.
    """
    theme = THEMES["extra" if EXTRA_CREDIT_RE.search(section["heading"]) else "default"]
    cell = "border:none;padding:8px 10px;vertical-align:top;"
    box_cell = cell + f"width:{CHECKBOX_COL_WIDTH};"
    header_rule = f"border-bottom:1.5pt solid {theme['border']};"

    out = ['<table style="border-collapse:collapse;width:100%;border:none;">']

    # Heading row: tinted band, section number kept in the text so "3."
    # still reads as the third thing to do.
    out.append(
        f'<tr><td style="{box_cell}{header_rule}background-color:{theme["header_bg"]};"></td>'
        f'<td style="{cell}{header_rule}background-color:{theme["header_bg"]};">'
        f'<span style="font-size:13pt;color:{theme["header_fg"]};">'
        f'<b>{_inline(section["heading"])}</b></span></td></tr>'
    )

    for kind, text in section["rows"]:
        if kind == "task":
            out.append(
                f'<tr><td style="{box_cell}"></td>'
                f'<td style="{cell}"><span style="color:{BODY_FG};">{_inline(text)}</span></td></tr>'
            )
        elif kind == "prose":
            out.append(
                f'<tr><td colspan="2" style="{cell}">'
                f'<span style="color:{BODY_FG};">{_inline(text)}</span></td></tr>'
            )
        elif kind == "code":
            out.append(
                f'<tr><td colspan="2" style="{cell}'
                f'background-color:{CODE_BG};">{_code_html(text)}</td></tr>'
            )
        elif kind == "space":
            out.append(
                f'<tr><td colspan="2" style="{cell}">'
                + "&nbsp;" + "<br>" * WRITING_SPACE_LINES
                + "</td></tr>"
            )
        elif kind == "mdtable":
            # Docs cannot nest tables, so step outside this one, draw the
            # grid, then resume the section in a fresh headerless table.
            out.append("</table>")
            out.append(SPACER)
            out.append(_render_mdtable(text))
            out.append(SPACER)
            out.append('<table style="border-collapse:collapse;width:100%;border:none;">')

    out.append("</table>")
    return "".join(out)


def markdown_to_minimal_html(md_text: str) -> str:
    """
    Dependency-free markdown-to-HTML pass, tuned for the handout structure
    we actually use. Each "## " section becomes a checkbox table; "> " lines
    become a callout box; {{writing-space}} becomes blank writing room.
    Drive's import step turns this into a real formatted Google Doc.

    Blank lines in the source are not meaningful here: spacing between
    blocks is emitted deliberately, because Docs collapses whatever it
    feels like otherwise.
    """
    parts = []

    for kind, payload in _parse_blocks(md_text):
        if kind == "title":
            # "Week 1 Homework: Getting Comfortable With Your Laptop" becomes
            # a course-and-week line over a descriptive subtitle.
            lead, _, subtitle = payload.partition(":")
            parts.append(f"<h2>{COURSE_NAME} - {_inline(lead.strip())}</h2>")
            if subtitle.strip():
                parts.append(f"<h3>{_inline(subtitle.strip())}</h3>")
        elif kind in ("paragraph", "task"):
            parts.append(f'<p><span style="color:{BODY_FG};">{_inline(payload)}</span></p>')
        elif kind == "code":
            parts.append(f'<p>{_code_html(payload)}</p>')
        elif kind == "mdtable":
            parts.append(_render_mdtable(payload))
            parts.append(SPACER)
        elif kind == "callout":
            parts.append(SPACER)
            parts.append(
                f'<table style="border-collapse:collapse;width:100%;'
                f'border:1px solid {CALLOUT_BORDER};"><tr>'
                f'<td style="border:1px solid {CALLOUT_BORDER};padding:10px 12px;'
                f'background-color:{CALLOUT_BG};">'
                f'<span style="color:#5f6368;">{_inline(payload)}</span>'
                f"</td></tr></table>"
            )
            parts.append(SPACER)
        elif kind == "space":
            parts.append("<p>" + "&nbsp;" + "<br>" * WRITING_SPACE_LINES + "</p>")
        elif kind == "section":
            # One blank line before every table: it separates the tables
            # from each other and from the intro paragraph above the first
            # one, leaving room to write notes.
            parts.append(SPACER)
            # Extra breathing room ahead of the optional AP block so it
            # reads as a separate thing, not the tail of the homework.
            if EXTRA_CREDIT_RE.search(payload["heading"]):
                parts.append(SPACER)
                parts.append(SPACER)
            parts.append(_render_section(payload))

    # Trailing blank line so the last table also has note room under it.
    parts.append(SPACER)

    return (
        '<html><body style="font-family:Arial,sans-serif;">'
        + "\n".join(parts)
        + "</body></html>"
    )


def _cell_text(cell: dict) -> str:
    return "".join(
        element.get("textRun", {}).get("content", "")
        for item in cell.get("content", [])
        for element in item.get("paragraph", {}).get("elements", [])
    ).strip()


def _is_section_table(table: dict) -> bool:
    """
    Tell a checkbox section table from a content grid (a truth table, say).

    A section table is two columns whose very first cell is empty, because
    that cell exists only to hold a checkbox. Every grid table starts with
    a header label instead.
    """
    if table.get("columns") != 2:
        return False
    rows = table.get("tableRows", [])
    return bool(rows) and not _cell_text(rows[0].get("tableCells", [{}])[0])


def _checkbox_cell_ranges(document: dict):
    """
    Ranges of the empty left-hand cells that should get a checkbox.

    A full-width row keeps two cells after import and marks the first one
    columnSpan 2, so the span -- not the cell count -- is what separates a
    checkbox row from a prose row, the writing-space row, or the callout.
    Requiring the cell to be empty guards the rest.
    """
    ranges = []
    for element in document.get("body", {}).get("content", []):
        table = element.get("table")
        if not table or not _is_section_table(table):
            continue
        for row in table.get("tableRows", []):
            cells = row.get("tableCells", [])
            if len(cells) != 2:
                continue
            first = cells[0]
            if first.get("tableCellStyle", {}).get("columnSpan", 1) != 1:
                continue
            paragraphs = [i for i in first.get("content", []) if "paragraph" in i]
            if len(paragraphs) != 1:
                continue
            text = "".join(
                e.get("textRun", {}).get("content", "")
                for e in paragraphs[0]["paragraph"].get("elements", [])
            )
            if text.strip():
                continue
            ranges.append({"startIndex": paragraphs[0]["startIndex"],
                           "endIndex": paragraphs[0]["endIndex"]})
    return ranges


def _table_width_requests(document: dict, content_width_pt: float):
    """
    Pin every table to the full text width.

    HTML import flattens width:100% into whatever fixed width it feels
    like, which leaves the tables visibly narrower than the surrounding
    paragraphs. Setting the columns explicitly is the only way to get a
    straight right edge down the page.
    """
    requests = []
    for element in document.get("body", {}).get("content", []):
        table = element.get("table")
        if not table:
            continue
        location = {"index": element["startIndex"]}
        columns = table.get("columns", 1)
        if _is_section_table(table):
            widths = [CHECKBOX_COL_PT, content_width_pt - CHECKBOX_COL_PT]
        else:
            widths = [content_width_pt / columns] * columns
        for index, width in enumerate(widths):
            requests.append({
                "updateTableColumnProperties": {
                    "tableStartLocation": location,
                    "columnIndices": [index],
                    "tableColumnProperties": {
                        "widthType": "FIXED_WIDTH",
                        "width": {"magnitude": width, "unit": "PT"},
                    },
                    "fields": "widthType,width",
                }
            })
    return requests


def apply_doc_formatting(docs, doc_id: str):
    """
    Post-import pass for the things HTML import cannot express: real
    checkbox bullets (clickable in the Docs app, unlike a U+2610
    character) and narrower page margins.

    Must run after every upload, because re-importing HTML replaces the
    document body and takes the bullets with it.
    """
    document = docs.documents().get(documentId=doc_id).execute()

    requests = [{
        "updateDocumentStyle": {
            "documentStyle": {
                "marginLeft": {"magnitude": PAGE_MARGIN_SIDE_PT, "unit": "PT"},
                "marginRight": {"magnitude": PAGE_MARGIN_SIDE_PT, "unit": "PT"},
                "marginTop": {"magnitude": PAGE_MARGIN_VERT_PT, "unit": "PT"},
                "marginBottom": {"magnitude": PAGE_MARGIN_VERT_PT, "unit": "PT"},
            },
            "fields": "marginLeft,marginRight,marginTop,marginBottom",
        }
    }]

    page_width = document["documentStyle"]["pageSize"]["width"]["magnitude"]
    requests += _table_width_requests(
        document, page_width - 2 * PAGE_MARGIN_SIDE_PT)

    # Reverse document order: applying a bullet can shift the indices of
    # everything after it, so work from the end backwards.
    for rng in sorted(_checkbox_cell_ranges(document),
                      key=lambda r: r["startIndex"], reverse=True):
        requests.append({
            "createParagraphBullets": {"range": rng, "bulletPreset": "BULLET_CHECKBOX"}
        })
        requests.append({
            "updateParagraphStyle": {
                "range": rng,
                "paragraphStyle": {
                    "indentFirstLine": {"magnitude": BULLET_INDENT_FIRST_PT, "unit": "PT"},
                    "indentStart": {"magnitude": BULLET_INDENT_START_PT, "unit": "PT"},
                },
                "fields": "indentFirstLine,indentStart",
            }
        })

    docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
    return sum(1 for r in requests if "createParagraphBullets" in r)


def find_or_create_folder(drive, name: str) -> str:
    query = (
        f"name = '{name}' and mimeType = 'application/vnd.google-apps.folder' "
        "and trashed = false"
    )
    results = drive.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])
    if files:
        return files[0]["id"]
    folder = drive.files().create(
        body={"name": name, "mimeType": "application/vnd.google-apps.folder"},
        fields="id",
    ).execute()
    print(f"Created Drive folder: {name}")
    return folder["id"]


def find_existing_doc(drive, folder_id: str, title: str):
    query = (
        f"name = '{title}' and '{folder_id}' in parents "
        "and mimeType = 'application/vnd.google-apps.document' and trashed = false"
    )
    results = drive.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])
    return files[0]["id"] if files else None


def upload_doc(drive, folder_id: str, title: str, html: str, existing_id: str = None) -> str:
    media = MediaInMemoryUpload(html.encode("utf-8"), mimetype="text/html", resumable=True)
    if existing_id:
        drive.files().update(fileId=existing_id, media_body=media).execute()
        return existing_id
    file = drive.files().create(
        body={
            "name": title,
            "parents": [folder_id],
            "mimeType": "application/vnd.google-apps.document",
        },
        media_body=media,
        fields="id",
    ).execute()
    return file["id"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="Path to the cs-course repo")
    parser.add_argument(
        "--folder-name",
        default="CS Course - Student Handouts",
        help="Drive folder to hold the generated Docs (created if missing)",
    )
    parser.add_argument("--weeks", default="", help="Range to act on, e.g. 1-5. Default: all weeks found.")
    parser.add_argument("--dry-run", action="store_true", help="List what would happen, change nothing")
    args = parser.parse_args()

    week_range = None
    if args.weeks:
        start_s, _, end_s = args.weeks.partition("-")
        week_range = (int(start_s), int(end_s or start_s))

    handouts_dir = Path(args.repo) / "handouts"
    if not handouts_dir.is_dir():
        sys.exit(f"No handouts/ directory found at {handouts_dir}")

    files = sorted(handouts_dir.glob("week-*-homework.md"))
    if not files:
        sys.exit(f"No week-NN-homework.md files found in {handouts_dir}")

    classroom, drive = get_services()
    docs = None if args.dry_run else get_docs_service()
    folder_id = None if args.dry_run else find_or_create_folder(drive, args.folder_name)

    for path in files:
        m = WEEK_FILE_RE.search(path.name)
        if not m:
            continue
        week = m.group(1)
        if week_range and not (week_range[0] <= int(week) <= week_range[1]):
            continue
        title = f"Week {week} - Homework"
        md_text = path.read_text(encoding="utf-8")
        html = markdown_to_minimal_html(md_text)

        if args.dry_run:
            print(f"[dry run] would create/update Doc: {title}")
            continue

        existing_id = find_existing_doc(drive, folder_id, title)
        doc_id = upload_doc(drive, folder_id, title, html, existing_id)
        boxes = apply_doc_formatting(docs, doc_id)
        action = "Updated" if existing_id else "Created"
        print(f"{action}: {title}  ({boxes} checkboxes, fileId {doc_id})")

    print("\nDone. Run sync_classroom.py next to attach these to assignments.")


if __name__ == "__main__":
    main()
