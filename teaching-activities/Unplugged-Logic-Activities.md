# Unplugged Logic Activities

Offline, physical activities that teach computer-science logic with no computers. They fit this class especially well: they need zero computer fluency, so they are ideal in the early weeks while iPad-only students are still learning the laptop, and they level up or down naturally across the 8th-to-11th-grade range. The pattern throughout is physical first, then code.

Free printable materials and known-good instructions for many of these are online, listed below. The descriptions in this document are written so you can run each one without them, but the weekly teacher guides should link to the specific instructions or a video for any activity they use.

### Known-good instructions and videos

Verify these links are live before class; sites reorganize.

- Human Robot Maze (cup-stacking version): Code.org's My Robotic Friends unplugged lesson, which includes a symbol key and a teacher video, at `https://curriculum.code.org/csf-18/coursee/1/` (a newer edition of the same lesson lives under `https://curriculum.code.org/csf-current/`). If those paths move, find the current version via Code.org CS Fundamentals.
- Sorting Network: CS Unplugged, `https://classic.csunplugged.org/activities/sorting-networks/` (a demonstration video is on the site).
- Human Sorting (bubble and selection): CS Unplugged Sorting Algorithms, from the activities index at `https://classic.csunplugged.org/activities/`.
- Binary Cards: CS Unplugged Binary Numbers, from the same activities index, with an updated version at `https://www.csunplugged.org`.
- Parity Magic (error detection): CS Unplugged, `https://classic.csunplugged.org/activities/error-detection/` and `https://www.csunplugged.org/en/topics/error-detection-and-correction/`.
- Packet Routing: CS Unplugged Routing and Deadlock, and Network Protocols, from the activities index.
- Caesar Cipher and the paint-mixing key exchange: CS Unplugged Cryptographic Protocols and Public Key Encryption, from the activities index. For a short video on key exchange, search Computerphile's Diffie-Hellman explainer.

The CS Unplugged activity hub is `https://classic.csunplugged.org/activities/`, the current site is `https://www.csunplugged.org`, and Code.org's unplugged lessons live under `https://curriculum.code.org`.

## How to schedule them

Run one aligned activity at the launch of each major concept, roughly one every two to three weeks, for 20 to 45 minutes, before the on-screen version. They also make excellent first-day activities and warm-ups. A suggested mapping to the course:

This table reflects the weeks as actually written in `lessons/`. If you move an activity, update both places.

| Week | Activity | Reinforces |
|---|---|---|
| 1 | Robot Chef (optional energizer) | Precision, decomposition |
| 2 | Binary Cards, Pixel Grid | Binary, data representation, compression |
| 3 | Robot Chef (if not run in Week 1), Human Robot Maze (sequence stage) | Algorithms, sequencing, precision |
| 6 | Human Logic Gates | Boolean logic |
| 11 | Human Robot Maze (conditionals stage) | Selection |
| 12 | Human Robot Maze (loops stage) | Iteration |
| 13 | Human Stack, Queue, and Linked List | Data structures |
| 14 | Human Sorting, Sorting Network, Guess My Number | Sorting, searching, Big-O intuition |
| 15 | Human Robot Maze (functions stage, run as a bug hunt) | Procedures, debugging |
| 19 | Packet Routing | Networking, fault tolerance |
| 28 | Caesar Cipher, Paint-Mixing Key Exchange, Parity Magic | Cryptography, error detection |

Barrier Drawing is not scheduled into a specific week; keep it as a spare warm-up for any session that needs one, and as an alternate for Robot Chef.

---

## The flagship: the Human Robot Maze

Tape a grid on the floor (masking tape, about 6 by 6 squares). Mark a start square, a goal square, and a few obstacle squares (walls). One student is the "robot." The others are the "programmers." The programmers write a sequence of commands to move the robot from start to goal without hitting a wall or leaving the grid.

Use exactly three commands to start:
- MOVE FORWARD (one square, in the direction the robot faces)
- TURN LEFT (90 degrees, in place)
- TURN RIGHT (90 degrees, in place)

**The one rule that makes this teach programming:** the robot does exactly and only what is written, literally, with no common sense. If the program says forward into a wall, the robot walks into the wall. If it forgets a turn, the robot goes the wrong way. Bugs become physically visible, and students learn the central truth that a computer has no idea what you meant, only what you said.

**The second rule that matters: compile, then run.** Programmers must write the entire program first, then hand it over and execute it start to finish without changing it mid-run. No live steering. This is the difference between programming and using a remote control, and it is the single most important idea in the whole activity. When the program fails, they fix the written program and run it again from the top. That is debugging.

Have the robot face away or wear a blindfold in a later round so the programmers cannot rely on the robot quietly correcting course. It forces them to fully specify every step.

### The progression (this scaffolds the real Python curriculum)

Reuse the same maze across the year, adding one construct at a time so the physical version arrives just before the coding version.

1. **Sequence (Weeks 1 to 3).** Just the three commands in a list. Teaches that a program is an ordered sequence and that order matters.
2. **Conditionals (Unit 3).** Add a sensor command, CAN MOVE FORWARD, that is true or false. Now programs can say: IF CAN MOVE FORWARD, move; OTHERWISE, turn right. The robot can handle a maze the programmers cannot fully see in advance.
3. **Loops (Unit 3).** Add REPEAT n TIMES and REPEAT UNTIL AT GOAL. A long path collapses into a short program, and students feel exactly why loops exist.
4. **Functions (Unit 3).** Let students define a reusable named sub-sequence, for example a procedure called TURN AROUND that is TURN RIGHT, TURN RIGHT. Teaches abstraction and why we name and reuse blocks of steps.

### The AP tie-in

The AP CSP exam has robot-on-a-grid questions using exactly this idea, with the commands MOVE_FORWARD, ROTATE_LEFT, ROTATE_RIGHT, and CAN_MOVE. Running this maze all year is direct, hands-on practice for that question type. Use those exact command names in the later rounds so the exam vocabulary is already familiar (see the AP Pseudocode Bridge sheet).

---

## More activities, by concept

### Algorithms and precision

**Robot Chef (Exact Instructions).** Students write step-by-step instructions to make a peanut butter sandwich. You follow them literally and comically wrong: told to "put peanut butter on the bread," you set the jar on top of the loaf. Students revise until the instructions are unambiguous. The funniest and fastest way to teach precision and decomposition. Materials: bread, peanut butter, a plate. (This is also question 1 on the readiness diagnostic.)

**Barrier Drawing.** Two students sit back to back. One has a simple shape or arrangement of colored blocks and describes it; the other must reproduce it without seeing it. Teaches specification, communication, and ambiguity. Materials: paper, colored blocks or shapes, a divider.

### Binary and data representation

**Binary Cards.** Five cards showing 1, 2, 4, 8, and 16 dots. Flipping cards face up or down represents numbers in binary. Students count in binary, and discover place value and that everything reduces to on and off. Extend to bytes, then to encoding letters as numbers (ASCII). Materials: printed dot cards.

**Pixel Grid.** Give students a grid and a string of numbers or bits; they color squares to reveal a picture, showing that images are just pixels and numbers. Then have them compress a mostly-blank row by writing "5 white, 2 black" instead of coloring every square. That is run-length encoding, the unplugged version of the compression topic in Week 2. Materials: grid paper, markers.

### Boolean logic

**Human Logic Gates.** Assign students to be AND, OR, and NOT gates. Inputs are students holding up 1 or 0 cards; each gate student outputs a 1 or 0 by its rule. Wire several together into a small circuit, such as a half-adder, and feed inputs through. Makes boolean logic physical and previews the logic-gate breadboard lab. A lighter version: show input and output pairs and have students deduce which gate it is. Materials: 1 and 0 cards, floor space.

### Sorting and searching

**Human Sorting.** Line students up holding number cards and run a sorting algorithm out loud, one compare-and-swap at a time. Do bubble sort one day and selection sort another, and count the comparisons each takes. This is the step-by-step sorting experience, and counting the steps builds Big-O intuition without any logarithms. Materials: number cards.

**Sorting Network.** Tape a network of paths on the floor with comparison nodes. Students holding numbers walk through; at each node the two who meet compare and the smaller takes the left exit. Everyone comes out sorted, and several move at once, which quietly introduces parallelism. Memorable and a little magical. Materials: masking tape, number cards.

**Guess My Number.** You think of a number from 1 to 100; the class guesses, and you say higher or lower. They quickly discover that halving the range each time wins fastest. That is binary search, and the handful of guesses it takes for 100 numbers is O(log n) made concrete. No materials needed.

### Data structures

**Human Stack, Queue, and Linked List.** For a stack, use a tray dispenser or a pile of paper plates: last on, first off. For a queue, use a line of students: first in, first out, and act out enqueue and dequeue. For a linked list, each student holds a value card and points to the next student; insert or delete by re-pointing, which shows why linked lists are cheap to rearrange. Ties directly to the Week 13 lesson. Materials: plates or trays, value cards.

### Networking

**Packet Routing.** Students stand as network nodes holding hands or connected by string. Messages written on index cards must travel from a source student to a destination student, hop by hop, with each node deciding where to pass it next. Then have a node sit down mid-delivery, forcing a reroute. Teaches routing, redundancy, and why the internet keeps working when parts fail. Materials: index cards for packets, string (optional). Pairs with the "what happens when you open google.com" lesson.

### Cryptography and error detection

**Caesar Cipher.** Students build a cipher wheel (two circles pinned at the center) and encrypt and decrypt messages by shifting the alphabet. Then try to crack an intercepted message using letter frequency. Teaches substitution ciphers and why simple ones are breakable. Materials: printed cipher wheels, a brad pin each.

**Paint-Mixing Key Exchange.** The classic demonstration of public-key ideas. Two students each start with a secret color and a shared public color; they mix and swap in a set order and both end up with the same final color that an eavesdropper cannot reproduce without a secret. The most intuitive way to teach the counterintuitive idea of exchanging a secret in the open. Materials: paint or colored paper chips, or just do it with labeled cups.

**Parity Magic.** Lay out a grid of cards showing black or white, then add one extra row and column so every line has an even number of black cards. Turn away while a student flips exactly one card; you find the flipped card instantly because two lines now break the even rule. Feels like a trick, teaches error detection and correction. Materials: two-color cards.

---

## A one-time materials kit

Assemble this once and you can run everything above.

- A roll of masking or painter's tape (grids and networks on the floor)
- Two decks of playing cards, or printed number cards
- Printed dot cards (1, 2, 4, 8, 16) for binary
- Index cards (packets, values, pointers)
- 1 and 0 cards and true or false cards for logic
- Grid and graph paper, markers
- Cipher wheels and brad pins
- Two-color cards or chips for parity
- Bread, peanut butter, plates for Robot Chef
- Colored blocks or chips for barrier drawing and key exchange

Most of this you likely already have, and none of it depends on the laptops being ready.
