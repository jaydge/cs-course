# AP CSP Course and Exam Description: source reference

This is a pointer file, not the document itself. The College Board's AP Computer
Science Principles Course and Exam Description (CED) is copyrighted and is not
stored in this repository. Use this file to find a fact and its page number
without re-fetching or re-reading the whole PDF.

**Source:** `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-course-and-exam-description.pdf`
**Edition:** Effective Fall 2023. 266 pages. Confirmed current as of this check;
College Board revises the CED periodically, so re-verify the edition date before
relying on page numbers below in a future year.
**Last checked against this repo:** August 2026, against a personal copy supplied
for this check. If you need the full text again, re-download from the link above
or supply the PDF for that session.

## Confirmed accurate against the repo

`ap-track/AP-CSP-Topic-Coverage.md`'s five Big Idea exam-weighting percentages
match the CED's Course at a Glance (pp. 26 to 27) exactly:

| Big Idea | CED weighting |
|---|---|
| 1, Creative Development | 10 to 13% |
| 2, Data | 17 to 22% |
| 3, Algorithms and Programming | 30 to 35% |
| 4, Computer Systems and Networks | 11 to 15% |
| 5, Impact of Computing | 21 to 26% |

The 35-topic count used throughout this repo is correct: 4 + 4 + 18 + 3 + 6 = 35.

## Topic page index (Course Framework, Big Idea Guides)

All 35 topics, for citing a specific page rather than searching the PDF again.

**Big Idea 1, Creative Development, p. 34**
1.1 Collaboration, p. 39 · 1.2 Program Function and Purpose, p. 41 ·
1.3 Program Design and Development, p. 43 · 1.4 Identifying and Correcting Errors, p. 46

**Big Idea 2, Data, p. 48**
2.1 Binary Numbers, p. 53 · 2.2 Data Compression, p. 56 ·
2.3 Extracting Information from Data, p. 58 · 2.4 Using Programs with Data, p. 61

**Big Idea 3, Algorithms and Programming, p. 64**
3.1 Variables and Assignments, p. 70 · 3.2 Data Abstraction, p. 72 ·
3.3 Mathematical Expressions, p. 75 · 3.4 Strings, p. 77 ·
3.5 Boolean Expressions, p. 78 · 3.6 Conditionals, p. 80 ·
3.7 Nested Conditionals, p. 82 · 3.8 Iteration, p. 83 ·
3.9 Developing Algorithms, p. 85 · 3.10 Lists, p. 87 · 3.11 Binary Search, p. 90 ·
3.12 Calling Procedures, p. 91 · 3.13 Developing Procedures, p. 94 ·
3.14 Libraries, p. 97 · 3.15 Random Values, p. 98 · 3.16 Simulations, p. 99 ·
3.17 Algorithmic Efficiency, p. 101 · 3.18 Undecidable Problems, p. 103

**Big Idea 4, Computer Systems and Networks, p. 104**
4.1 The Internet, p. 109 · 4.2 Fault Tolerance, p. 112 ·
4.3 Parallel and Distributed Computing, p. 114

**Big Idea 5, Impact of Computing, p. 116**
5.1 Beneficial and Harmful Effects, p. 121 · 5.2 Digital Divide, p. 123 ·
5.3 Computing Bias, p. 124 · 5.4 Crowdsourcing, p. 125 ·
5.5 Legal and Ethical Concerns, p. 126 · 5.6 Safe Computing, p. 128

Appendix 2, the full Conceptual Framework with every learning objective and
essential knowledge statement underneath each topic, starts at p. 226.
The AP CSP Exam Reference Sheet (the pseudocode reference the bridge sheet
mirrors) is Appendix 1, p. 218 to 225.

## Exam structure (p. 170 to 176)

**Section I, multiple choice:** 70 questions total, 65 individual plus one set
of 5 questions tied to a reading passage about a computing innovation. Weighted
by Computational Thinking Practice, not by Big Idea:

| Practice | Weighting |
|---|---|
| 1, Computational Solution Design | 18 to 25% |
| 2, Algorithms and Program Development | 20 to 28% |
| 3, Abstraction in Program Development | 7 to 12% |
| 4, Code Analysis | 12 to 19% |
| 5, Computing Innovations | 28 to 33% |

Practice 6, Responsible Computing, is not assessed in the multiple-choice section.

**Section II, Create Performance Task:** assesses Practices 1 through 4 across
six rubric rows, split between the submitted program itself (Skill 2.B, twice)
and three written responses (Program Design/Function/Purpose, Algorithm
Development, Errors and Testing, Data and Procedural Abstraction).

## Create Performance Task requirements (Student Handouts, p. 202 to 209)

**Class time:** a minimum of 9 hours of class time is provided to complete and
submit the task. This matches the "9 required hours" language already used in
`curriculum/CS-Curriculum-and-Setup.md` and the Week 27 to 32 guides.

**Three submission components:**
1. Program code, as one PDF containing all code including comments, created
   independently or with a partner.
2. A video demonstrating the program running: input, at least one piece of
   functionality, and output. Created independently, no collaboration.
   Format is .webm, .mp4, .wmv, .avi, or .mov. Maximum 1 minute long, maximum
   30 MB. No voice narration (text captions are allowed) and no distinguishing
   information about the student.
3. Code Segments for the Personalized Project Reference, created independently.

**What the student-developed program code must contain**, all required:
- input from the user, a device, an online data stream, or a file
- at least one list or other collection type, used to manage program complexity
  or help fulfill the program's purpose, in a way that is justified: the
  abstraction should make the program easier to develop or easier to maintain,
  not just present
- at least one procedure that contributes to the program's purpose, with a
  defined name, parameters, and a return type if applicable. Built-in or
  library procedures such as event handlers or a main method do not count as
  student-developed.
- an algorithm using sequencing, selection, and iteration inside that procedure
- a call to the student-developed procedure
- output, in any form: visual, audible, tactile, or textual

This checklist is worth checking directly against the Week 27 proposal form and
the Week 31 to 32 rubric and submission checklist when Unit 6 is reviewed, since
it is the actual grading bar rather than a paraphrase of it.

## Not yet checked against the repo

This pass verified the Big Idea weightings and pulled the structural facts
above. It did not cross-check every individual topic's essential-knowledge
statements against what each weekly guide claims to cover, and it did not
check the Computational Thinking Practice weightings against anything in the
repo, since nothing currently cites them. Worth doing during the Unit 6 review
if AP alignment claims in Weeks 27 to 32 turn out to need it.
