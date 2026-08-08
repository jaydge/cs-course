# Week 10 Homework: From a Key Press to a Pixel

Unit 2 is finished. You started five weeks ago with one transistor and ended with the whole machine. This homework is lighter than usual because the checkpoint was in class. Plan on about 30 minutes.

## 1. Write the path

From memory, in your own words, write out what happens between pressing a key and seeing the letter on screen. Aim for at least eight steps in the right order. Numbered list is fine; full sentences are better.

Do it from memory first. Then check it against your notes and add anything you missed in a different color or marked with a star, so you can see what you actually remembered.

## 2. Two written answers

- What is an interrupt, and why is it better than the CPU constantly checking the keyboard to see if anything happened? Two or three sentences.
- Your keyboard does not send the letter A. What does it send, and why does that distinction matter?

## 3. Look at your own bytecode

Pick two functions you have written this year, from Hangman, the text analyzer, the gate lookup, or anything else. For each one, run this in Thonny:

```python
import dis
dis.dis(your_function_name)
```

Then answer:

- How many bytecode instructions did each function turn into?
- Which function had more, and does that match which one felt more complicated to write?
- Pick any three instruction names from the output and write down what you think each one does. Guessing from the name is fine; that is half the point.

## 4. One reflection

In Segment 3 we counted twelve stages between your finger and the pixel, and noticed that the person who wrote the text editor had to think about almost none of them.

Write three or four sentences on this: what does it mean for each layer to hide the one underneath it, and why would software be impossible to build if that were not true? Use the word "abstraction" at least once and make sure it is doing real work in the sentence.

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episode 8 ("Instructions and Programs"), Episode 22 ("Keyboards and Command Line Interfaces"), and Episode 23 ("Screens and 2D Graphics"). Episode 22 covers today directly. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

## 6. Looking ahead

Unit 3 starts next week and it is the biggest block of the year: dictionaries, objects and classes, data structures, searching and sorting, testing, and a text adventure at the end of it. It is all programming. Come with your Python working and your CS Class folder tidy.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

Also worth saying, now that Unit 2 is done: be ready to explain any part of the key-press path out loud, in your own words. If you can explain it, you own it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

This week introduces no new AP content, and there is no unit to point you at. Key presses, interrupts, and Python bytecode are not on the exam. The one real connection is the idea of abstraction itself, which the exam does test, usually as questions asking what a given abstraction hides and why hiding it is useful. Question 4 in the main homework is genuinely good AP practice for that, so if you do nothing else here, do that one carefully.

**Your unit for this week.** This is a consolidation week rather than a new slice. Do only what is listed.

- **Project STEM (the AP spine):** Unit 2, Programming. Finish anything you still have open in the programming unit. Do not start a new unit: the ones after Programming line up with our Unit 3 and Unit 5, and you will get more out of them when the class is there too. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** finish Unit 6, Lists, Loops, and Traversals, at `https://studio.code.org/courses/csp-2025/units/6`. This has been your target for Weeks 6, 7, and 9, so this is the week to close it out. Hold off on Unit 7; it belongs with our Unit 3 starting next week.

**Take stock, which is the real assignment this week.**

- Open `ap-track/AP-CSP-Topic-Coverage.md` and read the Big Idea 3 table. Ten weeks in, you have seen 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.12, 3.13, 3.14, and 3.15. That is most of the largest section of the exam. Mark each one solid, shaky, or not yet, and bring the shaky ones to class.
- Notice which big ideas you have barely touched: 4 (Computer Systems and Networks) and 5 (Impact of Computing) are almost entirely ahead of you, in Units 4 and 6. Nothing to do about that now; just know where you stand.

**Extra practice if you want it.**

- Go back through the trace problems in `ap-track/AP-Pseudocode-Bridge.md` and do every one you have not done yet. Time yourself. On the exam these are worth about ninety seconds each.
- Write one paragraph explaining what a Python function is as an abstraction: what does the person calling it not have to know, and what would change if they did have to know it? This is exactly the shape of an exam question about abstraction, and writing one is the fastest way to learn to answer them.
