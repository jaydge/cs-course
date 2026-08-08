# Week 27 Homework: A Machine That Learns, and a New Rule

This week you built something that taught itself, and the class rule about AI changed for the first time all year. Read the help policy at the bottom carefully; it is different from every other handout you have been given. Plan on about 60 minutes, most of it on the proposal.

## 1. Finish the perceptron

Open `perceptron.py` from class and make sure it still works.

1. Confirm it learns AND: the `wrong` count reaches 0 and stays there.
2. Change the four target values to OR (`0, 1, 1, 1`) and run it. Write down the final weights and bias for AND and for OR, side by side.
3. Change the targets to XOR (`0, 1, 1, 0`) and run it. It will never reach 0 wrong. Let it run all 20 epochs and copy down what the last three lines say.

Save the file into your CS Class folder.

## 2. Write four short answers

A few sentences each. Handwritten or in a file, your choice.

1. Point at one weight in your trained AND perceptron and say what that number means. Not "it learns," but what that specific number does when the program runs.
2. Draw the four XOR inputs as four dots on a small grid, label each 0 or 1, and use the drawing to explain why one straight line cannot do the job.
3. Explain the difference between training and inference. Then answer this: when you type a question into a chatbot, does the model learn from what you typed? Why or why not?
4. Explain what a hallucination is and why it happens. Your answer should not use the word "mistake," because that is not quite what it is.

## 3. Your project proposal (the important one)

This is the start of your final project, which is 20 percent of your course grade. It is due next week, and it is not a formality. Fill in the proposal form from class:

- **Working title.**
- **What the program does,** in two sentences.
- **What a person does with it.** Describe someone actually using it, step by step, in five or six lines.
- **What list or collection it manages.** A list of scores, a dictionary of items, a list of records read from a file, something.
- **One procedure you will write yourself,** with a name, what goes in, and what comes out.
- **Your definition of done.** The smallest version that would count as finished and be worth demonstrating.

Two pieces of advice, from watching this go wrong before:

**Make it smaller than you think it should be.** Almost every first proposal is too big. You have Week 31 and part of Week 32 in class, plus whatever you do at home. A small finished program beats an ambitious unfinished one every single time, and it always will.

**Pick something you actually want to exist.** You are going to look at this for six weeks.

## 4. Optional: catch it being wrong

Only if your family allows you to use an AI assistant, and only with a parent knowing you are doing it. Some services require you to be 13 or older, so check before you sign up for anything.

Ask an AI assistant to write a short Python function for something you already know how to do. Then, without running it:

1. Look up every function and method it used in the official Python documentation at `https://docs.python.org/3/`. Does each one really exist, with those arguments?
2. Now run it. Does it do the right thing at the edges? Try an empty list, a zero, a negative number.
3. Write down what you found, whether it was correct or not. "It was fine" is a legitimate answer, and so is "it invented a method."

Bring what you found to class.

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episodes 34 and 35, cover machine learning and computer vision: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

**The help policy has changed. Read this.**

From this week, you may use AI assistants on your homework builds, your side projects, and the extra-credit tracks. Three rules come with that:

1. **Verify everything.** Run it. Read the errors. Check that the functions it used are real.
2. **Never turn in code you cannot explain.** If you cannot walk through a line out loud, it does not count as yours and it will not be graded as yours. That check has not changed all year and it is not going to.
3. **Say so.** Any work you submit that used AI gets a comment at the top of the file saying what you asked for and what you changed yourself.

**And one thing that has not changed.** If you are submitting an AP Create Performance Task, your Create Task is completely off limits to AI, from now until you submit it. Not the code, not the planning, not the written pieces. That is a College Board rule, not a class rule, you will sign a statement saying the work is yours, and nothing your instructor says can change it. If you are not sure whether something counts as Create Task work, assume it does and do not use AI on it.

If you are not doing the Create Task, your instructor will tell you exactly which parts of the final project are AI-free. Write that down when you are told, because "I did not know" is not going to work in Week 32.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**An honest note first.** Everything in today's class about neural networks, embeddings, and language models is not on the AP CSP exam. There is no AI topic in the framework. Today was here because it matters, not because it is tested. Do not spend AP study time on it.

What today does do for AP is start the clock on the Create Performance Task, which is 30 percent of your AP score.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, is the closest match to today's material. Work only its lessons on computing innovations and emerging technology. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** there is no AI unit, so do not go hunting for one. Start Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`, properly this time rather than skimming it as you did in Week 16. It will tell you exactly what the finished submission has to contain.

**The Create Task rules, in full, because this is where they start mattering.**

- Your Create Task must be entirely your own work. No AI, no code from a friend, no code from a tutorial pasted in and lightly edited.
- You may not use AI at any stage of it: not for ideas, not for code, not for debugging, not for the written pieces.
- You will attest that the work is yours. A false attestation is a serious matter and College Board investigates it.
- The rest of your coursework is now AI-permitted. Your Create Task is not. Keep those two things separate in your head, and if you are ever unsure, do not use it.
- Verify the current year's rules yourself on AP Central at `https://apcentral.collegeboard.org/courses/ap-computer-science-principles`. College Board updates this policy and the version that counts is the one in force when you submit.

**Create Task milestone for this week.**

Your proposal above is your Create Task proposal. Two additions if you are on the AP track:

- Name specifically what list or collection your program uses **to manage complexity**. The exam wants a collection that makes the program simpler than it would be without one, not a list that happens to be there. Write one sentence explaining what your program would look like without it.
- Name a **student-developed procedure that takes at least one parameter** and contains selection (an if) and iteration (a loop). You will be screen-capturing this later, so decide now what it is.

**Extra practice if you want it.**

- Write your perceptron's `predict` function in AP pseudocode using `ap-track/AP-Pseudocode-Bridge.md`. Watch the indexing: AP lists start at 1 and Python lists start at 0.
- Read the official AP CSP Exam Reference Sheet at `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`. This is the pseudocode you get on exam day. Twenty minutes with it now is worth an hour in April.
