# Week 4 Teacher Guide

## 1. Header

- **Week:** 4 of 32
- **Unit:** 1, Thinking Like a Computer Scientist
- **Theme question:** Why do programming languages exist? (Mystery Day)
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Write a `for` loop over a range of numbers and explain what each part does.
- Write a `while` loop with a condition that eventually becomes false, and say what would make it run forever.
- Choose between a `for` loop and a `while` loop for a given problem.
- Import and use a library, specifically `random.randint()`, and explain in one sentence what a library is and why one exists.
- Build a working calculator and a Rock Paper Scissors game.

## 3. Where this sits

Week 3 gave programs a fork; this week gives them repetition, which is the second of the three big control ideas. Students arrive having written deliberately repetitive code twice already (the five-bit converter in Week 2, three sequential guesses in Week 3), so loops land as relief rather than abstraction. The `import random` moment is the first time students use code somebody else wrote, which is the AP Libraries topic and the seed for every later import. Functions in Week 5 complete the set, and the Mystery Day question motivates the whole idea of a language sitting above the machine.

## 4. Materials and setup

- Whiteboard with the theme question written large.
- Each student's laptop with Thonny; projector for live coding.
- Printed Week 4 homework handout, one per student.
- The taped floor maze from Week 3 if it is still down, for the optional loop round.
- Optional for Mystery Day: the Apple IIe at the BASIC prompt, and a printed line of assembly or Python bytecode from `dis` to hold up.

## 5. Pre-class prep checklist

- Write and test the calculator and Rock Paper Scissors builds on the demo machine, including the loop versions. (15 min)
- Prepare the infinite-loop demo and make sure you can stop it cleanly in Thonny (the stop button, or Control-C in the shell). Practice once. (5 min)
- For Mystery Day, decide your three-layer example and have it ready: one line of Python, the same idea in assembly, and the machine code. Keep it to one slide or one board diagram. (10 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up (0:00 to 0:10)

- **You do:** Put trace problem (b) from last week's homework on the board and have the class talk through it. Answer any conditional questions still lingering.
- **You do:** Show their Week 3 guessing game with three copy-pasted guess blocks, and ask what would happen if they wanted twenty guesses. Let the groan happen. That is the motivation for today.

### Segment 2: Loops in Python (0:10 to 0:45), Coding strand

- **You do:** At the projector, start with the simplest `for` loop and narrate every part:

  ```python
  for i in range(5):
      print(i)
  ```

  Point out that it prints 0 through 4, not 1 through 5. Do not gloss over this; write both on the board. Then show `range(1, 6)` and `range(0, 10, 2)`.
- **Students do:** Print the numbers 1 to 10, then the even numbers to 20, then a countdown from 5 using `range(5, 0, -1)`.
- **You do:** Introduce the `while` loop as the other shape: "a `for` loop runs a known number of times; a `while` loop runs until something becomes true."

  ```python
  total = 0
  while total < 20:
      total = total + 3
      print(total)
  ```
- **You do:** Deliberately run an infinite loop (`while True:` printing something, or a `while` whose variable never changes) and let it fill the screen for a few seconds before stopping it. Ask what was missing. This is the single most useful thing they will remember about `while`.
- **Students do:** Rewrite their Week 2 five-bit binary converter using a loop, or if that is too much, rewrite the Week 3 guessing game so the player keeps guessing until correct. The second is the better choice for most students and feeds Segment 4.

### Segment 3: Libraries and randomness (0:45 to 1:05)

- **You do:** Ask how the computer could pick a number it does not already know. Introduce the idea before the syntax: somebody else already wrote code that does this, it ships with Python, and you can borrow it.

  ```python
  import random
  n = random.randint(1, 10)
  ```
- **You do:** Name the parts: `import` brings in a library, `random` is the library's name, `randint` is a function inside it, and `random.randint(1, 10)` includes both 1 and 10. Say plainly that a library is a collection of prewritten code you can use without knowing how it works inside, and that this is how all real software gets built.
- **Students do:** Add `import random` to the guessing game so the secret number changes every run. Combined with the Segment 2 loop, they now have a real game.

### Segment 4: Stretch (1:05 to 1:10)

### Segment 5: Mystery Day, why do programming languages exist? (1:10 to 1:25), Systems strand

- **You do:** Hold up the three layers. Show one line of Python they wrote today. Then show roughly what the machine actually executes: a handful of numeric instructions. Then say that in between sits a translator.
- **You do:** Make the point concrete. Ask them to imagine writing today's guessing game in nothing but numbers, and then imagine changing it. Languages exist because humans cannot hold machine code in their heads, and because a program written once should run on more than one machine.
- **You do:** If the Apple IIe is available, boot it and show BASIC alongside Python on the projector. Forty years apart, same idea: a human-readable line that becomes machine action. Tell them Week 10 opens this box properly with the `dis` module.
- **Purpose:** A fifteen-minute wow segment that motivates the entire systems arc without teaching any new syntax.

### Segment 6: Build the calculator and Rock Paper Scissors (1:25 to 1:55)

- **Students do, build one:** A calculator that asks for two numbers and an operator, then prints the result. It needs conditionals for the operator choice and, wrapped in a `while` loop, keeps going until the user types `quit`. Guard the divide-by-zero case with an `if`; that conversation is worth having.
- **Students do, build two:** Rock Paper Scissors against the computer, using `random` for the computer's throw and conditionals to decide the winner. Loop it for best of five and keep score in two variables.
- **You do:** Circulate. Most students will get one of the two finished; that is the expectation, not both. Pair anyone stuck.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out homework, noting the Extra Credit AP Track section. Exit question: what makes a `while` loop run forever?

## 7. Key scripts and analogies

- **Why loops:** "You already wrote the same three lines three times. A loop is how you say 'do that again' without saying it again. Every time you find yourself copying and pasting code, a loop is probably the answer."
- **`for` versus `while`:** "Use `for` when you know how many times: read twenty pages. Use `while` when you know the stopping condition but not the count: read until you fall asleep."
- **`range(5)`:** "Python starts counting at zero, so `range(5)` gives you 0, 1, 2, 3, 4. Five numbers, just not the five you expected. You will trip on this; everyone does."
- **Infinite loops:** "A `while` loop is a promise that something inside will eventually make the condition false. Break that promise and the program runs until you stop it."
- **Libraries:** "Somebody already solved this and left the solution where you can pick it up. You do not need to know how `randint` works inside, only what it gives you. That is most of professional programming."
- **Why languages exist:** "The machine only understands numbers. You only understand words. A programming language is the treaty between the two."

## 8. Differentiation

- **Younger or newer students:** Stick to `for` loops with `range` and skip `while` beyond seeing the demo; the guessing-game loop can be a `for` loop with a fixed number of tries. Give the calculator as a fill-in-the-blanks skeleton. One finished build is a full week's work.
- **Extensions for advanced or AP-track students:** Add input validation that reloops on bad input; use a nested loop to print a multiplication table (this previews Week 9); track and report a win percentage in Rock Paper Scissors; explore what else is in the `random` library with `dir(random)` in the shell.

## 9. Common pitfalls

- **Off-by-one with `range`.** Expect it constantly this week. Write the produced sequence on the board every time you use `range` in a new form.
- **Infinite `while` loops.** Make sure every student knows how to stop a running program in Thonny before Segment 2 ends, or you will spend the session force-quitting.
- **Indentation drift inside loops.** A line that should be inside the loop sitting outside it produces baffling behavior. Have students read their indentation out loud when confused.
- **`random.randint` bounds.** Students assume it excludes the top value, by analogy with `range`. It does not; both ends are included. Say this explicitly, and note that AP pseudocode's `RANDOM(a, b)` behaves the same way.
- **Trying to finish both builds.** Set the expectation up front that one working build beats two broken ones.

## 10. Homework

Full details in `handouts/week-04-homework.md`. In summary: finish whichever build was not completed in class; trace two loop programs on paper; a short written answer on why programming languages exist; optional Crash Course episode; the Extra Credit AP Track section closes the handout.

## 11. Assessment

Observational during the builds, plus the homework traces. The specific thing to look for is whether a student can say, before running, how many times a loop will execute. That predicts the rest of Unit 3 better than anything else this week. Homework is a completion check against the weekly-labs rubric.

## 12. AP alignment

This session covers AP CSP topics 3.8 Iteration, 3.14 Libraries, and 3.15 Random Values, and continues 3.6 Conditionals through both builds. The `random.randint(1, 10)` behavior matches AP pseudocode's `RANDOM(1, 10)` exactly, including both endpoints, which is worth naming for AP-track students now.

**AP-track self-study for this week, and only this week's slice.** One matching unit below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming. Work only the iteration lessons this week, picking up where Week 3 stopped. Procedural abstraction later in the same unit is next week's slice. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the loops lessons only. Note that this CodeAI unit bundles loops with lists, and lists do not arrive in our course until Week 6, so stop when the material turns to lists and come back to it then.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Optional loop round of the Human Robot Maze: if the tape grid is still down, add `REPEAT n TIMES` to the command set from Week 3 and have groups collapse a long path into a short program. Full progression in `teaching-activities/Unplugged-Logic-Activities.md`; the canonical source is CodeAI's My Robotic Friends, `https://curriculum.code.org/csf-18/coursee/1/`, teacher video `https://youtu.be/M_qD3hPXrVQ`.
- Python `random` module documentation, for your own reference: `https://docs.python.org/3/library/random.html`
- Crash Course Computer Science, Episode 11 ("The First Programming Languages"), which pairs directly with the Mystery Day segment. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Unit 6 (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
- AP pseudocode equivalents for loops and `RANDOM`: `ap-track/AP-Pseudocode-Bridge.md`
