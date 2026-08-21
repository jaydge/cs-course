# Week 2 Teacher Guide

## 1. Header

- **Week:** 2 of 32
- **Unit:** 1, Thinking Like a Computer Scientist
- **Theme question:** Why only 1s and 0s?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Count in binary using the dot cards and convert a small number (0 to 31) between decimal and binary by hand using place values.
- Explain that everything in a computer (numbers, letters, images, sound) is stored as bits, and that a code like ASCII maps letters to numbers.
- Say what compression is for and give the difference between lossless (ZIP) and lossy (JPEG, MP3) in one sentence each.
- Write a Python program that uses a variable, gets input from the user, and prints a response. This is the Week 1 coding ramp, landing here.
- Distinguish an integer from a string in Python and convert between them with `int()` and `str()`.

## 3. Where this sits

Week 1 front-loaded the computer-fluency intro, so this session carries a double load on purpose: it absorbs the Python ramp that slid out of Week 1 (variables, input, the greeting program) and opens the course's first real systems topic, binary and data representation. The unplugged binary work comes first, before any screen time, per the physical-first pattern. Everything in Unit 1 builds on the two skills started here: reading binary and writing small interactive programs. The compression topic is AP-tested material and returns in Week 25's data lab.

## 4. Materials and setup

- Binary dot cards, one set of five per pair of students, showing 1, 2, 4, 8, and 16 dots. Printable versions are linked in Section 13, but hand-drawn index cards work just as well. Make one oversized set for the front of the room.
- Printed pixel grids (about 8 by 8 squares) and markers, one per student.
- A printed ASCII table, one per pair.
- Each student's laptop charged and logged in, Thonny working (verified in Week 1).
- Projector for Thonny demos; whiteboard with the theme question written large.
- Printed Week 2 homework handout, one per student.
- The readiness diagnostics collected in Week 1, reviewed beforehand so you know who needs pairing (see Section 8).

## 5. Pre-class prep checklist

- Review the Week 1 diagnostics and decide pairings for the unplugged activity and the coding segment. (10 min)
- Print and cut the binary card sets; print pixel grids, ASCII tables, and homework handouts. (15 min)
- Run through the binary card sequence in Segment 2 once, out loud, with the cards in your hands. The activity lives or dies on the patter, and the steps below go faster than they read. (10 min)
- On the demo machine, write and test the greeting program and the type-conversion examples you will live-code. (10 min)
- Check which students completed the account-setup homework from Week 1; note stragglers to follow up with parents. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Have every student open Finder and find the file they saved for homework. Quick fist-to-five: who found it without help?
- **You do:** Pose the theme question: last week you told a computer to print. This week, what does the computer actually store when you do that? Why only 1s and 0s?
- **Purpose:** Confirms the Week 1 file-system core stuck, and frames the day.

### Segment 2: Binary Cards, unplugged (0:10 to 0:40), Systems strand

Run this entirely from the steps below; the canonical source and its video are in Section 13 for prep.

1. **Set up.** Bring five volunteers to the front, each holding one oversized card. Arrange them in a line facing the class, **largest card on the left**: 16, 8, 4, 2, 1. Say why out loud, that this is the same left-to-right, biggest-first order as the hundreds, tens, and ones columns they already use.
2. **State the convention explicitly.** A card held face up, dots showing, counts. A card turned face down counts as zero. There is no third option. Write on the board: face up = 1, face down = 0.
3. **Find the doubling rule.** Ask: how many dots on this card compared to the one on its right? Walk down the line until the class says it themselves, that each card is double the one to its right. Ask what the next card to the left would be (32), and the one after that (64).
4. **Model reading one number aloud yourself, before asking anyone else to.** Set the volunteers to 1, 0, 1, 0, 1 and think out loud: "16 is up, so 16. 8 is down, skip it. 4 is up, so 16 plus 4 is 20. 2 is down. 1 is up, so 21." Then write `10101` on the board next to 21. Do not skip this step; students copy the method they just watched.
5. **Class reads.** Flip the volunteers to two or three new arrangements and have the room call out the value. Then reverse it: name a decimal number (13, 25, 6) and let the class direct the volunteers on which cards to flip.
6. **Count up together.** Starting from all cards down, have the volunteers count 0, 1, 2, 3, up to about 8, one number at a time. Students will spot the pattern that the 1-card alternates every step, the 2-card every two steps, and so on.
7. **Seatwork in pairs.** Students mirror with their own card sets: make 9, 17, and 25; find the largest number five cards can make (31); and answer why every odd number has the 1-card face up.
8. **Extend to bytes and letters.** Ask what eight cards could hold (0 to 255, one byte). Hand out the ASCII table and have each pair write their initials as decimal numbers, then as binary. Land the idea: letters are numbers in costume.

**Purpose:** The physical version of binary arrives before any notation or arithmetic, and the place-value idea is discovered rather than told.

### Segment 3: The Python ramp lands (0:40 to 1:10), Coding strand part 1

- **You do:** At the projector, build up the greeting program live, one line at a time: `name = input("What is your name? ")` then `print("Hello, " + name)`. Name the two new ideas: a variable is a labeled box; `input` pauses and waits for the user.
- **Students do:** Type and run it themselves, then extend it: ask a second question (favorite food, pet's name) and print a sentence using both variables. Save it into the CS Class folder.
- **You do:** Circulate. The predictable errors are missing quotes, missing parentheses, and case. Let students hit them and read the error message out loud before you fix anything.
- **Purpose:** This is the Week 1 coding content, deferred by design. Every student leaves having written an interactive program with variables, which Unit 1 assumes from here on.

### Segment 4: Stretch and transition (1:10 to 1:15)

- A short break. Collect the binary cards.

### Segment 5: Encoding and compression (1:15 to 1:35), Systems strand

Full steps below; the related canonical activity is in Section 13.

1. **Hand out the pixel grids.** Explain the format: you will read a row at a time as pairs of numbers, alternating white and black, always starting with white. So "3, 2, 3" on an eight-square row means three white, two black, three white.
2. **Read out a small picture.** Use five or six rows that form a simple shape (a letter, a heart, a smiley). Students color as you read. Let the picture appear before you explain anything.
3. **Land the first idea.** Images are just numbers. A photo is a grid of colored squares, and each color is a number.
4. **Invent compression.** Point at a mostly-blank row. Ask how they would send that row to a friend using as few numbers as possible. They will say something like "six white, two black" on their own. Tell them the name: run-length encoding, and that they just invented a real compression method used in actual image formats.
5. **Push on the limits.** Ask when this trick saves a lot (big blocks of one color) and when it makes things worse (every square a different color). That tradeoff is the whole subject in one question.
6. **Lossless vs lossy, at the projector.** ZIP is lossless: unzip it and every original bit comes back exactly, which is what their row-counting does. JPEG and MP3 are lossy: they permanently throw away detail people are unlikely to notice, and it never comes back. If time allows, show the same photo saved at high quality and at the lowest JPEG quality side by side.

**Purpose:** Compression carries real weight on the AP exam's Data section and is the most commonly skipped topic. Twenty physical minutes is enough for the concept.

### Segment 6: Numbers vs text in Python (1:35 to 1:55), Coding strand part 2

- **You do:** Live-code the classic trap: `age = input("Age? ")` then `print(age + 1)`. It crashes. Read the error together: `input` always hands you a string. Fix it with `int(age)`.
- **Students do:** Write a tiny program: ask for a number, print that number doubled and that number plus 10. That is the core outcome for this segment; every student should reach it.
- **Extension, for anyone who finishes with time left:** a five-bit binary converter that uses the card method in code, five repetitive blocks of "is it at least 16? then subtract" logic scaffolded on the board with `//` and `%`. Provide the skeleton; students fill in the numbers. No loops yet; the repetition is the point, because when loops arrive in Week 4 this program is the one they will shorten. See Section 8 for who this is aimed at and how far to take it.
- **Purpose:** Integers, strings, arithmetic, and conversion, anchored to the morning's cards. The converter, for students who reach it, connects the two strands of the day into one artifact.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out and walk through the homework, including the Extra Credit AP Track section at the end so AP-track students know it is there. Exit question at the door: what number is binary 101? (Answer: 5.)

## 7. Key scripts and analogies

- **Why binary:** "A wire is either carrying electricity or it is not. That is one of two states, and it is the only thing the hardware can tell for sure. Everything the computer does is built out of that one reliable trick, done billions of times."
- **Place value:** "You already use place value in base ten: the columns are 1, 10, 100. Binary is the same idea with doubling columns: 1, 2, 4, 8, 16. Nothing new, just a different ladder."
- **ASCII:** "Letters are numbers wearing costumes. Capital A is 65. The computer never stores an A; it stores 65, in binary, and the screen draws the costume."
- **A variable:** "A labeled box. The label is the name you chose; the box holds the value. When you use the name, Python opens the box."
- **input:** "The program stops and holds its breath until the user types something and presses return. Whatever they typed lands in your box."
- **Strings vs integers:** "To Python, the text '7' and the number 7 are as different as a photo of a sandwich and a sandwich. `int()` turns the photo into the real thing so you can do arithmetic on it."
- **Lossless vs lossy:** "Lossless is folding a shirt: it comes back exactly. Lossy is juicing an orange: smaller, still recognizably orange, but you are never getting the orange back."

## 8. Differentiation

- **Younger or newer students:** Use the place-value alternate from the curriculum's Section 11: give them a printed conversion table (16, 8, 4, 2, 1 with checkboxes) and focus on reading binary and checking answers with the cards rather than multi-step mental arithmetic. The doubling program in Segment 6 is their full outcome; the converter extension is not expected of them.
- **Extensions for advanced or AP-track students, in order:** first, the five-bit binary converter from Segment 6, which is the main extension for this week and the one to offer first. Students who finish that with time left can spell their whole name in ASCII binary, extend the converter to eight bits, or try `bin(n)` in the Thonny shell and compare with their own output. Point them at the Extra Credit AP Track section of this week's handout, which is squarely on topic for this session.

## 9. Common pitfalls

- **The double load runs long.** If you must cut, cut Segment 5 short (compression can compress) and protect Segment 3, the Python ramp. Do not let students leave a second week without having written a variables-and-input program. The Segment 6 converter is already an extension rather than a core deliverable, so a tight session simply means fewer students reach it; that is expected, not a failure to cut.
- **Binary arithmetic anxiety.** Keep the cards on the table all session. A student who can set cards to make 13 understands binary; speed at mental conversion is not the objective and is explicitly scaffolded away for younger students.
- **Cards drift out of order.** If a pair lays their cards smallest-first, their binary will read backwards and nothing will match the board. Check the left-to-right order as you circulate.
- **`input` plus arithmetic crashes.** This is planned (Segment 6). Do not pre-empt it; the crash is the lesson.
- **Students typing quotes wrong.** Smart quotes from notes apps break Python. Have students type code fresh in Thonny, never paste from a document.
- **Account-setup stragglers.** Follow up with parents outside class time. Do not burn class minutes on account problems; nothing this week requires the accounts yet.

## 10. Homework

Full details in `handouts/week-02-homework.md`. In summary: convert six numbers between decimal and binary using the card method; extend the greeting program with one more question and a number-doubling line, then save it; optional Crash Course episodes on binary and ASCII; optional 15 minutes of typing practice; finish account setup with a parent if not done. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice.

## 11. Assessment

Low-stakes and observational. The exit question (binary 101) and a walk of the room during Segment 6 tell you who has each of the two core outcomes: reading binary and writing a variables-and-input program. Homework is a completion check against the weekly-labs rubric. Note which students used the place-value scaffold; that informs Week 14's Big-O alternate decision later.

## 12. AP alignment

This session directly covers AP CSP topics 2.1 Binary Numbers and 2.2 Data Compression, and begins 3.1 Variables and Assignments and 3.3 Mathematical Expressions. Data representation is 17 to 22 percent of the AP multiple-choice exam and leans on exactly today's material.

**AP-track self-study for this week, and only this week's slice.** Students do the one matching unit below, not the whole course, and it is extra credit rather than required work:

- **Project STEM:** Unit 3, Data Representation. The relevant lessons are the ones on binary encoding, base conversion, and ASCII; the lists material later in that unit belongs with our Week 6, so stop after ASCII.
- **CodeAI (free alternative):** Unit 1, Digital Information, at `https://studio.code.org/courses/csp-2025/units/1`. The binary-number, text-representation, and lossless-versus-lossy compression lessons match today directly.

Nothing here is required of non-AP students. Verify the Project STEM unit numbering against the live course once enrolled; see the provider unit reference in the README.

## 13. Resources used this week

- Binary Cards, canonical instructions, printable dot cards, and a demonstration video: CS Unplugged Binary Numbers, `https://classic.csunplugged.org/activities/binary-numbers/` (updated edition at `https://www.csunplugged.org`). The step-by-step in Segment 2 is complete on its own; review the source during prep if you want the fuller patter and extension questions. Verify links are live before class; sites reorganize.
- Pixel Grid and run-length encoding: Segment 5 is self-contained. The related canonical activity is CS Unplugged Image Representation, `https://classic.csunplugged.org/activities/image-representation/`, and the compression companion is Text Compression, `https://classic.csunplugged.org/activities/text-compression/`.
- Crash Course Computer Science, Episode 4 ("Binary: Representing Numbers and Letters") and Episode 21 ("Compression"), assigned as the optional homework video. These two match the session's two halves. Note that the curriculum outline's older "Ep. 4 to 5" reference is off: Episode 5 is the ALU, which belongs with Week 7, not here. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Unit 1, Digital Information (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/1`
- Younger-student binary alternate: Section 11 of `curriculum/CS-Curriculum-and-Setup.md`.
- Full activity descriptions and the canonical link list: `teaching-activities/Unplugged-Logic-Activities.md`.
