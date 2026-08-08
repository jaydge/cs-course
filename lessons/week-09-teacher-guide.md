# Week 9 Teacher Guide

## 1. Header

- **Week:** 9 of 32
- **Unit:** 2, Inside the Computer
- **Theme question:** Which part actually thinks?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Describe the motherboard's job as connecting parts rather than computing, and locate six landmarks on a real board.
- Explain what a bus is and why the address lines, data lines, and control lines are separate.
- State what firmware is and what UEFI does between the power button and the operating system.
- Put the boot sequence in order: power on, firmware self-test, find the boot device, load the bootloader, start the operating system.
- Say why a Raspberry Pi is a complete computer and point to its processor, memory, storage, and ports.
- Answer the theme question correctly: the CPU executes, and nothing in the machine understands anything.
- Write a nested loop, and predict how many times the inner body runs given the two ranges.

## 3. Where this sits

Week 8 laid the parts on the table. This week puts them back into relationship with each other and adds the two things a pile of components still lacks: the wiring that connects them, and the firmware that wakes them up. That completes the hardware picture, so Week 10 can walk a single key press across the finished machine and close the unit.

This session also serves as the unit's Mystery Day. "Which part actually thinks?" is a wow question with a genuinely surprising answer, and it is the right place to say clearly that no component understands anything, which is a claim students need before the AI unit in Week 27 lands honestly.

On the coding side, nested loops are the last new control structure before Unit 3. They are the piece students most often fake their way through, so the segment is built around predicting iteration counts out loud before running anything.

## 4. Materials and setup

- The dead or spare motherboard, plus the parts removed during last week's teardown if you left them out.
- A machine you can safely enter firmware setup on: the teardown PC if it still boots, or a spare Windows laptop. Know the key beforehand, since it varies by manufacturer.
- Raspberry Pi with power supply, microSD card, HDMI cable, monitor or TV, keyboard, and mouse. Boot it before class and leave it running.
- A short length of ribbon cable or a bundle of jumper wires, to hold up as a physical bus.
- Whiteboard with the theme question, plus space for the bus diagram and the boot sequence list.
- Student laptops with Thonny; projector for live coding.
- Printed Week 9 homework handout, one per student.

## 5. Pre-class prep checklist

- Boot the Raspberry Pi and confirm it reaches the desktop, that the display works at the right resolution, and that the keyboard and mouse are paired or plugged in. Run the four commands from Segment 4 once so you know what output they give on your Pi. (20 min)
- Find and note the firmware setup key for whichever machine you will demonstrate on. Common ones are Delete, F2, F10, and F12, pressed repeatedly during the first second after power on. Get into setup once during prep so you are not fumbling in front of the class, and make a note of one harmless setting you can point at, such as boot order. (15 min)
- Do not change any firmware settings you do not intend to change back, and know how to exit without saving. (Included above.)
- Identify the six landmarks on your specific dead motherboard and mark them with small sticky flags: CPU socket, RAM slots, PCIe slots, SATA or M.2 connectors, the firmware chip, and the CMOS battery. Board layouts differ, and hunting for the firmware chip in front of the class wastes five minutes. (15 min)
- Write and test the nested-loop examples, the multiplication table, and one ASCII art pattern. (15 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up (0:00 to 0:10)

- **You do:** Homework check on the slicing answers; put the three that were most often wrong on the board.
- **You do:** Pose the theme question and take a vote. Write the candidates on the board (CPU, RAM, motherboard, the operating system, the screen) and count hands. Do not reveal anything. Tell them the answer arrives at the end of the session and that most of them are about to be half right.

### Segment 2: The motherboard and buses (0:10 to 0:30), Systems strand

Work directly on the dead board, passing it around or gathering the group around one table.

1. **State the board's job in one sentence.** It computes nothing. It is the wiring, the power distribution, and the connectors that let the parts talk. Then show the copper: hold the board at an angle to the light so the traces are visible, and let them see that it is thousands of tiny wires printed on layered fiberglass.
2. **Find the six landmarks together,** using your sticky flags as the answer key but letting students guess first. The CPU socket, the largest and most intricate connector. The RAM slots, the long thin ones with clips at both ends. The PCIe slots, the long ones near the back edge for expansion cards. The SATA ports, the small L-shaped connectors, or the M.2 slot, a short flat one on the surface. The firmware chip, a small rectangular chip usually labeled with the board maker's name. The CMOS battery, an obvious coin cell.
3. **Explain the coin cell, because it is the best small mystery on the board.** It keeps a tiny amount of settings memory and the real-time clock alive while the machine is unplugged. Tell them that when an old computer forgets the date every time it is unplugged, that battery is dead, and it costs about a dollar. Students remember this one.
4. **Introduce the bus.** Hold up the ribbon cable or wire bundle. A bus is a shared set of wires that many components connect to at once, rather than a private wire between every pair of parts. Ask why sharing is worth it, and let them reach the answer themselves by counting how many private wires you would need to connect eight components to each other.
5. **Split the bus into its three jobs, on the board.** Address lines carry which location we want. Data lines carry the actual value. Control lines carry whether this is a read or a write, and when. Give the postal analogy: the address on the envelope, the contents of the envelope, and the instruction "deliver" or "collect."
6. **Name the buses they can see.** PCIe for expansion cards and graphics, SATA for drives, USB for peripherals, and the memory bus between the CPU and the RAM slots. Point at each physically. Say that the difference between these is mostly how fast they are and how far the signal has to travel, and that the closer to the CPU a bus is, the faster it tends to be, which is the Week 8 hierarchy showing up again in physical distance.

### Segment 3: Firmware, UEFI, and the boot sequence (0:30 to 0:50), Systems strand

1. **Ask the question that motivates firmware.** The operating system is a program stored on the drive. Who reads it off the drive? Something has to run before the operating system exists in memory, and it cannot itself come from the drive. Let them sit with the chicken-and-egg problem for a moment.
2. **Answer it.** A small program permanently stored in that chip on the motherboard, the one you flagged in Segment 2. Called BIOS on older machines and UEFI on modern ones. Firmware is the word for software that lives in hardware and is always there, whether or not a drive is even connected.
3. **Write the boot sequence on the board as a numbered list and leave it up.** Power arrives and the power supply stabilizes. The firmware runs a self-test, checking that a CPU and memory are present and working. The firmware looks through its boot order for a device holding a bootloader. It loads the bootloader into RAM and hands control to it. The bootloader loads the operating system kernel. The operating system starts services and eventually draws a login screen.
4. **Demonstrate it live.** Power on the demo machine and press the setup key repeatedly. Show the setup screen, walk through the boot order list, and point out that the machine will try each device in order. Say that this is how a recovery USB gets used, and that it is the same mechanism they will use in Unit 4. Exit without saving.
5. **Say what UEFI added over BIOS, briefly.** Support for drives larger than about two terabytes, a graphical interface with mouse support, faster startup, and Secure Boot, which checks that the bootloader is signed before running it. Note the tradeoff out loud: Secure Boot is real protection and also the thing that gets in the way of installing another operating system, which is a genuine tension rather than a flaw.
6. **Connect it to the Mac side.** Macs boot differently and do not expose a UEFI setup screen. Apple Silicon machines hold the power button to reach startup options instead. Tell them the concept is the same, that firmware runs first and then finds an operating system to load, but the buttons differ. Do not go further; Unit 4 handles operating systems properly.

### Segment 4: Raspberry Pi tour (0:50 to 1:15), Systems strand

The Pi should already be booted to the desktop before the class gathers.

1. **Hand it around, unpowered, first.** Let each student hold the board. Then say the thing that makes the point: this costs a small fraction of a laptop, fits in a hand, and is a complete computer running a full operating system.
2. **Find last week's components on it.** Have students point them out on this board using the vocabulary from Week 8. The processor, a single chip in the middle that also contains the graphics and often the memory, which is why it is called a system on a chip. The RAM, either stacked with the processor or as a separate small chip. The storage, which is the microSD card, and it slides out. The ports, USB, ethernet, HDMI, and the power input. The GPIO header, the double row of forty pins, which is the thing a laptop does not have.
3. **Pull the microSD card out while it is powered off and hold it up.** Say plainly that this is the whole hard drive, and that swapping the card swaps the computer's entire installation. This is a genuinely surprising fact for students used to sealed laptops.
4. **Power it on and show it running.** A desktop, a web browser, a file manager, and Python already installed. Open Thonny on the Pi, since it ships with the standard Raspberry Pi OS image, and run a one-line program in front of them. The point is that this is not a toy version of a computer.
5. **Open a terminal and run four commands, reading the output aloud.** `lscpu` for the processor and core count. `free -h` for total and used memory. `df -h` for storage and free space. `vcgencmd measure_temp` for the processor temperature, which ties back to the giant heatsink in last week's PC. Do not teach the terminal here; Unit 4 owns that. Today it is just a window that shows you the specifications.
6. **Point at the GPIO header and say what it means.** Forty pins that a program can turn on and off directly. Connect it back to Week 6: the LEDs and switches they wired by hand could be wired to these pins and controlled by Python instead of a finger. That is what "embedded" means, and it is the hardware extra-credit track in the curriculum.
7. **Answer the theme question, which is the wow moment of the unit.** Take the vote again from Segment 1. Then answer it properly. The CPU is the only part that executes instructions, so if anything "thinks," it is that. But then push harder: the CPU is following a fetch-decode-execute loop over numbers, and it has no idea what any of the numbers mean. There is no understanding anywhere in the machine, at any layer, only a very fast, very literal chain of switches. The intelligence in a computer belongs entirely to the person who wrote the instructions. Sit in the silence for a second, then tell them Week 27 asks whether that is still true of AI, and that they will be better equipped to answer it than most adults.

**Purpose:** The Pi collapses the whole unit into one object a student can hold, and the theme question gives the unit its punchline.

### Segment 5: Stretch (1:15 to 1:20)

### Segment 6: Nested loops (1:20 to 1:55), Coding strand

- **You do:** Build up from the loop they know. Write a single loop printing 1 to 3, run it, then put a second loop inside it.

  ```python
  for i in range(1, 4):
      for j in range(1, 4):
          print(i, j)
  ```
  Before running, ask the class how many lines will print. Take answers, then run it. Nine. Write on the board: the inner loop runs completely, every single time the outer loop takes one step.
- **You do:** Make it physical. Say the outer loop is hours and the inner loop is minutes; the minute hand goes all the way around for each single hour. Then have three students act it out: the outer student takes one step forward, and the inner student paces three times before the outer student moves again.
- **You do:** Show the multiplication table, which is the classic and remains the best example.

  ```python
  for row in range(1, 11):
      for col in range(1, 11):
          print(row * col, end="\t")
      print()
  ```
  Two things here need explicit naming. `end="\t"` stops `print` from starting a new line and inserts a tab instead. The bare `print()` after the inner loop is what ends the row, and it must be indented to the outer loop, not the inner one. Deliberately indent it wrongly first, run it, and let them see the whole table collapse into one long line. That mistake is the entire lesson of the segment.
- **Students do:** Type the multiplication table and get it working. Then change it to a 5 by 5 table, then to a table that only shows even products.
- **You do:** Move to ASCII art, where the inner loop count depends on the outer loop variable.

  ```python
  for row in range(1, 6):
      for star in range(row):
          print("*", end="")
      print()
  ```
  Run it and get a triangle. Ask why the rows get longer, and get the answer that the inner range depends on `row`. That is the idea worth having.
- **Students do, build:** Produce three shapes, using a nested loop for each: a 5 by 5 square of stars, a left-aligned triangle, and a right-aligned triangle (which needs spaces printed before the stars). The third one is genuinely challenging and is the right stretch target.
- **You do:** Circulate. The three predictable errors are indentation of the closing `print()`, using the same variable name for both loops, and expecting `end=""` to be needed on the outer print when it is not.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Tell them that next week the unit closes by following one key press through everything they have seen, and that there is a short checkpoint. Hand out homework, noting the Extra Credit AP Track section. Exit question: a nested loop with `range(4)` outside and `range(5)` inside runs its inner body how many times? (Answer: 20.)

## 7. Key scripts and analogies

- **The motherboard:** "It computes nothing. It is the city's roads and power lines. Nothing there thinks, and nothing works without it."
- **A bus:** "A shared hallway instead of a private tunnel between every pair of rooms. Eight components connected privately need twenty-eight tunnels. One hallway is cheaper, and the only cost is taking turns."
- **The three bus lines:** "The address on the envelope, the letter inside, and the instruction telling the postman whether to deliver or collect."
- **Firmware:** "Software that lives in the hardware and is there before anything else is. The operating system is on the drive, so somebody has to go get it. Firmware is that somebody."
- **The boot sequence:** "Wake up, check you still have all your limbs, find your shoes, put them on, then start the day. The self-test really is the machine checking it still has a CPU and memory."
- **The CMOS battery:** "A dollar coin cell keeping the clock alive while the machine is unplugged. When an old computer thinks it is 2009 every morning, that is what died."
- **The Raspberry Pi:** "A whole computer on one board, and its hard drive is a memory card you can pull out with two fingers. Swap the card and it is a different computer."
- **Which part thinks:** "The CPU executes. Nothing understands. There is no meaning anywhere in there, only switches following rules very fast. The only understanding in the room is yours."
- **Nested loops:** "Hours and minutes. The minute hand goes all the way around for every single tick of the hour hand. Outer step, full inner sweep, outer step, full inner sweep."

## 8. Differentiation

- **Younger or newer students:** In the systems segments, give them a labeled diagram of a motherboard to match against the real board, rather than finding landmarks unaided. In the coding segment, the multiplication table typed and working is a full success; the shapes are optional and the right-aligned triangle definitely so. Pairing works well here since the two loop variables are easier to keep straight when one person says them out loud.
- **Extensions for advanced or AP-track students:** Have them find the firmware version on a classroom machine and look up what its most recent update changed. On the Pi, they can inspect `/proc/cpuinfo` and report what it says. In Python, have them print a multiplication table with aligned column headers, or produce a diamond shape, which requires two nested loop sections and real thought about the space counts. Point them at the Extra Credit AP Track section.

## 9. Common pitfalls

- **Changing firmware settings by accident.** Know your exit-without-saving key before you enter setup. Never demonstrate on a student's daily machine.
- **The Pi does not boot in front of the class.** Boot it during prep and leave it running. A Pi that will not display is nearly always the HDMI port or the display's input selection, not the Pi, but you do not want to debug that live.
- **Losing the microSD card.** It is small, it is the entire computer, and it will end up on the floor. Pass it in a tray, not hand to hand.
- **Static on the bare board.** Same rules as last week: hold boards by the edges, and use the strap if you have it out.
- **Nested-loop indentation.** The single biggest source of confusion this week. Have students read their indentation aloud, and put the wrong version on the projector deliberately so they know the symptom.
- **Reusing the same loop variable.** `for i` inside `for i` produces behavior no student can debug on their own. Enforce distinct names, and prefer meaningful ones like `row` and `col` over `i` and `j`.
- **Iteration-count guessing.** Do not let students run a nested loop before predicting the count out loud. Once they run it, the number is given to them and the thinking never happens.
- **Answering the theme question too early.** Hold it to Segment 4. The vote at the start and the reveal at the end are what make it land.

## 10. Homework

Full details in `handouts/week-09-homework.md`. In summary: label six components on a motherboard diagram; put the boot sequence in order; a short written answer on what firmware is and why it cannot live on the hard drive; finish the multiplication table and the two triangles; one nested-loop counting question; a short written answer to the theme question; optional Crash Course episode on integrated circuits. The handout closes with an Extra Credit AP Track section. It also warns students that Week 10 has the Unit 2 checkpoint and lists what it covers.

## 11. Assessment

Observational. In the systems segments, the diagnostic is whether a student can point at the firmware chip and say what it does without prompting, and whether they can put the boot steps in order when asked cold. In the coding strand, the diagnostic is the prediction: a student who can state the iteration count before running understands nested loops, and a student who runs first does not yet. Homework is a completion check against the weekly-labs rubric. Motherboard identification, the boot sequence, and one nested-loop trace all appear on the Unit 2 checkpoint next week, so any student who is shaky here should be flagged now.

## 12. AP alignment

This session covers AP CSP topic 3.8 Iteration in the coding strand, extending Week 4's loops into nested iteration, which appears regularly on the exam in trace questions and in grid-and-robot problems.

The systems strand does not map to AP CSP at all, and this is the weakest week of the unit for AP purposes. Motherboards, buses, firmware, boot sequences, and single-board computers appear nowhere in the framework. Say so plainly to AP-track students rather than inventing a connection; the correct instruction for them this week is to keep working the programming unit.

**AP-track self-study for this week, and only this week's slice.** One matching unit below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming. Continue in the programming unit and work the iteration lessons, including any nested-loop material. If a student has already finished that unit across Weeks 3 through 8, the better use of this week is the pseudocode trace practice in the handout rather than starting a new unit early. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. This is the third week pointing at Unit 6, which is deliberate: it is the unit that matches our coding strand right now. Students who have finished it can begin Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`, which lines up with our Unit 3 rather than with this week.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Motherboard landmarks and the Raspberry Pi tour: Segments 2 and 4 are complete on their own. Flag your specific board during prep, since layouts differ between manufacturers.
- Raspberry Pi documentation, for your own reference and for the GPIO extension: `https://www.raspberrypi.com/documentation/`. Review only if you plan to go beyond the four commands in Segment 4.
- Firmware setup keys vary by manufacturer. Look up the key for your specific demo machine during prep; the common candidates are Delete, F2, F10, and F12.
- UEFI specification and background, if you want the authoritative source for your own reading: `https://uefi.org`. Not needed to teach the segment.
- Crash Course Computer Science, Episode 17 ("Integrated Circuits and Moore's Law"), assigned as optional homework viewing, which explains why all of this fits on one board. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- Hardware and embedded extra-credit track, for students who want to drive the GPIO pins: Section 9 of `curriculum/CS-Curriculum-and-Setup.md`.
- CodeAI CSP Unit 6 (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
- AP pseudocode loop notation and trace problems: `ap-track/AP-Pseudocode-Bridge.md`
