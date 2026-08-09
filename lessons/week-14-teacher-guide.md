# Week 14 Teacher Guide

## 1. Header

- **Week:** 14 of 32
- **Unit:** 3, Programming Like a Professional
- **Theme question:** Why is one program fast and another one slow?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Describe linear search and binary search, and state the precondition binary search requires.
- Explain why halving the search range beats checking one item at a time, using the number of guesses as evidence.
- Run a sorting algorithm by hand on physical cards and count the comparisons it takes.
- Time linear search against binary search in Python on a large list and report the difference.
- Say, in plain language, what it means for one algorithm to scale well and another to scale badly, and name the informal notations O(1), O(log n), O(n), and O(n squared).
- State that some problems cannot be solved by any algorithm at all, name the halting problem as the standard example, and distinguish that from a problem that is merely slow.

## 3. Where this sits

Week 13 gave students the intuition that different data shapes cost different amounts. This week names that cost and measures it. It is the most AP-aligned week in the entire course: binary search, algorithmic efficiency, and undecidable problems are three separate exam topics, and all three land today.

It is also the week where the course's physical-first pattern pays off most obviously. Students who have personally executed bubble sort with cards in their hands, and personally counted the comparisons, understand why n squared hurts. Students who were told about it do not.

From this week on, hand out the AP pseudocode bridge sheet and use two of its trace problems as a warm-up in Weeks 15 and 16. Students are now fluent in lists and procedures, which is the prerequisite the bridge sheet names, and the 1-indexing work from Week 13 has already broken the ground.

## 4. Materials and setup

- Number cards, one per student, for Human Sorting. Playing cards work; numbers 1 to 20 on index cards work better because the ordering is unambiguous.
- A roll of masking tape for the sorting network, and floor space roughly 3 metres by 3 metres.
- A whiteboard with the theme question written large, and space for a comparison-count tally that stays up all session.
- Each student's laptop with Thonny; projector for live coding and timing.
- Printed Week 14 homework handout, one per student.
- Printed copies of `ap-track/AP-Pseudocode-Bridge.md`, one per AP-track student and a few spares.

## 5. Pre-class prep checklist

- Tape the sorting network. Lay six parallel lanes running left to right, about 60 cm apart, each about 3 m long. Then tape short rungs between adjacent lanes in a brick pattern: column 1 has rungs joining lanes 1 and 2, lanes 3 and 4, and lanes 5 and 6; column 2 has rungs joining lanes 2 and 3 and lanes 4 and 5; and so on alternating for six columns in total. Number the lanes 1 to 6 at the entry end. (20 min)
- Walk the network once yourself with six numbered slips of paper, moving them by hand, to confirm the layout sorts. (10 min)
- Write and test the search-race program and the sort-comparison program on the demo machine, and note the actual timings you get, since they vary by machine and students will ask. (20 min)
- Rehearse the halting-problem argument out loud once. It is fifteen minutes of pure reasoning with no props, and it only lands if the delivery is tight. (10 min)
- Print homework handouts and bridge sheets. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Guess My Number, unplugged warm-up (0:00 to 0:12), Systems strand

1. Announce that you are thinking of a whole number between 1 and 100, and that the class must find it. You will answer only "higher," "lower," or "correct."
2. Take the first three guesses from whoever shouts, and tally every guess on the board. Do not coach.
3. When someone says 50 for the first time, stop and ask why that guess is better than 3. Get them to say that it cuts the possibilities in half either way.
4. Play a second round with the halving strategy enforced. Count the guesses; it will take seven or fewer.
5. Write the numbers on the board: 100 possibilities, 7 guesses. Then ask what 1000 possibilities would cost. Take guesses, then tell them: 10. And a million? 20.
6. Name it. Guessing one at a time from the bottom is linear search. Halving is binary search. Say the phrase they should remember: doubling the problem adds one step, rather than doubling the work.
7. State the catch now, because it is the exam's favorite trap: halving only works because the numbers are in order. On an unsorted pile, "higher" and "lower" mean nothing.

**Purpose:** Binary search and the shape of a logarithm arrive as a game outcome, with no notation, in twelve minutes.

### Segment 2: Human Sorting (0:12 to 0:35), Systems strand

Run this from the steps below. The canonical source is in Section 13 for prep.

1. **Line up eight students** facing the class, each holding a number card so the room can see it. Shuffle so the order is genuinely bad.
2. **Run bubble sort out loud.** The rule: compare the leftmost pair; if the left is bigger, the two students swap places; then move one position right and repeat to the end of the line. That is one pass. Repeat passes until a full pass happens with no swaps.
3. **Tally every comparison on the board** as it happens, with a student keeping count. Do not skip this; the number is the entire point of the segment.
4. **Ask what they notice after the first pass.** The largest number has travelled to the end. Name it: that is why it is called bubble sort, and it is why each pass can be one shorter than the last.
5. **Record the total.** Eight cards costs somewhere near 28 comparisons. Write it up and leave it.
6. **Reshuffle and run selection sort.** The rule: scan the whole line for the smallest card, swap it into position 1, then scan the remaining line for the next smallest, and so on. Tally again.
7. **Compare the two totals.** They will be close. Land the point that matters: neither one is a small improvement over the other, because both grow the same way. Ask what would happen with 16 students instead of 8, and take a prediction. The answer is roughly four times the work, not twice.
8. **Ask the killer question.** How many comparisons for the whole school, a thousand students? Let them estimate. Half a million is close enough. This is where n squared stops being notation and becomes a feeling.

**Purpose:** Students execute a sorting algorithm as a physical procedure, and the comparison counts they generate are the data that Segment 6 turns into Big-O.

### Segment 3: Sorting Network (0:35 to 0:50), Systems strand

1. **Give six students a number card each** and stand them at the six numbered lanes at the entry end.
2. **State the single rule.** Walk forward along your lane. When you reach a rung, wait for the person at the other end of that rung. Compare cards. The smaller number leaves on the lane nearer lane 1; the larger leaves on the lane nearer lane 6. Then keep walking.
3. **Send them in all at once.** Do not stagger them.
4. **Read the exit order aloud.** They come out sorted, every time, which reliably gets a reaction.
5. **Run it twice more with reshuffled cards.** The point is that it is not luck.
6. **Ask what was different from the line-up version.** Steer them to the answer: several comparisons happened at the same moment. In the bubble sort, only one pair compared at a time.
7. **Name it.** That is parallelism. Some algorithms can be spread across many workers at once, and some cannot, and this is a real limit on what more processors can buy you. Connect it forward one sentence: this is why a phone has multiple cores, and why doubling the cores rarely doubles the speed.
8. **Optional if the room is engaged:** ask whether the network could sort seven cards. It cannot; the network is built for exactly six. Hardware that is fast is often inflexible, which is a genuine engineering tradeoff worth naming.

**Purpose:** Parallelism arrives physically and memorably, and it seeds AP topic 4.3 for Unit 6.

### Segment 4: Stretch (0:50 to 0:55)

### Segment 5: The search race and the sort visualization (0:55 to 1:20), Coding strand

- **You do:** Build the race at the projector. Make the list large enough that the difference is unmissable:

  ```python
  import time

  data = list(range(1, 1000001))
  target = 999999

  start = time.time()
  found = -1
  for i in range(len(data)):
      if data[i] == target:
          found = i
          break
  print("linear:", time.time() - start, "seconds, index", found)
  ```

  Then binary search on the same data:

  ```python
  start = time.time()
  low = 0
  high = len(data) - 1
  steps = 0
  while low <= high:
      steps = steps + 1
      mid = (low + high) // 2
      if data[mid] == target:
          break
      elif data[mid] < target:
          low = mid + 1
      else:
          high = mid - 1
  print("binary:", time.time() - start, "seconds, in", steps, "steps")
  ```
- **You do:** Read the step count out loud. About twenty steps for a million items, and never more than twenty. Point back at the board where they wrote 20 for a million during Guess My Number and say: same algorithm, you invented it an hour ago.
- **Students do:** Run both, then change the list size to 100, 10000, and 1000000 and record the timings in a table. They will see linear search's time grow in step with the list and binary search's barely move.
- **You do:** Break binary search on purpose. Shuffle the list with `random.shuffle(data)` and run the binary search again. It fails to find the target. Ask why. This is the precondition from Segment 1, now proven in code.
- **Students do:** Time bubble sort against Python's built-in sort:

  ```python
  import random
  import time

  def bubble_sort(items):
      n = len(items)
      for i in range(n - 1):
          for j in range(n - 1 - i):
              if items[j] > items[j + 1]:
                  items[j], items[j + 1] = items[j + 1], items[j]
      return items

  nums = []
  for i in range(2000):
      nums.append(random.randint(1, 1000))
  copy = list(nums)

  start = time.time()
  bubble_sort(nums)
  print("bubble:", time.time() - start)

  start = time.time()
  copy.sort()
  print("built-in:", time.time() - start)
  ```
- **You do:** Have them double the 2000 to 4000 and run again. Bubble sort takes roughly four times as long; the built-in barely notices. Say the professional lesson plainly: you learn to write bubble sort so you understand what sorting costs, and then you call the built-in sort for the rest of your life.

### Segment 6: Big-O, conceptually (1:20 to 1:35), Systems strand

1. **Start from their own numbers,** not from notation. Point at the board: 8 cards cost about 28 comparisons, 1000 students cost about half a million, a million-item binary search costs 20 steps.
2. **Draw the table** and fill it with the class:

   | Items | O(1) | O(log n) | O(n) | O(n squared) |
   |---|---|---|---|---|
   | 10 | 1 | about 3 | 10 | 100 |
   | 1,000 | 1 | about 10 | 1,000 | 1,000,000 |
   | 1,000,000 | 1 | about 20 | 1,000,000 | 1,000,000,000,000 |
3. **Give one plain-language name to each row heading.** O(1): the cost never changes, like looking up a dictionary key. O(log n): doubling the data adds one step, like binary search. O(n): the cost tracks the data, like linear search or printing every item. O(n squared): the cost explodes, like bubble sort or any loop nested inside a loop over the same data.
4. **Say what Big-O ignores and why.** It ignores constants and it ignores small inputs. A slow O(n) program can beat a fast O(log n) program on ten items. Big-O is a claim about what happens as the data grows, which is the only thing that matters when the data eventually does grow.
5. **Send them back to their own code.** Ask what the nested loop in bubble sort costs, and what the Week 9 nested loop over a multiplication table cost. Both are n squared, and both were written by them.
6. **Two rules of thumb to write down.** A loop over the data is O(n). A loop inside a loop over the same data is O(n squared). That covers almost everything a student in this course will write.

**Purpose:** Notation lands last, on top of numbers the students generated themselves.

### Segment 7: Problems no algorithm can solve (1:35 to 1:50), Systems strand

1. **Call back the spinning robot** from Week 12, the one stuck turning forever in the corner.
2. **Ask the question straight.** Could you write a program, call it `will_it_finish`, that reads any other program plus its input and correctly answers yes or no, will this finish or will it run forever? Take a show of hands. Most say yes, with a compiler or enough cleverness.
3. **Grant the easy cases.** For simple programs it is easy. `while True:` obviously never finishes. A `for` loop over ten items obviously does. The claim is much stronger: it must work for every program, always, with no wrong answers.
4. **Build the contradiction on the board,** slowly, in three moves. First, suppose `will_it_finish(program, input)` exists and is always right. Second, write a new program using it:

   ```python
   def trouble(program):
       if will_it_finish(program, program):
           while True:
               pass
       else:
           return "done"
   ```

   Third, ask what happens when you run `trouble(trouble)`. If `will_it_finish` says it finishes, `trouble` loops forever. If it says it loops forever, `trouble` finishes immediately. Either answer is wrong.
5. **Draw the conclusion carefully.** The contradiction does not mean we have not found the right program yet. It means no such program can exist, for any language, on any hardware, ever. This is Alan Turing, 1936, and it predates the computers it describes.
6. **Kill the two predictable objections.** A faster computer does not help, because this is not about speed. More memory does not help either. The problem is not hard; it is impossible.
7. **Name the AP distinction, because the exam tests it.** An undecidable problem has no algorithm at all that always gives a correct answer. That is different from a problem that has an algorithm but takes an unreasonable amount of time, sometimes called intractable, where the answer exists but you cannot wait for it. Both appear on the exam and students mix them up.
8. **Land it in the real world.** This is why your editor warns you about a possible infinite loop rather than guaranteeing there is not one, why antivirus software cannot perfectly decide whether an unknown program is malicious, and why no compiler will ever prove your program correct in general. Real tools give conservative approximations because perfection is provably unavailable.

**Purpose:** AP topic 3.18 in one honest fifteen-minute argument, and it is the single most memorable idea in the unit.

### Segment 8: Wrap and homework (1:50 to 2:00)

- **You do:** Hand out the homework and walk through it, including the Extra Credit AP Track section. Hand the printed pseudocode bridge sheet to AP-track students and anyone curious, and say that two of its trace problems will open the next two classes. Exit question at the door: your search is instant on a sorted list and useless on an unsorted one. Which search is it, and why?

## 7. Key scripts and analogies

- **Linear versus binary search:** "Looking for a name in the phone book by starting at page one, versus opening the middle. Both work. One of them ends before lunch."
- **The precondition:** "Binary search buys its speed with an assumption. If the list is not sorted, 'higher' and 'lower' are lies, and the algorithm walks confidently to the wrong place."
- **On logarithms without saying logarithm:** "Every time you double the data, binary search costs you one more step. One. That is the whole reason computers can search things the size of the internet."
- **n squared:** "Eight students took about 28 comparisons. A thousand students take about half a million. You did not make the problem 125 times bigger; you made the work 15,000 times bigger."
- **Big-O ignores constants:** "Big-O is not a stopwatch. It is a prediction about what happens when the data grows. It answers 'will this still work next year when we have a hundred times more users.'"
- **Why write bubble sort at all:** "So that you know what you are buying when you call `.sort()`. Professionals do not write sorting algorithms. Professionals know what sorting costs."
- **The halting problem:** "This is not a gap in our knowledge that a smarter person will close. It is a proof that the thing cannot exist. Computing has a hard edge, and Turing found it before the first computer was built."
- **Undecidable versus slow:** "Slow means the answer is out there and you will be dead before it arrives. Undecidable means there is no answer to arrive."

## 8. Differentiation

- **Younger or newer students:** Use the alternate from the curriculum's Section 11. Drop the log and exponent notation entirely and teach the same content through the timing race and qualitative language: scales well, scales badly, stops working when the data gets big. They should still be able to say that binary search needs a sorted list and that a loop inside a loop gets expensive fast. That is the whole outcome for them. The halting-problem argument works fine at any age; it is logic, not math.
- **Extensions for advanced or AP-track students:** Have them write binary search as a function that returns the index or -1, then instrument it to print `low`, `mid`, and `high` at every step. Have them count comparisons inside bubble sort with a counter variable and confirm the count matches the classroom tally formula for small n. The strongest students can add an early exit to bubble sort that stops when a pass makes no swaps, then time it on an already-sorted list and explain why it becomes O(n).

## 9. Common pitfalls

- **Binary search on unsorted data.** Students accept the precondition verbally and forget it instantly. The deliberate shuffle-and-fail demonstration in Segment 5 exists for this reason; do not cut it.
- **Off-by-one errors in the binary search loop.** `while low <= high`, and `mid + 1` and `mid - 1` when narrowing. A version with `low = mid` loops forever. This is a good live bug to let happen.
- **Integer division.** `(low + high) / 2` gives a float and breaks indexing. `//` is required. Students who skipped it in Week 4 will hit it here.
- **Confusing Big-O with actual time.** A student will report that their O(log n) run took longer than someone else's O(n) run on a different laptop and conclude the theory is wrong. Address it: Big-O compares growth, not machines.
- **Believing the halting problem is about difficulty.** Watch for "so we just need a better algorithm." Repeat the proof structure rather than repeating the conclusion.
- **The sorting network sorting nothing.** If the tape layout is wrong, it fails visibly in front of the class. Walk it during prep with paper slips; this is the one prep step not to skip.
- **The session running long.** There is a lot here. If you must cut, cut the sorting network to ten minutes and protect Segments 6 and 7, which are the two AP topics.

## 10. Homework

Full details in `handouts/week-14-homework.md`. In summary: run the search race at three list sizes and write up the numbers; sort six cards by hand and count the comparisons; three growth-rate questions; a short written explanation of the halting problem in their own words; optional Crash Course episodes on algorithms and on Turing. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice, which is the richest of the unit.

## 11. Assessment

Observational plus the written homework paragraph. During Segment 5, check that each student can state the binary search precondition without prompting. The exit question is a fast check on the same thing.

The homework's halting-problem paragraph is the best single artifact of the week: a student who can explain in their own words why no such program can exist has understood something genuinely hard. Score homework against the weekly-labs rubric, but read those paragraphs properly.

Note which students needed the Section 11 alternate for Big-O. The Unit 3 checkpoint in Week 16 asks a growth-rate question, and those students should get the qualitative version of it.

## 12. AP alignment

This is the strongest AP week in the course. The session directly covers AP CSP topics 3.11 Binary Search, 3.17 Algorithmic Efficiency, and 3.18 Undecidable Problems, and reinforces 3.10 Lists and 3.8 Iteration throughout. Together these carry real weight in the Algorithms and Programming section, which is 30 to 35 percent of the multiple-choice exam.

Two exam-specific details to say out loud today. First, the exam expects students to know that binary search requires sorted data and that it is more efficient than linear search on large data sets. Second, the exam distinguishes an undecidable problem, where no algorithm can give a correct answer in all cases, from a problem that is solvable but only in an unreasonable amount of time. Students conflate these; separate them explicitly.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming, specifically its algorithmic efficiency lessons, the searching and sorting material, and the lesson covering undecidable problems. If the efficiency material sits elsewhere in your account, follow the topic rather than the number. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the traversal and algorithm lessons, which include searching a list and comparing how much work different approaches take.

This is also the week to start the pseudocode bridge sheet. It is designed to be introduced once students are fluent with lists and procedures, which is now.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human Sorting: Segment 2 is complete on its own and needs only number cards. Canonical source is CS Unplugged Sorting Algorithms, from the activities index at `https://classic.csunplugged.org/activities/`. Verify links are live before class; sites reorganize.
- Sorting Network: Segment 3 is complete on its own, and the taping instructions are in Section 5. Canonical source, including a printable network diagram and a demonstration video, is CS Unplugged Sorting Networks, `https://classic.csunplugged.org/activities/sorting-networks/`. Review this during prep if you want the printable layout; the brick-pattern layout described in Section 5 is simpler to tape and also sorts correctly, but the canonical one uses fewer comparison nodes.
- Guess My Number: fully inline in Segment 1, no materials needed.
- Python `time` module, for the race lab: `https://docs.python.org/3/library/time.html`. `time.time()` is adequate here; `time.perf_counter()` is more precise and is worth using if you want steadier numbers.
- Crash Course Computer Science, Episode 13 ("Intro to Algorithms") and Episode 15 ("Alan Turing"), optional homework viewing; Episode 15 covers the halting problem directly. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`. Confirm episode numbers in the playlist before assigning; numbering in reuploads sometimes differs.
- AP pseudocode bridge sheet, handed out today: `ap-track/AP-Pseudocode-Bridge.md`. The official College Board reference sheet it mirrors is at `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`; confirm it is the current version before printing, since College Board revises it.
- CodeAI CSP Unit 6, Lists, Loops, and Traversals (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
- Younger-student Big-O alternate: Section 11 of `curriculum/CS-Curriculum-and-Setup.md`.
