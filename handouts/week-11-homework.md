# Week 11 Homework: Dictionaries and Modeling Real Data

This week you learned to store things by name instead of by position, which is how almost all real data is organized. Plan on about 40 minutes.

## 1. Finish the contact manager

Get it working end to end. It must be able to:

- add a contact,
- look one up by name and say something sensible when the name is not there,
- list every contact,
- delete a contact,
- quit cleanly.

It must use at least three functions, and each of them must take the contact dictionary as a parameter rather than reaching for a global.

Save it into your CS Class folder.

## 2. Model something real

Pick a real thing and model one of it as a nested dictionary: a game character with stats, a recipe with ingredients and a cook time, a bike with its specs, a song with its artist and length. Anything, as long as it has at least four fields and at least one of those fields is itself a dictionary or a list.

Then print two things from inside it, one of them from the nested part. Write one comment line at the top saying what you chose and why a dictionary suits it better than a list.

## 3. Predict, then run

Write down what each snippet prints before you run it. Then run it and note anything that surprised you.

**a.**
```python
stock = {"apples": 4, "pears": 2}
stock["apples"] = 7
stock["plums"] = 1
print(stock)
print(len(stock))
```

**b.**
```python
scores = {"Ana": 90, "Ben": 82}
print(scores.get("Cleo", 0))
print(scores["Cleo"])
```

**c.**
```python
ages = {"cat": 3, "dog": 5, "fish": 1}
for animal, age in ages.items():
    if age > 2:
        print(animal)
```

**d.**
```python
book = {"Priya": {"phone": "555-0143", "grade": 10}}
print(book["Priya"]["grade"])
print(book["Priya"]["email"])
```

For b and d, one line crashes. Name the error type and say in one sentence why Python refuses.

## 4. Read, if you want (optional)

The dictionaries part of the official Python tutorial is short and clear: `https://docs.python.org/3/tutorial/datastructures.html#dictionaries`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**A straight warning about this week.** The AP slice is thin here, thinner than most weeks, and you should know why. Python dictionaries are not on the AP CSP exam. The exam has exactly one collection type, the list, and its lists start counting at 1, not 0. So today's syntax will not appear on the test. What does appear is the idea underneath it, data abstraction: keeping many related values in one named structure instead of scattering them across separate variables. That idea is tested, and you just used it hard.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** There is no dictionary unit, because dictionaries are not tested. The nearest fit is Unit 2, Programming, and specifically the lessons on lists and data abstraction. Treat it as review. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the list and traversal lessons only, and stop there.

**Extra practice if you want it.**

- Rewrite your contact book using two parallel lists instead of a dictionary: one list of names, one list of phone numbers, matched by position. Write a lookup that walks the names list, finds the position, and returns the number at the same position in the other list. That is how an AP exam question would have to do it, and doing it once tells you exactly what a dictionary saves you.
- In that parallel-list version, write down which line would change if the list started counting at 1 instead of 0. We will come back to this in Week 13, and it is the single most common wrong answer on the exam.
- Look at the robot commands table in `ap-track/AP-Pseudocode-Bridge.md` and write out, in AP pseudocode, the maze program you ran in class today.
