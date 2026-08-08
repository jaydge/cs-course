# Week 13 Teacher Guide

## 1. Header

- **Week:** 13 of 32
- **Unit:** 3, Programming Like a Professional
- **Theme question:** Does the shape of the container change what you can do?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Describe an array or list as numbered slots laid out in order, and say why position lookup is instant.
- Act out and then implement a stack: last in, first out, with push and pop.
- Act out and then implement a queue: first in, first out, with enqueue and dequeue.
- Explain a linked list as values that each point to the next one, and say why inserting in the middle is cheap for a linked list and expensive for an array.
- Choose the right structure for a described problem and defend the choice in one sentence.
- State the difference that matters most on the AP exam: Python lists start at index 0, AP pseudocode lists start at index 1.
- Build a working to-do stack and a working print queue.

## 3. Where this sits

Weeks 11 and 12 added two new containers, the dictionary and the object. This week steps back and asks the design question those weeks raised: given a job, what shape should the data be? That is the question professional programmers actually spend their time on, and it is why this week is placed in the middle of the unit rather than at the start.

Everything here is built out of what students already have. The stack and the queue are ordinary Python lists used with discipline, and the linked list is built from the class they learned last week, which makes the payoff for Week 12 immediate and visible.

This is also the week to surface the 0-versus-1 indexing difference between Python and AP pseudocode. Students have used `list[0]` since Week 6 without ever seeing an alternative, so the belief is hardened and needs to be broken deliberately. Week 14 starts using the pseudocode bridge sheet as a warm-up, and this segment is the setup for that.

## 4. Materials and setup

- A stack of about ten paper plates, or a spring-loaded tray dispenser if the kitchen has one. Plates work fine.
- Index cards, one per student, each with a value written on it (a word or a number), for the linked-list round.
- A second set of index cards or sticky notes to act as pointers, or students can simply point with their arm.
- Open floor space for a line of students.
- Each student's laptop with Thonny; projector for live coding.
- Whiteboard with the theme question written large.
- Printed Week 13 homework handout, one per student.

## 5. Pre-class prep checklist

- Write value cards for the linked-list round, one per student, and shuffle them. (5 min)
- Run the plate stack once yourself so the patter is smooth; it is thirty seconds of activity carrying five minutes of meaning, and it falls flat if you fumble it. (5 min)
- Write and test the to-do stack and print queue builds in the scaffolded form students will work from. (20 min)
- Write and test the linked-list demonstration in Segment 6, including the traversal loop. Confirm it runs on your Python version exactly as written. (10 min)
- Prepare the indexing comparison for Segment 3 on the board or a slide: the same five-element list numbered both ways, side by side. (10 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Ask three questions and take fast answers. Who was the last person to join the lunch line, and who gets served first? If you pile books on a desk, which one comes off first? If a printer is given four jobs, in what order should they come out?
- **You do:** Pose the theme question. Say that today's containers are not new features of Python; they are disciplines about how you are allowed to add and remove things, and that discipline is the whole point.
- **Purpose:** Both structures arrive from lived experience before either gets a name.

### Segment 2: Human Stack, Queue, and Linked List, unplugged (0:10 to 0:45), Systems strand

Run this entirely from the steps below. The canonical description is in Section 13 for prep.

**Part A, the stack (about 10 minutes).**

1. Hold the plates. Write three tasks on three plates as you say them out loud, then stack them: "email Ms. Rivera," then "study for the quiz," then "take out the trash."
2. Ask which one you have to deal with first. The answer is forced: the top one, the last one added.
3. Name it. This is a stack. Adding is a push, removing is a pop, and the rule is last in, first out, abbreviated LIFO.
4. Ask what you would have to do to reach the bottom plate. They will say take everything off. Say that this is not a limitation to work around; it is the guarantee the structure gives you.
5. Land the real-world hit: this is why the browser back button works, and it is why an unfinished task interrupted by another unfinished task feels the way it does. Add one more: when a function calls a function, Python stacks them, which is exactly what a traceback prints out.

**Part B, the queue (about 10 minutes).**

1. Line up six students facing the same direction. The front of the line is the front of the queue.
2. Call the front student out and say the word: dequeue. Add a new student at the back and say the word: enqueue.
3. Ask what would happen if you served from the back instead. Get the word "unfair" out of them, then translate it: a queue exists to guarantee order of arrival. First in, first out, abbreviated FIFO.
4. Run one round where you deliberately serve from the back and let the class object. The objection is the lesson.
5. Land the real-world hit: print jobs, ticket lines, the buffer holding your keystrokes when a program freezes and then dumps them all at once.

**Part C, the linked list (about 15 minutes).**

1. Hand out one value card per student. Stand six students in a scattered arrangement around the room, deliberately not in a line.
2. Give each one the address of the next: student A points at student B, B points at C, and so on. The last one points at nothing and says so out loud. Name that: the end of the list is a pointer to nothing.
3. Give one student the title "head." Traverse the list: start at the head, read the value, follow the pointer, repeat until you reach the one pointing at nothing. Have the class read the values in order as you walk it.
4. Ask the key question: how do I get the fourth value? They will realize you must walk from the head, one at a time. There is no jumping. Say that this is exactly what an array gives you and a linked list does not.
5. Now insert. Bring in a new student with a new card and place them between B and C. Only two pointers change: B now points at the new student, and the new student points at C. Nobody else moves.
6. Contrast it physically. Line six students up shoulder to shoulder in numbered positions, then insert someone in the middle. Everyone after them has to shuffle down. That is what inserting into the middle of an array costs.
7. Delete. Remove one student from the scattered version by having their predecessor point at their successor. The removed student walks away and nothing else changes.
8. Debrief with the tradeoff in one sentence: an array is fast to read at a position and slow to rearrange; a linked list is slow to read at a position and fast to rearrange. Neither is better. The job decides.

**Purpose:** These structures are pointers and rules, not syntax, and thirty-five physical minutes teaches them better than any amount of code. Python hides pointers, so without this segment the linked list in Segment 6 is meaningless.

### Segment 3: Indexing, and the difference that costs AP points (0:45 to 1:00), Systems strand

1. **Draw the same list twice on the board,** five boxes holding 10, 20, 30, 40, 50. Number the first copy 0, 1, 2, 3, 4 and label it Python. Number the second copy 1, 2, 3, 4, 5 and label it AP pseudocode.
2. **Ask for the third element in each.** Both are 30, but in Python it is `nums[2]` and in pseudocode it is `nums[3]`. Write both under the boxes.
3. **Say why Python counts from zero,** briefly and honestly: the index is an offset from the start of the block, so the first element is zero steps in. That connects to the memory layout they saw in Unit 2 and makes it stop feeling arbitrary.
4. **Say what the exam does with this.** AP pseudocode lists start at 1, `LENGTH (aList)` gives the count, and the last element is at `LENGTH (aList)`, not `LENGTH (aList) - 1`. Write both endings on the board.
5. **Add the second trap.** In AP pseudocode, an index below 1 or above the length is a hard error that terminates the program, and trace questions use that on purpose.
6. **Drill it once, out loud.** Give the list `["a", "b", "c", "d"]` and ask, in alternating order: Python index of "c"? Pseudocode index of "c"? Python last index? Pseudocode last index? Do six of these fast. Speed is the point; the goal is a reflex, not a discussion.
7. **Tell them why you are making a fuss.** This is the most common wrong answer on the AP exam, and it is entirely avoidable. Non-AP students should still know it exists, because most languages do it Python's way and a few do not, and mixing them up is a career-long source of off-by-one bugs.

**Purpose:** The belief that indexing starts at 0 is now seven weeks old and unquestioned. Breaking it here, in a dedicated segment, is worth more than mentioning it repeatedly later.

### Segment 4: Stretch (1:00 to 1:05)

### Segment 5: Build the to-do stack and the print queue (1:05 to 1:35), Coding strand part 1

- **You do:** Show that both structures are an ordinary Python list plus a rule about which end you touch:

  ```python
  todo = []
  todo.append("wash dishes")
  todo.append("finish homework")
  next_task = todo.pop()
  print(next_task)
  print(todo)
  ```

  Then the queue:

  ```python
  print_queue = []
  print_queue.append("essay.pdf")
  print_queue.append("poster.png")
  next_job = print_queue.pop(0)
  print(next_job)
  print(print_queue)
  ```
- **You do:** Put the difference on the board in one line: `pop()` takes from the end, `pop(0)` takes from the front. One character of difference, two completely different behaviors.
- **You do:** Show the empty-container crash on purpose. `[].pop()` raises an `IndexError`. Ask what a real printer should do when asked to print with nothing queued, and get them to write the guard themselves.
- **Students do:** Build both, each wrapped in functions and a small menu:

  ```python
  def push_task(stack, task):
      stack.append(task)

  def pop_task(stack):
      if len(stack) == 0:
          return "Nothing to do."
      return stack.pop()
  ```

  The print queue is the same shape with `pop(0)`. Both should print the current contents after every operation so students can watch the order.
- **You do:** Circulate. Watch for students who use `pop()` in the queue and then cannot explain why their printer prints backwards; make them trace it on paper rather than telling them.

### Segment 6: A linked list in Python (1:35 to 1:50), Coding strand part 2

- **You do:** Build it at the projector, and connect every line back to the students who were standing in the room:

  ```python
  class Node:
      def __init__(self, value):
          self.value = value
          self.next = None

  first = Node("apple")
  second = Node("banana")
  third = Node("cherry")
  first.next = second
  second.next = third

  current = first
  while current is not None:
      print(current.value)
      current = current.next
  ```
- **You do:** Point at `self.next = None` and say that this is the student pointing at nothing. Point at the traversal loop and say this is you walking the room. Point at `current = current.next` and say that this single line is the whole idea: move your finger to whoever the current one points at.
- **You do:** Do the insertion live. Make a fourth node and splice it between `first` and `second` with two assignments. Re-run the traversal. Nothing else changed, exactly as in the unplugged round.
- **Students do:** Type it, add a fourth node, and perform one insertion and one deletion by reassigning pointers.
- **Note for you:** Do not build a full `LinkedList` class with methods this year. The conceptual model is the objective; the implementation is a data structures course.

### Segment 7: Wrap and homework (1:50 to 2:00)

- **You do:** Hand out and walk through the homework, including the Extra Credit AP Track section. Exit question at the door: undo in a text editor, is that a stack or a queue, and why?

## 7. Key scripts and analogies

- **Stack:** "A pile of plates. You can only touch the top one. Last in, first out. Your browser's back button is a stack, and so is the list of function calls Python prints in a traceback."
- **Queue:** "A line at a ticket window. Join at the back, leave from the front. First in, first out. Every printer, every checkout, every download manager."
- **Array or list:** "Numbered lockers bolted to a wall. Locker 7 is instant to find, but adding a locker in the middle means renumbering everything after it."
- **Linked list:** "A scavenger hunt. Each clue holds a value and tells you where the next one is. Finding the fourth clue means following the first three, but slipping a new clue into the middle only means rewriting two of them."
- **The tradeoff:** "Arrays are fast to read and slow to rearrange. Linked lists are slow to read and fast to rearrange. There is no winner; there is only the job you are doing."
- **On zero versus one:** "Python's index is not a count, it is a distance from the start. The first element is zero steps in. The AP exam's pseudocode counts instead of measuring, so its first element is 1. Same list, two rulers."
- **On discipline:** "Nothing stops you reaching into the middle of your stack. Python will let you. The rule is a promise you make so the rest of your program can trust the order."

## 8. Differentiation

- **Younger or newer students:** Stack and queue only, and skip the linked list in code; the physical round is enough for them to carry the idea. Give them the menu loop and have them write only `push_task` and `pop_task`. For the indexing segment, give them the two-ruler drawing on paper to keep.
- **Extensions for advanced or AP-track students:** Add a `peek` operation that returns the top or front item without removing it, and a `size` function. Implement the print queue so that each job is an object from a small `Job` class with a name and a page count, and have the queue report total pages waiting. For the linked list, write a function that takes the head node and returns its length by walking it.

## 9. Common pitfalls

- **`pop()` versus `pop(0)`.** The single most common bug of the week, and it is silent: the program runs and the order is simply wrong. Teach students to print the container after every operation.
- **Popping from an empty list.** An `IndexError` that students read as a mysterious crash. Guard it in class so they write the guard by habit.
- **Believing a stack and a queue are different types.** They are both Python lists here. Some students want an `import`. Say plainly that the structure is the rule, not the type.
- **Losing the rest of the linked list during insertion.** If a student writes `first.next = new_node` before setting `new_node.next = second`, the tail is gone. Have them redo it physically with two students in the room; it takes ten seconds and never needs saying twice.
- **`current.next` versus `current.next.value`.** Students print the node object and get something like `<__main__.Node object at 0x...>`, which reads as an error to them. Explain it once, at the projector, before they hit it.
- **The indexing segment being treated as trivia.** It is not trivia, it is the highest-frequency exam error in the course. Run the fast drill; do not just say it.

## 10. Homework

Full details in `handouts/week-13-homework.md`. In summary: finish the to-do stack and the print queue; five "which structure and why" scenarios; a paper linked-list drawing with one insertion and one deletion; a short indexing drill; optional Crash Course episode on data structures. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice.

## 11. Assessment

Observational plus the exit question. During Segment 5, confirm each student's queue actually preserves arrival order; that is the one outcome most likely to be silently wrong. During Segment 2, note who can explain the insertion tradeoff without prompting, since that is the reasoning Week 14 will lean on.

The exit question (undo is a stack) is a reliable one-line check on whether the LIFO idea landed. Homework is a completion check against the weekly-labs rubric. Record who still hesitates on the two-ruler indexing drill; those students need the pseudocode warm-ups from Week 14 onward most.

## 12. AP alignment

This session covers AP CSP topics 3.2 Data Abstraction and 3.10 Lists, and it sets up 3.11 Binary Search and 3.17 Algorithmic Efficiency in Week 14 by giving students the cost intuition that Big-O formalizes.

Note what is and is not tested. Stacks, queues, and linked lists are not AP CSP exam topics; the exam's only collection is the list. But two things from today are heavily tested. First, list operations: `APPEND`, `INSERT`, `REMOVE`, `LENGTH`, and the way `INSERT` and `REMOVE` shift the elements around them, which is exactly the array-cost lesson from Part C of the unplugged segment. Second, 1-indexing, which is the single most common source of wrong answers on the exam.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 3, Data Representation, the lists lessons, if not already done in Week 6; otherwise Unit 2, Programming, and its list-manipulation lessons. Work only the list material and stop. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the list-operation and traversal lessons. This is the closest thing the AP course has to today's material.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human Stack, Queue, and Linked List: Segment 2 is complete on its own and needs only plates and index cards. The activity description is in `teaching-activities/Unplugged-Logic-Activities.md`, under Data structures. No external source needs reviewing to run it.
- Python list methods, for your reference: `https://docs.python.org/3/tutorial/datastructures.html`. Note that Python's `list.pop(0)` is fine at classroom sizes; `collections.deque` is the real answer for large queues and is worth knowing yourself, but do not introduce it to students this week.
- AP pseudocode list operations and the 1-indexing rules: `ap-track/AP-Pseudocode-Bridge.md`, the Lists table and the first item in "The five differences that cause the most mistakes."
- Crash Course Computer Science, Episode 14 ("Data Structures"), optional homework viewing; it covers arrays, stacks, queues, and linked lists in eleven minutes and matches today almost exactly. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`. Confirm the episode number in the playlist before assigning; numbering in reuploads sometimes differs.
- CodeAI CSP Unit 6, Lists, Loops, and Traversals (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
