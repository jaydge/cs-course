# Week 4 Homework: Loops and Borrowed Code

This week your programs learned to repeat themselves, and you used code somebody else wrote for the first time. Plan on about 30 to 45 minutes.

## 1. Finish your build

In class you started a calculator and Rock Paper Scissors, and most people finished one. Finish the other one at home, or improve the one you finished.

Whichever you do, it should use a loop so the program keeps going until the player chooses to stop. Save it into your CS Class folder.

## 2. Trace these on paper

Pencil first, then check in Thonny if you want.

**a.** How many lines does this print, and what is the last one?
```python
for i in range(3):
    print("row", i)
```

**b.** What is the value of `total` when this finishes?
```python
total = 0
for n in range(1, 5):
    total = total + n
print(total)
```

**c.** This one has a bug. What does it do, and what single line would fix it?
```python
count = 10
while count > 0:
    print(count)
```

## 3. Short answer

In two or three sentences: why do programming languages exist at all, if the computer only understands numbers? Write it in your own words and save it as a file in your CS Class folder.

## 4. Watch, if you want (optional)

Crash Course Computer Science, Episode 11, "The First Programming Languages," goes with today's Mystery Day question: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

## 5. Typing practice (optional)

About 15 minutes at `typing.com` or `keybr.com`.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming. Work only the iteration lessons, picking up where you stopped last week. Stop before procedural abstraction; that is next week. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the loops lessons only, and stop when it turns to lists. We reach lists in Week 6, and you can come back to the rest then.

**Extra practice if you want it.**

- AP pseudocode writes loops as `REPEAT n TIMES` and `REPEAT UNTIL (condition)`. Rewrite trace problems (a) and (b) above in AP pseudocode. The tables in `ap-track/AP-Pseudocode-Bridge.md` show the translation.
- Work trace problems 3 and 9 in that same bridge sheet. Problem 9 is a `REPEAT UNTIL` loop, the pseudocode version of the `while` loop from class.
- One thing worth knowing for the exam: `random.randint(1, 10)` in Python and `RANDOM(1, 10)` in AP pseudocode both include 1 and 10. This is different from `range(1, 10)`, which stops at 9. Try all three and convince yourself.
