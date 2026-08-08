# Week 3 Teacher Guide

## 1. Header

- **Week:** 3 of 32
- **Unit:** 1, Thinking Like a Computer Scientist
- **Theme question:** How do we tell a computer what to do?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Write a precise, ordered sequence of instructions for a task and find the ambiguity in someone else's.
- Explain what an algorithm is and break a problem into smaller steps (decomposition).
- Write a Python `if` / `elif` / `else` statement that chooses between paths.
- Use the comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and combine conditions with `and`, `or`, and `not`.
- Build and run a working number-guessing game that responds "too high" or "too low."

## 3. Where this sits

Weeks 1 and 2 gave students a file system and a program that runs top to bottom. This week the program gains a fork in the road, which is the first genuinely new idea in programming rather than a new piece of syntax. The unplugged work comes first and is physical: the Human Robot Maze at its sequence stage, which makes "the computer does exactly what you said, not what you meant" visible in the room. Conditionals here set up loops in Week 4 and functions in Week 5, and the number-guessing game becomes the shell that Week 4's loop drops into.

## 4. Materials and setup

- Masking or painter's tape, enough for a grid of about 6 by 6 squares on the floor. Lay it before class if you can.
- Index cards for writing programs, several per group.
- Bread, peanut butter, a plate, and a knife for Robot Chef, if you did not run it in Week 1.
- Whiteboard with the theme question written large.
- Each student's laptop with Thonny; projector for live coding.
- Printed Week 3 homework handout, one per student.
- Optional: a blindfold or a paper bag for the later maze round.

## 5. Pre-class prep checklist

- Tape the floor grid, marking a start square, a goal square, and three or four wall squares. (15 min)
- Walk the maze yourself once as the robot, following a written program, so you know the pacing and where students will trip. (10 min)
- If running Robot Chef, watch the classic "exact instructions" demonstration during prep so your comic literalism lands; the activity depends entirely on your performance. See Section 13. (10 min)
- Write and test the number-guessing game on the demo machine, in the no-loop version students will build. (10 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and review (0:00 to 0:10)

- **You do:** Two binary numbers on the board to read aloud as a class, keeping Week 2 warm. Then collect a show of hands: whose greeting program worked?
- **You do:** Pose the theme question. Point out that so far their programs do the same thing every time. Today the program starts making decisions.

### Segment 2: Robot Chef, unplugged (0:10 to 0:25)

Skip this segment if you already ran it in Week 1; go straight to Segment 3 and give the maze the extra time.

1. **Set up in front of the class.** Bread, peanut butter jar, plate, knife on a table. Announce that you are a robot and will do exactly what the instructions say, nothing more.
2. **Collect instructions.** Ask students to call out steps for making a peanut butter sandwich, and write each one on the board as given, without improving it.
3. **Execute literally and comically.** "Put the peanut butter on the bread" means setting the closed jar on top of the loaf. "Open the jar" without "pick up the jar" means struggling with a jar on the table. Never correct them; just fail visibly and wait.
4. **Let them revise.** Students rewrite the failed step with more precision. Run it again. Repeat two or three cycles until a sandwich actually happens or nearly does.
5. **Name what happened.** They wrote an algorithm, found bugs by running it, and fixed them. That loop is the whole job. Also name decomposition: "make a sandwich" turned out to be a dozen smaller steps.

### Segment 3: Human Robot Maze, sequence stage (0:25 to 0:55)

Run from these steps; the canonical version and its teacher video are in Section 13 for prep.

1. **Introduce the command set.** Write exactly three commands on the board and allow no others: `MOVE FORWARD` (one square, in the direction faced), `TURN LEFT` (90 degrees, in place), `TURN RIGHT` (90 degrees, in place).
2. **Pick the robot and the programmers.** One student stands on the start square facing a direction everyone agrees on. The rest work in groups of three or four.
3. **State the two rules that make this teach programming.** First, the robot does exactly and only what is written, with no common sense; if the program says forward into a wall, the robot walks into the wall. Second, and more important, **compile then run**: groups write the entire program on index cards first, hand it over, and it executes start to finish with no changes mid-run. No live steering.
4. **Model one short program yourself.** Write a three-command program on the board for a simple two-square path and have the robot run it, saying each command aloud as it executes. Students need to see the read-execute rhythm once.
5. **Groups write and run.** Each group writes a full program from start to goal, then hands it to a robot from another group. Programmers stay silent during execution. When it fails, the group fixes the written program and runs it again from the top.
6. **Debrief the bugs.** Ask what went wrong and why nobody noticed while writing. The usual answers are a forgotten turn and an off-by-one count of forward moves. Name that second one; they will meet it again all year.
7. **The blindfold round, if time allows.** Have the robot face away or wear a blindfold so it cannot quietly self-correct. Groups discover how much they were relying on the robot being a person.

**Note for later:** this same maze returns in Unit 3 with conditionals, loops, and functions added. Leave the tape down if the room allows.

### Segment 4: Stretch (0:55 to 1:00)

### Segment 5: Conditionals in Python (1:00 to 1:30), Coding strand

- **You do:** At the projector, start from a variable and add a fork:

  ```python
  age = int(input("How old are you? "))
  if age >= 13:
      print("You can sign up.")
  else:
      print("You need a parent to sign up.")
  ```

  Name each part out loud: the condition, the colon, the indented block. Stress that indentation is not decoration in Python; it is how the language knows what is inside the `if`.
- **You do:** Add an `elif` branch, then show the comparison operators on the board as a set. Flag the single trap: `=` assigns, `==` compares. Deliberately type `if age = 13:` so they see the error once.
- **Students do:** Write a program that asks for a number and prints whether it is positive, negative, or zero. That is three branches, so it needs `if`, `elif`, and `else`.
- **You do:** Introduce `and`, `or`, `not` with a quick truth-table on the board, then have students extend their program to say "single digit" when a number is between 0 and 9.

### Segment 6: Build the number-guessing game (1:30 to 1:55)

- **You do:** Frame the build. The computer picks a number, the player guesses, the program says too high, too low, or correct.
- **Students do:** Build it with a fixed secret number (say 7) and exactly three guesses written out one after another, since loops do not arrive until next week. The repetition is deliberate and will make Week 4 land.

  ```python
  secret = 7
  guess = int(input("Guess a number from 1 to 10: "))
  if guess == secret:
      print("Correct!")
  elif guess > secret:
      print("Too high.")
  else:
      print("Too low.")
  ```
- **You do:** Circulate. Common breakages are forgetting `int()` around `input`, inconsistent indentation, and `=` for `==`.
- **Students do:** Save to the CS Class folder.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out homework, noting the Extra Credit AP Track section at the end. Exit question: what is the difference between `=` and `==`?

## 7. Key scripts and analogies

- **Algorithm:** "A recipe. An ordered list of steps precise enough that someone who has never done the task can follow it and get the right result."
- **Decomposition:** "Nobody writes 'make a sandwich' in one step. You break it into pieces small enough that each one is obvious. That is most of what programming is."
- **The literal robot:** "The computer has no idea what you meant. It only knows what you said. That is not the computer being stupid; that is the computer being exact."
- **Compile then run:** "Writing the whole program before you run it is what makes this programming instead of a remote control. Real code does not get steered mid-flight; it gets fixed and run again."
- **Conditionals:** "A fork in the road. The program reaches it, checks the condition, and takes exactly one path."
- **Indentation:** "The indent is how Python knows which lines are inside the `if`. Other languages use braces; Python uses whitespace, and it is not optional."
- **`=` versus `==`:** "One equals sign puts something in the box. Two equals signs asks whether two things match. Mixing them up is the single most common beginner bug."

## 8. Differentiation

- **Younger or newer students:** Give them the robot role first in the maze; it is the easiest entry and they still see the logic. For the coding, provide the guessing game with the structure printed and blanks to fill in, rather than a blank editor. Two branches instead of three is fine.
- **Extensions for advanced or AP-track students:** Have them make the maze harder by adding a square that can only be entered from one direction. In code, have them nest one `if` inside another and predict the output before running, or add input validation that rejects guesses outside 1 to 10.

## 9. Common pitfalls

- **Groups steering the robot mid-run.** This is the most common failure and it destroys the point of the activity. Enforce silence during execution from the first round.
- **The maze taking the whole session.** Cap it at 30 minutes even if groups want another turn. The conditionals segment is the week's core.
- **`if` conditions with a single `=`.** Expect it. Show the error message rather than just correcting the line.
- **Indentation mixing tabs and spaces.** Thonny handles this reasonably, but if a student's code looks right and still errors, check for a stray tab.
- **Forgetting `int()`.** Comparing a string to a number gives a confusing result or an error. Tie it back to Week 2's sandwich-photo analogy.

## 10. Homework

Full details in `handouts/week-03-homework.md`. In summary: write precise instructions for an everyday task; trace three short conditional programs on paper; extend the guessing game with a friendlier message; optional Crash Course episode; the Extra Credit AP Track section closes the handout.

## 11. Assessment

Observational plus the homework trace problems, which are the best early signal of who can follow code in their head. Watch during Segment 5 for students who can predict the output before running rather than running and reading. Homework is a completion check against the weekly-labs rubric.

## 12. AP alignment

This session covers AP CSP topics 3.5 Boolean Expressions, 3.6 Conditionals, and 3.9 Developing Algorithms, and begins 3.7 Nested Conditionals. The Human Robot Maze is direct practice for the exam's robot-on-a-grid question type; from Unit 3 onward we switch to the exam's exact command names (`MOVE_FORWARD`, `ROTATE_LEFT`, `ROTATE_RIGHT`, `CAN_MOVE`), which are listed in `ap-track/AP-Pseudocode-Bridge.md`.

**AP-track self-study for this week, and only this week's slice.** One matching unit below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming. Work only the lessons on sequencing, selection, and simple conditionals. Stop before iteration, which lines up with our Week 4. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 4, Variables, Conditionals, and Functions, at `https://studio.code.org/courses/csp-2025/units/4`. Do the conditionals lessons only.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human Robot Maze: Segment 3 is complete on its own. The canonical version is CodeAI's My Robotic Friends unplugged lesson, with a symbol key and printables, at `https://curriculum.code.org/csf-18/coursee/1/` (newer edition under `https://curriculum.code.org/csf-current/`). The teacher video is at `https://youtu.be/M_qD3hPXrVQ`. Watch it during prep if you want to see the classroom management modeled; you do not need it to run Segment 3.
- Robot Chef: fully inline in Segment 2. It is a performance, so rehearse the literal-failure bit during prep.
- Full activity descriptions and the year's maze progression: `teaching-activities/Unplugged-Logic-Activities.md`.
- Crash Course Computer Science, Episode 11 ("Programming Languages") or Episode 12 ("Programming Basics: Statements and Functions"), optional homework viewing. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Unit 4 (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/4`
