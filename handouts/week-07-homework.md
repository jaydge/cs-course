# Week 7 Homework: From Gates to a Machine, and Lists That Change

This week you built an adder out of nothing but NAND gates, and you learned how to add things to a list, take things out, and walk through it. Plan on about 40 minutes.

## 1. Finish the adder (or prove you understood it)

If you did not reach the adder level in nandgame during class, finish it at home at `https://nandgame.com`. It is free, needs no account, and runs in a browser.

Important: the game saves your progress in the browser on the machine you played on. If you played on a school laptop, your progress is on that laptop. Starting over at home is fine and honestly goes fast the second time.

If you already finished the adder, replay any one level and write down two things: which parts you had built earlier and reused, and what that level would have taken if you had to build everything from raw NAND gates every time.

## 2. One written answer

In two or three sentences: what makes a circuit able to remember something? You built gates last week that just react to whatever is on their inputs right now. What changes when a gate's output is fed back into its own input?

## 3. List methods

Write a program that starts with this list:

```python
animals = ["cat", "dog", "owl"]
```

Then, in order, and printing the list after each step so you can see what happened:

- Add "fox" to the end.
- Remove "dog".
- Add "bat" to the end.
- Print how many animals are in the list.
- Print `True` or `False` for whether "owl" is in the list, using `in`.
- Sort the list alphabetically and print it one last time.

Save it into your CS Class folder.

## 4. Find the largest, the hard way

Given this list:

```python
readings = [12, 45, 7, 88, 23, 61]
```

Write a loop that finds the largest number and prints it. Do not use `max()`. The trick is to keep a variable holding the best value you have seen so far, and update it whenever you find something bigger.

When it works, change the list to some other numbers and run it again to be sure it was not a fluke.

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episode 5 ("How Computers Calculate: the ALU"), Episode 6 ("Registers and RAM"), and Episode 7 ("The Central Processing Unit"). Episode 5 covers the adder you built today. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

Being honest about this week: the systems half is not AP material. Latches, registers, the ALU, and the fetch-decode-execute cycle are not tested on the AP CSP exam, and neither is anything you did in nandgame. Do it because it is one of the best things in the course, not for exam points. The AP value this week is entirely in the coding half, and list traversal is one of the most heavily tested things on the whole exam.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming. Keep going in the same unit and work the list-traversal and iteration lessons that follow the lists material from last week. This week the instruction is simply to keep working the programming unit, since our systems content is not on the exam. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the traversal lessons, which finish the unit you started back in Week 4.

**Extra practice if you want it.**

- Rewrite your question 4 largest-number loop in AP pseudocode, using `FOR EACH item IN list`. The tables are in `ap-track/AP-Pseudocode-Bridge.md`. Then compare yours with trace problem 11 in that sheet, which is the same algorithm.
- Work trace problems 6, 7, and 8 in the bridge sheet. They cover `APPEND`, `REMOVE`, and `INSERT`, and every one of them is designed to punish a Python habit. Watch the 1-indexing.
- On the exam, "traverse a list and count how many items meet a condition" is a question shape you will see more than once. Write it once yourself: loop through `readings` from question 4 and print how many values are above 20.
