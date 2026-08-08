# Week 13 Homework: Stacks, Queues, and the Shape of Data

This week was about containers and the rules that come with them. A stack, a queue, and a linked list are all just ways of agreeing where you are allowed to add things and where you are allowed to take them out. Plan on about 40 minutes.

## 1. Finish the to-do stack and the print queue

Both should run, and both should print their full contents after every operation so you can watch the order.

Requirements:

- The stack pushes tasks and pops the most recent one.
- The queue enqueues jobs and dequeues the oldest one.
- Neither crashes when it is empty. Print a sensible message instead.
- Each uses at least two functions that take the list as a parameter.

Save both into your CS Class folder.

## 2. Which structure, and why

For each situation, say stack, queue, plain list, or dictionary, and give one sentence of reasoning. There is a defensible answer for each; the reasoning matters more than the label.

1. Undo in a text editor.
2. Customers waiting for support tickets to be answered.
3. Looking up a student's grade by their name.
4. The pages you visited in a browser, so the back button works.
5. Songs waiting to play next in a playlist.

## 3. Linked list on paper

Draw four boxes across a page. Each box holds a value and an arrow to the next box. The last arrow points to the word `None`.

Then, on the same page:

- Draw the insertion of a new box between the second and the third. Cross out the arrows that change and draw the new ones. Exactly two arrows should change.
- Draw the deletion of the second box. Again, show which arrows change.
- Write one sentence answering this: to read the fourth value, how many boxes do you have to visit, and how is that different from a Python list?

## 4. Indexing drill

Given `letters = ["a", "b", "c", "d", "e"]`:

1. What is `letters[0]`?
2. What is `letters[4]`?
3. What does `letters[5]` do, and what is the error called?
4. What is `len(letters)`, and what is the index of the last element in terms of `len`?
5. In AP pseudocode, lists start at 1 instead of 0. In that notation, what index holds `"c"`, and what index holds the last element?

Question 5 is worth doing even if you never touch the AP exam. Python counts from 0, some other languages and notations count from 1, and mixing them up is the most common off-by-one bug there is.

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episode 14, covers arrays, stacks, queues, and linked lists in about eleven minutes: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

This is where the AP mapping gets strong again. Stacks, queues, and linked lists themselves are not tested, but list operations are, and so is the 1-indexing rule you drilled today. Both show up constantly in the multiple-choice section.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 3, Data Representation, the lists lessons, if you have not already worked them; if you have, use Unit 2, Programming, and its list-manipulation lessons instead. Work only the list material and stop there. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the list-operation and traversal lessons.

**Extra practice if you want it.**

- Read the Lists table in `ap-track/AP-Pseudocode-Bridge.md`, then work trace problems 5, 6, 7, and 8. All four are list-index problems, and all four are designed to catch a Python habit. Do them on paper before checking the answer key.
- Note what `INSERT (aList, i, v)` and `REMOVE (aList, i)` do to everything after position `i`: they shift. That shifting is exactly the cost you acted out in class with six students standing shoulder to shoulder. Write one sentence connecting the two.
- Write out, in AP pseudocode, a procedure that takes a list and returns its last element. Remember that the last element is at `LENGTH (aList)`, not `LENGTH (aList) - 1`. Getting that right on the first try is a small thing that has cost a lot of people points.
