# Classroom sync tools

Publishes the course's weekly homework handouts to Google Classroom as
Google Docs, one editable copy per student. Only `handouts/` is ever
touched; `lessons/` (teacher guides) is never uploaded anywhere by
these scripts, since that is instructor prep material.

## One-time setup

1. `pip install -r requirements.txt` (Python 3.9+)
2. Put your OAuth client file (downloaded from Cloud Console) at the
   repo root as `credentials.json`. It is already gitignored.
3. Enable three APIs on the Cloud project: **Classroom**, **Drive**, and
   **Docs**. Docs is easy to miss and the failure is unmistakable —
   every run dies with `403 SERVICE_DISABLED` — but no extra OAuth
   scope is needed, since `drive.file` already covers documents these
   scripts created.
4. While the OAuth consent screen is in "Testing" mode, add your own
   Google address under **Audience > Test users**. Without it,
   authorization fails with `Error 403: access_denied` even though you
   own the project.
5. First run of either script opens a browser to authorize your
   personal Google account. A `token.json` is cached in this folder
   afterward so you are not re-prompted every time. Google may
   periodically expire it while in "Testing" mode; just re-authorize.
6. Find your Classroom course ID:
   ```
   python sync_classroom.py --list-courses
   ```

## Normal run

```bash
# 1. Convert this week's (or all) markdown handouts into Google Docs
python publish_handouts_to_docs.py --repo /path/to/cs-course

# 2. Preview what would be created in Classroom, changes nothing
python sync_classroom.py --course-id YOUR_ID --repo /path/to/cs-course --dry-run

# 3. Create the topics and assignments as drafts
python sync_classroom.py --course-id YOUR_ID --repo /path/to/cs-course

# 4. Review the drafts in Classroom > Classwork, then either publish
#    from the UI, or re-run with --publish to publish immediately
python sync_classroom.py --course-id YOUR_ID --repo /path/to/cs-course --weeks 1-5 --publish
```

Both scripts are safe to re-run: existing Docs are updated in place by
title match, and existing assignments are detected and skipped rather
than duplicated. Both also take `--weeks N` or `--weeks N-M` to work on
part of the course, which is the quickest way to iterate on one handout
without rewriting all 32.

## Handout markdown

Beyond ordinary markdown (headings, lists, bold, links, `>` callouts,
fenced code, pipe tables), handouts understand two markers:

| Marker | Effect |
| --- | --- |
| `{{writing-space}}` | Blank lines in the Doc for a written answer |
| `{{question: ...}}` | A Classroom short-answer Question, created by `sync_classroom.py --questions`. Never appears in the Doc. |

Each `## ` section becomes a two-column table: a checkbox column and the
content. Both `- ` bullets and `1. ` numbered items become checkbox rows;
paragraphs become full-width rows without a checkbox. A heading matching
"extra credit" or "AP track" switches that table to the amber palette, so
the optional AP block reads as separate.

## How the formatting works

Docs are built by importing generated HTML, then applying a second pass
with the Docs API for the things HTML import cannot express: real
clickable checkbox bullets (a `☐` character is not clickable), page
margins, and exact table widths (`width:100%` gets flattened on import,
which leaves tables narrower than the surrounding text).

That second pass must run on every upload, because re-importing HTML
replaces the document body and takes the checkboxes with it. Publishing
through any other route will lose them.

Google Docs cannot nest tables, so a pipe table inside a section closes
the section table, draws the grid, and resumes in a fresh one.

## Notes

- Handouts attach with `shareMode: STUDENT_COPY`, so each student gets
  their own editable copy in their Drive, not a shared view-only link.
- Assignments default to Classroom topics named after the six course
  units (see `UNITS` in `sync_classroom.py`); update that list if the
  curriculum's week ranges ever change.
- Assignments are created as `DRAFT` unless you pass `--publish`, so
  nothing reaches students until you choose to release it.
- Everything is scoped to one course at a time; nothing here reads or
  writes outside the course ID you pass in.
