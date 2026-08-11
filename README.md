# High School Computer Science: Course Materials

Everything for a 32-week, 2-hour-per-week high school computer science course built around one question: how does a button press become something useful? A Mac-primary classroom, Python for programming depth, hands-on hardware and unplugged activities, and an optional opt-in AP Computer Science Principles track. Designed for a small, in-person, mixed-age co-op (8th to 11th grade) taught by a technical instructor.

## What is inside

Start with the curriculum. Everything else is a companion it references.

### curriculum/
- **CS-Curriculum-and-Setup.md** — the main plan and the spine of everything: the 32-week outline, assessment and grading, credit and AP alignment, lab equipment, the Mac and Windows laptop configuration checklists, software platforms and accounts, extra-credit tracks, the AI-use policy, and adjustments for younger students.

### ap-track/
- **AP-Layer-Project-STEM-Overlay.md** — how to run an audited, opt-in AP CSP track underneath the course using Project STEM, with no exam pressure on younger students.
- **AP-CSP-Topic-Coverage.md** — a topic-by-topic map of all 35 AP CSP framework topics against where the course covers them, with a Covered, Strengthened, or Added status for each.
- **AP-Pseudocode-Bridge.md** — a Python-to-AP-pseudocode reference and trace-practice sheet for AP-track students.

### student-prep/
- **Course-Intro-Computer-Basics.md** — the brief 2-to-4-hour first-session computer-fluency intro, since there is no pre-course class.
- **Younger-Student-Readiness-and-Prep.md** — where younger students may get lost, a readiness diagnostic, optional supplemental videos, and recommended books.

### teaching-activities/
- **Unplugged-Logic-Activities.md** — offline logic games (the human-robot maze and more) mapped to the units they reinforce, with known-good online instructions and video links.

### reference/
- **Curriculum-Comparison.md** — how this course compares to paid and free programs (CompuScholar, CodeHS, Project STEM, CS50, Code.org), with syllabus links and a gap analysis.

### syllabus/
- **parent-syllabus.md** — the parent-facing syllabus: course overview, time commitment, unit schedule, grading, accounts and consent, devices, optional prep, and the opt-in AP track in plain language.
- **course-vs-ap-at-a-glance.html** — a printable visual for parents: two swim lanes showing the complete AP CSP core on the left and everything the course layers on top of it on the right, unit by unit, with the real-local-machine differentiator called out. Open in any browser; prints to letter across two pages. This HTML file is the source of record; edit it here.
- **course-vs-ap-at-a-glance.pdf** — the same visual rendered to PDF, and the copy attached in Google Classroom, since Classroom previews a PDF inline while an HTML attachment has to be downloaded before it renders. It is generated from the HTML, so regenerate it after any edit rather than editing it directly:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --no-pdf-header-footer \
  --print-to-pdf=syllabus/course-vs-ap-at-a-glance.pdf \
  file://$PWD/syllabus/course-vs-ap-at-a-glance.html
```

### lessons/
- Per-week in-depth teacher guides. **week-01-teacher-guide.md** is the format prototype; the remaining weeks follow its structure.

### handouts/
- Per-week student-facing homework handouts. **week-01-homework.md** is the prototype.

### tools/
- Scripts that push the handouts into Google Classroom, since Classroom has no bulk import. **publish_handouts_to_docs.py** turns each `handouts/week-NN-homework.md` into a formatted Google Doc, and **sync_classroom.py** creates the unit topics and one draft assignment per week with that week's Doc attached as a per-student copy. Teacher guides in `lessons/` are never uploaded. Start with **tools/README.md** for setup and the run order.

## How the pieces fit

The curriculum drives day-to-day teaching. The AP overlay and coverage map sit underneath as an opt-in layer for students who want the credential. The prep and activities support the first weeks and the mixed age range. The comparison and the pseudocode bridge are reference material. The lessons and handouts are the week-by-week teaching materials produced from the curriculum.

## Conventions

- **House style is plain prose.** No em dashes, no emojis, and no sales or pitch-deck language anywhere in this repository, including the parent-facing documents. Descriptions are factual rather than promotional: say what something is, not how good it is. This applies to generated material as much as to hand-written material, and it is the convention most easily lost in a bulk generation pass, so check it after one.
- **Activities and labs must be runnable from the guide alone.** Every weekly teacher guide contains concise but complete step-by-step instructions for each activity or lab, especially offline ones like the maze and logic puzzles, sufficient to run it in class without opening an external URL mid-session. Canonical URLs and videos are still linked, in the week's Resources section, and the guide adds a short explicit prep note only where the instructor genuinely needs to review that source or watch the video in advance to run the activity well (for example, to learn the demonstration patter). The assumption is that the instructor reads external docs and watches videos during prep, then teaches from the guide. The canonical link list lives in `teaching-activities/Unplugged-Logic-Activities.md`.
- **Every homework handout ends with an "Extra Credit AP Track" section.** It uses exactly that title, sits at the very end, and leaves the main homework above it untouched. It is optional, for AP-track students or anyone curious, either for interest or AP preparation, and counts only as extra credit: never required, never part of the base grade. It consolidates that week's optional AP work in one place, so AP students always know where to look. It holds the week's specific AP self-study pointer plus any AP-relevant extras for that week, such as pseudocode-bridge practice or Create Task preparation in the spring weeks.
- **AP unit pointers are specific, never "do the course."** In both the teacher guide's Section 12 and the handout's Extra Credit AP Track section, name the particular provider unit that matches that week's topic, and the specific lessons within it where those can be confirmed, and state plainly that the student does only that slice this week. Give the CodeAI (formerly Code.org) CSP unit as the free alternative alongside the Project STEM unit. Do not invent lesson numbers that cannot be confirmed; where a week does not map cleanly to a unit, say so and point to the nearest relevant one rather than forcing the match.

**Provider unit reference (verified August 2026; re-verify each year).** CodeAI rebranded from Code.org in June 2026; the CSP course continues unchanged. The current CodeAI CSP edition (`csp-2025`) has nine units, and note that Data moved to Unit 5 in this edition from Unit 9 in older ones: 1 Digital Information, 2 The Internet, 3 Intro to App Design, 4 Variables/Conditionals/Functions, 5 Data, 6 Lists/Loops/Traversals, 7 Parameters/Return/Libraries, 8 Cybersecurity and Global Impacts, 9 Create PT Prep. Unit pages are at `https://studio.code.org/courses/csp-2025/units/<n>`. Project STEM's current unit list is behind a teacher login and could not be verified from public sources; the unit titles used in the weekly guides follow its long-standing structure (1 Intro and Computational Thinking, 2 Programming, 3 Data Representation, 4 Digital Media Processing plus the Create Task, 5 Big Data, 6 Innovative Technologies, 7 AP Exam Review). Confirm these against the live course once enrolled and correct the weekly guides if the numbering has changed.
- Prices, links, and third-party course details change over time. Verify anything time-sensitive (laptop costs, provider endorsements, AP dates and fees, activity URLs) before relying on it.
- These are living documents. Edit freely.
- This repository can double as the live example for the course's Git and version-control unit (Unit 5, Week 23).
