# Week 5 Teacher Guide

## 1. Header

- **Week:** 5 of 32
- **Unit:** 1, Thinking Like a Computer Scientist
- **Theme question:** How do we stop repeating ourselves?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Define a function with `def`, call it, pass it arguments, and return a value.
- Explain why a function exists: naming a block of steps so it can be reused and understood.
- Read a Python traceback and identify the line number and the error type.
- Use three debugging moves: read the error, print intermediate values, and step through with Thonny's debugger.
- Build a working Hangman game that uses at least two functions.
- Demonstrate Unit 1 mastery on the checkpoint: binary conversion and basic Python.

## 3. Where this sits

This is the last week of Unit 1 and completes the control trio: sequence, selection, iteration, and now abstraction. Functions are the idea that makes every later unit possible, since data structures, classes, and the final project all assume them. Debugging gets its first formal treatment here rather than being left implicit, because students have now generated enough of their own errors for the skill to mean something. The Unit 1 checkpoint closes the unit, and Hangman is the capstone build that exercises everything from Weeks 1 through 5 at once.

## 4. Materials and setup

- Printed Unit 1 checkpoint, one per student (see Section 11 for what it covers).
- Each student's laptop with Thonny; projector for live coding.
- Whiteboard with the theme question written large.
- Printed Week 5 homework handout, one per student.
- Optional: index cards for the unplugged function warm-up.
- Optional: the taped floor maze if still down, for the functions round.

## 5. Pre-class prep checklist

- Write the checkpoint and print it. Keep it to about 15 minutes of work: four or five binary conversions, three short trace questions, and one "find the bug" item. (20 min)
- Write and test the Hangman build, in the scaffolded version students will work from. Decide how much of the skeleton you hand out. (20 min)
- Practice Thonny's debugger once: Control-F5 to start stepping, F6 for a big step, F7 for a small step. If you have not used it, spend five minutes here; it is the segment students remember. (10 min)
- Prepare three broken programs for the debugging segment, one with a syntax error, one with a name error, and one with a logic error that runs but gives the wrong answer. (10 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up, an unplugged function (0:00 to 0:10)

1. Ask the class to give you the steps for "turn around" using only the maze commands from Week 3. They will say `TURN RIGHT`, `TURN RIGHT`.
2. Write it on the board and draw a box around it. Give the box a name: `TURN AROUND`.
3. Now say `TURN AROUND` and have a student do it. Then use it twice in a longer program.
4. Land the idea before any syntax: you just made a new command out of old commands, gave it a name, and used the name instead of the steps. That is a function.

### Segment 2: Functions in Python (0:10 to 0:50), Coding strand

- **You do:** Start with the simplest possible function and build up in four steps at the projector, running after each:

  ```python
  def greet():
      print("Hello!")

  greet()
  ```

  Then add a parameter, then a second parameter, then a return value:

  ```python
  def add(a, b):
      return a + b

  answer = add(3, 4)
  print(answer)
  ```
- **You do:** Name each part deliberately: `def`, the function name, the parameters in parentheses, the indented body, and `return`. Make the distinction between *defining* a function (writing the recipe) and *calling* it (cooking the meal). Show that defining it alone prints nothing, which surprises students.
- **You do:** Show the difference between `print` inside a function and `return` from a function, side by side. This is the single most confused point of the week; spend real time here.
- **Students do:** Write three small functions and call each: one that takes a name and prints a greeting, one that takes two numbers and returns the larger, and one that takes a number and returns True if it is even. The third one previews the boolean-returning helpers they will need in Hangman.
- **You do:** Circulate. Watch for functions defined but never called, and for a missing `return` in a function whose value is being assigned.

### Segment 3: Debugging (0:50 to 1:15)

1. **Read the error.** Put your prepared syntax-error program on the projector and run it. Read the traceback out loud from the bottom up: the last line names the error type, the line above gives the line number. Say plainly that the reported line is where Python noticed the problem, which is sometimes one line after the actual mistake.
2. **Name the common error types.** Write on the board: `SyntaxError` (typed wrong), `NameError` (used a name that does not exist, often a typo), `TypeError` (mixed a string and a number, the Week 2 trap), `IndentationError`. Four names covers nearly everything they will hit this year.
3. **Print your way in.** Run the logic-error program, the one that produces a wrong answer with no error message. Ask where it goes wrong; nobody can tell. Add `print()` calls showing the value of each variable partway through, run again, and the culprit becomes obvious. Name this: when the program lies to you, make it show its work.
4. **Step through it.** Now do the same program with Thonny's debugger: Control-F5, then F6 and F7 to step. Watch the variables panel change. This is where students see that the computer is doing one small thing at a time, which many still do not fully believe.
5. **Students do:** Hand each pair one broken program and have them fix it using whichever of the three moves fits.

### Segment 4: Stretch (1:15 to 1:20)

### Segment 5: Build Hangman (1:20 to 1:45)

- **You do:** Decompose it on the board before anyone types. Ask what the pieces are and write the list: pick a secret word, track guessed letters, show the word with blanks, check a guess, count wrong guesses, decide win or lose. Point out that each line of that list is a candidate function.
- **Students do:** Build it with at least two functions, working from your skeleton. A reasonable target:

  ```python
  import random

  def pick_word():
      words = ["python", "binary", "loop", "function"]
      return random.choice(words)

  def show_progress(secret, guessed):
      display = ""
      for letter in secret:
          if letter in guessed:
              display = display + letter
          else:
              display = display + "_"
      return display
  ```

  The main loop below that asks for a letter, adds it to `guessed`, and stops on win or on six wrong guesses.
- **You do:** Circulate hard. This build uses everything from the unit and some students will need the main loop given to them so they can focus on the functions.

### Segment 6: Unit 1 checkpoint (1:45 to 2:00)

- **Students do:** Complete the checkpoint individually, no laptops. About 15 minutes.
- **You do:** Collect it. Hand out homework as students finish, noting the Extra Credit AP Track section.

## 7. Key scripts and analogies

- **Why functions:** "You have written the same few lines three times now. A function lets you write it once, give it a name, and use the name forever after. Naming a thing is how you stop thinking about its insides."
- **Define versus call:** "Writing a recipe is not cooking. `def` writes the recipe down. Calling the function cooks it. A recipe you never cook produces no dinner and no error message either."
- **`print` versus `return`:** "`print` shows a value to the human. `return` hands a value back to the program. If you `print` when you meant to `return`, you can see the answer but your program cannot use it."
- **Parameters:** "The blanks in the recipe. `add(a, b)` says: I need two numbers, and I will call them `a` and `b` while I work."
- **Reading a traceback:** "Read it bottom up. The last line tells you what kind of problem. The line above tells you where Python was standing when it noticed. Those are two different things."
- **Print debugging:** "When the program will not tell you what is wrong, make it tell you what it knows. Put a print on every variable and watch where reality diverges from what you expected."
- **On being stuck:** "Every professional programmer spends most of their time on code that does not work yet. That is not the bad part of the job; that is the job."

## 8. Differentiation

- **Younger or newer students:** Functions with no parameters and no return first; add parameters only when that is solid. Give the Hangman main loop complete and ask them to write only `show_progress`. For debugging, the read-the-error and add-a-print moves are enough; the stepper can wait.
- **Extensions for advanced or AP-track students:** Have them add a function that validates input (rejects non-letters and repeated guesses), refactor the whole game so the main body is five function calls, or add a scoring function. If the maze is still taped down, have them define a named procedure like `GO AROUND WALL` and use it twice in a maze program.

## 9. Common pitfalls

- **Functions defined but never called.** The program runs, prints nothing, and the student concludes their function is broken. Check for this first whenever a student says "nothing happens."
- **Confusing `print` and `return`.** The most common conceptual error of the week. When a student's function "works" but the value cannot be used downstream, this is why.
- **Indentation of the function body.** Everything inside `def` must be indented. A body at zero indentation gives an `IndentationError` immediately, which is at least an honest failure.
- **Hangman scope creep.** Students want graphics, scorekeeping, and a word list from a file. Hold them to a working core first.
- **Checkpoint anxiety.** Say clearly that it is low-stakes and diagnostic. It counts under the unit-checkpoint slice of the grade, not as a test students should be nervous about.

## 10. Homework

Full details in `handouts/week-05-homework.md`. In summary: finish Hangman; refactor an earlier program to use a function; a short debugging exercise; optional Crash Course episode; the Extra Credit AP Track section closes the handout.

## 11. Assessment

**Unit 1 checkpoint**, administered in Segment 6 and covering: decimal-to-binary and binary-to-decimal conversion, one compression question (lossless versus lossy), three short traces using a conditional and a loop, and one find-the-bug item. Score it against the unit-checkpoint component of the grade. It is diagnostic as much as evaluative; a weak binary result points at the Section 11 place-value scaffold, and a weak trace result points at pairing that student deliberately in Unit 3.

Also observational: whether each student can explain, in their own words, what one of their Hangman functions does. That explanation is the AI-policy enforcement mechanism as much as it is the assessment.

## 12. AP alignment

This session covers AP CSP topics 3.12 Calling Procedures, 3.13 Developing Procedures, and 1.4 Identifying and Correcting Errors, and consolidates 3.9 Developing Algorithms through the Hangman decomposition. The checkpoint covers 2.1 and 2.2 from Week 2.

**AP-track self-study for this week, and only this week's slice.** One matching unit below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming. Work only the procedural abstraction lessons, which finish the unit begun in Weeks 3 and 4. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 4, Variables, Conditionals, and Functions, at `https://studio.code.org/courses/csp-2025/units/4`. Do the functions lessons, finishing the unit started in Week 3. Students wanting more can look ahead to Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`, which matches the parameter and return material from today.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Unplugged function warm-up: fully inline in Segment 1, no materials needed beyond the board. The fuller version, defining a named sub-sequence in the floor maze, is the functions stage of the Human Robot Maze progression in `teaching-activities/Unplugged-Logic-Activities.md`; canonical source CodeAI My Robotic Friends, `https://curriculum.code.org/csf-18/coursee/1/`.
- Thonny's debugger: Control-F5 to start stepping, F6 for a big step, F7 for a small step. Feature overview at `https://thonny.org`. Practice once during prep if you have not used it.
- Python tutorial section on defining functions, for your own reference: `https://docs.python.org/3/tutorial/controlflow.html#defining-functions`
- Crash Course Computer Science, Episode 12 ("Programming Basics: Statements and Functions"), optional homework viewing. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Units 4 and 7 (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/4` and `https://studio.code.org/courses/csp-2025/units/7`
