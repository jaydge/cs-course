# Week 6 Teacher Guide

## 1. Header

- **Week:** 6 of 32
- **Unit:** 2, Inside the Computer
- **Theme question:** What is a transistor really?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Describe a transistor in one sentence as a switch that is operated by electricity instead of by a finger.
- Complete the truth tables for AND, OR, and NOT from memory, and read a two-gate combination.
- Build a working AND gate, OR gate, and NOT gate on a breadboard with switches and LEDs, and explain which part is the input and which is the output.
- State the four electrical safety rules that govern the lab: low-voltage battery power only, a series resistor on every LED, never connect the positive rail straight to ground, and disconnect the battery before rewiring or if anything gets warm.
- Create a Python list, read an element by index, change an element, and get the length with `len()`.
- Explain that Python list indexes start at 0, and predict what `IndexError` means.

## 3. Where this sits

Unit 1 taught students to think like a programmer. Unit 2 opens the box and asks what the thing running their programs actually is. This week is the bottom of the stack: electricity, one switch, and the three gates that everything else is built from. Week 2 already established that a wire is either carrying current or it is not; this week they hold the wire. Weeks 7 through 9 build upward from here (gates to memory to a CPU to a whole board), and Week 10 walks the finished machine end to end.

On the coding side, lists are the first data structure of the course and the reason Week 4's loops matter. Week 7 adds list methods and traversal, and Unit 3 assumes both. This is also the moment the Week 4 note comes due: AP-track students were told to stop partway through CodeAI's lists-and-loops unit and come back when lists arrived. They arrive today.

## 4. Materials and setup

- Breadboard and logic kit: one breadboard per pair, jumper wires, LEDs, resistors (220 ohm and 470 ohm and 1k ohm), tactile or slide switches (two per pair), and NPN transistors (2N2222 or BC547, two per pair plus spares).
- Power for each breadboard: a 3xAA battery pack (about 4.5 V) or a USB 5 V breakout. No wall adapters, no mains voltage, nothing above 6 V.
- One basic multimeter for the front-of-room demo.
- 1 and 0 cards for the Human Logic Gates activity, roughly ten of each, plus floor space.
- Whiteboard with the theme question written large, and room to draw three truth tables side by side.
- Each student's laptop with Thonny; projector for live coding.
- Printed Week 6 homework handout, one per student.
- Optional backup: a browser logic simulator open on the demo machine in case a kit part fails (see Section 13).

## 5. Pre-class prep checklist

- Build all three circuits yourself on one breadboard and confirm they work. Do not skip this. Breadboard rail wiring, LED polarity, and transistor pinout are the three things that eat class time, and ten minutes of prep removes all three. (25 min)
- Identify the pinout of the specific transistor you bought. A 2N2222 and a BC547 in the same TO-92 package have their collector and emitter on opposite pins. Check the part marking against its datasheet, then write the pin order on a card and tape it to the front table. (10 min)
- Sort the resistors into labeled cups by value. Loose mixed resistors will cost you the lab. (10 min)
- Pre-cut or pre-bend jumper wires if your kit ships them long, and lay out one complete parts tray per pair. (10 min)
- Run through the Human Logic Gates sequence in Segment 2 once out loud, deciding in advance which students you will put in which role. (5 min)
- Write and test the list examples and the truth-table lookup program you will live-code. (10 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Quick check that Hangman runs and uses at least two functions. Note who is behind; do not fix code now.
- **You do:** Pose the theme question. Remind them of the Week 2 claim, that a wire is either on or off, and say that today they find out what is doing the switching. Write on the board: a transistor is a switch, and a computer is about twenty billion of them.
- **Purpose:** Closes Unit 1 and opens the hardware arc.

### Segment 2: Human Logic Gates, unplugged (0:10 to 0:35), Systems strand

Run this entirely from the steps below. The activity description is in the repo's unplugged activities guide, listed in Section 13.

1. **Set the convention.** Hand out 1 and 0 cards. A student holding a 1 card overhead means the wire is on; a 0 card means off. There is no third state. Say it once and hold everyone to it, because the whole activity depends on it.
2. **Make an AND gate.** Stand three students in a small triangle: two inputs facing a single gate student. Give the gate student one rule and only one rule: "Hold up 1 if both of my inputs are 1. Otherwise hold up 0." Now walk the inputs through all four combinations (0 0, 0 1, 1 0, 1 1) and have the class call out the output. Fill in the truth table on the board as you go.
3. **Make an OR gate.** Swap in a new gate student with the rule "Hold up 1 if either input is 1, or both." Walk the same four combinations. Draw the second truth table beside the first.
4. **Make a NOT gate.** One input, one gate student, rule "Hold up the opposite of what I see." Two rows only. Note out loud that NOT is the only one of the three with a single input.
5. **Reverse it, which is the real learning.** Send a gate student out of earshot and give them a secret rule. Feed inputs, let the class watch outputs, and have them deduce which gate it is. Do this twice. Students discover that the truth table *is* the gate; nothing else about it matters.
6. **Wire two gates together.** Put an AND gate's output into a NOT gate's input, so the second student reads the first student's card as their own input. Walk all four input combinations. The class has just built NAND, and you can say plainly that this one gate can be used to build every other gate, which is what next week's lab does.
7. **Build a half adder if time allows.** Two inputs feed both an AND gate and an XOR gate. Define XOR on the spot as "1 if the inputs are different." Point out that the XOR output is the sum bit and the AND output is the carry bit, and that these five students just added 1 plus 1 and got 10 in binary. Do not belabor it; the full version is next week.

**Purpose:** Boolean logic becomes a physical rule that a person can follow, before it becomes a circuit or a truth table on paper. The deduce-the-gate round is the segment worth protecting if time runs short.

### Segment 3: Electricity and the transistor (0:35 to 0:50), Systems strand

1. **Three words, no more.** On the board: voltage is push, current is flow, resistance is restriction. Use the water-in-a-hose picture and do not go further into electrical theory than that; the goal is enough vocabulary to survive the lab.
2. **Multimeter demo.** Set the meter to DC volts, measure the battery pack, and read the number aloud. Then measure across an LED that is lit in a working circuit and note that some of the voltage is used up there. This takes three minutes and makes "voltage" a thing you can see a number for.
3. **The switch that has no finger.** Draw a simple circuit: battery, switch, resistor, LED. Ask what the switch does. Then ask the actual question of the week: what if the thing pressing the switch were another wire? That is a transistor. Three legs: two for the circuit you want to control, one for the control signal.
4. **Land the consequence.** A switch operated by electricity can be operated by the output of another switch. That is the entire trick. Stack it up and you get gates; stack gates and you get arithmetic and memory; stack those and you get a computer. Say the scale out loud: a modern phone chip holds well over ten billion of these, each one smaller than a virus.
5. **Safety briefing, before anyone touches a kit.** Read these four rules out and write them on the board. Battery power only, never a wall outlet or anything from a mains adapter. Every LED gets a resistor in series, always, because an LED connected straight across the supply draws all the current it can and destroys itself. Never connect the positive rail directly to the ground rail; that is a short, and the battery pack will get hot. Disconnect the battery before rewiring, and if any part becomes warm to the touch, disconnect immediately and raise your hand.

### Segment 4: Breadboard gate lab (0:50 to 1:20), Systems strand

Students work in pairs. Steps below are complete; do not open a tutorial mid-class.

1. **Orient the breadboard.** Point out the two long rails down the sides (one for positive, one for ground) and the short five-hole rows in the middle. Say the rule that matters: holes in the same five-hole row are connected to each other, and the two halves of the board are separated by the center channel. Have each pair connect the battery pack red lead to the positive rail and black lead to the ground rail, then leave the battery unplugged until their circuit is fully built.
2. **LED polarity.** Every LED has a long leg (anode, goes toward positive) and a short leg next to a flat spot on the rim (cathode, goes toward ground). Backwards LEDs are the number one reason a circuit looks dead. Have pairs check each other's before powering on.
3. **Build the AND gate.** From the positive rail, run a wire to one side of switch A. From the other side of switch A, wire to one side of switch B. From the other side of switch B, wire to a 220 ohm resistor, then to the LED long leg, then the LED short leg to the ground rail. Connect the battery. The LED lights only when both switches are closed. Have the pair fill in a truth table on paper by testing all four combinations.
4. **Name what they built.** Two switches in a row means the current has to get through both. That is AND, and it is series wiring.
5. **Build the OR gate.** Disconnect the battery. Rewire so both switches sit side by side: each switch has one side on the positive rail and the other side on a shared row. From that shared row, go through the 220 ohm resistor to the LED, then to ground. Reconnect and test all four combinations. Either switch alone lights it. That is OR, and it is parallel wiring.
6. **Build the NOT gate, which needs the transistor.** Disconnect the battery. Place the NPN transistor across the center channel and identify its three legs using the pinout card you posted. Wire it as follows: emitter to the ground rail; collector to an empty row, call it row X; a 470 ohm resistor from the positive rail to row X; the LED long leg in row X, then the LED short leg through a 220 ohm resistor to the ground rail; and a 1k ohm resistor from the transistor base to one side of a switch, with the other side of that switch going to the positive rail.
7. **Test the NOT gate.** Reconnect the battery. With the switch open (input 0), the LED is lit (output 1). Press or close the switch (input 1) and the LED goes out (output 0). That is inversion, built out of one transistor. Tell them the LED will be visibly dimmer than in the previous two circuits, and give them the real reason, because a student will ask. When the LED is lit the transistor is off, so nothing is being shared with it; instead the current now has to pass through the 470 ohm pull-up as well as the LED's own 220 ohm resistor, roughly 690 ohms in series where the AND and OR circuits had only 220. Less current, dimmer LED. This is expected rather than a fault.
8. **Debug the predictable failures as you circulate.** Nothing lights: check LED direction first, then the battery leads, then whether both rail wires are actually in the rails. Always on regardless of the switch: the switch is wired across the wrong pair of pins, which is common with four-pin tactile switches, so have them rotate the switch ninety degrees and retry. Transistor circuit dead in both states: the pinout is reversed, so swap collector and emitter.
9. **Tear down.** Disconnect batteries first, then return parts to the trays sorted. Budget three minutes for this or you will lose the kit piece by piece across the unit.

**Purpose:** The three gates stop being notation and become objects the student wired with their own hands. Nearly every student remembers this lab at the end of the year.

### Segment 5: Stretch (1:20 to 1:25)

- Break, hands washed, laptops open.

### Segment 6: Lists and indexing (1:25 to 1:55), Coding strand

- **You do:** Motivate it before the syntax. Ask how they would store the scores of twenty students with what they know now. Twenty variables. Let that land, then introduce the list as one box that holds many things in order.

  ```python
  scores = [90, 85, 100, 72]
  print(scores)
  print(scores[0])
  print(len(scores))
  ```
- **You do:** Say the hard part out loud and write it on the board: the first item is at index 0. The last item of a four-item list is at index 3, not 4. Then show that `scores[4]` raises `IndexError: list index out of range`, and read the error together. Do not skip the deliberate crash; it is the same teaching move as Week 2's `input` trap.
- **You do:** Show reading, writing, and negative indexing.

  ```python
  scores[1] = 95
  print(scores[-1])
  ```
- **Students do:** Make a list of five things they own, print the third one, change the first one, and print the length. Then print the last item using a negative index.
- **Students do, the cross-strand build:** Store this morning's AND truth table as a list and look up answers by index.

  ```python
  and_table = [0, 0, 0, 1]
  a = int(input("Input A (0 or 1)? "))
  b = int(input("Input B (0 or 1)? "))
  print("AND output:", and_table[a * 2 + b])
  ```

  Walk through why `a * 2 + b` turns two bits into the row number 0, 1, 2, or 3. Then have students add `or_table` and `not_table` the same way. A student who finishes has written a lookup table, which is exactly how some real hardware implements logic.
- **You do:** Circulate. Watch for off-by-one index errors and for students who try to index a string of digits rather than converting to `int`.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out homework and point at the Extra Credit AP Track section, noting that this week is a real AP week for the coding half. Exit question at the door: in the list `[4, 7, 9]`, what is at index 1? (Answer: 7.)

## 7. Key scripts and analogies

- **What a transistor is:** "A light switch you flip with your finger. Now imagine a light switch you flip with another wire. That is a transistor, and there are billions of them in your phone, each one smaller than a virus."
- **Why gates matter:** "You cannot build a computer out of one switch. You can build one out of switches that control other switches. Everything above this line in the course sits on that single idea."
- **AND as series:** "Two doors in a hallway, one after the other. You get through only if both are open."
- **OR as parallel:** "Two doors side by side into the same room. Either one gets you in."
- **NOT:** "A contrarian. Whatever you tell it, it says the opposite. Boring alone, essential in company."
- **The truth table is the gate:** "You never need to know what is inside. If it produces those outputs for those inputs, it is that gate. That is abstraction, and it is the same move as calling a function without reading its body."
- **Why a resistor with an LED:** "An LED has no self-control. Given the chance it will pull every bit of current the battery can give and burn out in about a second. The resistor is the adult in the circuit."
- **Lists:** "A variable is a labeled box. A list is a labeled shelf, with numbered slots. You still use one name, but now you say which slot."
- **Zero-indexing:** "Python counts the way a floor counter counts in Europe: the first one is the ground floor, zero. Annoying for two weeks, then invisible forever."

## 8. Differentiation

- **Younger or newer students:** In the lab, give them the AND and OR circuits only, and let them observe a partner build the transistor NOT gate. Both series and parallel are complete concepts on their own. In the coding segment, stop at reading and writing single elements; the truth-table lookup with `a * 2 + b` is optional, and pairing works well for it. If arithmetic on indexes is the blocker, let them type the four rows as a printed table and just read the answer.
- **Extensions for advanced or AP-track students:** Build NAND by feeding the AND output into the transistor's base, then use the multimeter to measure the voltage at the collector in both states and connect the number to the 1 and the 0. In Python, write a function `gate(name, a, b)` that looks up the right table by name, or build a list of lists holding all three tables. Point them at the Extra Credit AP Track section, which is a strong match this week.

## 9. Common pitfalls

- **The lab runs long and eats the coding strand.** This is the single biggest risk of Week 6. Set a hard stop at 1:20 and mean it. If pairs are still building, have them finish AND and OR and skip NOT rather than losing the lists segment, because lists are load-bearing for the next ten weeks and the NOT gate is not.
- **Backwards LEDs.** Expect this from at least half the pairs on the first circuit. Check polarity before anyone connects a battery.
- **Four-pin tactile switches.** These connect two pairs of pins internally, so wiring across the wrong pair gives a switch that is permanently closed. If a circuit is always on, rotate the switch ninety degrees first before debugging anything else.
- **Transistor pinout confusion.** 2N2222 and BC547 are not interchangeable leg for leg. Post the pinout for your exact part; do not rely on memory.
- **Shorting the rails.** A stray wire between positive and ground makes the battery pack warm. Teach students to disconnect power before rewiring and to feel for heat.
- **Off-by-one on list indexes.** Constant this week. When a student says the list is broken, ask them to count the slots out loud starting at zero.
- **Mixing up `scores[1]` and `scores = 1`.** Reading an element and reassigning the whole list look similar to a beginner. Say the difference out loud each time you use it.

## 10. Homework

Full details in `handouts/week-06-homework.md`. In summary: complete three truth tables and one two-gate combination on paper; write a short program that builds a list, indexes it, and changes an element; extend the truth-table lookup program to all three gates; one written question on what a transistor is; optional Crash Course episodes on electronic computing and boolean logic. The handout closes with an Extra Credit AP Track section.

## 11. Assessment

Observational plus the homework. In the lab, the thing to watch is whether a pair can point at their own circuit and say which part is the input and which is the output; a pair that built it by copying wire positions without that understanding needs a follow-up question. In the coding segment, the diagnostic is whether a student can predict what `scores[0]` returns before running it. Homework is a completion check against the weekly-labs rubric. The truth tables from the homework feed directly into the Unit 2 checkpoint in Week 10.

## 12. AP alignment

This session covers AP CSP topic 3.5 Boolean Expressions through the gates and truth tables, and opens 3.10 Lists in the coding strand. Note the honest limits: transistors, breadboards, and circuit construction are not AP CSP content at all. The exam does not test hardware internals. What transfers is the boolean reasoning and the lists, so that is where the AP slice points.

**AP-track self-study for this week, and only this week's slice.** One matching unit below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming, and within it one topic only: creating a list, reading and writing an element by index, and list length. Stop when the lessons turn to traversing a list, which is next week's slice. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. In Week 4 students were told to stop when that unit turned from loops to lists. This is the week to resume. Do the lists lessons and stop before traversals, which are next week.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human Logic Gates: Segment 2 is complete on its own. The activity description and the classroom variants are in `teaching-activities/Unplugged-Logic-Activities.md` under Boolean logic.
- Breadboard basics, for your own reference if you have not used one recently: SparkFun's "How to Use a Breadboard", `https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard`, and its LED tutorial covering polarity and series resistors, `https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds`. Review during prep only; Segment 4 does not require them.
- Transistor pinout: check the datasheet for your exact part number. Do not assume 2N2222 and BC547 match.
- Backup if the hardware fails: a free browser circuit simulator such as CircuitVerse, `https://circuitverse.org`, or the Falstad circuit simulator, `https://www.falstad.com/circuit/`, both of which can show AND, OR, and NOT built from switches. Have one open on the demo machine. Verify these are live before class; sites move.
- Crash Course Computer Science, Episode 2 ("Electronic Computing") and Episode 3 ("Boolean Logic and Logic Gates"), assigned as optional homework viewing. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`. Episode numbering and titles are worth a quick check before you assign them.
- Lab equipment sources and approximate costs: Section 7 of `curriculum/CS-Curriculum-and-Setup.md`. Prices there are approximate and should be verified at purchase time.
- CodeAI CSP Unit 6, Lists, Loops, and Traversals (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/6`
- AP pseudocode list notation, including the 1-indexing difference: `ap-track/AP-Pseudocode-Bridge.md`
