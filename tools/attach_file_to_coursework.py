"""
Post an extra file (in-class code, a worked example, anything that isn't
one of the standard handouts) to Classroom, alongside a Week's homework
assignment that has already been created by sync_classroom.py.

publish_handouts_to_docs.py and sync_classroom.py cover the weekly
handout-to-Doc-to-assignment pipeline, but neither of them touches an
assignment after it has been posted. That turns out to be a hard limit,
not just a missing feature: the Classroom API's courseWork.patch and
courseWorkMaterials.patch both reject "materials" in updateMask ("Non-
supported update mask fields specified"). Materials can only be set when
an item is created, never added afterward. So this script does not try
to edit the existing "Week NN - Homework" assignment. Instead it uploads
the file to Drive as-is and creates a small, separate Material in the
same Classroom topic as that week's assignment, titled "Week NN -
In-Class Code".

Usage:
    python3 attach_file_to_coursework.py --course-id YOUR_ID --repo /path/to/cs-course \
        --week 4 --file code/week-04-class.py

Safe to re-run: if a file with the same title already exists in the Drive
folder, its content is replaced in place rather than duplicated, and if a
Material with the same title already exists in the course, its
description and file are refreshed in place rather than duplicated.
"""

import argparse
import mimetypes
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from classroom_auth import get_services
from publish_handouts_to_docs import (
    find_existing_file,
    find_or_create_folder,
    upload_raw_file,
)

DEFAULT_FOLDER_NAME = "CS Course - Student Handouts"


def find_coursework(classroom, course_id: str, title: str):
    page_token = None
    while True:
        response = classroom.courses().courseWork().list(
            courseId=course_id,
            courseWorkStates=["PUBLISHED", "DRAFT"],
            pageSize=100,
            pageToken=page_token,
        ).execute()
        for item in response.get("courseWork", []):
            if item.get("title") == title:
                return item
        page_token = response.get("nextPageToken")
        if not page_token:
            return None


def find_material(classroom, course_id: str, title: str):
    page_token = None
    while True:
        response = classroom.courses().courseWorkMaterials().list(
            courseId=course_id,
            courseWorkMaterialStates=["PUBLISHED", "DRAFT"],
            pageSize=100,
            pageToken=page_token,
        ).execute()
        for item in response.get("courseWorkMaterial", []):
            if item.get("title") == title:
                return item
        page_token = response.get("nextPageToken")
        if not page_token:
            return None


def guess_mimetype(path: Path) -> str:
    mimetype, _ = mimetypes.guess_type(path.name)
    if mimetype:
        return mimetype
    if path.suffix == ".py":
        return "text/x-python"
    return "application/octet-stream"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course-id", required=True, help="Classroom course ID")
    parser.add_argument("--repo", required=True, help="Path to the cs-course repo")
    parser.add_argument("--week", required=True, type=int,
                        help="Week number this code goes with")
    parser.add_argument("--file", required=True,
                        help="Path to the file to post, relative to --repo unless absolute")
    parser.add_argument("--title", default=None,
                        help="Drive file title. Default: the file's own name")
    parser.add_argument("--material-title", default=None,
                        help="Classroom Material title. Default: 'Week NN - In-Class Code'")
    parser.add_argument("--description", default="Code from class, for reference.",
                        help="Material description shown to students")
    parser.add_argument("--folder-name", default=DEFAULT_FOLDER_NAME,
                        help="Drive folder the file is uploaded into (same one handouts use)")
    parser.add_argument("--share-mode", choices=["VIEW", "STUDENT_COPY"], default="VIEW",
                        help="VIEW: everyone sees the same file. "
                             "STUDENT_COPY: each student gets their own editable copy.")
    parser.add_argument("--publish", action="store_true",
                        help="Post as PUBLISHED. Default: DRAFT, same as the other scripts.")
    parser.add_argument("--dry-run", action="store_true", help="List what would happen, change nothing")
    args = parser.parse_args()

    repo = Path(args.repo)
    file_path = Path(args.file)
    if not file_path.is_absolute():
        file_path = repo / file_path
    if not file_path.exists():
        parser.error(f"File not found: {file_path}")

    drive_title = args.title or file_path.name
    assignment_title = f"Week {args.week:02d} - Homework"
    material_title = args.material_title or f"Week {args.week:02d} - In-Class Code"
    state = "PUBLISHED" if args.publish else "DRAFT"

    if args.dry_run:
        print(f"[dry run] would upload {file_path} as '{drive_title}' "
              f"(share mode: {args.share_mode})")
        print(f"[dry run] would create/update material '{material_title}' "
              f"(state: {state}), topic matched to '{assignment_title}'")
        return

    classroom, drive = get_services()

    coursework = find_coursework(classroom, args.course_id, assignment_title)
    if not coursework:
        print(f"WARNING: no coursework titled '{assignment_title}' found. "
              f"Posting the material without a matching topic.")
    topic_id = coursework.get("topicId") if coursework else None

    folder_id = find_or_create_folder(drive, args.folder_name)
    existing_file_id = find_existing_file(drive, folder_id, drive_title)
    data = file_path.read_bytes()
    mimetype = guess_mimetype(file_path)
    file_id = upload_raw_file(drive, folder_id, drive_title, data, mimetype, existing_file_id)
    print(f"{'Updated' if existing_file_id else 'Uploaded'}: {drive_title}  "
          f"({mimetype}, fileId {file_id})")

    existing_material = find_material(classroom, args.course_id, material_title)
    if existing_material:
        # materials can't be patched (see module docstring), so if the
        # underlying Drive file changed, only description/state can be
        # refreshed here -- the file content itself was already updated
        # in place above since it shares the same Drive file ID.
        classroom.courses().courseWorkMaterials().patch(
            courseId=args.course_id,
            id=existing_material["id"],
            updateMask="description,state",
            body={"description": args.description, "state": state},
        ).execute()
        print(f"Refreshed material: {material_title}")
        return

    body = {
        "title": material_title,
        "description": args.description,
        "state": state,
        "materials": [{"driveFile": {"driveFile": {"id": file_id},
                                     "shareMode": args.share_mode}}],
    }
    if topic_id:
        body["topicId"] = topic_id
    classroom.courses().courseWorkMaterials().create(
        courseId=args.course_id, body=body,
    ).execute()
    print(f"Created ({state}) material: {material_title}")


if __name__ == "__main__":
    main()
