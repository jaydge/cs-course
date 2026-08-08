# Week 15 Homework: Debugging and Testing

This week you stopped checking your programs by squinting at the screen and started checking them on purpose. Plan on about 45 minutes.

## 1. Finish Tic-Tac-Toe

Get the game working end to end: two human players take turns, the board is displayed after every move, and the game ends on a win or on a full board.

It must also have a test function with at least three assertions in it, and that test function must be called so it actually runs. At least one of your three tests must cover an edge case, for example an empty board or a board with one square left.

If your game works but has no tests, that counts as not done. Save it into your CS Class folder.

## 2. Read these tracebacks

For each one, write down three things: the error type, the line Python reported, and what you think the actual mistake was. Remember that those last two are often not the same line.

**a.**
```
Traceback (most recent call last):
  File "contacts.py", line 8, in <module>
    show(book, "Dana")
  File "contacts.py", line 5, in show
    print(book[name])
KeyError: 'Dana'
```

**b.**
```
Traceback (most recent call last):
  File "pets.py", line 12, in <module>
    biscuit.feed(2)
TypeError: Pet.feed() takes 1 positional argument but 2 were given
```
(Reminder: `self` counts as one of those positional arguments.)

**c.**
```
Traceback (most recent call last):
  File "printer.py", line 10, in <module>
    print(next_job(jobs))
  File "printer.py", line 6, in next_job
    return q.pop(0)
IndexError: pop from empty list
```

For each one, also write one sentence saying how you would prevent it from happening again, rather than just making this run go away.

## 3. Write a test that finds the bug

Here is a function that is supposed to say whether a Tic-Tac-Toe board is full. It has a bug.

```python
def is_full(board):
    for square in board:
        if square == " ":
            return False
        else:
            return True
```

Do it in this order, and do not skip step 1:

1. Write a test with at least two assertions that fails on this version of the function. Run it and watch it fail.
2. Fix the function.
3. Run your test again and watch it pass.
4. Write one sentence describing what the bug actually was.

That order, test first and then fix, is how professionals do it. The failing test is proof that your test is capable of catching something.

## 4. Optional

If tracebacks still feel unreadable, reread the errors and exceptions page of the Python tutorial: `https://docs.python.org/3/tutorial/errors.html`. The first two sections are enough.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

Be ready to point at any one of your assertions and say what would have to break for it to fail. If you can explain it, you own it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

Today maps cleanly to a real exam topic, 1.4 Identifying and Correcting Errors. Worth knowing how it is actually tested: the exam never asks you to use a debugger. It shows you a short procedure and asks what it displays, or which input makes it give the wrong answer, or which of four proposed fixes is correct. That is hand-tracing under time pressure, which is the same skill you practiced reading someone else's maze program in class.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming, and specifically its lessons on program development, testing, and identifying and correcting errors. Work only that material and stop. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`. Its lessons build and debug procedures meant to be called by other people, which is the closest fit. If you want a second pass, Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`, also carries testing and debugging practice.

**Extra practice if you want it.**

- Work trace problems 3, 4, and 9 in `ap-track/AP-Pseudocode-Bridge.md`. Trace them on paper with a column for every variable. Two more trace problems open next class, so this is direct preparation.
- Take one AP pseudocode trace problem you got wrong at any point and write down exactly where your reasoning left the rails. Most exam mistakes are the same three or four habits repeating, and finding yours is worth more than doing twenty more problems.
- Take your `winner` function from Tic-Tac-Toe and rewrite it in AP pseudocode. You will hit the 1-indexing problem immediately, since your winning lines are written with Python indexes. Renumber them correctly and you have done exactly the translation the exam expects you to be able to read.
