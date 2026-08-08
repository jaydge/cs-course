# Week 3 Homework: Instructions and Decisions

This week your programs learned to make decisions. The homework practices writing precise instructions and reading code in your head. Plan on about 30 to 45 minutes.

## 1. Write instructions a robot could follow

Pick one everyday task: tying a shoe, brushing your teeth, or making a bowl of cereal. Write the instructions one step per line, precise enough that someone who has never done it could follow them exactly and succeed.

Then read your own instructions back as literally as you can and find at least one step that could go wrong. Mark it and fix it. Finding your own bug is the point.

## 2. Trace these on paper

Do not run these in Thonny. Work out the answer with a pencil first, then check if you want.

**a.**
```python
x = 8
if x > 10:
    print("big")
else:
    print("small")
```

**b.**
```python
score = 75
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```

**c.**
```python
age = 15
has_ticket = False
if age >= 12 and has_ticket:
    print("Come in")
else:
    print("Not yet")
```

For each one, write down what gets printed and one sentence on why.

## 3. Improve your guessing game

Open the number-guessing game you built in class. Make two changes:

- After a wrong guess, print how far off they were. (Hint: you want the difference, and it should never be negative. Think about which number to subtract from which, using an `if`.)
- Add a welcome message at the start that uses the player's name.

Save it into your CS Class folder.

## 4. Watch, if you want (optional)

Crash Course Computer Science, Episode 12, covers statements and functions in about eleven minutes: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

## 5. Typing practice (optional)

About 15 minutes at `typing.com` or `keybr.com`.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming. Work only the lessons on sequencing, selection, and conditionals, then stop. Iteration comes next week. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 4, Variables, Conditionals, and Functions, at `https://studio.code.org/courses/csp-2025/units/4`. Do the conditionals lessons only.

**Extra practice if you want it.**

- The AP exam asks robot-on-a-grid questions using the same idea as our floor maze, but with the command names `MOVE_FORWARD()`, `ROTATE_LEFT()`, `ROTATE_RIGHT()`, and `CAN_MOVE(direction)`. Rewrite your group's maze program from class using those exact names.
- Trace problem 4 in `ap-track/AP-Pseudocode-Bridge.md`, which is an AP-style conditional. Notice that AP pseudocode writes `=` where Python writes `==`, the reverse of the trap from class today.
