# Week 6 Homework: Gates and Lists

This week you built three logic gates out of real parts and met your first data structure. The homework practices both halves. Plan on about 35 to 45 minutes.

## 1. Truth tables on paper

Fill in the output column for each. No computer needed.

**AND**

| A | B | Output |
|---|---|---|
| 0 | 0 | |
| 0 | 1 | |
| 1 | 0 | |
| 1 | 1 | |

**OR**

| A | B | Output |
|---|---|---|
| 0 | 0 | |
| 0 | 1 | |
| 1 | 0 | |
| 1 | 1 | |

**NOT**

| A | Output |
|---|---|
| 0 | |
| 1 | |

**Now a combination.** An AND gate's output is fed into a NOT gate. Fill in the final output for all four input combinations. This gate has a name; if you can work out what people call it, write that down too.

## 2. One written answer

In two or three sentences: what is a transistor, and why does a computer need billions of them instead of a few? Write it in your own words. If you use the word "switch" you are on the right track.

## 3. Lists in Python

Write a new program that does all of this:

- Makes a list of at least five items (numbers, words, whatever you like).
- Prints the whole list.
- Prints the first item and the last item.
- Prints how many items the list has, using `len()`.
- Changes one item to something else, then prints the list again so the change is visible.

Save it into your CS Class folder.

## 4. Finish the gate lookup program

In class you started this:

```python
and_table = [0, 0, 0, 1]
a = int(input("Input A (0 or 1)? "))
b = int(input("Input B (0 or 1)? "))
print("AND output:", and_table[a * 2 + b])
```

Finish it so it also prints the OR result and the NOT result for input A. You will need two more lists. The NOT table only has two rows, so think about which index to use for it.

When it works, answer this in a comment at the top of the file: why does `a * 2 + b` give the right row number?

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episode 2 ("Electronic Computing") and Episode 3 ("Boolean Logic and Logic Gates"). Episode 3 is the one that matches today exactly. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

Worth knowing what does and does not count here. The breadboard, the transistors, and the wiring are not on the AP exam; AP CSP does not test hardware internals. The boolean logic and the lists are on it, and both are heavily tested, so that is what this week's slice covers.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming, and one topic within it: making a list, reading and changing an element by index, and list length. Stop when the lessons turn to traversing a list; that is next week's slice. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Back in Week 4 you were told to stop when this unit turned from loops to lists. This is the week to pick it back up. Do the lists lessons and stop before traversals, which are next week's slice.

**Extra practice if you want it.**

- The exam calls today's gates boolean expressions and writes them as `a AND b`, `a OR b`, and `NOT a`. Rewrite each of your three truth tables as a one-line boolean expression, then write the same three in Python using `and`, `or`, and `not`.
- The big list trap: AP pseudocode lists start at index 1, Python lists start at index 0. Read the Lists section of `ap-track/AP-Pseudocode-Bridge.md`, then work trace problems 5 and 6. Problem 5 exists specifically to catch people who trace it with Python habits.
- Write the boolean expression for the gate you identified in question 1's combination, using `NOT` and `AND`. Then check whether `NOT (a AND b)` gives the same answers as `(NOT a) OR (NOT b)`. If it does, you have just discovered a real law of boolean algebra; look up whose name is on it.
