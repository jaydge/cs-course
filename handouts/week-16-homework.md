# Week 16 Homework: Finish the World, Run the Simulation

This finishes Unit 3. Nothing in this week's work is new; everything in it came from the last five weeks. Plan on about 45 minutes.

## 1. Finish the text adventure

Your game is done when all of these are true:

- It has at least three rooms held in a dictionary, and every exit leads to a room that actually exists.
- The player is an object made from a class, with a location and a bag.
- There are at least two functions or methods beyond `__init__`.
- The player can pick up at least one item and it goes into the bag.
- Typing `quit` ends the game cleanly, and typing nonsense does not crash it.

Then add one thing of your own. A locked door that needs an item, a room that changes its description after you have been there, a simple score, anything. One thing, finished, beats three things half-built.

Save it into your CS Class folder.

## 2. Run the simulation and write up what you see

Take the dice simulation from class. Run it three times with different trial counts: 100, 1,000, and 100,000.

Change `bar` along with `trials`, to 1, 10, and 1000 in that order. `bar` is how many rolls one asterisk stands for. If you leave it at 10 for all three runs, the 100-trial run draws almost nothing and the 100,000-trial run draws over a thousand asterisks per line and wraps around your screen. The counts underneath are still correct either way; it is only the picture that breaks.

Answer these in a sentence or two each:

1. Which total came up most often at 100,000 trials? Why that one?
2. Describe how the shape of the output changed as the trial count went up.
3. Run the 100-trial version three separate times. Did you get the same answer each time? What does that tell you about trusting a simulation you only ran once?
4. Name two things this simulation leaves out about real dice. Then name one question where leaving them out would make the simulation useless.

## 3. Pick the structure

For each situation, say what you would use to hold the data: a list, a dictionary, a stack, a queue, or a class. One sentence of reasoning each. There is more than one defensible answer for some of these; the reasoning is what counts.

1. The high scores for a game, in order, best first.
2. Every student's locker number, looked up by student name.
3. A monster in a game, with health, a name, and an attack.
4. The jobs waiting for the school printer.
5. The moves made so far in a chess game, so a player can take one back.

## 4. Optional, and worth doing on your own machine

Open Activity Monitor on a Mac, or Task Manager on Windows, and look at what is running that you did not start. Count how many processes there are. Then look at your login items and see how many programs start themselves when you turn the machine on. Write down the number of each. You do not need to change anything; just look.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

Unit 3 is finished, so this matters more than usual: be ready to explain, out loud, why you chose a dictionary for your rooms and a class for your player. If you can explain it, you own it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

Today's simulation work is a real exam topic, 3.16 Simulations. Three things the exam expects you to know, all of which you just did:

- A simulation is a model of something real, and it always leaves things out on purpose. Simplification is the technique, not a flaw.
- You use one when the real thing would be too slow, too expensive, too dangerous, or impossible to test directly.
- A simulation that uses random values gives different results on different runs, and its conclusions are only as good as the assumptions built into it.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming, and specifically the simulation and random-values lessons. Work only that material and stop. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** the simulation topic is spread across the course rather than sitting in one unit, so pick by topic. Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`, has the loop-and-count machinery a simulation is built from. Unit 5, Data, at `https://studio.code.org/courses/csp-2025/units/5`, covers reading conclusions out of collected results.

**A look ahead, for orientation only.**

CodeAI Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`, shows what the AP Create Performance Task actually asks for: a program you design yourself, a video of it running, and written responses about it. Skim it for twenty minutes if you are curious. Do not start it. Create Task work begins in February, in Unit 6 of this course, and the submission deadline is in late April. Check the current year's deadline on AP Central rather than trusting a date from a handout; College Board moves it. The only reason to look now is so that the project ideas you start having over the next couple of months are the right shape.

**Extra practice if you want it.**

- Work through the remaining trace problems in `ap-track/AP-Pseudocode-Bridge.md` that you have not done. From here the warm-ups move out of class time, so this is on you.
- Write your dice simulation in AP pseudocode. You will need `RANDOM(1, 6)`, which includes both endpoints, and a `REPEAT n TIMES` loop. Since pseudocode has no dictionary, you will have to count with a list, which is a genuinely useful exercise in working within the exam's limits.
- Unit 3 is finished, and it was the heart of Big Idea 3, which is 30 to 35 percent of the exam. Open `ap-track/AP-CSP-Topic-Coverage.md`, read the Big Idea 3 table, and mark each topic as solid, shaky, or not yet. Bring the shaky ones to class.
