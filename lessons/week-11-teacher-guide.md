# Week 11 Teacher Guide

## 1. Header

- **Week:** 11 of 32
- **Unit:** 3, Programming Like a Professional
- **Theme question:** How do we model something real in code?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Create a dictionary with `{}`, read a value by key, add a new key, change an existing value, and delete a key.
- Explain the difference between a list and a dictionary in one sentence: a list finds things by position, a dictionary finds things by name.
- Test for a key with `in`, and avoid a `KeyError` by using `.get()` with a default.
- Loop over a dictionary with `.items()` and print each key and value.
- Model one real-world record as a nested dictionary, and a collection of records as a dictionary of dictionaries.
- Build a working contact manager that adds, looks up, lists, and deletes contacts.
- Write a maze program that uses a sensor condition, using the AP exam's command names.

## 3. Where this sits

This opens Unit 3, the Tier 1 programming core and the center of gravity of the whole course. Units 1 and 2 gave students the machine model and the basic control constructs; from here to Week 16 the work is sustained programming, and the systems narrative goes quiet until Unit 4.

Weeks 6 and 7 gave students lists, which answer the question "what is at position 3?" Dictionaries answer the different and more common question "what do I know about Marcus?" Nearly all real data is shaped that way, so this week is the hinge between toy programs and programs that model something. Week 12 turns these records into classes, Week 13 asks what shape a container should have, and Week 16's text adventure is built on a dictionary of rooms written this week in miniature.

The Human Robot Maze also returns today at its conditionals stage. Students last used it in Weeks 1 to 3 for pure sequence. From this week forward, use the AP exam's exact command names so the vocabulary is familiar long before anyone sees an exam question.

## 4. Materials and setup

- The taped floor maze: masking tape, about 6 by 6 squares, with a marked start square, a marked goal square, and three or four wall squares. Tape it before students arrive.
- Index cards for the short sequence programs in Round 1, several per team, plus one full sheet of paper per team for Round 2, which is too long for a card.
- A blindfold or a scarf, optional, for the last maze round.
- Each student's laptop with Thonny; projector for live coding.
- Whiteboard with the theme question written large.
- Printed Week 11 homework handout, one per student.
- Optional: a printed one-page dictionary syntax reference for students who want a crutch through the build.

## 5. Pre-class prep checklist

- Tape the floor maze and walk it yourself once as the robot, following a written program literally, to confirm the goal is reachable and the walls actually force a decision. (15 min)
- Write the four AP command names on the board or on a poster you can reuse for the rest of the unit: `MOVE_FORWARD ()`, `ROTATE_LEFT ()`, `ROTATE_RIGHT ()`, `CAN_MOVE (direction)`. (5 min)
- Write and test the contact manager in the scaffolded version students will work from, and decide how much of the menu loop you hand out. (20 min)
- Prepare the live-coding sequence for Segment 3 on the demo machine so you are not inventing keys at the projector. (10 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Write two things on the board: a list of five student names, and a phone contact card. Ask which one you would use to answer "who is third in line" and which to answer "what is Priya's number." Take answers, do not resolve them yet.
- **You do:** Pose the theme question. Point out that everything they have stored so far has been found by position, and almost nothing in the real world is organized that way.
- **Purpose:** Creates the gap that dictionaries fill, before any syntax.

### Segment 2: Human Robot Maze, conditionals stage (0:10 to 0:30), Systems strand

Run this entirely from the steps below. The canonical source is in Section 13 for prep.

1. **Re-establish the two rules out loud.** First, the robot does exactly and only what is written, with no common sense; if the program says forward into a wall, the robot walks into the wall. Second, compile then run: the team writes the whole program first, hands it over, and it executes start to finish with no live steering. When it fails, they fix the written program and run it again from the top.
2. **Switch to the exam vocabulary.** Point at the board and say that from now on the commands have their AP names: `MOVE_FORWARD ()` moves one square in the direction faced, `ROTATE_LEFT ()` and `ROTATE_RIGHT ()` turn 90 degrees in place, and `CAN_MOVE (forward)` is new. Explain that `CAN_MOVE` is not an action; it is a question that answers true or false.
3. **Round 1, sequence only, to reactivate.** Teams of three write a straight sequence of commands from start to goal on an index card. Run two of them. Expect one crash into a wall; that is useful.
4. **Break their program on purpose.** Move one wall by a single square. Re-run the same program without letting them edit it. It fails. Ask what kind of program would have survived the change.
5. **Introduce the conditional form.** Write on the board:

   ```
   IF (CAN_MOVE (forward))
   {
     MOVE_FORWARD ()
   }
   ELSE
   {
     ROTATE_RIGHT ()
   }
   ```

   Read it aloud as one rule: if you can go forward, go; otherwise turn right.
6. **Round 2.** Each team writes that block out twelve times, in order, as their entire program. No loops yet, on purpose. Give them a full sheet of paper rather than an index card, since the block as written on the board is eight lines and twelve copies of it run to about ninety-six, and have the three team members split the copying rather than putting one scribe through all twelve. Copying should take about four minutes; if a team is still writing after five, let them run the copies they have. Hand the sheet to the robot and run it. Most teams reach the goal on a maze they could not fully plan for.
7. **Blind round, optional if time holds.** Have the robot face away between steps or wear the blindfold so the programmers cannot rely on the robot quietly correcting course.
8. **Debrief in two lines.** First, a conditional lets one program handle situations the programmer did not know in advance. Second, ask how they felt writing the same block twelve times, and tell them that next week they get to collapse it.

**Purpose:** Selection becomes physical again before the week's Python work, and the exam's command vocabulary enters use a full year before the exam.

### Segment 3: Dictionaries in Python (0:30 to 0:55), Coding strand part 1

- **You do:** Build the contact idea up at the projector, running after every line:

  ```python
  phones = {"Priya": "555-0143", "Marcus": "555-0198"}
  print(phones["Priya"])
  phones["Ana"] = "555-0177"
  phones["Marcus"] = "555-0200"
  del phones["Priya"]
  print(phones)
  ```
- **You do:** Name the parts deliberately: the braces make a dictionary, each entry is a key and a value separated by a colon, and the key goes in the square brackets where an index used to go. Say plainly that keys are unique, so assigning to an existing key replaces the value rather than adding a second one. Students expect a duplicate; show them there is none.
- **You do:** Crash it on purpose with `print(phones["Nobody"])` and read the `KeyError` out loud. Then show the two defenses:

  ```python
  if "Nobody" in phones:
      print(phones["Nobody"])
  print(phones.get("Nobody", "not in the book"))
  ```
- **You do:** Show iteration:

  ```python
  for name, number in phones.items():
      print(name, "is at", number)
  ```

  Mention `.keys()` and `.values()` briefly, then go back to `.items()`, which is the one they will actually use.
- **Students do:** Build a dictionary of five capital cities keyed by country, print one lookup, add a sixth country, change one value, and print the whole thing with a loop.
- **You do:** Circulate. The predictable errors are square brackets versus braces, a missing colon between key and value, and quoting the key on assignment but not on lookup.

### Segment 4: Modeling a real record (0:55 to 1:10), Coding strand part 2

- **You do:** Ask the class what a contact really holds. They will say phone, email, birthday, nickname. Show that a value can itself be a dictionary:

  ```python
  contacts = {
      "Priya": {"phone": "555-0143", "email": "priya@example.com", "grade": 10},
      "Marcus": {"phone": "555-0198", "email": "marcus@example.com", "grade": 11},
  }
  print(contacts["Priya"]["email"])
  ```
- **You do:** Read the double subscript out loud, left to right: go to Priya's record, then inside it go to email. Draw it on the board as a box inside a box. This picture is what makes nesting click.
- **You do:** Name the design decision in plain language. The outer dictionary is a filing cabinet keyed by name; the inner dictionary is one card in the drawer. A list of dictionaries is the other common shape, and is better when there is no natural unique key.
- **Students do:** Model one real thing of their own choosing as a nested dictionary: a game character with stats, a recipe with ingredients and times, or a playlist entry. One record only, printed once.

### Segment 5: Stretch (1:10 to 1:15)

- A short break. Collect the maze sheets and index cards before they scatter.

### Segment 6: Build the contact manager (1:15 to 1:50), Coding strand part 3

- **You do:** Decompose on the board before anyone types. The jobs are: add a contact, look one up, list them all, delete one, and quit. Point out that each line of that list is a function, exactly as in the Week 5 Hangman decomposition.
- **Students do:** Build it from your skeleton. A reasonable target:

  ```python
  contacts = {}

  def add_contact(book, name, phone):
      book[name] = phone

  def find_contact(book, name):
      return book.get(name, "No contact by that name.")

  def list_contacts(book):
      for name, phone in book.items():
          print(name, phone)
  ```

  The menu loop below that reads a choice with `input`, calls the matching function, and stops on quit.
- **You do:** Circulate hard. Two things to watch for: students who put the whole program inside one giant `if` chain with no functions, and students who forget that `add_contact` changes the dictionary in place and does not need to return it.
- **Extension for anyone who finishes:** store a nested record per contact instead of a bare phone string, and add a search that matches part of a name.

### Segment 7: Wrap and homework (1:50 to 2:00)

- **You do:** Hand out and walk through the homework, including the Extra Credit AP Track section at the end. Exit question at the door: name one thing in this room that is better stored as a dictionary than as a list, and say what the key would be.

## 7. Key scripts and analogies

- **List versus dictionary:** "A list is a row of numbered lockers. A dictionary is a coat check: you hand over a ticket with a name on it and get your thing back. Numbered lockers are great until you have to remember that Marcus is number 14."
- **Keys are unique:** "Two coats cannot share one ticket. If you check a new coat under an old ticket, the old coat is gone."
- **Nesting:** "The outer dictionary is the filing cabinet, the key is the name on the tab, and the value is the whole card inside. `contacts['Priya']['email']` means open the Priya drawer, then read the email line."
- **KeyError:** "Python is not being difficult. You asked for a ticket that was never checked in. `.get()` is the polite version that shrugs instead of shouting."
- **Why this matters:** "Almost every real program is a pile of records with names on them. Your phone, your school's grade book, and every website you have ever logged into are dictionaries underneath."
- **On CAN_MOVE:** "It is not a command, it is a question. The robot is not moving; it is looking."

## 8. Differentiation

- **Younger or newer students:** Keep values simple strings and skip the nested-dictionary segment; a flat name-to-phone book is the full outcome for them. Give them the menu loop complete so all they write is the three functions. Pair them with a student who was solid on Week 7's list iteration, since `.items()` looping is the same muscle.
- **Extensions for advanced or AP-track students:** Convert the contact book to a nested record per person and add an edit command that changes only one field. Add a sort so `list_contacts` prints alphabetically using `sorted(book)`. In the maze, rewrite the twelve-block program as the shortest program that still works and predict how few lines a loop would need next week.

## 9. Common pitfalls

- **Braces versus brackets.** `{}` makes a dictionary, `[]` makes a list, and lookups use `[]` on both. Students mix these for the first hour; expect it and correct it fast rather than discussing it.
- **Assigning to a missing key works, reading a missing key crashes.** This asymmetry surprises everyone. Say it explicitly: writing creates, reading demands.
- **Quoting keys inconsistently.** `contacts[name]` and `contacts["name"]` are different lookups. This produces a `KeyError` that students read as a Python bug.
- **Rebuilding the dictionary instead of updating it.** Watch for students who create a whole new dictionary inside `add_contact`. Ask them to print the book before and after to see it happen.
- **The maze round runs long.** If Segment 2 is going past twenty minutes, cut the blind round, not the debrief. The debrief is the part that transfers.
- **Scope creep in the build.** Students will want to save contacts to a file. File input and output arrives in Week 18. Hold them to a working in-memory core.

## 10. Homework

Full details in `handouts/week-11-homework.md`. In summary: finish the contact manager with lookup and delete working; model one real thing of their choice as a nested dictionary; four short predict-the-output dictionary drills; optional reading in the Python tutorial. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice.

## 11. Assessment

Low-stakes and observational. Walk the room during Segment 6 and check two things per student: a working key lookup, and at least one function that takes the dictionary as a parameter. The exit question tells you who has the list-versus-dictionary distinction, which is the concept that matters most for the rest of the unit.

Homework is a completion check against the weekly-labs rubric. Note anyone who could not get `.items()` iteration working; Week 13's build assumes it.

## 12. AP alignment

This session covers AP CSP topic 3.2 Data Abstraction, and reinforces 3.6 Conditionals through the maze round using the exam's own robot commands.

**Be straight with students about the limits here.** Python dictionaries are not AP CSP exam content. The exam's only collection type is the list, and its lists are 1-indexed rather than 0-indexed. The transferable idea today is data abstraction itself, which is tested: using one named structure to hold many related values instead of a pile of separate variables. When an AP question wants what a dictionary would do, it uses parallel lists, one holding names and another holding values at matching positions. Show that side by side if an AP-track student asks.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** There is no dictionary unit, because dictionaries are not tested. The nearest fit is Unit 2, Programming, and specifically its lessons on lists and data abstraction; treat this as a revisit rather than new ground. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the list and traversal lessons only. This is the exam-shaped version of what we did today.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human Robot Maze, conditionals stage: Segment 2 is complete on its own. Canonical source is CodeAI My Robotic Friends, `https://curriculum.code.org/csf-18/coursee/1/`, with a newer edition under `https://curriculum.code.org/csf-current/`. Review it during prep only if you have not run the maze before and want the demonstration patter. The full progression and the AP command mapping are in `teaching-activities/Unplugged-Logic-Activities.md`. Verify links are live before class; sites reorganize.
- AP robot command names and the pseudocode they appear in: `ap-track/AP-Pseudocode-Bridge.md`, robot commands table.
- Python tutorial section on dictionaries, for your reference and as optional student reading: `https://docs.python.org/3/tutorial/datastructures.html#dictionaries`
- CodeAI CSP Unit 6, Lists, Loops, and Traversals (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
- Unit 3 outline and the build list for this week: Section 5 of `curriculum/CS-Curriculum-and-Setup.md`.
