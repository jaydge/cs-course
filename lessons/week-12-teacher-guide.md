# Week 12 Teacher Guide

## 1. Header

- **Week:** 12 of 32
- **Unit:** 3, Programming Like a Professional
- **Theme question:** What if the data knew how to behave?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Explain the difference between a class and an object in one sentence: the class is the blueprint, the object is the thing built from it.
- Write a class with `__init__`, set attributes on `self`, and create two independent objects from it.
- Write a method that reads and changes the object's own state, and call it with dot notation.
- Say why a class is worth using instead of a dictionary: the behavior travels with the data.
- Build a working pet or inventory class with at least two attributes and two methods, and drive it from a small program.
- Collapse a repetitive maze program into a loop using the AP exam's command names.

## 3. Where this sits

Last week students learned to keep related values together in a dictionary. This week the values get verbs. A contact record cannot do anything; a pet can be fed. That is the whole move, and it is the last major Python language feature the course introduces, because Weeks 13 through 16 spend their time using these tools rather than adding new ones.

Classes matter here for a practical reason more than a theoretical one: Week 13 builds a linked list out of node objects, Week 15 tests methods, and Week 16's text adventure has a `Player` class at its center. Students who leave today without a working `__init__` will struggle in all three, so protect the build time.

The Human Robot Maze returns at its loops stage. Last week students wrote the same conditional block twelve times and complained about it, which is exactly the setup for today's opener.

## 4. Materials and setup

- The taped floor maze from Week 11, still down if possible. If it came up, retape a 6 by 6 grid with a start, a goal, and three or four walls.
- Index cards for maze programs.
- Each student's laptop with Thonny; projector for live coding.
- Whiteboard with the theme question written large. Leave room for a blueprint drawing that stays up all session.
- Printed Week 12 homework handout, one per student.
- Optional: blank paper "character sheets" with fields for name, species, hunger, and mood, one per student, for the blueprint analogy.

## 5. Pre-class prep checklist

- Confirm the maze is still taped and reachable, and decide the one wall you will move mid-activity. (5 min)
- Write and test the pet class in the exact form you will live-code, including the deliberate two-object demonstration in Segment 3. Run it once and read the output as a student would. (20 min)
- Prepare the "same class, two objects" trap: a version where a student writes `hunger = 5` at class level instead of on `self`, so you can show the shared-state failure if it comes up. (10 min)
- Decide which build variant each group gets, pet or inventory, and write the skeleton for both. (15 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Ask two students to read out the nested dictionary they modeled for homework. For each, ask the class: what could this thing *do*? A pet gets fed. A song gets played. A bike gets ridden. Write the verbs next to the nouns on the board.
- **You do:** Pose the theme question. Say plainly that so far data has been inert; today it gets behavior attached to it.
- **Purpose:** Objects arrive as an answer to a question the students just asked, not as vocabulary.

### Segment 2: Human Robot Maze, loops stage (0:10 to 0:25), Systems strand

Run this from the steps below. Canonical source is in Section 13 for prep.

1. **Restate the two rules in one breath.** The robot does exactly what is written with no common sense, and the program is written in full before it runs, with no live steering.
2. **Put last week's program back up.** Write one copy of the block on the board and remind them they wrote it twelve times:

   ```
   IF (CAN_MOVE (forward))
   {
     MOVE_FORWARD ()
   }
   ELSE
   {
     ROTATE_RIGHT ()
   }
   ```
3. **Introduce the two loop forms.** Write both:

   ```
   REPEAT 12 TIMES { block }
   REPEAT UNTIL (AT_GOAL) { block }
   ```

   Ask which is safer if you do not know how far away the goal is. Let them argue for thirty seconds; the answer is the second, and they will get there.
4. **Round 1.** Each team writes a program that is a single `REPEAT UNTIL` wrapped around a single conditional block. That is about ten written lines, replacing the ninety-odd they copied out last week. Say the ratio out loud; the shrink is the whole point of the segment. Run two teams' programs.
5. **Move a wall and re-run the same card, unedited.** It still works. Say the payoff out loud: the program got shorter and more general at the same time, which almost never happens by accident.
6. **Round 2, the failure case.** Give one team a maze where turning right forever traps the robot in a corner, or simply ask what happens if the goal is unreachable. Run it and let the robot spin. Name it: an infinite loop. Tell them to remember that spinning robot, because in two weeks they will meet a famous question about whether you can ever detect it in advance.
7. **Debrief in one line.** A loop plus a conditional is a program that handles a whole family of mazes rather than one maze.

**Purpose:** Iteration is re-derived physically, the exam vocabulary keeps circulating, and the infinite loop gets planted for Week 14's halting problem.

### Segment 3: From a dictionary to a class (0:25 to 0:50), Coding strand part 1

- **You do:** Start with what they already know, at the projector:

  ```python
  pet = {"name": "Biscuit", "species": "dog", "hunger": 5}

  def feed(p, amount):
      p["hunger"] = p["hunger"] - amount

  feed(pet, 2)
  print(pet["hunger"])
  ```
- **You do:** Ask what is awkward about this. Steer to the real answer: the function and the data are separate, so nothing stops you calling `feed` on a song or a bike. The data does not know what can be done to it.
- **You do:** Now write the class version beside it, line by line, running as you go:

  ```python
  class Pet:
      def __init__(self, name, species):
          self.name = name
          self.species = species
          self.hunger = 5

      def feed(self, amount):
          self.hunger = self.hunger - amount
          if self.hunger < 0:
              self.hunger = 0

  biscuit = Pet("Biscuit", "dog")
  biscuit.feed(2)
  print(biscuit.name, biscuit.hunger)
  ```
- **You do:** Name every part deliberately and slowly. `class` with a capitalized name declares a blueprint. `__init__` runs automatically when you build one, and its job is to fill in the blanks. `self` is the particular object this call is about. Attributes are the nouns, methods are the verbs, and the dot is how you reach either.
- **You do:** Make the blueprint concrete. Draw a rectangle on the board labeled `Pet` with empty fields, then draw two filled-in copies beside it. Then prove it in code:

  ```python
  crumb = Pet("Crumb", "cat")
  biscuit.feed(3)
  print(biscuit.hunger, crumb.hunger)
  ```

  It prints `0 5`. Feeding one pet does not feed the other. Students need to see this; many assume otherwise.
- **Students do:** Type the `Pet` class exactly, make two pets, feed one, and print both hungers.

### Segment 4: Stretch (0:50 to 0:55)

- A short break. Leave the blueprint drawing up on the board; the rest of the session refers back to it.

### Segment 5: Methods that carry state (0:55 to 1:20), Coding strand part 2

- **You do:** Add two more methods at the projector and discuss why each is a method rather than a loose function:

  ```python
      def play(self):
          self.hunger = self.hunger + 1
          return self.name + " had fun."

      def describe(self):
          return self.name + " the " + self.species + " (hunger " + str(self.hunger) + ")"
  ```
- **You do:** Reuse the Week 5 distinction directly: `describe` returns a string and prints nothing; that is deliberate, because returning is more useful than printing. Show `print(biscuit.describe())`.
- **You do:** Show the two errors they are about to hit, on purpose. First, define a method without `self` in the parameter list and call it, then read the `TypeError` out loud. Second, write `hunger = hunger - 1` inside a method instead of `self.hunger`, run it, and read the resulting error. Say the rule: inside a method, anything belonging to the object needs `self.` in front of it, every single time.
- **Students do:** Add two methods of their own to `Pet`, one that changes an attribute and one that returns a description. Then write three lines that use both.

### Segment 6: Build a pet or an inventory (1:20 to 1:50), Coding strand part 3

- **You do:** Give the choice. Either an RPG-style `Pet` or `Character` with health, or an `Item` class plus a small inventory. Decompose the inventory version on the board so both groups see the same shape:

  ```python
  class Item:
      def __init__(self, name, value, quantity):
          self.name = name
          self.value = value
          self.quantity = quantity

      def total_value(self):
          return self.value * self.quantity

  inventory = [Item("rope", 5, 2), Item("lamp", 12, 1)]
  for item in inventory:
      print(item.name, item.total_value())
  ```
- **You do:** Point at the list of objects and say what just happened: everything they learned about lists in Weeks 6 and 7 works unchanged on objects. Nothing new is needed to hold many of them.
- **Students do:** Build their chosen version with at least two attributes and two methods, create at least three objects, put them in a list, and loop over the list calling a method on each.
- **You do:** Circulate hard. The two failure modes are missing `self` and code accidentally written inside the class body instead of below it. Both produce confusing errors; go to them first.

### Segment 7: Wrap and homework (1:50 to 2:00)

- **You do:** Hand out and walk through the homework, including the Extra Credit AP Track section. Exit question at the door: `biscuit` and `crumb` were both made from `Pet`. Feeding `biscuit` does what to `crumb`, and why?

## 7. Key scripts and analogies

- **Class versus object:** "The class is the cookie cutter. The object is the cookie. You can make a hundred cookies from one cutter, and eating one does not eat the others."
- **`__init__`:** "The form you fill in when the object is born. Name, species, and a starting hunger of five. Python calls it for you the moment you write `Pet(...)`."
- **`self`:** "`self` means *this one*. When a hundred pets share one `feed` method, `self` is how the method knows which pet is in front of it."
- **Why not just a dictionary:** "A dictionary is a filing card. A class is a filing card that comes with its own set of instructions stapled to it. When the data and the rules for changing it travel together, the rules do not get lost."
- **Attributes and methods:** "Nouns and verbs. `pet.name` is a noun. `pet.feed(2)` is a verb. The dot is the possessive apostrophe: this pet's name, this pet's feeding."
- **On the loop payoff:** "Your maze program got shorter and it got smarter. Shorter usually costs you something. Here it did not, because the repetition was never the point."

## 8. Differentiation

- **Younger or newer students:** One attribute and one method is a complete outcome. Give them the `Pet` class typed out and have them only add a second method. Skip the list-of-objects step; three separately named objects are fine. Do not spend time on why `self` exists; spend it on the mechanical rule that `self.` goes in front of the object's own things.
- **Extensions for advanced or AP-track students:** Build a `Robot` class whose methods are `move_forward`, `rotate_left`, `rotate_right`, and `can_move`, holding an x, a y, and a facing direction, and run today's maze program against it in Python. That is the AP exam's robot question turned into an object, and it is genuinely good practice. Others can add a second class that interacts with the first, for example a `Shelter` that holds a list of pets and feeds all of them.

## 9. Common pitfalls

- **Forgetting `self` in the parameter list.** The resulting `TypeError` about positional arguments is unreadable to a beginner. Teach the message so they can recognize it: if the count is off by exactly one, `self` is missing.
- **Forgetting `self.` inside the method body.** This one is worse because it sometimes runs. A method that assigns to a bare `hunger` creates a local variable that vanishes on return, and the object never changes. Watch for "my method does nothing."
- **Indentation of methods.** Methods sit one level in from `class`. Code at the wrong level either becomes a loose function or ends up inside the previous method.
- **Assuming objects share state.** Some students expect changing one pet to change all of them. The two-object demo in Segment 3 is there specifically to kill this belief; do not skip it.
- **Calling a method without parentheses.** `print(biscuit.describe)` prints a method object rather than the string. It looks like gibberish, and students think they broke Python.
- **Overbuilding.** Students want inheritance because they heard the word. Not this year, and not this week. Two attributes, two methods, three objects.

## 10. Homework

Full details in `handouts/week-12-homework.md`. In summary: finish the pet or inventory class and add one more attribute and method; write a second class and make two objects interact; three trace questions on class code; optional Crash Course episode on software engineering. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice.

## 11. Assessment

Observational, with one specific check. During Segment 6, confirm for each student that two objects made from their class hold independent values. That single check catches nearly every misconception in the topic.

Also ask two or three students to explain what `self` means in their own words. As in Week 5, that explanation is the AI-policy enforcement mechanism as much as it is the assessment.

Homework is a completion check against the weekly-labs rubric. Flag anyone whose class does not run; Week 13's linked list and Week 16's text adventure both assume a working `__init__`.

## 12. AP alignment

This session covers AP CSP topic 3.2 Data Abstraction, and reinforces 3.13 Developing Procedures, since a method is a procedure with a parameter that happens to be the object itself. The maze segment reinforces 3.8 Iteration in the exam's own notation.

**Be straight with students about the limits here, again.** Classes and objects are not AP CSP exam content at all. The exam has no `class` keyword, no objects, and no dot notation. This is the second and last week of Unit 3 where the AP mapping is genuinely thin, and it is worth saying so plainly rather than pretending. The transferable ideas are two: abstraction, meaning you build a named thing and then use it without reopening it, and procedures with parameters, which is exactly what a method is. Both are tested. From Week 13 onward the mapping tightens up considerably.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** No unit covers objects, because they are not tested. The nearest fit is Unit 2, Programming, and specifically the lessons on procedures, parameters, and abstraction. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 7, Parameters, Return, and Libraries, at `https://studio.code.org/courses/csp-2025/units/7`. Do the parameters and return lessons. A method is a procedure that receives its data as a parameter, so this is the exam-shaped version of today.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Human Robot Maze, loops stage: Segment 2 is complete on its own. Canonical source is CodeAI My Robotic Friends, `https://curriculum.code.org/csf-18/coursee/1/`, with a newer edition under `https://curriculum.code.org/csf-current/`. The full four-stage progression is in `teaching-activities/Unplugged-Logic-Activities.md`. Verify links are live before class; sites reorganize.
- Python tutorial section on classes, for your reference: `https://docs.python.org/3/tutorial/classes.html`. Read the first two subsections only; the rest is well beyond this course.
- Crash Course Computer Science, Episode 16 ("Software Engineering"), optional homework viewing; it covers objects and why large programs are organized into named pieces. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`. Confirm the episode number in the playlist before assigning it; numbering in reuploads sometimes differs.
- CodeAI CSP Unit 7, Parameters, Return, and Libraries (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/7`
- AP robot commands, for the advanced `Robot` class extension: `ap-track/AP-Pseudocode-Bridge.md`.
