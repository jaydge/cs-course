# Week 5 Homework: Functions and Finding Bugs

This week you learned to name a block of code and reuse it, and you learned three ways to hunt down a bug. That finishes Unit 1. Plan on about 40 minutes.

## 1. Finish Hangman

Get your game working end to end: it picks a word, shows blanks, accepts letters, reveals correct guesses, and ends when the player wins or runs out of tries.

It must use at least two functions. If yours currently works but has no functions, that counts as not done; pull two pieces out into functions and call them.

Save it into your CS Class folder.

## 2. Refactor something older

Open your Rock Paper Scissors game or your calculator from Week 4. Find a chunk of code that does one identifiable job and pull it out into a function with a good name.

Write one sentence at the top of the file, as a comment starting with `#`, saying what you moved and why. Then run it to be sure it still works.

## 3. Debug these

Each program below has one bug. Write down the error type if there is one, the line, and the fix.

**a.**
```python
def double(n):
    return n * 2

print(dubble(5))
```

**b.**
```python
def add(a, b):
    print(a + b)

total = add(2, 3)
print("The total is", total)
```
(Hint: this one runs without an error message but still misbehaves. What does it print, and why?)

**c.**
```python
def countdown(n):
while n > 0:
    print(n)
    n = n - 1
```

## 4. Watch, if you want (optional)

Crash Course Computer Science, Episode 12, covers statements and functions: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

## 5. Typing practice (optional)

About 15 minutes at `typing.com` or `keybr.com`.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

Also worth saying, now that Unit 1 is done: be ready to explain any line of your Hangman game out loud. If you can explain it, you own it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming. Work only the procedural abstraction lessons, which finish the unit you started in Week 3. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 4, Variables, Conditionals, and Functions, at `https://studio.code.org/courses/csp-2025/units/4`. Do the functions lessons to finish that unit. If you want more, Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`, matches today's parameter and return work.

**Extra practice if you want it.**

- AP pseudocode writes a function as `PROCEDURE name (a, b) { ... RETURN (expr) }`. Rewrite your `double` function and one Hangman function in AP pseudocode using the tables in `ap-track/AP-Pseudocode-Bridge.md`.
- Work trace problem 10 in that bridge sheet, which calls a procedure inside a loop.
- Unit 1 is finished, so you now have every idea the AP exam calls Big Idea 3 basics: variables, expressions, conditionals, iteration, and procedures. Skim the topic list in `ap-track/AP-CSP-Topic-Coverage.md` and mark which ones you feel solid on. Bring any you are unsure about to class.
