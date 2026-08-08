# Week 16 Teacher Guide

## 1. Header

- **Week:** 16 of 32
- **Unit:** 3, Programming Like a Professional
- **Theme question:** How do you build a world out of data?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Design a small program by deciding what data structure holds the world before writing any code.
- Build a text adventure that uses a dictionary of rooms, at least two functions, and one class.
- Write a simulation that uses random values, runs many trials, and counts the outcomes.
- Explain what a simulation leaves out and why leaving things out is the point.
- Explain in plain language why a computer appears to get slower over time.
- Demonstrate Unit 3 mastery on the checkpoint.

## 3. Where this sits

This closes Unit 3 and the Tier 1 programming core. Weeks 11 through 15 added dictionaries, classes, data structures, algorithmic cost, and testing. Today those are not taught; they are used. The text adventure is deliberately built so that each of the five weeks shows up in it: rooms are a dictionary of dictionaries, the player is a class, movement is a function, the inventory is a list used as a container, and the whole thing gets at least one test.

The simulation exercise is short but carries a real AP topic, 3.16, and it is the first time students use randomness for something other than a game. It also previews Week 25's data work, since counting outcomes and summarizing them is the same motion as extracting information from a dataset.

Unit 4 opens next week with operating systems and the terminal, and the systems narrative resumes after six weeks of near-continuous coding. The Mystery Day question today is chosen to sit on that seam: it is a systems question that students can now answer partly in algorithmic terms.

## 4. Materials and setup

- Printed Unit 3 checkpoint, one per student. See Section 11 for what it covers.
- Each student's laptop with Thonny; projector for live coding.
- Whiteboard with the theme question written large, and a clear area for the room map drawing, which stays up through the build.
- Printed Week 16 homework handout, one per student.
- Two AP pseudocode trace problems written on the board before students arrive.
- Optional: a machine with visibly many login items and browser tabs, for the Mystery Day demonstration.

## 5. Pre-class prep checklist

- **Write and print the Unit 3 checkpoint.** Keep it to about 15 minutes of work and cover the six areas listed in Section 11. Write the answer key at the same time. (30 min)
- Write and test the text adventure in the scaffolded form students will work from, including the rooms dictionary and the `Player` class, and decide how much you hand out versus how much they write. (25 min)
- Write and test both simulation variants, dice and random walk, and note the shape of the output so you can predict what students will see. (15 min)
- Prepare the Mystery Day demonstration: open Activity Monitor on the demo Mac, and if you have an older machine with a long list of login items, have it ready. On the Windows fleet the equivalent is Task Manager's Startup tab. (10 min)
- Choose two pseudocode trace problems for the warm-up and write them on the board. (5 min)
- Print homework handouts and checkpoints. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **Students do:** The two pseudocode trace problems on the board, on paper, four minutes.
- **You do:** Resolve them at the board quickly. Second and last time this year for the warm-up as a whole-class routine; from Unit 4 it becomes AP-track homework only.
- **You do:** Quick check on the Tic-Tac-Toe tests. Ask for a show of hands: whose test function actually ran and printed its pass line? Follow up individually with anyone whose did not, during the build.
- **You do:** Pose the theme question and set the day's shape out loud: build for forty minutes, run a simulation, one mystery, then the checkpoint.

### Segment 2: Designing the world before coding it (0:10 to 0:20), Coding strand part 1

1. **Draw a four-room map on the board:** hall, library, kitchen, cellar, with arrows for the exits. Keep it small; four rooms is enough and six is too many for the time available.
2. **Ask the design question first, before syntax.** What holds this map? Take answers. Steer to the right one and write it up:

   ```python
   rooms = {
       "hall": {"description": "A dusty hall.", "north": "library", "east": "kitchen"},
       "library": {"description": "Shelves to the ceiling.", "south": "hall"},
       "kitchen": {"description": "It smells of burnt toast.", "west": "hall", "down": "cellar"},
       "cellar": {"description": "Dark, and colder than it should be.", "up": "kitchen"},
   }
   ```
3. **Point at the shape and name it.** A dictionary of dictionaries, keyed by room name, exactly the pattern from Week 11. Note that the exits are keys too, so checking whether a direction is legal is just `if direction in rooms[here]`.
4. **Ask what the player is,** and why a class fits better than a dictionary here. The answer they should reach: the player has state that changes and rules for changing it, so the behavior should travel with the data.
5. **List the functions on the board** before anyone types: describe the current room, list the available exits, and read a command. Three functions, one class, one dictionary.
6. **Set the definition of done** explicitly so nobody drifts: at least three rooms, movement in at least two directions, one item that can be picked up, and a quit command that works. Anything beyond that is bonus.

### Segment 3: Build the text adventure (0:20 to 1:00), Coding strand part 2

- **You do:** Give them the `Player` class as a starting point and read it aloud once:

  ```python
  class Player:
      def __init__(self, start):
          self.location = start
          self.bag = []

      def move(self, direction):
          exits = rooms[self.location]
          if direction in exits:
              self.location = exits[direction]
              return True
          return False

      def take(self, item):
          self.bag.append(item)
          return "You picked up the " + item + "."
  ```

  Point out that `move` returns True or False rather than printing. That is the Week 5 distinction, still earning its keep: the game loop decides what to say, and the class decides what is legal.
- **You do:** Give the loop skeleton or write it with them, depending on the group:

  ```python
  player = Player("hall")

  while True:
      here = rooms[player.location]
      print(here["description"])
      command = input("> ").strip().lower()
      if command == "quit":
          break
      elif player.move(command):
          print("You go", command)
      else:
          print("You cannot go that way.")
  ```
- **Students do:** Build it, then extend it in their own direction: more rooms, an item in a room that can be taken, a locked door that needs an item in the bag, or a description that changes after a first visit.
- **You do:** Circulate hard for the full forty minutes. This is the largest program most of them have written. Prioritize in this order: programs that do not run, then programs with no class, then programs with no functions, then extensions.
- **Say this out loud somewhere around the twenty-minute mark:** every single piece of this was taught in the last five weeks, and none of it is new today. That realization is the actual point of a build week.

### Segment 4: Stretch (1:00 to 1:05)

### Segment 5: Simulation (1:05 to 1:25), Coding strand part 3

1. **Ask the question first.** Roll two dice and add them. Which total comes up most often, and how much more often? Take predictions and write three of them on the board. Many students say all totals are equally likely.
2. **Say why we would simulate rather than calculate.** You could work it out with probability. You could also roll dice ten thousand times, which nobody wants to do by hand. A simulation is the third option: build a small model of the thing and let the computer do the tedious part.
3. **Build it at the projector:**

   ```python
   import random

   counts = {}
   for trial in range(1000):
       total = random.randint(1, 6) + random.randint(1, 6)
       counts[total] = counts.get(total, 0) + 1

   for total in range(2, 13):
       print(total, "*" * (counts.get(total, 0) // 10))
   ```
4. **Read the output as a shape.** The asterisks form a triangle peaking at 7. Ask why 7 and not 2. Get them to count the ways: there are six ways to make 7 and one way to make 2.
5. **Students do:** Run it at 100 trials, then 1000, then 100000. The shape gets cleaner as the trials increase. Name that plainly: more trials means less noise, and a simulation run once tells you almost nothing.
6. **Students do, second variant:** A random walk, which is the same idea with a different question:

   ```python
   import random

   position = 0
   for step in range(100):
       position = position + random.choice([-1, 1])
   print("Ended at", position)
   ```

   Have them wrap that in an outer loop of 1000 walks and count how many end further than 20 steps from the start.
7. **Land the AP framing in three sentences.** A simulation is a program that models something real. It always simplifies, leaving out details that do not matter for the question being asked, and that simplification is a feature rather than a flaw. We use one when the real experiment would be too slow, too expensive, too dangerous, or simply impossible, and the price we pay is that the answer is only as good as the model.
8. **Ask for the limits.** What does the dice model leave out? Everything: the table, the throw, tiny weight differences in the dice. Ask when that would matter. If you were testing whether a specific casino's dice were loaded, this model would be worthless.

### Segment 6: Mystery Day, why does a computer get slower over time? (1:25 to 1:40), Systems strand

1. **Take the theories first.** Ask the class why an old laptop feels slow. Write every answer on the board without judging. Expect "the parts wear out," "it fills up with junk," and "they do it on purpose."
2. **Kill the wrong one first.** Transistors do not get tired. A CPU from 2015 executes instructions today at exactly the speed it did in 2015. The hardware is not slower; something else changed.
3. **Walk the four real causes.**
   - **The workload grew.** Every OS update, every app update, and every web page is bigger than its predecessor. The machine is doing more work for the same apparent task. Open a text-heavy news site and show the network panel or just the tab's memory in Activity Monitor.
   - **Things accumulate in the background.** Show the login items list and the process list. Every app that ever asked to start at login is still starting at login. Each one costs memory and a slice of CPU forever.
   - **Memory runs out and the machine starts swapping.** When RAM is full, the OS parks pages on the SSD, which is thousands of times slower than RAM. This is the single biggest cause of a machine that feels stuck rather than merely slow. Connect it straight back to Unit 2's memory hierarchy.
   - **Storage pressure and thermal throttling.** A nearly full SSD has fewer free blocks and slows down. Dust and dried thermal paste make the CPU hot, and a hot CPU deliberately slows itself down to survive.
4. **Add the honest fifth cause.** Expectations. A three-second launch felt fast in 2018 and feels slow now, and the machine did not change.
5. **Connect it to this unit in one line.** Ask what Big-O has to say. If a program is O(n squared) in the number of files, photos, or messages you have, it was fast when you had 200 photos and is slow at 20,000. The algorithm did not change; n did.
6. **End with the practical answer.** What actually helps: fewer login items, fewer background apps, more free disk space, more RAM if the machine allows it, and a clean reinstall as the nuclear option. What does not help: the "speed booster" apps advertised at them, most of which are the problem wearing a costume.

### Segment 7: Unit 3 checkpoint (1:40 to 1:55)

- **Students do:** Complete the checkpoint individually, no laptops, about 15 minutes.
- **You do:** Collect it. Hand out homework as students finish, noting the Extra Credit AP Track section.

### Segment 8: Wrap (1:55 to 2:00)

- **You do:** Close the unit deliberately. Point at the board and name what they can now do that they could not six weeks ago: model real data, define their own kinds of things, choose a data structure on purpose, say what an algorithm costs, and prove their code works. Tell them Unit 4 leaves the editor and goes underneath it, into the operating system and the terminal.

## 7. Key scripts and analogies

- **Data first:** "Before you write a line, decide what holds the world. Get that right and the code writes itself. Get it wrong and no amount of clever code saves you."
- **Rooms as a dictionary:** "The map is not drawn anywhere. It exists only as which room names appear as values in which other rooms' exits. That is the whole map, and it is fifteen lines."
- **Why the player is a class:** "The rooms just sit there. The player has state that changes and rules about how it may change. When the rules and the data live in the same place, the rules do not get lost."
- **What a simulation is:** "A model of a piece of the world, simple enough to run and detailed enough to answer one question. Leaving things out is not cheating; it is the entire technique."
- **On trial counts:** "One run of a simulation is an anecdote. Ten thousand runs is a result."
- **Old computers:** "Your laptop is exactly as fast as the day you bought it. The world it runs got heavier."
- **Swapping:** "When RAM fills up, the operating system starts using the disk as pretend memory. Disk is thousands of times slower than RAM. That is not a slow computer, that is a computer standing in a queue it did not tell you about."

## 8. Differentiation

- **Younger or newer students:** Give the complete rooms dictionary, the complete `Player` class, and the complete game loop, and have them extend it: add two rooms, add an item, change the descriptions. That is a full outcome, and it exercises reading code, which is a legitimate skill in its own right. For the simulation, running the supplied dice program at three trial counts and describing the shape is enough; skip the random walk. On the checkpoint, use the qualitative wording of the growth-rate question for students who used the Section 11 Big-O alternate.
- **Extensions for advanced or AP-track students:** Add an inventory-gated door that only opens if a specific item is in the bag. Add a test function for `Player.move` that asserts a legal move changes the location and an illegal one does not. For the simulation, have them compute and print the percentage of trials for each dice total and compare it to the exact probability, then explain the remaining gap. The strongest can simulate a two-dimensional random walk and report the average distance from the origin.

## 9. Common pitfalls

- **Rooms and exits getting out of sync.** A typo in a destination name gives a `KeyError` on the next move, or worse, an exit that leads to a room that does not exist. Suggest they write the map on paper first and check both directions of every doorway.
- **`rooms` used as a global inside the class.** It works and is fine for today, but say out loud that it is a shortcut and that a larger program would pass the map in. Do not refactor it in class.
- **Input case and whitespace.** A student types "North" and the game says they cannot go that way. `.strip().lower()` is in the skeleton for this reason; make sure they kept it.
- **The infinite loop with no quit.** Someone will remove the `break` and be unable to stop their game. Show Control-C in the Thonny shell once, for everyone.
- **Simulation with too few trials.** A student runs 10 trials, sees a flat-ish distribution, and concludes the theory is wrong. That is a teachable moment, not a mistake; make them run it again with 10,000.
- **Confusing `random.randint` with `random.randrange`.** `randint(1, 6)` includes 6; `randrange(1, 6)` does not. This matters for the dice and is also an AP detail, since AP's `RANDOM(a, b)` includes both ends.
- **Time pressure on the checkpoint.** Start it at 1:40 even if the build is going well. The build can continue at home; the checkpoint cannot.

## 10. Homework

Full details in `handouts/week-16-homework.md`. In summary: finish the text adventure to the stated definition of done; run the dice simulation at three trial counts and write up what changes; a short written reflection choosing data structures for three described problems; optional Mystery Day follow-up on their own machine. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice and the first orientation pointer toward the Create Task.

## 11. Assessment

**Unit 3 checkpoint**, administered in Segment 7 and covering six areas:

1. **Dictionaries.** Given a small dictionary, write the expression that reads one value, and write the line that adds a new key. One question on what happens when you read a key that is not there.
2. **Classes.** Given a short class definition, trace what two objects made from it hold after a method is called on one of them. This is the independence-of-objects idea from Week 12.
3. **Data structures.** Two scenarios; name stack or queue and justify in one sentence. One question on why inserting into the middle of a linked list is cheaper than inserting into the middle of an array.
4. **Indexing.** One item giving a five-element list, asking for a specific element's index in Python and then in AP pseudocode. This is the deliberate 1-versus-0 check.
5. **Efficiency and searching.** One question on which search to use and what it requires, and one growth-rate ranking question. Use the qualitative wording for students on the Section 11 alternate. One short item asking what an undecidable problem is, in a sentence.
6. **Debugging.** One find-the-bug item on a short program that runs but gives the wrong answer, plus one traceback to read for error type and actual cause.

Score it against the unit-checkpoint component of the grade. It is diagnostic as much as evaluative. A weak indexing result means that student needs the pseudocode bridge drills continued as homework; a weak debugging result should inform pairing for the Unit 4 terminal labs, where errors are less forgiving than Thonny's.

The unit build is the text adventure. Assess it against the weekly-labs rubric with one addition: the student should be able to explain, out loud, why they chose a dictionary for the rooms and a class for the player. As in Week 5, that explanation is the AI-policy enforcement mechanism as much as it is the assessment.

## 12. AP alignment

This session directly covers AP CSP topic 3.16 Simulations and consolidates 3.2 Data Abstraction, 3.9 Developing Algorithms, 3.13 Developing Procedures, and 3.15 Random Values through the build. The checkpoint covers the Unit 3 topics as a whole, including 3.11 and 3.17 from Week 14.

On simulations specifically, the exam expects three things and they are all worth stating in class: a simulation is a model that intentionally simplifies reality, it is used when the real experiment is too costly, too slow, too dangerous, or impossible, and its results depend on the assumptions built into the model. The exam also expects students to know that simulations using randomness produce different results on different runs, which is exactly what students saw at 100 trials versus 100,000.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 2, Programming, and specifically its simulation and random-values lessons. Work only the simulation material. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`, has the loop-and-count machinery a simulation is built from, and Unit 5, Data, at `https://studio.code.org/courses/csp-2025/units/5`, covers reading results out of collected data. Either is a reasonable fit; the simulation topic is spread across the CodeAI course rather than concentrated in one unit, so pick by topic rather than expecting a clean match.

**One forward-looking pointer, orientation only.** AP-track students may skim CodeAI Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`, purely to see what the Create Performance Task asks for. This is not the time to start it. Create Task work begins in February, in Unit 6 of our course, and the submission deadline is in late April; verify the current year's deadline on AP Central rather than trusting any date printed here. The only useful thing to take from a skim today is what the finished artifact looks like, so that the project ideas forming in their heads over the next few months are the right shape.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Text adventure and simulation builds: both are complete in Segments 3 and 5. No external source needs reviewing.
- Python `random` module, for your reference: `https://docs.python.org/3/library/random.html`. Note that `randint(a, b)` includes both endpoints and `randrange(a, b)` excludes the upper one; the first matches the AP exam's `RANDOM(a, b)`.
- Mystery Day demonstration tools: Activity Monitor on macOS (Applications, Utilities), and System Settings, General, Login Items. On Windows, Task Manager's Processes and Startup tabs. Nothing needs installing.
- AP pseudocode trace problems used as the warm-up: `ap-track/AP-Pseudocode-Bridge.md`.
- CodeAI CSP Units 5, 6, and 9 (AP-track reinforcement and Create Task orientation): `https://studio.code.org/courses/csp-2025/units/5`, `https://studio.code.org/courses/csp-2025/units/6`, and `https://studio.code.org/courses/csp-2025/units/9`
- AP Create Performance Task requirements and the current year's deadline, for your planning: AP Central, `https://apcentral.collegeboard.org/courses/ap-computer-science-principles`. Deadlines and requirements change annually; verify before relying on anything here.
- Unit 3 outline, the checkpoint's place in the grade, and the younger-student Big-O alternate: Sections 3, 5, and 11 of `curriculum/CS-Curriculum-and-Setup.md`.
