# Week 7 Teacher Guide

## 1. Header

- **Week:** 7 of 32
- **Unit:** 2, Inside the Computer
- **Theme question:** How do gates turn into a computer?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Explain how feeding a gate's output back into its own input creates memory, and say in one sentence what a latch stores.
- Distinguish a flip-flop from a register from RAM by how much each one holds.
- Describe what the clock does, in the sense that it is the drumbeat that says "now."
- Trace a half adder and say which output is the sum and which is the carry.
- Name the three parts of a simple CPU (registers, ALU, control unit) and state the fetch, decode, execute cycle in order.
- Use `append()`, `remove()`, `pop()`, and `sort()` on a Python list, and check membership with `in`.
- Write a `for` loop that iterates over the items of a list, and explain how it differs from looping over `range()`.

## 3. Where this sits

Week 6 ended with three gates on a breadboard. This week those gates become a machine. The arc is deliberately one level per step: a loop of gates gives memory, a row of memory gives a register, gates arranged differently give arithmetic, and a controller that shuttles values between the two gives a CPU. Nothing new is invented after this point in the hardware story; Weeks 8 and 9 are about making the same machine fast and packaging it on a board.

The in-game lab is the centerpiece and does something no lecture can: students build a working adder out of nothing but NAND, which makes the "everything from one gate" claim personally verified rather than asserted. On the coding side, list methods and traversal complete what Week 6 started and are the last prerequisite before Unit 3's dictionaries and objects.

## 4. Materials and setup

- Student laptops with a browser, one per pair, for the nandgame lab. No accounts and no installation required.
- Optional: Turing Complete installed on one lab machine if you own it, plus the projector, for the whole-class version of the same lab. It is a paid Steam game, roughly $20 for a single purchase; verify the current price and system requirements before buying.
- Reliable internet for the browser lab. If the connection is unreliable, load nandgame.com on each machine before class starts and leave the tabs open.
- 1 and 0 cards left over from Week 6, for the half-adder warm-up.
- Whiteboard with the theme question, and room for a running stack diagram you add to all session.
- Projector for live coding.
- Printed Week 7 homework handout, one per student.

## 5. Pre-class prep checklist

- Play nandgame.com yourself, from the first level through the adder. This is the one prep item you genuinely cannot skip, because the wiring interface has its own feel and students will ask how to delete a wire in the first ninety seconds. Budget the time honestly. (45 min)
- Decide which lab you are running: nandgame on student laptops, Turing Complete on the projector, or both. Note that nandgame stores progress in the browser's local storage on that machine, so if you want students to keep progress across weeks, tell them to use the same laptop and the same browser and not to clear site data. (10 min)
- Draw the running stack diagram you will build up on the whiteboard (transistor, gate, latch, register, adder, ALU, CPU) and decide where each segment adds to it. (10 min)
- Write and test the list-methods examples and the shopping-list build you will live-code. (15 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up, the human half adder (0:00 to 0:25), Systems strand

Steps below are complete. This picks up the last step of last week's unplugged activity and finishes it properly.

1. **Review the gates.** Quick round: call out AND, OR, NOT and have the class recite each truth table. Sixty seconds, no more.
2. **Ask the question that motivates everything.** Write on the board: 1 + 1 = ? in binary. The answer is 10, two digits. Ask what that means for a machine that can only hold one bit per wire. It means addition needs two output wires, not one.
3. **Introduce XOR.** One more gate, defined as "1 if the inputs are different, 0 if they are the same." Put a gate student in front with that rule and walk all four input combinations. Write the truth table beside last week's three.
4. **Wire the half adder with people.** Two input students. Both of their cards are read by two gate students at once: one XOR and one AND. Label the XOR student's output SUM and the AND student's output CARRY, with a sign or a card on the floor in front of each.
5. **Run all four cases and record them.** 0 + 0 gives sum 0, carry 0. 0 + 1 gives sum 1, carry 0. 1 + 0 gives sum 1, carry 0. 1 + 1 gives sum 0, carry 1, which reads as binary 10. Write the four results on the board as a table.
6. **Land it.** Four students following two rules just did arithmetic. Nobody in the circuit knows what addition is. Say it plainly: arithmetic is not a special ability the machine has, it is a shape you can wire gates into.
7. **Name the missing piece.** Ask what happens when you add three-digit binary numbers and a carry comes in from the column to the right. That needs a third input, and the version that handles it is called a full adder. Tell them they will build one in the lab.

### Segment 2: Memory, registers, and the CPU (0:25 to 0:45), Systems strand

Build the stack diagram on the board as you go. Keep this tight; it is a lot of new vocabulary and the lab reinforces most of it.

1. **The feedback trick.** Draw two NOR gates with each one's output feeding the other's input. Do not derive it formally. Instead make the point with a question: if the output feeds back into the input, what is the circuit's state a moment from now? It depends on what it already was. That is memory. A circuit whose output depends on its own history remembers something.
2. **Name the pieces.** A latch holds one bit. A flip-flop is a latch that changes only at a specific moment rather than whenever the inputs wiggle. Eight or thirty-two flip-flops side by side make a register, which holds one number the CPU is working on right now. Millions of similar cells make RAM.
3. **The clock.** A square wave, on and off, millions or billions of times a second. Its only job is to say "now" to every flip-flop at once, so the whole machine steps forward together instead of drifting. Tie the vocabulary forward: this is the number in "3.2 GHz", and Week 8 asks whether a bigger number means a faster computer.
4. **The ALU.** Gates arranged to add, subtract, compare, and do AND and OR on whole numbers at once. The half adder from Segment 1, repeated eight or sixty-four times across, with carries chained between columns.
5. **Assemble the CPU.** Three parts on the board: registers to hold values, an ALU to compute with them, and a control unit that reads instructions and decides what happens. Then the cycle, written in order and circled: fetch an instruction from memory, decode what it means, execute it, repeat. Say that this loop is running billions of times per second in the laptop in front of them and has been since they opened it.
6. **Set up the lab.** Tell them the game they are about to play starts them with one gate, NAND, and nothing else, and that by the end of the session they will have used it to build an adder. Everything in between they build themselves.

### Segment 3: Gates to adder, in-game lab (0:45 to 1:15), Systems strand

Run the free browser version. If you own Turing Complete, the projector variant is in step 8.

1. **Open the game.** Each pair opens `https://nandgame.com` in a browser. There is no account, no login, and no installation. Progress saves to that browser on that machine only.
2. **Read the screen once, together.** Levels are listed down one side in order. The middle is the work area. Available parts are shown for dragging in. The top of the puzzle shows the input switches and the target behavior for the level.
3. **Teach the three interface moves before anyone starts, because these are what students get stuck on.** Drag a part from the parts list into the work area to place it. Click an output pin and then an input pin to draw a wire between them. Click an existing wire to remove it. Toggle the input switches at the top to test your circuit by hand.
4. **The rule that makes the game teach.** Once you complete a level, that component becomes a part you can use in later levels. You are never asked to rebuild something you already built. This is abstraction as a game mechanic, and it is worth saying out loud when a student first notices it.
5. **Work in order, and do not skip ahead.** The early levels build a relay and then NAND. From there the order is roughly NOT, AND, OR, XOR, half adder, full adder, and then a multi-bit adder. Pairs work at their own pace.
6. **The target for today is the adder.** Stop there. The game continues on into memory, an ALU, and a full CPU, and some students will want to keep going; point them at the homework rather than letting them race ahead of the class discussion.
7. **Circulate with one question.** When a pair completes a level, ask them which earlier part they reused. If they cannot answer, they clicked their way through and should redo the level. That question is the whole assessment for this segment.
8. **Turing Complete variant, if you own it.** Run it on one machine at the projector as a whole-class build. Take turns letting students direct the wiring out loud while you place components, and run the same progression from NAND to adder. It is more polished and more fun to watch, but it is one screen for the room, so it works best as a demonstration with the browser version as the hands-on option. Verify the current price before purchasing; it was about $20 as a one-time purchase.

**Purpose:** The claim that a computer is nothing but gates is not believable until you have personally built an adder out of nothing but NAND. This segment converts the claim into an experience.

### Segment 4: Stretch (1:15 to 1:20)

### Segment 5: List methods and iterating over lists (1:20 to 1:55), Coding strand

- **You do:** Start from where Week 6 ended. Lists exist and can be indexed. Now show that a list can change size.

  ```python
  shopping = ["milk", "eggs"]
  shopping.append("bread")
  shopping.remove("eggs")
  last = shopping.pop()
  print(shopping, last)
  ```
- **You do:** Name the shape of the syntax, because it is new and it is the first time they have seen it: the thing, a dot, and something the thing knows how to do. Contrast `len(shopping)`, a function you call on the list, with `shopping.append("x")`, a method the list itself carries. Do not go further into objects; Week 12 owns that.
- **You do:** Add `sort()` and the `in` test.

  ```python
  numbers = [5, 2, 9, 1]
  numbers.sort()
  print(numbers)
  print(9 in numbers)
  ```
  Point out that `sort()` changes the list in place and returns nothing, which is why `numbers = numbers.sort()` throws away the data. Show that mistake deliberately and let them see `None` printed.
- **You do:** Now traversal, which is the important one.

  ```python
  for item in shopping:
      print(item)
  ```
  Put it side by side with `for i in range(len(shopping)):` and `print(shopping[i])`. Both work. Say plainly which to prefer: iterate over the items when you want the items, and over the indexes only when you need the position. Then show a running total over a list of numbers, since that pattern shows up in every unit from here on.

  ```python
  total = 0
  for n in numbers:
      total = total + n
  print(total)
  ```
- **Students do, build one:** A shopping list manager. It loops, asks the user to add an item, remove an item, or quit, and prints the current list after every change. This exercises `append`, `remove`, `in` (to check before removing), and a `while` loop from Week 4.
- **Students do, build two if they finish:** Take a list of numbers and find the largest one with a loop, without using `max()`. The pattern of "keep a best-so-far variable and update it" is worth its own conversation, and it is a standard AP exam question shape.
- **You do:** Circulate. The two predictable errors are calling `remove()` on something not in the list, which raises `ValueError`, and modifying a list while looping over it, which produces baffling skips. Both are worth surfacing to the whole room when they happen.

### Segment 6: Wrap and homework (1:55 to 2:00)

- **You do:** Point at the board diagram, now filled in from transistor to CPU, and say that next week the question changes from "how does it work" to "why is one of these faster than another." Hand out homework, noting the Extra Credit AP Track section. Exit question: what does a latch remember? (Answer: one bit.)

## 7. Key scripts and analogies

- **Memory from feedback:** "Two gates each shouting the other one down. Whoever won last is still winning. That stalemate is a stored bit."
- **The clock:** "A drummer. Nobody in the band decides when to play; they all play when the drummer hits. Take the drummer away and the whole machine falls out of step within microseconds."
- **Register versus RAM:** "A register is what is on your desk right now, one or two things, instantly reachable. RAM is the filing cabinet across the room. Both hold work in progress, but only one of them is at your fingertips."
- **The ALU:** "A calculator that cannot do anything else and does not want to. Hand it two numbers and an operation code, get an answer back the same tick."
- **Fetch, decode, execute:** "Read the next line of the recipe, work out what it is asking, do it, then read the next line. Billions of times a second, and it never once wonders why."
- **NAND as the universal gate:** "One gate, from which every other gate can be built. It is the single Lego brick that the entire machine is made of. You are about to prove that yourself, not take my word for it."
- **Methods:** "`len(x)` is something you do to the list. `x.append(v)` is something the list knows how to do. Same result, different grammar, and the dot is the tell."
- **`for item in list`:** "You are not counting, you are going down the row and picking each thing up. Use index numbers only when the position itself matters."

## 8. Differentiation

- **Younger or newer students:** In the lab, pair them with a stronger partner and let reaching the XOR level count as a full success. Building an adder is a stretch goal, not a requirement. In the coding segment, `append`, `remove`, and `for item in list` are the core; `pop()` and the sort-in-place gotcha can wait. Give the shopping-list manager as a skeleton with the `while` loop already written.
- **Extensions for advanced or AP-track students:** In the lab, continue past the adder into the memory and ALU levels and report back next week on what a register level actually looked like. In Python, write the largest-number search as a function, then a second function that returns the *index* of the largest, which is the harder and more AP-flavored version. Point them at the Extra Credit AP Track section.

## 9. Common pitfalls

- **The lab swallows the session.** It is genuinely fun and students will not want to stop. Announce the 1:15 stop at the start of the segment and give a five-minute warning. The coding strand is not optional.
- **Progress does not save.** nandgame keeps progress in browser local storage. A different machine, a different browser, or a cleared cache means starting over. Tell students this before they invest thirty minutes.
- **Clicking through the lab without understanding.** Some pairs will solve levels by trial and error. The "which part did you reuse" question is your detector; use it on every pair at least once.
- **Latch derivation rabbit hole.** Do not attempt a full SR latch truth table on the board with this group. The feedback intuition plus the name is the correct depth here; formal sequential logic is a college topic.
- **`numbers = numbers.sort()`.** Destroys the list and leaves `None`. Show it deliberately so they recognize the symptom later.
- **`remove()` on a missing item.** Raises `ValueError`. Teach the `if item in list:` guard at the same time you teach `remove`.
- **Modifying a list while iterating over it.** Produces skipped items with no error message. If a student's loop misses every other element, this is why.
- **Confusing `pop()` and `remove()`.** One takes a position, the other takes a value. Say it that way every time.

## 10. Homework

Full details in `handouts/week-07-homework.md`. In summary: finish the adder in nandgame if it was not reached in class, or replay one level and write down which earlier parts it reused; a short written answer on what makes a circuit remember; a list-methods program; a loop that finds the largest value in a list without `max()`; optional Crash Course episodes on the ALU, registers and RAM, and the CPU. The handout closes with an Extra Credit AP Track section.

## 11. Assessment

Observational. In the lab, the diagnostic is whether a pair can name which previously built component they used inside the current one; that is the abstraction check and it matters more than how far they got. In the coding strand, watch for students writing `for i in range(len(x))` when `for item in x` would do, which usually means they are pattern-matching from Week 4 rather than reading their own problem. Homework is a completion check against the weekly-labs rubric. The half adder and the fetch-decode-execute cycle both appear on the Unit 2 checkpoint in Week 10.

## 12. AP alignment

Be plain with students about this one: almost nothing in this week's systems strand is AP CSP content. Latches, registers, the ALU, and the CPU cycle are not tested on the exam, and building an adder from NAND, valuable as it is, earns no exam points. Big Idea 4, Computer Systems and Networks, is about the internet rather than processor internals, and our course covers it in Unit 4.

The coding strand is where the AP value is this week: list methods and list traversal extend topic 3.10 Lists and apply 3.8 Iteration, and list-traversal questions are among the most common on the multiple-choice exam.

**AP-track self-study for this week, and only this week's slice.** One matching unit below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming, and one topic within it: list traversal, meaning walking a list item by item and doing something with each. That is a genuinely different cluster of lessons from last week's index-and-length material, and it is the only part of the unit to work this week. Strings are next week and nested iteration is the week after. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Do the traversal lessons, which finish the unit begun in Week 4 and continued in Week 6.

Nothing here is required of non-AP students.

## 13. Resources used this week

- nandgame, the free browser lab used in Segment 3: `https://nandgame.com`. Play it through to the adder during prep; the interface has a learning curve and Segment 3's steps assume you already know it. Verify the site is live before class.
- Turing Complete, the paid alternative on Steam: `https://store.steampowered.com/app/1444480/Turing_Complete/`. Roughly $20 as a one-time purchase for a single lab machine. Verify current price, platform support, and system requirements before buying; the lab is fully runnable without it.
- nand2tetris, for any student who wants the full build-the-stack version: `https://www.nand2tetris.org`. This is the extra-credit "Build the Stack" track in Section 9 of `curriculum/CS-Curriculum-and-Setup.md`.
- Human half adder: Segment 1 is complete on its own. It is the extension step of Human Logic Gates in `teaching-activities/Unplugged-Logic-Activities.md`.
- Crash Course Computer Science, Episode 5 ("How Computers Calculate: the ALU"), Episode 6 ("Registers and RAM"), and Episode 7 ("The Central Processing Unit"), assigned as optional homework viewing. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- Python list methods, for your own reference: `https://docs.python.org/3/tutorial/datastructures.html`
- CodeAI CSP Unit 6, Lists, Loops, and Traversals (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
- AP pseudocode list operations (`APPEND`, `INSERT`, `REMOVE`, `LENGTH`) and the list trace problems: `ap-track/AP-Pseudocode-Bridge.md`
