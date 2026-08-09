# Week 31 Homework: Finish It

This is the last homework of the course that produces something. Next week you demonstrate it. Everything here is aimed at showing up on demo day with a program that works and a story about it that you can tell. Plan on about two to three hours across the week: roughly 60 to 90 minutes finishing the artifact, 30 on the writeup, 20 rehearsing the demo twice, and 15 on the repository.

Do not do it all the night before, because the one thing that always goes wrong is the thing you find on the first clean run.

## 1. Finish the artifact

Look at the definition of done you wrote at the top of your rubric in class. Get there.

Rules for this week, and they matter more than they sound:

- **No new features.** Whatever exists now is the project. Adding something new this week is how a working program becomes a broken one on demo day.
- **Make it survive a stranger.** Run it in a fresh terminal, from a fresh clone, on a machine that is not the one you built it on if you can. Anything that only works because of a file sitting on your desktop is going to fail in front of everyone.
- **Handle at least the obvious bad input.** Somebody will type a word where a number goes. That should print a message, not a traceback.
- **Seed some data.** If your program is boring until eight things have been typed into it, load a sample set at startup so your demo has something to show in the first thirty seconds.

## 2. Write the one page

Four short paragraphs. One page total, and the one-page limit is part of the assignment.

1. **What it does.** Who it is for and what problem it solves. Two or three sentences, no code.
2. **How it works.** The main pieces and how they fit. Name your data structure and your key procedure.
3. **What it stands on.** This is the important one and it is worth more than the other three together.
4. **What you would do next.** What is broken, what you cut, and what version two would be.

For paragraph 3, start at your own code and walk downward and outward. Your Python, then the interpreter that reads it, then the standard library and any packages, then the operating system with its files and processes, then machine code and the CPU. If your project touches the network, keep going: HTTP, TCP, IP, DNS, and whatever is answering on the other end.

Then, for each layer, name one thing you could not have said about it in September. That is what the last thirty weeks were for, and this paragraph is where you prove it.

## 3. Rehearse the demo, out loud, with a timer

Twice. Not once, and not in your head.

The five minutes:

- **0:00 to 0:30, the pitch.** What it does and who it is for. No code on screen.
- **0:30 to 2:30, the live run.** Show it working. Actually run it.
- **2:30 to 4:00, one piece of code.** Open the file. Show one procedure you are proud of. Explain what it does and why you built it that way.
- **4:00 to 5:00, honesty.** What is broken. What you would do next. The hardest bug you fixed and how you found it.

That last minute is graded. "Nothing is broken" is the worst possible answer, because it tells us you have not looked.

You will be asked at least one question about your own code. Point at any line in your project right now and see whether you can explain it. Do that for every line you are unsure about, before next week.

## 4. Repository housekeeping

- [ ] Everything pushed
- [ ] README saying what it is, what it needs installed, and the exact command to run it
- [ ] License file, the one you chose in Week 30
- [ ] Commit history that shows the work happening, not one giant commit at the end
- [ ] Any AI-assisted code carries a comment saying what you asked for and what you changed

## 5. The rubric, so there are no surprises

| Component | Points |
|---|---|
| Proposal and scope | 10 |
| Working artifact: runs clean, does what it claims, survives bad input | 30 |
| Technical substance: a collection that manages complexity, a procedure with a parameter using selection and iteration, a structure that fits the problem | 20 |
| Five-minute demo, including explaining your own code accurately | 15 |
| One-page layers writeup | 15 |
| Process: repository, README, license, commit history | 10 |

Two things about this table worth reading twice. The demo and the writeup together are worth 30, the same as the code. And a small program that is finished scores better than a big one that is not, on every single line.

---

**A reminder on getting help.** AI assistants are permitted on non-AP project work, under the three rules: verify everything, never turn in code you cannot explain, and put a comment at the top saying what you asked for and what you changed. The explain-it rule is not decorative this week. You will be asked to explain a line of your project out loud, in front of the room, and it is part of your demo score.

If you are submitting an AP Create Performance Task, your project is completely AI-free at every stage, including this week, including debugging, right up to the moment you submit. College Board's rule.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

Except that if you are taking the AP exam, this section is not really extra credit this week. The Create Performance Task is 30 percent of your AP score, and this is the week it gets finished.

**Verify everything below yourself.** The video rules, the Personalized Project Reference format, the file specifications, and the deadline all change from year to year. Read the current official requirements at `https://apcentral.collegeboard.org/courses/ap-computer-science-principles` and use that, not this handout, as the authority. If something here disagrees with AP Central, AP Central is right.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** the Create Performance Task materials, including the mock task, the checklist, and the template. Work their checklist against your own project. If the placement on your account does not match what your instructor described, ask; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`. You have been taking this unit a slice at a time since Week 26. This week's slice is the planning and project-development lessons, worked against your own project rather than the unit's example. Do not redo the requirements lessons from Week 27 or the written-response lessons from Week 30. Leave the final review and submission lessons for next week.

**The AP hour.** The supervised hour after class runs this week and next, plus office hours by arrangement. If your logged total is short of nine hours, tell the instructor today so the remaining sessions can be scheduled before you submit.

**Create Task submission checklist.**

- [ ] **Program code.** Complete, as a PDF, in whatever format the current specification requires.
- [ ] **Video.** Your program running, showing input, what it does, and output. Short, small, and within the current length and file-size limits. No identifying information about you. Check the current rule on narration before you record; narration has been prohibited and if it still is, a narrated video is a compliance problem rather than a style choice.
- [ ] **Personalized Project Reference.** Two screen captures from your own code: one list or other collection being used to manage complexity, and one procedure you wrote yourself that takes at least one parameter and contains both an if and a loop, together with a line that calls it.
- [ ] **Uploaded to the AP Digital Portfolio** through your hosting school's exam-only section. If you do not have a join code yet, tell your instructor today.
- [ ] **Final submit pressed.** This is a separate button from uploading. Files sitting in the portfolio unsubmitted do not count, and every year somebody finds this out afterwards.
- [ ] **Attestation completed honestly.** You are stating that the work is yours. It is, so this is easy, but read what you are signing.

**On the deadline.** It is in late April. The exact date moves and your hosting school may set an earlier internal cutoff of its own. Find out both dates this week and write them somewhere you will see them. Do not plan to submit on the last day; portals get slow and files get rejected for format reasons.

**Two last pieces of exam prep, if you want them.**

- The written-response section of the end-of-course exam asks about your own Create Task, in AP pseudocode. Rewrite your key procedure in pseudocode using `ap-track/AP-Pseudocode-Bridge.md` and the official reference sheet at `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`. Watch the indexing; AP lists start at 1.
- Read the current Create Task scoring guidelines and score your own submission against them honestly. Then fix whatever you scored yourself down on. This is the single most effective hour of AP preparation available to you right now.
