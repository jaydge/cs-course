# Week 14 Homework: Searching, Sorting, and What Cannot Be Done

This week you measured how much work an algorithm does, and you met a problem that no program can ever solve. Plan on about 45 minutes.

## 1. Run the search race and write up the numbers

Take the search race program from class. Run both searches on three list sizes: 100, 10,000, and 1,000,000. Record the times in a small table like this one:

| List size | Linear search time | Binary search time | Binary search steps |
|---|---|---|---|
| 100 | | | |
| 10,000 | | | |
| 1,000,000 | | | |

Then answer two questions in a sentence each:

- When the list got 100 times bigger, roughly what happened to the linear search time?
- When the list got 100 times bigger, roughly what happened to the number of binary search steps?

Save the program and your table into your CS Class folder.

## 2. Sort by hand

Write six different numbers on six scraps of paper and lay them out in a random order. Run bubble sort on them exactly as we did in class: compare the leftmost pair, swap if the left one is bigger, move one position right, repeat to the end, then start another pass. Stop when a full pass makes no swaps.

Record two things:

- The total number of comparisons you made.
- The number of passes it took.

Then answer: if you had twelve numbers instead of six, would you expect roughly twice as many comparisons, or roughly four times as many? Say why.

## 3. Growth rate questions

1. A program looks up one value in a dictionary by its key. Does the work grow when the dictionary gets bigger? What is this called?
2. A program prints every item in a list. If the list doubles, what happens to the work?
3. A program has a loop over a list, and inside it another loop over the same list. If the list doubles, what happens to the work?
4. Put these in order from fastest-growing to slowest-growing as the data gets large: O(n), O(1), O(n squared), O(log n).
5. Your friend says their program is "fast because it only takes 0.2 seconds." What have they not told you, and why does it matter?

## 4. Write it in your own words

In one short paragraph, four or five sentences, explain the halting problem to someone who has never taken this class. You must include:

- what the impossible program would do if it existed,
- the trick we used to show it cannot exist,
- and one sentence saying why a faster computer would not help.

Do not look it up. Write what you understood in class. A clear, honest paragraph in your own words is worth far more here than a correct-sounding one you copied.

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episode 13 covers algorithms including searching and sorting, and Episode 15 is about Alan Turing and includes the halting problem: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

That reminder matters more than usual on question 4. An AI will write you a fluent paragraph about the halting problem and you will learn nothing from it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

This is the richest AP week of the whole unit. Three separate exam topics landed today: binary search, algorithmic efficiency, and undecidable problems. If you only do one of these extra-credit sections all year, do this one.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming. Work the algorithmic efficiency lessons, the searching and sorting lessons, and the lesson on undecidable problems. If those sit under a different unit number on your account, follow the topic rather than the number. If the unit numbering does not match at all, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the traversal and algorithm lessons, which cover searching a list and comparing how much work different approaches take.

**Two exam details worth memorizing.**

- Binary search requires the data to be sorted first. Every year, questions offer an answer choice that runs binary search on unsorted data. It is always wrong.
- An undecidable problem is one where no algorithm can give a correct answer in every case. That is not the same as a problem that is solvable but takes an unreasonable amount of time. The exam asks about both and expects you to tell them apart.

**Start the pseudocode bridge sheet.**

You should have a printed copy of `ap-track/AP-Pseudocode-Bridge.md`. It translates the Python you write into the pseudocode the exam is written in. Two of its trace problems will open each of the next two classes, so getting ahead is worth it.

- Read the section titled "The five differences that cause the most mistakes." Read it twice. Then work trace problems 9 and 11, both of which involve loops and lists.
- Write binary search in AP pseudocode. You will need `REPEAT UNTIL`, integer arithmetic, and 1-indexed list access, so the middle element is not quite where your Python code puts it. Working out that difference by hand is excellent preparation.
