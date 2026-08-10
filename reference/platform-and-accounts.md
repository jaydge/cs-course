# Platform and Accounts

How the course is coordinated and what accounts each student needs. The decision: Google Classroom is the coordination hub, run from a personal Google account, since the whole roster is 13 or older.

Verify current platform features, prices, and age terms before each year; these change.

## Why Google Classroom

It is free, runs in a browser on Mac and Windows, and sits on the Google account students already create for Docs and Drive. For a small in-person co-op it provides the right amount of structure: announcements, handouts, due dates, a gradebook that maps to the course rubric, per-student feedback, and submission tracking. It does not replace teaching in the room; it is the backbone for materials, grades, and parent communication.

## The layered setup

Each tool does one job. Do not duplicate work across them.

- **Google Classroom** is the front door and coordination hub: announcements, handouts, due dates, the gradebook, feedback, and non-code submissions.
- **GitHub Classroom** is the code layer: each student gets a repository, and the Git unit becomes real work in the real tool. Post each coding assignment's accept link inside the matching Google Classroom assignment so students have one place to start.
- **The GitHub repository (`cs-course`)** stays the instructor's source of truth. Author guides and handouts here in Markdown, then publish student-facing copies (PDF or Google Doc) into Classroom. Author once, publish out.
- **Google Drive and Docs** hold student writeups and are the cross-platform document layer.

## Accounts each student needs

All students are 13 or older, so no parent-managed (Family Link) accounts are required. Still get parental consent before creating any account for a minor.

| Account | For | Notes |
|---|---|---|
| Google account | Google Classroom, Drive, and Docs | The account the class runs on; set up with a parent in Week 1 |
| GitHub account | Version control, the Git unit, project repos | Set up with a parent; used from the software unit onward |
| CodeAI (formerly Code.org) | Concept lessons, AP pseudocode practice, assessments | Free; a class section the instructor creates |
| Project STEM | AP track only | AP-track students only; the adopted AP syllabus provider |

LLM API access for the AI unit stays instructor-owned, not per student, because of cost and provider age terms.

## Personal-account Classroom: two limits to plan around

Running Classroom from a personal Google account (rather than Google Workspace for Education) has two consequences worth knowing:

- **No guardian email summaries.** Those automated weekly parent digests require a Workspace for Education account. On a personal account they are unavailable, so parent visibility is handled manually (see below).
- **Students cannot email classmates through Classroom.** Not a real loss for this course.

Neither blocks the plan. The age limitation that would matter, that children 13 and under should only use Classroom with a Workspace for Education or Nonprofits account, does not apply here since the roster is all 13-plus.

## Setup checklist

- [ ] Create one class named "Computer Science I" and share the join code with students.
- [ ] Set gradebook categories to the course rubric weights: weekly labs 40, unit checkpoints 20, milestones 15, final or Create Task 20, participation 5.
- [ ] Create Topics for navigation, either by unit (Unit 1 through 6) or by type (Handouts, Homework, AP Extra Credit, Reference). Keep AP extra-credit work in its own clearly optional topic so it never reads as required.
- [ ] Connect GitHub Classroom and confirm you can post an assignment accept link inside a Google Classroom assignment.
- [ ] Decide the parent-update method (see below) before Week 1.

## Weekly rhythm

- Post an announcement with the week's plan.
- Post the homework handout as an assignment with a due date.
- Post any coding work as an assignment linking out to GitHub Classroom.
- Keep the AP extra-credit slice in the optional topic, matching how the handouts frame it.

## Parent visibility

Because personal-account Classroom has no guardian summaries, send a short weekly parent note yourself. For a class this size that is a few minutes and fits the transparent-by-design approach in the parent syllabus. If you later want automated summaries and managed student accounts, that is the reason to move to Workspace for Education.

## Classroom setup: bulk-loading materials

Google Classroom has no native bulk-import; the Create menu adds one item at a time. Two scripts in `tools/` (`publish_handouts_to_docs.py` and `sync_classroom.py`) do this from the repo instead, using the Classroom and Drive APIs from a personal Google account (this works; no Workspace domain is required).

**Handout format:** each week's handout is published as its own Google Doc in a Drive folder, attached to the assignment with `shareMode: STUDENT_COPY`, so every student gets their own editable copy rather than a shared read-only file.

**What is never uploaded:** teacher guides (`lessons/`) are instructor prep material and are excluded by design; only `handouts/` is published.

**Topics:** Classroom has no separate "manage topics" screen. A topic is created either from the **+ Create > Topic** menu item, or inline from the Topic dropdown while creating any assignment. `sync_classroom.py` creates the six unit topics and an "AP Extra Credit Track" topic automatically on first run.

**One-time setup:** a Cloud project and OAuth client (already created), `credentials.json` at the repo root (gitignored), and `pip install -r tools/requirements.txt`. Three APIs must be enabled on the project — Classroom, Drive, and **Docs** — and while the OAuth consent screen is in "Testing" mode your own Google address has to be listed under Audience > Test users, or authorization fails with `access_denied` even as the project owner. See `tools/README.md` for the full run order.

**Normal workflow:**
```
python tools/publish_handouts_to_docs.py --repo /path/to/cs-course
python tools/sync_classroom.py --course-id YOUR_ID --repo /path/to/cs-course --dry-run
python tools/sync_classroom.py --course-id YOUR_ID --repo /path/to/cs-course
```
Assignments are created as drafts by default; review them in Classroom before publishing, or add `--publish`. Both scripts are safe to re-run: they update existing Docs and skip assignments that already exist rather than duplicating them. Skip-detection has to ask the Classroom API for draft coursework explicitly, because `courseWork.list` returns only published items by default — a tool that omits that cannot see its own drafts and silently creates a second copy of everything on the next run.

**Reflection questions:** a `{{question: ...}}` marker in a handout becomes a Classroom short-answer Question under that week's topic, created only when `sync_classroom.py` is passed `--questions`. Week 1 is the only handout carrying one so far.

**Handout formatting.** Each `## ` section renders as a table with a real, clickable Docs checkbox per task. Getting there needs a Docs API pass after the HTML import, since HTML cannot express a checkbox list bullet, page margins, or a table width that actually fills the text column. Consequence worth remembering: re-importing a handout replaces the document body and drops the checkboxes, so the formatting pass must run on every publish. `publish_handouts_to_docs.py` does this automatically; uploading a handout any other way will not.

## Why Google Classroom, and when to reconsider

Google Classroom's app-store ratings look alarming but reflect students protest-reviewing homework itself, not the product; sentiment among actual teachers on review platforms built for that purpose runs strongly positive. It is the right fit here because it is free, sits on the Google accounts students already use, and needs no per-student customization. Canvas's free-for-teacher tier is the one alternative worth a look if the course ever needs real quizzing or a heavier gradebook than the rubric requires; since the repo and Drive remain the source of truth, switching later would be a light lift, not a rebuild.



Google provides Workspace for Education free to U.S. homeschools and co-ops, and the free Fundamentals tier includes Classroom, guardian email summaries, managed student accounts, and an admin console. It requires qualifying as a recognized educational organization, verifying a domain, and roughly two weeks for approval. It would also make the co-op the consent authority and issue managed accounts, which is a cleaner answer to student-account and consent questions than personal Gmail accounts. Consider it for a future term if guardian summaries or managed accounts become worth the setup. Check HSLDA's homeschool guidance and Google's qualification page for current steps.
