# Week 15 Teacher Guide

## 1. Header

- **Week:** 15 of 32
- **Unit:** 3, Programming Like a Professional
- **Theme question:** How do you know it actually works?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Read a multi-frame Python traceback, name the error type, identify the line where Python stopped, and explain which frame called which.
- Name and recognize seven common error types: `SyntaxError`, `IndentationError`, `NameError`, `TypeError`, `IndexError`, `KeyError`, and `AttributeError`.
- Distinguish an error that crashes from a bug that runs and gives the wrong answer, and choose a different tactic for each.
- Write an `assert` statement, group several into a test function, and run it.
- Choose at least one edge case for a function they wrote and test it.
- Build a working Tic-Tac-Toe game with at least three passing tests.
- Debug a program written by someone else.

## 3. Where this sits

Week 5 introduced debugging when students had produced enough of their own errors for it to mean something. Ten weeks later they have produced far more, and their programs are now big enough that "just read the code" has stopped working. This is the week the course switches from finding bugs by inspection to finding them by method.

Testing is new here and is the professional half of the unit's title. Everything students have built so far was verified by running it and looking at the screen. That does not scale past about fifty lines, and the Week 16 text adventure is the first program where it will visibly fail them. Writing tests one week before the big build is deliberate.

The Human Robot Maze returns at its functions stage, and today it doubles as a bug hunt: teams debug a program written by another team, which is a skill no amount of debugging your own code teaches.

## 4. Materials and setup

- The taped floor maze. Retape a 6 by 6 grid with a start, a goal, and three or four walls if it came up.
- Index cards for maze programs, several per team.
- Each student's laptop with Thonny; projector for live coding.
- Whiteboard with the theme question written large.
- The error-type table from Segment 3, printed as a poster before class and posted where it stays visible all session.
- Printed Week 15 homework handout, one per student.
- Printed copies of three prepared broken programs, one per pair. See the prep checklist.
- Two AP pseudocode trace problems written on the board before students arrive.

## 5. Pre-class prep checklist

- Write two trace problems from `ap-track/AP-Pseudocode-Bridge.md` on the board for the warm-up. Problems 5 and 7 are good choices, since both punish a Python indexing habit. (5 min)
- Prepare three broken programs, printed, each with exactly one bug: one that crashes with a clear traceback across two functions, one that crashes with a `TypeError` or `AttributeError` inside a class method, and one that runs cleanly and produces a wrong answer. Reuse student code from Weeks 11 to 13 where you can; it lands harder. (20 min)
- Write and test the Tic-Tac-Toe skeleton and its three tests in the exact form you will hand out, and decide how much of the game loop students get. (25 min)
- Confirm the maze layout and pick the one deliberate bug you will plant in the swapped programs. (10 min)
- Refresh yourself on Thonny's debugger: Control-F5 to start stepping, F6 for a big step, F7 for a small step. (5 min)
- Print homework handouts, the broken programs, and the error-type poster. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **Students do:** The two pseudocode trace problems on the board, on paper, in silence. Four minutes.
- **You do:** Take answers and resolve them at the board, spending most of the time on any 1-indexing error. Say once more that this is the highest-frequency mistake on the exam, and move on. This warm-up repeats next week; the value is in repetition, not in discussion.
- **You do:** Collect the halting-problem paragraphs from homework and read one good one aloud if you have a willing student.
- **You do:** Pose the theme question. Ask how each of them currently knows a program works. The honest answer is "I ran it and it looked right." Accept that answer and then take it apart.

### Segment 2: Human Robot Maze, functions stage and bug hunt (0:10 to 0:30), Systems strand

Run this from the steps below. The canonical source is in Section 13 for prep.

1. **Restate the two rules once.** The robot does exactly what is written with no common sense, and the whole program is written before it runs, with no live steering.
2. **Introduce the functions stage.** Tell teams they may now define one named procedure of their own and use it by name. Model one on the board:

   ```
   PROCEDURE TURN_AROUND ()
   {
     ROTATE_RIGHT ()
     ROTATE_RIGHT ()
   }
   ```

   Then use it inside a larger program so they see the name substituting for the steps, exactly as in Week 5.
3. **Round 1, ten minutes.** Teams of three write a program using a loop, a conditional, and at least one procedure of their own definition. They write it on an index card with their team name on it.
4. **Swap the cards between teams.** Each team now holds a program they did not write.
5. **Plant a bug before you hand them over.** Change one line on each card yourself: delete a `ROTATE_RIGHT ()`, swap a left for a right, or move the closing brace of the procedure. Do not tell them what you changed.
6. **Round 2, the hunt.** Each team must find and fix the bug in the program they received, by reading it, before running it. Only then do they run it with a robot.
7. **Debrief in two questions.** First: was it harder to debug someone else's program than your own, and why? Second: what would have made it easier? Steer the second answer to two things, better names and shorter procedures, then say that professionals spend most of their working lives reading code they did not write.

**Purpose:** Procedures land physically for the third time, and reading unfamiliar code becomes a named skill rather than an occasional accident.

### Segment 3: Reading a traceback properly (0:30 to 0:50), Coding strand part 1

**Budget this segment.** Steps 1 through 7 are yours and should take ten minutes together, which means the traceback reading is unhurried and the Thonny walkthrough really is ninety seconds. Step 8 is the students' and needs the remaining ten. If you find yourself at 0:45 still talking, skip step 7 and go straight to the pairs; the debugger is a Week 5 reminder and the pair debugging is the objective.

1. **Run the crashing program at the projector.** Use one with two functions so the traceback has two frames:

   ```python
   def average(numbers):
       return sum(numbers) / len(numbers)

   def report(data):
       print("Average:", average(data))

   report([])
   ```
2. **Read the traceback out loud, bottom up.** The last line names the error type and gives the message: `ZeroDivisionError: division by zero`. The lines above are the call stack, printed oldest first. Point at each frame and say who called whom: the module called `report`, `report` called `average`, and `average` is where it died.
3. **Connect it to Week 13.** That call stack is a stack, the same last-in-first-out pile of plates. Python prints it from the bottom of the pile upward, which is why the line you care about is usually last.
4. **Say the thing students most need to hear.** The line Python reports is where the problem was *noticed*, not always where the mistake was *made*. Here the mistake is at `report([])`, three lines away from the reported crash.
5. **Put the error-type list up** and leave it there all session. Print it as a poster before class rather than writing it out live; seven rows costs three or four minutes at the whiteboard and this segment does not have them. Read it aloud instead, one row at a time, which is where the value is:

   | Error | What it usually means |
   |---|---|
   | `SyntaxError` | Typed wrong. Missing colon, bracket, or quote |
   | `IndentationError` | Wrong number of spaces |
   | `NameError` | Used a name that does not exist, usually a typo |
   | `TypeError` | Mixed types, or the wrong number of arguments to a function or method |
   | `IndexError` | List index past the end |
   | `KeyError` | Dictionary key that is not there |
   | `AttributeError` | Asked an object for something it does not have |

   Note that the last three are new since Week 5 and are direct products of Unit 3's dictionaries, lists, and classes. Expect someone to point out that the crash you just demonstrated, `ZeroDivisionError`, is not on the list. Say why: these seven are the ones they will meet constantly and should recognize on sight, and Python has dozens more that all read the same way once you know where to look on the traceback. Recognizing the shape matters more than memorizing the catalogue.
6. **Show the silent bug.** Run a program that produces a wrong answer with no traceback at all. Ask where it goes wrong; nobody can say. Add prints on every variable, run again, and watch where reality diverges from expectation. Name the tactic: when the program lies, make it show its work.
7. **Step through the same program with Thonny's debugger.** Control-F5, then F6 and F7, watching the variables panel. Ninety seconds is enough; they saw this in Week 5 and need the reminder, not the tour.
8. **Students do, in pairs:** Each pair takes one of the three prepared broken programs, names the error type, identifies the actual mistake as opposed to the reported line, and fixes it.

### Segment 4: Stretch (0:50 to 0:55)

- A short break. Collect the maze cards and the broken-program printouts, and leave the error-type poster up.

### Segment 5: Writing tests (0:55 to 1:20), Coding strand part 2

- **You do:** Start from the problem, not the tool. Put a function on the projector and ask how they would check it:

  ```python
  def is_even(n):
      return n % 2 == 0
  ```

  They will say run it and print. Do that, three times, by hand. Then ask what happens when there are twelve functions and they change one.
- **You do:** Introduce `assert` as a sentence that must be true:

  ```python
  assert is_even(4) == True
  assert is_even(7) == False
  ```

  Run it: nothing happens. Say plainly that silence is success. Then break the function on purpose and run again so they see the `AssertionError` and understand that a failing test is the point of the exercise.
- **You do:** Group them into a test function and call it:

  ```python
  def test_is_even():
      assert is_even(4) == True
      assert is_even(7) == False
      assert is_even(0) == True
      print("is_even tests passed")

  test_is_even()
  ```
- **You do:** Teach edge cases with one question: what inputs are most likely to break this? Collect answers and write them on the board as a general list: zero, an empty list or string, one item, a negative number, the very first and very last positions, and something of the wrong type entirely. Point out that `is_even(0)` is exactly such a case and that they would never have tried it by hand.
- **You do:** Give the professional framing in two sentences. A test is a claim about your code that the computer rechecks for free, forever. The value shows up not today but in three weeks, when you change something and the test tells you what you broke.
- **Students do:** Write tests for two functions they already wrote, one from the Week 11 contact manager and one from the Week 13 stack. At least one test must be an edge case, for example popping from an empty stack.
- **You do:** Circulate. Watch for tests that assert nothing useful, such as `assert True`, and for students calling the test function but never running the file.

### Segment 6: Build Tic-Tac-Toe with tests (1:20 to 1:50), Coding strand part 3

- **You do:** Decompose on the board before anyone types: make an empty board, show the board, make a move, decide whether anyone has won, decide whether the board is full, and swap the current player. Six jobs, six functions.
- **You do:** Hand out the skeleton. Represent the board as a list of nine strings, which reuses Week 6 indexing directly:

  ```python
  LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6)]

  def new_board():
      return [" "] * 9

  def winner(board):
      for a, b, c in LINES:
          if board[a] != " " and board[a] == board[b] and board[b] == board[c]:
              return board[a]
      return None

  def is_full(board):
      for square in board:
          if square == " ":
              return False
      return True
  ```
- **Students do:** Complete the game loop and write at least three tests. A reasonable target for the test function:

  ```python
  def test_winner():
      assert winner(["X", "X", "X", " ", " ", " ", " ", " ", " "]) == "X"
      assert winner([" "] * 9) is None
      assert winner(["O", " ", " ", " ", "O", " ", " ", " ", "O"]) == "O"
      print("winner tests passed")

  test_winner()
  ```
- **You do:** Circulate hard. Prioritize students whose tests do not run at all over students whose game does not run; the tests are today's objective and the game is the vehicle.
- **Extension for anyone who finishes:** write a test for `is_full` on a board with exactly one blank square left, and a test that a move cannot be played on an occupied square.

### Segment 7: Wrap and homework (1:50 to 2:00)

- **You do:** Hand out and walk through the homework, including the Extra Credit AP Track section. Remind AP-track students that next week opens with two more pseudocode trace problems. Exit question at the door: name one edge case for your `winner` function that you have not tested yet.

## 7. Key scripts and analogies

- **Reading a traceback:** "Read it bottom up. The last line says what went wrong. The lines above say how Python got there, oldest call first. It is a stack, the same pile of plates from two weeks ago, printed for you at the moment of the crash."
- **Reported line versus actual mistake:** "The traceback tells you where the program fell over, not where it was pushed."
- **Crash versus silent bug:** "A crash is a program with the decency to tell you it failed. A wrong answer with no error message is the expensive kind."
- **`assert`:** "A sentence you claim is true about your code. If it is true, nothing happens and that is good news. If it is false, Python stops and points."
- **Why test at all:** "You already test. You run the program and squint at the screen. A test is the same check, written down once, so the computer redoes it every time from now on for free."
- **Edge cases:** "Bugs live at the edges. Zero, empty, one, the first, the last, and the thing nobody thought to type. The middle of the range almost always works."
- **Debugging someone else's code:** "Most of your professional life will be spent reading code written by strangers, including the stranger you were six months ago."

## 8. Differentiation

- **Younger or newer students:** Two tactics are enough, read the error and add prints; the debugger can wait again. Give them the Tic-Tac-Toe game loop complete so they write only the tests, which is today's real objective anyway. One test with two assertions is a full outcome.
- **Extensions for advanced or AP-track students:** Have them write a test that currently fails, then fix the code until it passes, which is the test-first order used professionally. Have them write a `make_move` function that refuses an occupied square and prove the refusal with a test. The strongest can look at `unittest` in the standard library and report back in one sentence on how it differs from bare asserts; do not teach it to the class.

## 9. Common pitfalls

- **Reading the traceback top down.** Students look at the first line, see a filename, and give up. Insist on bottom up every single time until it is automatic.
- **Fixing the reported line rather than the cause.** The `average([])` example exists to inoculate against this. Use it.
- **Tests that pass because they assert nothing.** `assert winner(board)` passes for any non-empty string. Require an explicit `==` or `is` comparison.
- **Writing the test function and never calling it.** Same pitfall as Week 5's functions defined but never called, and it produces the same "nothing happens." Check for the call line first.
- **Comparing to `None` with `==`.** Both work, but teach `is None` and say why in one sentence: it asks whether it is that exact object, which is the correct question for `None`.
- **Believing tests prove correctness.** Say plainly that tests show the presence of bugs, not their absence. A passing suite means the cases you thought of work.
- **Tic-Tac-Toe scope creep.** Someone will want an unbeatable computer opponent. That is a fine extra-credit project and a bad use of the last thirty minutes. Hold them to two human players and three passing tests.

## 10. Homework

Full details in `handouts/week-15-homework.md`. In summary: finish Tic-Tac-Toe with at least three passing tests; read three tracebacks and name the error type, the reported line, and the actual mistake; write a test that catches a bug in a supplied function and then fix the function; optional rewatch of the Week 5 debugging material. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice.

## 11. Assessment

Two specific checks during Segment 6. First, does the student's test function actually run and print its success line? Second, can the student point at one assertion and say what would have to break for it to fail? The second question separates students who wrote tests from students who copied them.

The exit question about an untested edge case is a good indicator of whether the edge-case idea landed, which is the part most likely to be lost.

Homework is a completion check against the weekly-labs rubric. The traceback exercise is the one to grade carefully; the ability to name the actual mistake rather than the reported line is the week's transferable skill and it will be assessed again on the Unit 3 checkpoint next week.

## 12. AP alignment

This session directly covers AP CSP topic 1.4 Identifying and Correcting Errors, and reinforces 1.3 Program Design and Development and 3.13 Developing Procedures through the Tic-Tac-Toe decomposition.

Note how the exam tests this. It does not ask you to run a debugger. It shows a short program or procedure and asks what it displays, or which input produces the wrong result, or which of four fixes corrects it. That is exactly the skill practiced in Segment 3 and in the maze bug hunt: reading unfamiliar code carefully and predicting what it does. Hand-tracing is the exam technique, so the pseudocode warm-ups are doing double duty.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming, specifically its lessons on program development, testing, and identifying and correcting errors. Work only that testing and debugging material and stop. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`. Its lessons build and debug procedures that other people will call, which is the closest fit to today. Its Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`, also carries testing and debugging practice if you want a second pass.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human Robot Maze, functions stage: Segment 2 is complete on its own. Canonical source is CodeAI My Robotic Friends, `https://curriculum.code.org/csf-18/coursee/1/`, with a newer edition under `https://curriculum.code.org/csf-current/`. The full progression is in `teaching-activities/Unplugged-Logic-Activities.md`. Verify links are live before class; sites reorganize.
- Thonny's debugger: Control-F5 to start stepping, F6 for a big step, F7 for a small step. Feature overview at `https://thonny.org`.
- Python tutorial on errors and exceptions, for your reference: `https://docs.python.org/3/tutorial/errors.html`. The `assert` statement itself is documented at `https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement`.
- AP pseudocode trace problems used as the warm-up: `ap-track/AP-Pseudocode-Bridge.md`.
- CodeAI CSP Units 7 and 3 (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/7` and `https://studio.code.org/courses/csp-2025/units/3`
- The Week 5 guide's debugging segment, for the three original tactics: `lessons/week-05-teacher-guide.md`.
