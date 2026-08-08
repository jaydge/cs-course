# Week 9 Homework: The Board, the Boot, and Loops Inside Loops

This week you saw how the parts are wired together, what wakes a computer up before the operating system exists, and how to put a loop inside a loop. Plan on about 40 minutes.

**Heads up: next week has the Unit 2 checkpoint.** It is short, low-stakes, and diagnostic, and it is written to cover exactly what we did in Weeks 6 through 10. What is on it is listed at the bottom of this handout, above the extra credit section. Nothing to cram; just read the list.

## 1. Label the board

Find a photo of a desktop motherboard online, or use one from your notes, and label these six things:

- CPU socket
- RAM slots
- PCIe slot
- SATA port or M.2 slot
- Firmware chip (BIOS or UEFI)
- CMOS battery

Then answer in one sentence: what does the motherboard itself actually compute?

## 2. Put the boot in order

These five steps are scrambled. Write them in the right order.

- The bootloader loads the operating system.
- The firmware runs a self-test to check the CPU and memory are present.
- Power arrives and the power supply stabilizes.
- The firmware finds a boot device and loads the bootloader from it.
- The operating system starts up and eventually shows a login screen.

## 3. One written answer

What is firmware, and why can it not just be stored on the hard drive like everything else? Two or three sentences.

## 4. Counting nested loops

No computer for these. Work them out on paper, then check in Thonny.

**a.** How many lines does this print?

```python
for a in range(4):
    for b in range(5):
        print(a, b)
```

**b.** How many stars does this print in total?

```python
for row in range(1, 5):
    for star in range(row):
        print("*", end="")
    print()
```

**c.** What is wrong with this one, and what does it produce instead of a table?

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
        print()
```

## 5. Finish the shapes

Get all three working and save them in your CS Class folder:

- A 5 by 5 square of stars.
- A left-aligned triangle that grows from one star to five.
- A right-aligned triangle, where each row has spaces before the stars so the right edge lines up. This one is harder. Work out how many spaces row 1 needs, then row 2, and find the pattern before you write the loop.

## 6. The theme question

In your own words, three or four sentences: which part of the computer actually thinks? Say what the CPU is really doing, and say where the understanding in a computer actually comes from.

## 7. Watch, if you want (optional)

Crash Course Computer Science, Episode 17 ("Integrated Circuits and Moore's Law"), which explains how all of this ended up small enough to fit on one board. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

**What the Unit 2 checkpoint covers next week.** Truth tables for AND, OR, and NOT plus one two-gate combination; one question on what a transistor is; labeling components on a motherboard diagram; the difference between RAM and storage, and between an SSD and a hard drive; putting the boot sequence and the key-press signal path in order; and three short Python items covering a list index, a string slice, and a nested-loop count. Everything on it comes from Weeks 6 through 10. It takes about fifteen minutes and it is diagnostic, not something to be nervous about.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

This is the weakest week of the unit for AP purposes, and there is no point pretending otherwise. Motherboards, buses, firmware, boot sequences, and the Raspberry Pi are not in the AP CSP framework anywhere. The nested loops are, under topic 3.8 Iteration, and nested iteration turns up often enough in trace questions to be worth real practice.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming. Continue in the programming unit and work the iteration lessons, including nested loops. If you have already finished that unit over the last several weeks, skip it and do the practice below instead; do not start a new unit early, because the next ones line up with our Unit 3. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. Third week in a row pointing you here, on purpose, because it is the unit that matches what we are doing in Python right now. If you have finished it, you can look ahead at Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`, but that unit really belongs with our Unit 3 starting in Week 11.

**Extra practice if you want it.**

- Rewrite your left-aligned triangle in AP pseudocode using `REPEAT n TIMES` inside `REPEAT n TIMES`. The loop tables are in `ap-track/AP-Pseudocode-Bridge.md`.
- Work trace problems 3 and 9 in the bridge sheet, then do this: take problem 3 and wrap it in a second outer loop that runs three times. Predict the final value before you trace it.
- The exam's robot-on-a-grid questions are often solved with a nested loop that sweeps a grid row by row. Using the robot commands in the bridge sheet, write pseudocode that moves a robot across every square of a 4 by 4 grid, ending anywhere. Draw the path first.
