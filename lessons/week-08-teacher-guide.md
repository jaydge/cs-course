# Week 8 Teacher Guide

## 1. Header

- **Week:** 8 of 32
- **Unit:** 2, Inside the Computer
- **Theme question:** Why is one computer faster than another?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Explain what clock speed measures and give one reason a higher number does not automatically mean a faster computer.
- Describe pipelining and multiple cores as two different ways of doing more work per second.
- Order the memory hierarchy from fastest to slowest (registers, cache, RAM, SSD, hard drive) and say what gets bigger as it gets slower.
- State the difference between RAM and storage in terms of what survives a power cut.
- Physically identify the CPU, heatsink, RAM, storage drive, power supply, GPU, and motherboard in a real desktop PC.
- Follow the three teardown safety rules: unplug and discharge, wear the antistatic strap, and respect sharp edges.
- Index and slice a Python string, get its length, and loop over its characters.
- Use `.upper()`, `.lower()`, `.split()`, and `in` on strings, and explain why strings cannot be changed in place.

## 3. Where this sits

Weeks 6 and 7 built the machine conceptually, from a transistor up to a working CPU. This week asks the question a student actually cares about: why is one of these faster than another, and what are all these parts inside the case? The teardown is the physical anchor of Unit 2 and the one lab that makes the whole unit concrete, because until now every component has been a box on a whiteboard. Week 9 puts the parts back in context on the motherboard and adds firmware, and Week 10 walks a single key press through the whole assembly.

On the coding side, strings as sequences is the natural sequel to lists, since the two share indexing, slicing, `len()`, and `in`. It is also an AP-tested topic in its own right, and the text-processing patterns from today reappear in the Unit 3 builds and again in the Unit 5 data lab.

## 4. Materials and setup

- The old desktop PC for disassembly, with its case screws already loosened if they are stiff, plus a Phillips screwdriver per pair and a small parts tray or muffin tin for screws.
- The dead or spare motherboard, for the pairs not currently inside the PC.
- Antistatic wrist strap, with a metal point in the room to clip it to.
- A spare SSD and a spare mechanical hard drive if you have both. A hard drive with its lid removed, so the platters and head arm are visible, is the single best prop of the day.
- USB-to-SATA adapter if you plan to show a bare drive mounting on a laptop.
- Optional: a discrete graphics card, even a very old one, for comparison against integrated graphics.
- Whiteboard with the theme question and space for the memory-hierarchy pyramid.
- Student laptops with Thonny; projector for live coding.
- Printed Week 8 homework handout, one per student.

## 5. Pre-class prep checklist

- Open the PC yourself first and take it apart once, then reassemble loosely. You need to know which screws are stubborn, whether the CPU cooler is clipped or screwed, and whether anything inside is sharp or broken. Photograph each stage on your phone as you go; those photos are your reassembly reference and your backup if the teardown stalls. (30 min)
- Unplug the PC and leave it unplugged overnight if you can. On the day, with it unplugged, hold the front power button down for about ten seconds to drain the residual charge in the power supply, and do this again in front of the class so they see it. (5 min)
- Decide and mark what is off limits. The power supply is never opened; it holds capacitors that can retain charge, and there is nothing to learn inside it that is worth the risk. Put a piece of tape on it labeled "do not open." (5 min)
- Prepare the drive props: the opened hard drive, the SSD, and a labeled card for each. (5 min)
- Look up the actual specifications of the classroom machines (clock speed, core count, RAM, storage type) so the numbers in Segment 2 are about machines students are holding. On a Mac this is the Apple menu, About This Mac, then System Report; on Windows it is Settings, System, About, and Task Manager's Performance tab. (10 min)
- Write and test the string examples and the text-processing build. (15 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up (0:00 to 0:10)

- **You do:** Homework check on the largest-number loop; take one student's version and put it on the projector.
- **You do:** Pose the theme question by making it concrete. Put two real specification lists on the board, one older machine and one newer, and ask which is faster and how they would know. Collect guesses without correcting any of them; you will come back to this list at the end of Segment 2.

### Segment 2: What "fast" actually means (0:10 to 0:35), Systems strand

1. **Clock speed first, since it is the number everyone knows.** Remind them of last week's drummer. Clock speed is how many times per second the drummer hits: 3 GHz is three billion ticks a second. Then puncture it. Ask whether a person who takes more steps per second necessarily walks farther, and let them work out that step size matters too. A chip that does more per tick beats a chip that ticks faster, which is why comparing gigahertz across different chip designs tells you very little.
2. **Pipelining.** Use the laundry picture on the board. One load takes wash, dry, fold. Doing them strictly one load at a time wastes the dryer while you fold. Start washing the next load while the first is drying and you finish far more loads per hour without any machine running faster. CPUs do exactly this with fetch, decode, and execute, working on several instructions at once at different stages.
3. **Cores.** Now four separate washing machines. Ask the class what that gets you and, more usefully, when it does not help. It does not help if the four loads have to be done in order, which is why some programs get no benefit from more cores at all. That is a real limit, not a detail.
4. **The memory hierarchy, drawn as a pyramid.** From the top: registers (a handful of numbers, instant), cache in L1, L2 and L3 layers (kilobytes to megabytes, very fast), RAM (gigabytes, fast), SSD (hundreds of gigabytes, slow by comparison), mechanical hard drive (slowest of all). Write the rule beside it: as you go down, it gets bigger, cheaper per gigabyte, and slower. Every one of those trades is deliberate.
5. **Make the speed gap visceral.** Scale it up. If getting a value from a register takes one second, then cache takes a few seconds, RAM takes about a minute, an SSD takes a couple of days, and a mechanical hard drive takes weeks. These are rough teaching ratios rather than measured figures, and it is worth saying so, but the shape is right and the shape is the lesson: the CPU spends much of its life waiting.
6. **Why cache exists.** Given that gap, the machine keeps a small copy of whatever it just used close by, betting that it will need it again soon. That bet is right often enough to make modern computers usable. Name it: caching, and tell them the same idea shows up again in Unit 4 with web browsers and DNS.
7. **Return to the board.** Go back to the two specification lists from the warm-up and re-answer the question properly, naming which numbers actually matter and which are marketing.

### Segment 3: PC teardown lab (0:35 to 1:05), Systems strand

Safety briefing first, then work in pairs, rotating through the machine while others study the dead motherboard.

1. **Safety, out loud, before a screwdriver is touched.** Read these and write them on the board. The machine is unplugged from the wall and stays unplugged; confirm the cable is on the table, not in the outlet. Hold the power button down for ten seconds with the cable out to drain residual charge, and do this in front of them. Everyone handling parts wears the antistatic wrist strap clipped to bare metal on the case, because a static shock you cannot even feel can kill a chip. Handle circuit boards by their edges, never by the pins or the gold contacts. Case edges and the metal drive cage are genuinely sharp, so no reaching blindly into the case. The power supply, the sealed metal box with the fan, is never opened by anyone, including you.
2. **Remove the side panel.** Usually two thumbscrews at the back, then slide the panel back and lift it off. Set the screws in the tray.
3. **Look before touching.** Give the group two full minutes just to look inside and name anything they recognize. Do not narrate over this; the disorientation is productive and the naming that follows is more memorable when they asked for it.
4. **Find the CPU by finding its cooler.** The largest heatsink, usually with a fan on top, near the center of the board. Ask why the biggest cooling apparatus in the case sits on the smallest part in the case, and use their answer to make the point that computation produces heat because switching billions of transistors takes energy.
5. **Remove the cooler and expose the CPU, if it comes off easily.** Clips or four spring screws. If it fights you, leave it and use the dead motherboard's empty socket instead; a stuck cooler is not worth the class time. If you do get it off, pass the CPU around. Hold it by the edges. Have them look at the pin grid or contact pads and count roughly how many connections a single chip needs.
6. **Remove a RAM stick.** Push both retaining clips at the ends of the slot outward and the stick lifts. Pass it around. Say the number out loud: this holds eight or sixteen gigabytes and forgets every bit of it the instant power stops.
7. **Remove the storage drive.** Usually screwed into a cage or on a tool-less rail. Unplug the SATA data cable and the power cable first, noting that the connectors are L-shaped so they only fit one way, which is a small piece of good engineering worth pointing at.
8. **Trace the power.** Follow the thick bundle of cables from the power supply to the motherboard's large connector and to the drive. Explain, without opening anything, that the supply converts wall AC into the 12, 5, and 3.3 volt DC rails everything else uses, and connect that back to the battery pack from Week 6.
9. **Find the expansion slots.** Point out the long PCIe slot where a graphics card goes, and the graphics card itself if this machine has one. Note that a graphics card is essentially a second computer with its own processor and its own memory, bolted onto the first.
10. **Lay every removed part out on the table in a row and name them one at a time as a group.** This is the moment the lab lands. Do not skip it to save two minutes.
11. **Reassembly, or not.** You do not have to reassemble in class. Bag the screws by stage, keep the parts on the table for Week 9, and reassemble during prep if you want a working machine back.

**Purpose:** Every abstraction of the last two weeks becomes a physical object they held. This is the lab students describe to their parents.

### Segment 4: Stretch (1:05 to 1:10)

### Segment 5: Storage and the GPU, with parts in hand (1:10 to 1:25), Systems strand

1. **RAM versus storage, settled once.** Hold up the RAM stick and the drive together. RAM is volatile: pull the power and it is empty. Storage is not: pull the power and it is exactly as you left it. Then give the reason both exist, which is the memory hierarchy from Segment 2. If RAM kept its contents and cost the same as a drive per gigabyte, we would not have drives.
2. **Open the hard drive.** Pass around the opened mechanical drive. Spinning metal platters, a head arm that swings across them like a record player's tone arm, and a physical delay every single time the data you want is not under the head right now. Say the number: a few thousand revolutions per minute, versus a CPU running at billions of cycles per second.
3. **Compare with the SSD.** No moving parts, just flash memory chips and a controller. Ask what that means for speed, for noise, for a laptop that gets dropped, and for battery life. Let them list the advantages before you do.
4. **Say what is not free about an SSD.** Flash cells wear out after a large but finite number of writes, and cost per gigabyte is still higher than for a mechanical drive. This is a genuine tradeoff, not a strictly better product, which is why big archival storage is still spinning metal.
5. **The GPU.** Hold up the graphics card if you have one. Contrast the two designs: a CPU has a few very capable cores that can do anything, and a GPU has thousands of simple cores that all do the same operation to different data at once. Screens are millions of pixels needing the same math, so that shape fits. Then note where else that shape fits, which is machine learning, and flag that Week 27 comes back to this.

### Segment 6: Strings as sequences (1:25 to 1:55), Coding strand

- **You do:** Open with the connection, because it is the point of the segment. A string is a list of characters that happens to be written with quotes around it. Everything they learned about list indexing works.

  ```python
  word = "computer"
  print(word[0])
  print(word[-1])
  print(len(word))
  print("put" in word)
  ```
- **You do:** Introduce slicing, and slow down here.

  ```python
  print(word[0:4])
  print(word[4:])
  print(word[:4])
  ```
  Write out the rule on the board: the start index is included, the end index is not. Then have the class predict `word[0:4]` before you run it. This trips people for weeks, and the way to reduce that is to make them predict before every run today.
- **You do:** Iterate over characters.

  ```python
  for letter in word:
      print(letter)
  ```
- **You do:** Show the useful methods, tying back to last week's dot syntax.

  ```python
  name = "  Ada Lovelace  "
  print(name.upper())
  print(name.strip())
  print(name.split())
  ```
  Point out that `split()` hands back a list, which connects the two data types directly.
- **You do:** Demonstrate immutability by breaking it. Run `word[0] = "C"` and read the `TypeError` together. Then show the fix, building a new string rather than editing the old one: `word = "C" + word[1:]`. Say the rule plainly: strings cannot be changed, only replaced.
- **Students do, build one:** A text-analyzer. Ask the user for a sentence, then print the number of characters, the number of words (using `split()` and `len()`), and the number of vowels (loop over the characters and count). Three separate skills in one small program.
- **Students do, build two if they finish:** Ask for a word and print it backwards, either by looping from the end or by discovering `word[::-1]`. Both are legitimate; the loop version teaches more.
- **You do:** Circulate. The predictable errors are off-by-one on slice ends, counting spaces as vowels because of a sloppy condition, and forgetting `.lower()` before checking vowels so capital letters are missed.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out homework, noting the Extra Credit AP Track section and that strings are a directly AP-tested topic. Exit question: your program crashed and the computer lost power mid-run. Which of the two parts we passed around still has your data, RAM or the drive?

## 7. Key scripts and analogies

- **Clock speed:** "Steps per second. Useful, but a person taking tiny steps quickly is not beating someone taking long strides. Do not buy a computer on one number."
- **Pipelining:** "Laundry. You do not sit and watch the dryer before you start the next wash. Overlap the stages and you get more loads out per hour without any machine getting faster."
- **Cores:** "Four washing machines instead of one. Great for four independent loads. Useless if load two cannot start until load one is folded."
- **Memory hierarchy:** "Your hands, your desk, the shelf, the basement, the storage unit across town. Each one holds more and takes longer to reach, and no sane person keeps everything in one of them."
- **Cache:** "The computer's guess about what you are going to ask for next. It is right often enough that being wrong occasionally does not matter."
- **RAM versus storage:** "RAM is the whiteboard, storage is the notebook. Power goes out and the whiteboard is wiped clean. The notebook is exactly where you left it."
- **Hard drive versus SSD:** "One is a record player. The other has no moving parts at all. Now imagine dropping each of them."
- **GPU:** "A CPU is a few brilliant generalists. A GPU is ten thousand people who can each only do one kind of arithmetic, all at once. For painting two million pixels, you want the crowd."
- **Strings as sequences:** "A string is a list of letters in a trench coat. Every index and slice you learned last week still works."
- **Immutability:** "You cannot edit a string, only build a new one and point the name at it. It is a printed page, not a whiteboard."

## 8. Differentiation

- **Younger or newer students:** In the teardown, give them a named checklist with the seven components to find and let identifying the parts be the whole assignment, rather than doing the removal. In the coding segment, indexing, `len()`, and looping over characters are the core; slicing can be limited to `word[0:3]` style with the numbers given to them. Give the text analyzer as a skeleton with the vowel loop stubbed out.
- **Extensions for advanced or AP-track students:** Look up the classroom laptops' actual cache sizes and core counts and present a two-minute comparison next week. In Python, write the vowel counter as a function that returns the count, then extend the analyzer to report the most common letter using a list of counts. Point them at the Extra Credit AP Track section, which is squarely on topic this week.

## 9. Common pitfalls

- **The teardown runs over.** It will if you let it. The hard stop is 1:05. If the CPU cooler resists, abandon it immediately and use the dead motherboard.
- **Skipping the discharge and the strap because "it is a dead machine anyway."** Do not model this. Students who take this class will open a machine that matters someday, and the habit is the transferable part.
- **Everyone crowding one case.** Two pairs at the machine, the rest at the dead motherboard with a component checklist, and rotate at the halfway point. Plan the rotation before class rather than improvising it.
- **Lost screws.** A parts tray per stage. Losing case screws costs you a working machine.
- **Treating clock speed as the answer.** Students arrive believing gigahertz is the definition of fast. If you do not actively puncture it, they leave believing it.
- **Slice off-by-one.** `word[0:4]` gives four characters, not five. Make them predict before running, every time, for the whole segment.
- **Trying to assign into a string.** `word[0] = "C"` raises `TypeError`. Show it deliberately; it is the same teaching move as Week 2's `input` crash.
- **Vowel counting that catches capitals wrong.** A missing `.lower()` produces a plausible but wrong count, which is a good example of a bug with no error message. Connect it to Week 5's print-debugging.

## 10. Homework

Full details in `handouts/week-08-homework.md`. In summary: a short written explanation of why a computer needs both RAM and storage; order the memory hierarchy and label each level; identify five components from a photo or from a family computer's specification page; a string-slicing exercise on paper; finish the text analyzer and add a palindrome checker; optional Crash Course episodes on advanced CPU design and on memory and storage. The handout closes with an Extra Credit AP Track section.

## 11. Assessment

Observational during the lab, where the diagnostic is whether a student can name a component they are holding without looking at the checklist, and can say what it does in one sentence. In the coding strand, the diagnostic is whether a student can predict the output of a slice before running it. Homework is a completion check against the weekly-labs rubric. Component identification and the RAM-versus-storage distinction both appear on the Unit 2 checkpoint in Week 10, and the teardown vocabulary feeds the mid-year "trace the button press" milestone in Week 21.

## 12. AP alignment

This session covers AP CSP topic 3.4 Strings in the coding strand, and that is the whole of the direct AP content. The systems strand maps poorly, and it is worth telling students so rather than pretending otherwise: clock speed, cache, pipelining, storage technology, and GPUs are not on the AP CSP exam. Big Idea 4, Computer Systems and Networks, is about the internet and parallel computing rather than what is inside a case, and our course covers that in Unit 4 and Week 29.

**AP-track self-study for this week, and only this week's slice.** One matching unit below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming. Stay in the programming unit and work the strings lessons. As with last week, the correct instruction is to keep working the programming unit because this week's systems content is not AP-tested. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** there is no dedicated strings unit in the csp-2025 edition, so this is a poor fit rather than a clean one. The nearest useful material is the string handling inside Unit 4, Variables, Conditionals, and Functions, at `https://studio.code.org/courses/csp-2025/units/4`, and the traversal lessons in Unit 6, at `https://studio.code.org/courses/csp-2025/units/6`, since traversing a string works the same way as traversing a list. If a student has already finished both, the better use of this week is the AP practice below rather than hunting for a matching unit.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Teardown procedure: Segment 3 is complete on its own. If you want photographs of a specific machine's internals, iFixit's device guides are the best free reference, at `https://www.ifixit.com`, and their ESD safety page is worth reading once during prep. Do this in prep, not in class.
- Lab equipment list, including the antistatic strap, the USB-to-SATA adapter, and the dead motherboard: Section 7 of `curriculum/CS-Curriculum-and-Setup.md`. Costs there are approximate and should be verified at purchase time.
- Classroom machine specifications: on macOS, the Apple menu, About This Mac, then System Report; on Windows, Settings, System, About, plus Task Manager's Performance tab. Collect these during prep so Segment 2 uses real numbers from machines students actually use.
- Crash Course Computer Science, Episode 9 ("Advanced CPU Designs") and Episode 19 ("Memory and Storage"), assigned as optional homework viewing. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- Python string methods, for your own reference: `https://docs.python.org/3/library/stdtypes.html#string-methods`
- CodeAI CSP Units 4 and 6 (AP-track reinforcement, imperfect fit this week): `https://studio.code.org/courses/csp-2025/units/4` and `https://studio.code.org/courses/csp-2025/units/6`
- AP CSP topic 3.4 Strings and where the course covers it: `ap-track/AP-CSP-Topic-Coverage.md`
