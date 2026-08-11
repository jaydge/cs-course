"""
Sync the course's weekly homework into Google Classroom: creates the
unit topics (once) and one Assignment per week, attaching that week's
Google Doc handout so each student gets their own editable copy.

This tool is deliberately narrow. It only ever touches:
  - handouts/week-NN-homework.md file titles, to match each week to
    its already-uploaded Google Doc (run publish_handouts_to_docs.py
    first)
  - Topics and CourseWork in the one Classroom course you point it at

It never uploads lessons/ (teacher guides). Those are your prep
material, not student-facing, and this tool has no code path that
reads that directory.

Assignments are created as DRAFT by default so nothing reaches
students until you review and publish them yourself, in the Classroom
UI or by re-running with --publish.

Usage:
    # 1. One-time: find your course ID
    python sync_classroom.py --list-courses

    # 2. Dry run against a specific course, see what would happen
    python sync_classroom.py --course-id 123456789 --dry-run

    # 3. Create everything as drafts
    python sync_classroom.py --course-id 123456789

    # 4. Re-run any time; already-created topics and assignments are
    #    detected by name and skipped, so this is safe to re-run.

    # 5. When ready, publish a batch (e.g. just Unit 1)
    python sync_classroom.py --course-id 123456789 --weeks 1-5 --publish

Requires: pip install -r requirements.txt
"""

import argparse
import re
from pathlib import Path

from classroom_auth import get_services
from publish_handouts_to_docs import QUESTION_RE, handout_intro

# Matches the rubric shorthand in the curriculum (4 = works and can
# explain, 3 = works, 2 = partly, ...), so the Classroom grade is the
# rubric score with no conversion while marking.
RUBRIC_POINTS = 4

# Appended to every assignment description. Much of the week's work
# happens outside the Doc -- Python written in Thonny, mainly -- and
# nothing else tells students to attach it.
TURN_IN_NOTE = (
    "Your own copy of this week's handout is attached. Work in it and tick the "
    "checkboxes as you go. Use + Add or create to attach any Python files or "
    "screenshots, then click Turn in."
)

# Week ranges per unit. Update this if the curriculum's unit
# boundaries ever change; everything else derives from it.
UNITS = [
    (1, 5, "Unit 1: Thinking Like a Computer Scientist"),
    (6, 10, "Unit 2: Inside the Computer"),
    (11, 16, "Unit 3: Programming Like a Professional"),
    (17, 21, "Unit 4: Operating Systems and the Internet"),
    (22, 26, "Unit 5: Building Modern Software"),
    (27, 32, "Unit 6: The Future of Computing"),
]
AP_TOPIC_NAME = "AP Extra Credit Track"

WEEK_FILE_RE = re.compile(r"week-(\d{2})-homework\.md$")


def unit_topic_for_week(week: int) -> str:
    for start, end, name in UNITS:
        if start <= week <= end:
            return name
    raise ValueError(f"Week {week} does not fall in any configured unit range")


def parse_week_range(spec: str, all_weeks):
    if not spec:
        return all_weeks
    start_s, _, end_s = spec.partition("-")
    start, end = int(start_s), int(end_s or start_s)
    return [w for w in all_weeks if start <= w <= end]


def list_courses(classroom):
    results = classroom.courses().list(teacherId="me").execute()
    courses = results.get("courses", [])
    if not courses:
        print("No courses found for your account. Create the course in the Classroom UI first.")
        return
    print("Your courses:")
    for c in courses:
        print(f"  {c['id']}  {c['name']}  ({c.get('courseState', '?')})")


def get_or_create_topics(classroom, course_id: str, dry_run: bool) -> dict:
    """Returns {topic_name: topic_id}, creating any topic that doesn't exist yet."""
    existing = classroom.courses().topics().list(courseId=course_id).execute().get("topic", [])
    by_name = {t["name"]: t["topicId"] for t in existing}

    wanted = [name for _, _, name in UNITS] + [AP_TOPIC_NAME]
    for name in wanted:
        if name in by_name:
            continue
        if dry_run:
            print(f"[dry run] would create topic: {name}")
            continue
        topic = classroom.courses().topics().create(
            courseId=course_id, body={"name": name}
        ).execute()
        by_name[name] = topic["topicId"]
        print(f"Created topic: {name}")
    return by_name


def existing_coursework(classroom, course_id: str) -> dict:
    """
    Every assignment and question already in the course, keyed by title.

    Both arguments matter. courseWork.list defaults to PUBLISHED only and
    to one short page, so without them this tool cannot see the drafts it
    created on its last run -- and re-running duplicates the lot instead
    of skipping, which is exactly what the module docstring promises it
    will not do.
    """
    found = {}
    page_token = None
    while True:
        response = classroom.courses().courseWork().list(
            courseId=course_id,
            courseWorkStates=["PUBLISHED", "DRAFT"],
            pageSize=100,
            pageToken=page_token,
        ).execute()
        found.update({cw.get("title"): cw for cw in response.get("courseWork", [])})
        page_token = response.get("nextPageToken")
        if not page_token:
            return found


def find_doc_id(drive, folder_name: str, title: str):
    folder_q = (
        f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' "
        "and trashed = false"
    )
    folders = drive.files().list(q=folder_q, fields="files(id)").execute().get("files", [])
    if not folders:
        return None
    folder_id = folders[0]["id"]
    doc_q = (
        f"name = '{title}' and '{folder_id}' in parents "
        "and mimeType = 'application/vnd.google-apps.document' and trashed = false"
    )
    docs = drive.files().list(q=doc_q, fields="files(id)").execute().get("files", [])
    return docs[0]["id"] if docs else None


def assignment_description(handouts_dir: Path, week: int) -> str:
    path = handouts_dir / f"week-{week:02d}-homework.md"
    intro = handout_intro(path.read_text(encoding="utf-8")) if path.is_file() else ""
    return f"{intro}\n\n{TURN_IN_NOTE}".strip()


def questions_for_week(handouts_dir: Path, week: int):
    """Reflection prompts marked with {{question: ...}} in the week's handout."""
    path = handouts_dir / f"week-{week:02d}-homework.md"
    if not path.is_file():
        return []
    found = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = QUESTION_RE.match(line.strip())
        if m:
            found.append(m.group(1))
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course-id", help="Classroom course ID (see --list-courses)")
    parser.add_argument("--list-courses", action="store_true", help="List your courses and exit")
    parser.add_argument("--repo", help="Path to the cs-course repo (to discover which weeks exist)")
    parser.add_argument(
        "--folder-name",
        default="CS Course - Student Handouts",
        help="Drive folder created by publish_handouts_to_docs.py",
    )
    parser.add_argument("--weeks", default="", help="Range to act on, e.g. 1-5. Default: all weeks found.")
    parser.add_argument("--publish", action="store_true", help="Publish immediately instead of leaving as drafts")
    parser.add_argument(
        "--questions",
        action="store_true",
        help="Also create a short-answer Question for each {{question: ...}} in the handout",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Create highest week first. Classroom sorts each topic newest-first and "
             "exposes no ordering field, so creating in reverse is what puts Week 01 on top.",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Update description and points on items that already exist, "
             "instead of skipping them. Leaves title, topic and attachments alone.",
    )
    parser.add_argument("--dry-run", action="store_true", help="List what would happen, change nothing")
    args = parser.parse_args()

    classroom, drive = get_services()

    if args.list_courses:
        list_courses(classroom)
        return

    if not args.course_id or not args.repo:
        parser.error("--course-id and --repo are required unless using --list-courses")

    handouts_dir = Path(args.repo) / "handouts"
    all_weeks = sorted(
        int(WEEK_FILE_RE.search(p.name).group(1))
        for p in handouts_dir.glob("week-*-homework.md")
        if WEEK_FILE_RE.search(p.name)
    )
    weeks = parse_week_range(args.weeks, all_weeks)
    if not weeks:
        print("No matching weeks found. Check --repo and --weeks.")
        return
    if args.reverse:
        weeks = list(reversed(weeks))

    topics = get_or_create_topics(classroom, args.course_id, args.dry_run)
    state = "PUBLISHED" if args.publish else "DRAFT"
    existing = {} if args.dry_run else existing_coursework(classroom, args.course_id)

    for week in weeks:
        title = f"Week {week:02d} - Homework"
        topic_name = unit_topic_for_week(week)
        topic_id = topics.get(topic_name)

        # Questions go in before the week's assignment so that the
        # assignment, being newer, sorts above its own reflection.
        if args.questions:
            for n, prompt in enumerate(questions_for_week(handouts_dir, week), start=1):
                q_title = f"Week {week:02d} - Reflection"
                if n > 1:
                    q_title += f" {n}"
                if args.dry_run:
                    print(f"[dry run] would create question: {q_title}  "
                          f"(topic: {topic_name}, state: {state})")
                    continue
                if q_title in existing:
                    if args.refresh:
                        fields = {"description": prompt, "maxPoints": RUBRIC_POINTS}
                        if args.publish:
                            fields["state"] = "PUBLISHED"
                        classroom.courses().courseWork().patch(
                            courseId=args.course_id,
                            id=existing[q_title]["id"],
                            updateMask=",".join(fields),
                            body=fields,
                        ).execute()
                        print(f"{'Published' if args.publish else 'Refreshed'}: {q_title}")
                    else:
                        print(f"Skip (already exists): {q_title}")
                    continue
                classroom.courses().courseWork().create(
                    courseId=args.course_id,
                    body={
                        "title": q_title,
                        "description": prompt,
                        "workType": "SHORT_ANSWER_QUESTION",
                        "state": state,
                        "topicId": topic_id,
                        "maxPoints": RUBRIC_POINTS,
                    },
                ).execute()
                existing[q_title] = {"title": q_title}
                print(f"Created ({state}) question: {q_title}  -> topic '{topic_name}'")

        if title in existing:
            if args.refresh:
                fields = {
                    "description": assignment_description(handouts_dir, week),
                    "maxPoints": RUBRIC_POINTS,
                }
                if args.publish:
                    fields["state"] = "PUBLISHED"
                classroom.courses().courseWork().patch(
                    courseId=args.course_id,
                    id=existing[title]["id"],
                    updateMask=",".join(fields),
                    body=fields,
                ).execute()
                print(f"{'Published' if args.publish else 'Refreshed'}: {title}")
            else:
                print(f"Skip (already exists): {title}")
            continue

        doc_id = None if args.dry_run else find_doc_id(drive, args.folder_name, title)
        if not args.dry_run and not doc_id:
            print(f"WARNING: no Doc found for '{title}' in folder '{args.folder_name}'. "
                  f"Run publish_handouts_to_docs.py first. Skipping.")
            continue

        if args.dry_run:
            print(f"[dry run] would create assignment: {title}  (topic: {topic_name}, state: {state})")
            continue

        body = {
            "title": title,
            "description": assignment_description(handouts_dir, week),
            "workType": "ASSIGNMENT",
            "state": state,
            "topicId": topic_id,
            "maxPoints": RUBRIC_POINTS,
            "materials": [
                {
                    "driveFile": {
                        "driveFile": {"id": doc_id},
                        "shareMode": "STUDENT_COPY",
                    }
                }
            ],
        }
        classroom.courses().courseWork().create(courseId=args.course_id, body=body).execute()
        existing[title] = {"title": title}
        print(f"Created ({state}): {title}  -> topic '{topic_name}'")

    print("\nDone. Review in Classroom > Classwork before publishing any drafts.")


if __name__ == "__main__":
    main()
