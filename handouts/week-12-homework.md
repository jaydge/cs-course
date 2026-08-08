# Week 12 Homework: Classes and Objects

This week your data learned to do things. A dictionary holds facts; a class holds facts plus the operations that belong to them. Plan on about 40 minutes.

## 1. Finish your class

Take the pet, character, or item class you started in class and get it running end to end. It must have:

- at least three attributes set in `__init__`,
- at least two methods, one that changes an attribute and one that returns a string,
- at least three objects created from it,
- a loop over a list of those objects that calls a method on each.

Run it and make sure changing one object does not change the others. Save it into your CS Class folder.

## 2. Two classes that talk to each other

Write a second, small class that uses the first one. Some options:

- A `Shelter` that holds a list of pets and has a `feed_all` method.
- A `Backpack` that holds a list of items and has a `total_weight` method.
- A `Party` that holds a list of characters and has a `strongest` method.

It only needs one attribute and one method. The point is that an object can hold other objects.

## 3. Trace these

Write down what each prints before you run it.

**a.**
```python
class Counter:
    def __init__(self):
        self.count = 0

    def bump(self):
        self.count = self.count + 1

a = Counter()
b = Counter()
a.bump()
a.bump()
b.bump()
print(a.count, b.count)
```

**b.**
```python
class Box:
    def __init__(self, label):
        self.label = label

    def describe(self):
        return "Box of " + self.label

b = Box("rocks")
print(b.describe)
print(b.describe())
```
(One of those two lines prints something strange. Say in one sentence what the strange line actually printed and why.)

**c.**
```python
class Lamp:
    def __init__(self):
        self.on = False

    def flip(self):
        on = not self.on

lamp = Lamp()
lamp.flip()
print(lamp.on)
```
(This one runs with no error and still does the wrong thing. Find the bug and fix it.)

## 4. Watch, if you want (optional)

Crash Course Computer Science, Episode 16, on software engineering, covers why big programs get organized into objects and named pieces: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

Be ready to explain, out loud, what `self` means in your own code. If you can explain it, you own it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**A straight warning, same as last week.** Classes and objects are not on the AP CSP exam. There is no `class` keyword in AP pseudocode, no objects, and no dot notation. This is the last thin AP week in Unit 3; from Week 13 the material lines up with the exam much more closely. What does transfer today is procedures with parameters, since a method is just a procedure that receives its object as an argument, and abstraction, meaning you build something, name it, and then use it without reopening it.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** No unit covers objects, because they are not tested. The nearest fit is Unit 2, Programming, and specifically the lessons on procedures, parameters, and abstraction. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`. Do the parameters and return lessons and stop there.

**Extra practice if you want it.**

- Take one method from your class and rewrite it as an AP pseudocode procedure using the tables in `ap-track/AP-Pseudocode-Bridge.md`. Since pseudocode has no `self`, you will have to pass the values in explicitly. Notice how much longer it gets, and write one sentence on what the object was doing for you.
- Build a `Robot` class in Python with `move_forward`, `rotate_left`, `rotate_right`, and `can_move` methods, holding an x position, a y position, and a facing direction. Then run the maze program from class against it. This is the AP exam's robot-on-a-grid question, built rather than answered, and it is the best preparation for that question type you can do.
- Work trace problem 10 in the bridge sheet, which calls a procedure inside a loop. It is the closest pseudocode gets to what you did today.
