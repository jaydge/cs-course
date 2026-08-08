# Week 31 Teacher Guide

## 1. Header

- **Week:** 31 of 32
- **Unit:** 6, The Future of Computing
- **Theme question:** What does "done" actually mean?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- State their own definition of done for their project, in a form another person could check.
- Show a program that runs end to end, however small, with the rough edges known and written down.
- Explain, in layer terms, what their project stands on, from their Python source down to the hardware and out to the network.
- Give a five-minute demonstration structure and know what they will show in each minute.
- For AP-track students: record a compliant Create Task video and produce a Personalized Project Reference with the required screen captures.
- For everyone: submit a repository with a README, a license, and a commit history that shows the work.

## 3. Where this sits

This is the first of two project weeks and it is a work session, not a lesson. The two-strand structure pauses here; the whole two hours belongs to the project, with checkpoints and one workshop segment breaking it up.

The final project is 20 percent of the course grade, per Section 3 of the curriculum, and it needs four things: a proposal (submitted in Week 27), a working artifact, a five-minute demo, and a one-page writeup explaining the layers it touches. For AP-track students the same artifact is the Create Performance Task, which is 30 percent of the AP score, and which adds a video, a Personalized Project Reference, and a submission through the AP Digital Portfolio.

The writeup deserves a note, because it is the piece that makes this a capstone rather than just a program. It asks students to explain what their project sits on: the Python they wrote, the interpreter from Unit 1, the OS and filesystem from Unit 4, the network and HTTP from Units 4 and 5, the hardware from Unit 2. That is the mid-year "trace the button press" milestone from Week 21, aimed at their own code. It is the closing of the course's central question and it is worth as much of your attention as the code.

**A planning note on the nine hours.** College Board requires that Create Task students get nine hours of in-class time for the task. Two class sessions is four hours, and even counting the project blocks in Weeks 27 and 30 you land near four and a half. Plan additional protected sessions outside the normal slot for AP-track students, and log every one of them with dates and durations. Verify the current requirement, since College Board has changed the hour count and the rules around it before.

## 4. Materials and setup

- Every student's laptop, charged, with their project repository cloned and working.
- Projector, connected and tested with at least one student machine, so demo-day connection problems surface today rather than next week.
- Printed final project rubric, one per student. It is in Section 11 and it should be in their hands before they finish building, not after.
- Printed submission checklist, one per student. Section 11 again.
- Printed demo structure card, one per student: five minutes broken into named chunks.
- Printed Create Task submission checklist, for AP-track students only.
- A quiet corner or second room for video recording, since students recording audio in the same room as eight other people does not work.
- Your log of protected Create Task hours, to update at the end of the session.
- Whiteboard with the theme question and a visible list of every student's project title and current status.
- Printed Week 31 homework handout, one per student.

## 5. Pre-class prep checklist

- **Read every project's current state before class.** Clone or pull each repository, run each program, and write yourself one line per student: what works, what does not, and what the single most valuable next hour would be. This is the highest-leverage prep of the last six weeks. (45 min)
- **Verify the current AP Create Performance Task requirements and deadline on AP Central.** Specifically: what the video may and may not contain, what the Personalized Project Reference requires, what gets uploaded to the Digital Portfolio, and the submission date. All of these have changed in recent years. Print the current official requirements and teach from those rather than from this guide. (30 min)
- **Confirm the exam logistics for any student testing.** That they are enrolled in the hosting school's exam-only section, that they have the join code for the AP Digital Portfolio, and that the fee is paid. If any of this is unresolved in Week 31, it is now urgent; see Section 2 of the curriculum for the homeschool route. (20 min)
- Test screen recording on one student machine of each type. On macOS, Shift-Command-5. On Windows, the Xbox Game Bar with Windows-G, or OBS. Know which one you are telling students to use. (15 min)
- Build the demo-day schedule for Week 32 with real names and times, and bring it printed. See Section 6 of the Week 32 guide. (10 min)
- Print the rubric, both checklists, the demo card, and the homework handout. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Open, definition of done, and the rules (0:00 to 0:15)

1. **Put every project on the board** with a one-word status: running, partly running, not yet. Doing this publicly is uncomfortable and it is the most useful fifteen seconds of the session, because nobody can quietly be behind after it.
2. **Hand out the rubric and read it.** Students should see how the project is scored before they spend two more hours on it. Point out that the artifact is 30 of 100 and the demo and writeup together are another 30, which surprises students who assume the code is everything.
3. **Make everyone write a definition of done, in one sentence, on the top of their rubric.** Format: "It is done when a person can [do this] and [this] happens." If a student cannot write that sentence, their project has no target and that is the problem to fix in the next ten minutes, not the code.
4. **State the AI rules for the last time before they build.** Create Task students: no AI, at any stage, including planning and debugging, through submission. Everyone else: the rule you set in Week 27, restated exactly, plus the requirement that any AI-assisted code carries a comment and that they can explain every line at the demo. Say the enforcement out loud, because it is not a threat, it is just how it works: at the demo you will point at a line and ask what it does.
5. **Give the scope instruction that this session lives or dies on.** Anything not finished by the end of today is not going in the project. Today is for finishing what exists; next week is for polishing, recording, writing, and demonstrating. A student who starts a new feature in Week 32 will demonstrate a broken program.

### Segment 2: Build block one, with rolling conferences (0:15 to 0:55)

- **Students do:** Work. Heads down.
- **You do:** Conference with every student individually, three minutes each, in the order of your prep list with the most-behind first. Run each conference to the same four questions and keep it moving:
  1. Show me it running. Not the code, the program.
  2. What is the next thing you will type?
  3. What is the one thing most likely to stop you finishing?
  4. What are you cutting?
- **You do:** For any student without running code, do not debug for them. Cut the project instead. Find the smallest version of their idea that runs, agree on it out loud, write it on their rubric, and move on. A finished small thing scores far better than an unfinished large one against every line of the rubric.
- **You do:** Note anyone whose code you cannot follow. That is the conversation to have now, quietly, rather than at the demo in front of the room.

### Segment 3: Build block two, aimed at demonstrability (0:55 to 1:25)

1. **Interrupt for two minutes at 0:55 with one instruction:** from now on, work on what you will show. Ask each student to name the single moment in their demo where the program does its most interesting thing, and then to make that moment work reliably.
2. **Give the three practical things that make a demo survive contact with an audience,** and have them do all three before doing anything else:
   - **Seed the data.** A program that needs eight things typed in before it does anything interesting will not survive a five-minute demo. Pre-load sample data, or add a startup option that fills it in.
   - **Handle the obvious bad input.** Someone will type a letter where a number goes, live, in front of everyone. Wrap the input, catch the error, print a message.
   - **Make it start clean.** The program should run from a single command in a fresh terminal, with no manual setup and no files that only exist on their machine.
3. **Students do:** Build. You keep circulating, now checking the three items above rather than features.
4. **At 1:20, have every student run their program once from a fresh terminal, start to finish, as though demonstrating.** Watch for the failures that only appear on a clean run: a hardcoded path, a missing file, a module they installed and forgot.

### Segment 4: Stretch (1:25 to 1:30)

### Segment 5: Split workshop, video and writeup (1:30 to 1:52)

Two groups, running at the same time. Brief both before splitting, then work the AP group first since their requirements are external and unforgiving.

**Group A, AP-track students: the video and the Personalized Project Reference.**

Work from the current official requirements you printed during prep, not from this list. As of the most recent specification, and subject to verification:

1. **The video shows the program running.** It captures input, the program's functionality, and output. It is short, under a minute, and small, under about 30 MB.
2. **It contains no identifying information about the student** and, per the specification, no voice narration. Verify this; it is the rule students most often break and the one most likely to have changed. Text captions within the video are permitted.
3. **Record it with the built-in screen recorder.** On macOS, Shift-Command-5, choose the region or window, record, stop from the menu bar. On Windows, Windows-G opens the Game Bar with a capture widget. Export as .mp4.
4. **Rehearse the run before recording.** A one-minute video of a program that works is easy; a one-minute video of a program that needed three attempts is not.
5. **The Personalized Project Reference** is the written companion: screen captures of one list or other collection being used to manage complexity, and one student-developed procedure that takes at least one parameter and contains both selection and iteration, together with a call to that procedure. Both captures come from their own program code.
6. **Have them produce both today, in class.** Not the polished final version, but a complete draft of each. A student who has recorded one video already will record a better one next week; a student who has never recorded one will discover the problems on the last day.
7. **Log this time** against the nine protected hours.

**Group B, everyone else: the one-page writeup.**

1. **Give the structure on the board.** Four short paragraphs: what it does, how it works, what it stands on, and what you would do next.
2. **The third paragraph is the one that matters** and it is why this project is a capstone. Have them start at their own source code and walk downward and outward, naming the real layers: the Python they wrote, the interpreter that reads it, the standard library and any packages, the operating system and its filesystem and processes, the machine code and the CPU, and if their project touches the network then HTTP, TCP, IP, DNS, and the server on the other end. Then have them name one thing at each layer they could not have named in September.
3. **Set the length honestly.** One page. Not two. The constraint is the exercise.
4. **Students do:** Draft it now, in class, where you can read over shoulders. The most common failure is a writeup that describes features instead of layers; catch that today.

Both groups should also do the repository housekeeping in the last five minutes: a README with what the project is and how to run it, the license file they chose in Week 30's homework, and a final commit.

### Segment 6: Demo day briefing and wrap (1:52 to 2:00)

1. **Hand out the demo structure card and read it.** Five minutes, four parts:
   - **0:00 to 0:30, the pitch.** What it does and who it is for. No code.
   - **0:30 to 2:30, the live run.** Show it working. Actually run it.
   - **2:30 to 4:00, one piece of code.** Open the file, show one procedure they are proud of, and explain what it does and why it is built that way.
   - **4:00 to 5:00, honesty.** What is broken, what they would do next, and the hardest bug they fixed. Say clearly that this last minute is graded and that "nothing is broken" scores badly.
2. **Post the Week 32 schedule** with names and times, and tell students they will present in that order. Take the projector-connection issue seriously now: name which adapter each student needs.
3. **State next week's shape** so nobody arrives expecting more build time: a short submission block, then demos, then a final Mystery Day, then the course ends.
4. **Hand out the homework**, noting the Extra Credit AP Track section, which this week is the Create Task submission checklist.

## 7. Key scripts and analogies

- **On "done":** "Done is not when you run out of ideas. Done is a sentence you wrote down in advance that another person can check. Without that sentence you are not building, you are wandering."
- **On cutting scope:** "Cutting is not failure, it is the actual skill. Every shipped piece of software in the world is the version that survived somebody cutting things out of it."
- **On finishing versus starting:** "A finished small program beats an unfinished ambitious one on every line of the rubric, and it beats it in the demo by an even wider margin. Nobody has ever been impressed by a description of what a program would have done."
- **On demo failure:** "Everything that can go wrong in a demo goes wrong in a demo. That is why we do a cold run today. Whatever breaks now would have broken next week in front of everybody."
- **On the layers writeup:** "You have been answering 'how does a button press become something useful?' since September. This is the same question, asked about your own program, which is a much harder version because you cannot hand-wave the part you built."
- **On the last minute of the demo:** "Telling us what is broken is not an apology, it is evidence that you know your own code. A student who says nothing is broken is telling us they have not looked."
- **On the Create Task rules:** "This one is not ours to bend. You sign a statement, College Board investigates, and the consequences are theirs to apply, not mine to waive."

## 8. Differentiation

- **Younger or newer students:** Cut early and cut hard, in Segment 2 rather than hoping. A program with one clear feature, a list, a loop, and a function is a completely legitimate final project for an 8th grader and scores well against this rubric. For the writeup, give them the four-paragraph structure with the first sentence of each paragraph already written, and let them fill in from there. Pair them with an older student for the cold run in Segment 3, since the "works on a fresh terminal" check is the one most likely to defeat them alone.
- **Extensions for advanced or AP-track students:** Have them write tests for their own project using the Week 15 approach, and demo the tests running as part of their five minutes. Have them add a proper README with installation steps and a screenshot. Students on the AP track should treat the Personalized Project Reference as a first draft today and refine it next week, and should read their own written responses against the current College Board scoring guidelines. For anyone genuinely finished, the best use of the remaining time is helping a student who is not, and that counts under participation.

## 9. Common pitfalls

- **New features in Week 31.** The most common and most damaging. Say the rule in Segment 1 and enforce it in every conference: today finishes what exists.
- **Debugging for the student.** Tempting, fast, and it converts their project into yours, which then fails at the demo when they cannot explain a line. Ask questions, point at the traceback, and keep your hands off the keyboard.
- **The cold-run failure discovered on demo day.** Segment 3, step 4 exists entirely to prevent this. Do not skip it even if the room is busy.
- **The writeup describing features instead of layers.** Very common, and it hollows out the capstone. Read over shoulders during Segment 5 and redirect early.
- **The video recorded with narration.** If the current specification forbids narration, and it has, a narrated video is a compliance problem rather than a style problem. Check the current rule during prep and tell students explicitly.
- **The Digital Portfolio not set up.** A student can have a perfect Create Task and no way to submit it. Confirm enrollment and the join code this week, not next.
- **Nine hours not logged.** You must be able to attest to the in-class time. Keep a dated log from Week 27 onward and update it today.
- **A student whose code you cannot follow.** Handle it privately in Segment 2. It is either a student who copied something, or a student who is further ahead than you assumed, and both need a conversation rather than a public surprise.
- **Time slipping from Segment 5.** The workshop is not optional padding. A student who leaves without a draft video or a draft writeup will not produce a good one at home.

## 10. Homework

Full details in `handouts/week-31-homework.md`. In summary: finish the artifact to their written definition of done, complete the writeup, rehearse the demo out loud with a timer at least twice, and finish the repository housekeeping. The handout carries the full rubric and submission checklist so students have both in writing, and the Extra Credit AP Track section carries the Create Task submission checklist and the deadline warning.

## 11. Assessment

### The final project rubric

The final project is 20 percent of the course grade. Score out of 100 and convert. Give students this table in Week 31, not Week 32.

| Component | Points | What earns full marks |
|---|---|---|
| Proposal and scope | 10 | Submitted in Week 27, revised when asked, and the delivered project is recognizably the proposed one at an honest scale |
| Working artifact | 30 | Runs from a clean start, does what it claims, and handles obvious bad input without crashing |
| Technical substance | 20 | Uses a list or other collection that genuinely manages complexity, contains at least one student-written procedure with a parameter that uses both selection and iteration, and the structure fits the problem |
| Five-minute demo | 15 | Runs live, stays within time, explains one piece of code clearly, and answers questions about the code accurately |
| One-page layers writeup | 15 | Names the real layers beneath the project rather than listing features, and is specific about what happens at each |
| Process | 10 | A repository with a README, a license, and a commit history showing incremental work rather than one final dump |

Notes on applying it:

- **The explain-a-line check sits inside the demo score.** Point at a line and ask what it does. A student who cannot explain their own code does not score above 7 out of 15 on the demo regardless of how the program runs, and that is the AI policy's enforcement mechanism rather than any detection tool.
- **Scale is judged against the student, not against the class.** An 8th grader's finished small program and an 11th grader's finished larger one can both score 30 out of 30 on the artifact. Ambition is rewarded in technical substance, not in whether the thing works.
- **Undisclosed AI use** on a non-Create-Task project costs the process points and triggers a re-do of the disclosure comment. Say this in advance so it is a known rule rather than a judgment call.

### The submission checklist, for every student

- [ ] Repository pushed, with all project code in it
- [ ] README saying what it is, what it needs, and the exact command to run it
- [ ] License file, per the Week 30 decision
- [ ] Program runs from a clean clone on a machine that is not theirs
- [ ] One-page writeup committed to the repository or handed in on paper
- [ ] Demo rehearsed with a timer, twice
- [ ] Any AI-assisted code carries a disclosure comment

### The Create Task submission checklist, for AP-track students only

Verify each item against the current official requirements before relying on this list.

- [ ] Program code, complete, as a single PDF per the current specification
- [ ] Video of the program running: shows input, functionality, and output, within the current length and file-size limits, with no identifying information and no narration if narration is still prohibited
- [ ] Personalized Project Reference: screen capture of one list or collection managing complexity, and screen capture of one student-developed procedure with a parameter containing selection and iteration, plus its call
- [ ] All items uploaded to the AP Digital Portfolio through the hosting school's exam-only section
- [ ] Final submit button pressed in the portfolio, which is a separate action from uploading
- [ ] Attestation of original work completed honestly
- [ ] Nine hours of in-class time logged by the instructor

**Verify current AP deadlines and portfolio requirements before relying on any of this.** The submission deadline is in late April but the exact date, the file specifications, the video rules, and the portfolio workflow change from year to year. Read the current version on AP Central and treat this checklist as a prompt, not as an authority.

## 12. AP alignment

This week is Create Performance Task work, which is 30 percent of the AP score and the only place the exam assesses **Practice 6, Responsible Computing**. It is not assessed on the multiple-choice exam at all, which is worth telling AP-track students, because it reframes the task from a chore into a third of their score.

The artifact requirements themselves map onto Big Idea 3 topics students have held since Unit 1: **3.10 Lists** for the collection that manages complexity, **3.13 Developing Procedures** for the student-developed procedure, **3.6 Conditionals** and **3.8 Iteration** for the selection and iteration inside it, and **1.3 Program Design and Development** for the whole process. Nothing new is being taught; the task is an assembly of things they already have.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** its Create Performance Task materials, which sit alongside the Digital Media Processing unit in the long-standing structure, including the mock Create Task, the checklist, and the template. Work the checklist against their own project. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`. This is the whole point of that unit and this is the week for it.

Also point them at the official AP CSP Exam Reference Sheet, `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`, since the written-response portion of the end-of-course exam asks about their own Create Task using this notation.

Nothing here is required of non-AP students, who have a final project rather than a Create Task and no external deadline beyond Week 32.

## 13. Resources used this week

- **AP Create Performance Task official requirements, scoring guidelines, and the current year's deadline:** AP Central, `https://apcentral.collegeboard.org/courses/ap-computer-science-principles`. **Read this during prep and print the current version.** The video specification, the Personalized Project Reference format, and the deadline all change, and this guide should not be the authority for any of them.
- AP Digital Portfolio, for submission: reachable through the student's My AP account once the hosting school's coordinator has issued a join code for an exam-only section. Arrange this well before Week 31; see Section 2 of `curriculum/CS-Curriculum-and-Setup.md` for the homeschool route, the mid-November school ordering deadline, the mid-March late-addition window, the roughly $98 to $101 fee, and homeschool code 970000. Verify all of it for the current year.
- Screen recording: macOS Shift-Command-5, built in. Windows Game Bar with Windows-G, built in. OBS Studio, `https://obsproject.com`, free, if you need more control. Test whichever you are recommending on an actual student machine during prep.
- License selection, from the Week 30 decision: `https://choosealicense.com`
- The final project requirements and its 20 percent weight: Section 3 of `curriculum/CS-Curriculum-and-Setup.md`.
- The extra-credit project tracks, useful for students whose project finished early and who want somewhere to put the energy: Section 9 of the same document.
- CodeAI CSP Unit 9, Create PT Prep (AP-track): `https://studio.code.org/courses/csp-2025/units/9`
