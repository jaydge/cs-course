# Week 10 Teacher Guide

## 1. Header

- **Week:** 10 of 32
- **Unit:** 2, Inside the Computer
- **Theme question:** What happens when you press a key?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Trace a key press from the physical switch to the lit pixel, naming at least eight stages in order.
- Explain what a scancode is and why it is not the same thing as a letter.
- Describe an interrupt as the mechanism by which hardware gets the CPU's attention.
- Explain that Python source is compiled into bytecode before anything runs, and show the bytecode for a small function using the `dis` module.
- Identify at least three bytecode instructions and say roughly what each one does.
- Connect their own Python line to the fetch, decode, execute cycle from Week 7.
- Demonstrate Unit 2 mastery on the checkpoint: gates, components, memory versus storage, the boot and key-press sequences, and short Python items.

## 3. Where this sits

This is the closing session of Unit 2 and the payoff for the previous four weeks. Everything the unit built in isolation gets assembled into one continuous story: a finger, a switch, a controller, a bus, an interrupt, a CPU cycle, memory, a GPU, and a lit pixel. If a student can tell that story, the unit worked.

The `dis` segment closes the other half of the loop, the one Week 4's Mystery Day promised. Students were told that a translator sits between their Python and the machine's numbers. Today they open it, look at the actual instruction list Python produces, and see that it is a stack machine doing exactly the fetch-decode-execute cycle from Week 7. This is also the deepest connection between the coding strand and the systems strand in the whole course, and it is worth teaching slowly.

The unit checkpoint closes the unit. Unit 3 opens next week with dictionaries and becomes the programming core of the year, so this is the last hardware-heavy session for a long stretch.

## 4. Materials and setup

- Printed Unit 2 checkpoint, one per student (see Section 11 for what it covers).
- A sacrificial keyboard that can be opened, ideally a cheap membrane one, plus a screwdriver. A mechanical keyboard with a removable keycap and a visible switch is even better if you have one.
- Twelve index cards, each labeled with one stage of the signal path, for the human relay in Segment 3. Write these during prep.
- One index card with a large letter A on it, to act as the signal being passed.
- Whiteboard with the theme question and space to keep the full path visible all session.
- Student laptops with Thonny; projector for live coding.
- Printed Week 10 homework handout, one per student.
- Optional: last week's Raspberry Pi and the teardown parts, left on the table as props for the consolidation segment.

## 5. Pre-class prep checklist

- **Write and print the Unit 2 checkpoint.** Keep it to about fifteen minutes of work; the contents are specified in Section 11. Print one per student plus two spares. (25 min)
- Open the sacrificial keyboard during prep so you know how many screws it has and whether the membrane layers come apart cleanly. Have it half-opened and ready on the front table rather than opening it cold in class. (15 min)
- Write the twelve signal-path cards for Segment 3, one stage per card, in large letters. Shuffle them before class; the class puts them in order. (10 min)
- Run `dis.dis()` on your examples on the classroom's Python version and print or screenshot the output. **This matters:** bytecode instruction names change between Python versions, and the output on 3.11 and later differs noticeably from older versions, including extra instructions like `RESUME` at the top. Teach from whatever your machines actually produce, not from a remembered example. (15 min)
- Decide which three or four instruction names you will name explicitly, based on that output, and write them on a card. (5 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up (0:00 to 0:10)

- **You do:** Quick homework review, focusing on question 4c, the nested-loop indentation bug, and on the boot sequence ordering.
- **You do:** Pose the theme question by doing it. Press a single key on the demo laptop so a letter appears on the projected screen. Then say: name everything that just happened, in order. Take answers for two minutes and write them on the board in whatever order they come. Do not correct or reorder yet.
- **Purpose:** Establishes that they already know most of the pieces and are missing only the sequence, which is exactly the state you want before Segment 3.

### Segment 2: What is actually under a key (0:10 to 0:25), Systems strand

1. **Pull one keycap off** the mechanical keyboard, or open the membrane keyboard's case, and pass it around. Let them see that a key is a switch and nothing more. This connects directly to the switches they wired in Week 6.
2. **Show the layers on a membrane keyboard.** Two flexible plastic sheets printed with conductive traces, separated by a spacer sheet with holes. Pressing a key pushes the top layer through a hole so the two traces touch. That is the entire mechanism, and it costs almost nothing to manufacture.
3. **Explain the matrix, which is the interesting part.** A keyboard with 104 keys does not have 104 wires going to its chip. The keys are wired in a grid of rows and columns, so around twenty wires cover all of them. Draw a small 3 by 3 grid on the board and show that closing one switch connects one row to one column, and that the pair of numbers identifies the key uniquely. Ask how many keys a 10 by 10 grid can address, and let them get to a hundred.
4. **Introduce scanning.** The little chip inside the keyboard energizes one row at a time, thousands of times per second, and checks which columns respond. That is how it knows what is pressed. Say the consequence: the keyboard contains a small computer whose only job is to watch switches. There are dozens of these tiny processors in a laptop.
5. **Mention debounce in one sentence.** A metal contact physically bounces on closing, so the raw signal shows several rapid on-off transitions. The controller ignores changes for a few milliseconds after the first one. Without that, one press would type five letters.
6. **Name the scancode.** What leaves the keyboard is not the letter A. It is a number identifying which physical key changed state. What that key means depends entirely on the layout the operating system is using, which is why the same keyboard types different characters on a French system. Write on the board: keyboards send positions, not letters.

### Segment 3: Follow the signal, human relay (0:25 to 0:55), Systems strand

Run this from the steps below. It is the flagship activity of the unit.

1. **Hand out the twelve shuffled stage cards,** one per student, doubling up if the group is small. Do not explain them yet.
2. **Have the class arrange themselves in order,** standing in a line across the room, discussing among themselves. Give them four or five minutes and stay out of it. Arguments about whether the driver comes before or after the interrupt are the productive part.
3. **Walk the line and correct it together.** The correct order, which you should also write on the board and leave up for the rest of the session, is: the finger presses the switch; the keyboard matrix registers a row and column; the keyboard controller debounces and produces a scancode; the scancode is packaged into a USB report and sent when the host asks for it; the host controller in the computer receives it and raises an interrupt; the CPU stops what it was doing and runs the keyboard driver's handler; the operating system translates the scancode into a character using the current keyboard layout; the operating system puts an event into a queue and delivers it to whichever window has focus; the application decides what the character means, in this case inserting it into a document; the application asks the graphics layer to draw the updated text, and the glyph is turned into pixels; the GPU composites the finished frame into the framebuffer; the display controller scans that frame out to the panel and the pixels change.
4. **Now run the signal.** Hand the letter A card to the first student. Each student says their stage out loud in one sentence, then passes the card on. Do it once slowly. Then do it again, fast, with no hesitation. The second run is what makes it stick.
5. **Add the interrupt properly, because it is the concept students most often miss.** Ask what the CPU was doing before the key was pressed. It was working on something else entirely. Nobody was checking the keyboard. The hardware raised its hand and the CPU dropped what it was doing, handled it, and went back. Have the student holding the interrupt card physically tap the student holding the CPU card on the shoulder mid-sentence, so the CPU student has to stop, deal with it, and resume. That thirty seconds teaches interrupts better than a diagram does.
6. **Ask the timing question.** How long did all twelve stages take in reality? Answers will vary wildly. Give the honest range: typically a few tens of milliseconds from press to visible pixel, most of it spent in display refresh and software layers rather than in the electrical parts. Then land the comparison: at billions of cycles per second, the CPU executed an enormous number of instructions during that time and spent most of it idle or doing other work. The machine is almost always waiting for us.
7. **Ask the abstraction question, which is the real point.** Ask how many of these twelve stages the application programmer had to think about. Essentially none. Each layer hides the one below it, which is why one person can write a text editor without knowing anything about keyboard matrices. Write the word on the board: abstraction. Say that this is the single most important idea in the whole course and that the entire year is layers of it.
8. **Extend to the mid-year milestone.** Tell them that in Week 21 they will do this same exercise for a whole web page, from the button press to a server and back, and that it is the mid-year assessment. Today's twelve stages are the first half of that path.

**Purpose:** Unit 2 becomes one continuous story rather than five separate topics, and abstraction gets named at the exact moment students have enough concrete detail for the word to mean something.

### Segment 4: Stretch (0:55 to 1:00)

### Segment 5: Python bytecode with `dis` (1:00 to 1:30), Coding strand

- **You do:** Call back to Week 4's Mystery Day. You told them a translator sits between Python and the machine. Today you open it.
- **You do:** At the projector, in Thonny, write and run:

  ```python
  import dis

  def add(a, b):
      return a + b

  dis.dis(add)
  ```
  Read the output together. Do not pretend the exact instruction names are the ones you memorized; read what your Python version actually prints. Typically there is a load for each argument, a binary operation that adds them, and a return. Name three or four instructions explicitly and write them on the board with a plain-English meaning next to each: load a value, do an operation on the top values, return the result.
- **You do:** Make the connection to Week 7 explicit and slow. Each of those lines is one instruction. The CPU fetches it, decodes it, executes it, and moves to the next. This list is the recipe; the fetch-decode-execute loop is the cook. Point at the whiteboard where the CPU diagram still is.
- **You do:** Explain the stack in one image, without formal detail. Instructions push values onto a pile and pop them off. `LOAD` puts a value on the pile, the add instruction takes the top two off, adds them, and puts the answer back. Walk `add(3, 4)` through it verbally, one instruction at a time, saying what is on the pile after each.
- **Students do:** Run `dis.dis()` on a function of their own from an earlier week, ideally one of their Hangman functions or the vowel counter, and count how many bytecode instructions one line of their Python turned into. Have a few call the number out. The spread surprises them.
- **You do:** Show the compiler being clever.

  ```python
  dis.dis("x = 2 + 3")
  ```
  It never adds anything at runtime; the 5 is already computed and stored as a constant. Ask why. Because the compiler could see both numbers ahead of time, so doing the work once at compile time is free. Name it: this is what an optimizing compiler does, and it is why the code that runs is not always exactly the code you wrote.
- **Students do, if time allows:** Compare the bytecode of a `for` loop with the bytecode of the same work written out three times by hand. The loop version is shorter in source and includes a jump instruction that sends execution backwards. Point at the jump and say that this is what a loop actually is at the machine level: an instruction that changes which instruction comes next.
- **You do:** Say the honest caveat out loud, because a curious student will hit it. Python's bytecode is not the CPU's machine code. It is an intermediate language executed by the Python interpreter, which is itself a program made of real machine code. So there are two translation layers here, not one. Languages like C compile straight to machine instructions. Saying this plainly costs thirty seconds and prevents a genuine misconception.

### Segment 6: Unit 2 consolidation (1:30 to 1:40)

- **You do:** Build the whole stack on the board in one column, bottom to top, asking the class to supply each layer: electricity, transistor, logic gate, adder and latch, register and ALU, CPU, motherboard and buses, firmware and boot, operating system, application, Python bytecode, the line of Python they wrote. Twelve rows, five weeks of work, one board.
- **You do:** Ask one question about it: which of these layers did you not know existed five weeks ago? Let them answer. That is the unit's assessment in a single question.
- **You do:** Photograph the board. It is the reference you will point at in Week 21 and again in the final project.

### Segment 7: Unit 2 checkpoint and wrap (1:40 to 2:00)

- **Students do:** Complete the checkpoint individually, no laptops, about fifteen minutes. Say clearly that it is low-stakes and diagnostic.
- **You do:** Collect it. Hand out homework as students finish, noting the Extra Credit AP Track section and telling them that Unit 3 starts next week and is the programming core of the year.

## 7. Key scripts and analogies

- **A key is a switch:** "It is the same switch you wired on a breadboard in Week 6. There is nothing else under there. A hundred of them, watched by a tiny computer whose entire career is noticing whether anything moved."
- **The matrix:** "Not 104 wires. A grid, like naming a seat in a theater by row and column. Twenty wires, a hundred keys."
- **Scancodes:** "The keyboard does not know the alphabet. It sends you a position, not a letter. Which letter that position means is the operating system's opinion, and in France it is a different opinion."
- **Interrupts:** "The CPU is not watching the keyboard, any more than you are watching your front door. The doorbell exists so you do not have to. Hardware raises its hand, the CPU drops everything, deals with it, and goes back to what it was doing."
- **Layers:** "Twelve stages, and the person who wrote the text editor thought about roughly one of them. Every layer's job is to make the layer below it somebody else's problem. That is abstraction, and it is why software can be built at all."
- **On speed:** "The whole trip takes a few hundredths of a second, and in that time the CPU could have done tens of millions of things. Your computer spends nearly all of its life waiting for you."
- **Bytecode:** "You write a sentence. Python translates it into a list of very small, very boring instructions. Then the machine does them one at a time and never wonders what the sentence meant."
- **The stack:** "A pile of plates. Load puts a plate on top. Add takes the top two, mashes them together, and puts one plate back. That is most of what bytecode does."
- **Constant folding:** "You asked for 2 plus 3. The compiler already knows the answer, so it just writes 5. The code that runs is not always the code you wrote, and that is a feature."

## 8. Differentiation

- **Younger or newer students:** In the relay, give them a stage in the physical half of the path, which is more concrete, and pair them with a partner for the sentence. For the checkpoint, the Python items are the ones most likely to be hard; the systems items reward the students who engaged with the labs, which is deliberate. In the `dis` segment, running it and counting instructions is a complete success; understanding the stack is optional.
- **Extensions for advanced or AP-track students:** Have them find where in the path a wireless keyboard differs from a wired one, and report the answer next week. In `dis`, have them compare the bytecode of `x = x + 1` and `x += 1`, or of a list comprehension against the equivalent loop, and explain the difference. Anyone who wants the full version of this idea should be pointed at nand2tetris and the Build the Stack extra-credit track.

## 9. Common pitfalls

- **Running out of time for the checkpoint.** The relay is fun and will expand to fill any space you give it. Hard stop Segment 3 at 0:55. If something must be cut, cut the loop-bytecode comparison at the end of Segment 5, not the checkpoint.
- **Bytecode names not matching your notes.** Instruction names differ across Python versions. Generate your examples on the classroom Python during prep and teach from that output.
- **Students concluding bytecode is machine code.** Say the two-layer caveat explicitly. It takes half a minute and prevents a misconception that would resurface in Unit 5.
- **The relay becoming a lecture.** The students hold the cards and say the sentences. If you find yourself narrating all twelve stages, stop and hand it back to them.
- **Skipping the interrupt shoulder-tap.** It looks like a gimmick and it is the most effective thirty seconds of the session. Do it.
- **Checkpoint anxiety.** Same framing as Unit 1: low-stakes and diagnostic, counting under the unit-checkpoint slice of the grade. Say it before you hand it out, not after.
- **Treating "which part thinks" as settled.** Expect students to have moved back toward "the CPU understands" over the week. Re-ask it during the consolidation and hold the line.

## 10. Homework

Full details in `handouts/week-10-homework.md`. In summary: write the full key-press path from memory in their own words; a short written answer on what an interrupt is; run `dis` on two of their own functions and answer three questions about the output; one written reflection on abstraction; optional Crash Course episodes on instructions and programs, keyboards, and screens. It is deliberately lighter than usual because the checkpoint was in class. The handout closes with an Extra Credit AP Track section, which for this week is a consolidation and self-audit rather than a new unit.

## 11. Assessment

**Unit 2 checkpoint**, administered in Segment 7, about fifteen minutes, no laptops. It covers:

- Truth tables for AND, OR, and NOT, plus the output of one two-gate combination (Week 6).
- One short answer: what a transistor is, in one sentence (Week 6).
- Labeling six components on a printed motherboard diagram: CPU socket, RAM slots, PCIe slot, SATA or M.2, firmware chip, CMOS battery (Weeks 8 and 9).
- Two short answers: the difference between RAM and storage in terms of what survives a power cut, and one advantage and one disadvantage of an SSD compared with a mechanical hard drive (Week 8).
- Two ordering items: the boot sequence (Week 9) and the key-press signal path, given as scrambled steps (Week 10).
- Three short Python items: index into a given list, evaluate a given string slice, and state how many times the body of a given nested loop runs (Weeks 6, 8, and 9).

Score it against the unit-checkpoint component of the grade. Read it diagnostically as well as evaluatively. A weak result on the Python items, particularly the slice and the nested-loop count, matters more than a weak result on the hardware items, because Unit 3 depends on the former and not the latter; flag those students for deliberate pairing in Week 11. A student who does well on the ordering items but poorly on the labeling probably learned the narrative without the lab, which is worth a conversation but not a remediation.

Also observational: during the consolidation segment, whether a student can supply a layer of the stack unprompted.

## 12. AP alignment

This session introduces no new AP CSP topics, and that is the honest description of it. The key-press path, interrupts, and Python bytecode are not in the framework. The one genuine connection is conceptual rather than topical: the layered-abstraction idea at the heart of Segment 3 is a computational thinking practice that the exam does test, in the form of questions about what an abstraction hides and why that is useful.

The checkpoint covers material from Weeks 6 through 10, of which the AP-relevant slices are 3.5 Boolean Expressions, 3.10 Lists, 3.4 Strings, and 3.8 Iteration.

**AP-track self-study for this week, and only this week's slice.** This week is a consolidation week rather than a new-unit week, and it is extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming. Finish anything outstanding in the programming unit rather than starting a new one. Unit 3, Data Representation, was already worked in Week 2, and the units after Programming line up with our Unit 3 and Unit 5, so there is nothing to gain from starting one early. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** finish Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`, which has been the target for Weeks 6, 7, and 9. Students who have completed it should not start Unit 7 yet; it belongs with our Unit 3 from Week 11.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human signal relay: Segment 3 is complete on its own. Write the twelve stage cards during prep from the ordered list in step 3.
- Keyboard teardown: Segment 2 is complete on its own. Use a cheap membrane keyboard you do not mind destroying.
- Python `dis` module documentation, including the current instruction list for your Python version: `https://docs.python.org/3/library/dis.html`. Worth opening during prep specifically to confirm the instruction names your version emits, since they change between releases.
- Crash Course Computer Science, Episode 8 ("Instructions and Programs"), Episode 22 ("Keyboards and Command Line Interfaces"), and Episode 23 ("Screens and 2D Graphics"), assigned as optional homework viewing. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- nand2tetris, for students who want to build the whole stack themselves: `https://www.nand2tetris.org`. This is the Build the Stack extra-credit track in Section 9 of `curriculum/CS-Curriculum-and-Setup.md`.
- Mid-year milestone that this session sets up: "trace the button press," Section 3 of `curriculum/CS-Curriculum-and-Setup.md`, assessed in Week 21.
- CodeAI CSP Unit 6 (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
- AP CSP topic coverage, for the self-audit in the handout: `ap-track/AP-CSP-Topic-Coverage.md`
