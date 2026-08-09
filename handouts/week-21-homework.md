# Week 21 Homework: The Whole Story

That is Unit 4 finished, and the first half of the course with it. You wrote the trace, you took the concept check, and you have a five-minute oral coming up on the slip you were handed.

This homework is deliberately short. Plan on about 35 minutes.

## 1. Prepare for your oral by telling it to someone

This is the most useful thing in this handout, and it takes ten minutes.

Find someone at home who is not in this class and tell them what happens when you open google.com, from your finger to your eyes. Do not read from anything. Let them ask questions. Then write down the two stages you found hardest to explain out loud, and one question they asked that you could not answer.

Bring both to your oral. Being able to say "I know I am shaky on DNS" is worth more than pretending otherwise, and it is one of the things the oral actually asks you.

## 2. Two ways of answering the same question

When you ran `ssh` for the first time, your computer stopped, showed you a fingerprint, and asked whether you were sure. When you visit an HTTPS site, your browser does not ask you anything; it just shows a padlock.

Both are solving the same problem. In four or five sentences:

1. What is the problem both of them are solving?
2. How does SSH solve it?
3. How does the browser solve it?
4. Which approach would you rather have for a machine you connect to every day, and why?

## 3. Explore what you cloned

Open a terminal, go to the repository you cloned from the class server, and answer these. Write the command you used for each.

1. What files and folders are in it?
2. How many commits are in its history, and what does the commit message say?
3. There is a hidden folder in there that you will not see with a plain `ls`. What is it called, and what do you think it is for? (You do not need to look inside it.)

## 4. Half a year in

Write a short reflection, five or six sentences. Not a summary of what we covered, but an honest answer to this: name three things you can now explain to somebody that you could not explain in September, and for each one say who you would most like to explain it to and why.

Then name one thing that is still fuzzy. That one is genuinely useful to me, so be honest.

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episode 30, "The World Wide Web," is the new one this week, and it makes the point that the internet and the web are not the same thing. If you want more revision for the oral, Episodes 28 and 29 from the last two weeks are worth a second look, but that is a re-watch and not new homework: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

## What is coming

Next week we leave Thonny for VS Code and start building software the way it actually gets built: real project structure, real tools, and the week after that, Git properly. Everything you learned in the terminal over the last five weeks becomes the thing you use every day rather than a lab exercise.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

This one matters more than usual because of the oral. The whole point of that conversation is to hear your understanding in your own words. There is nothing to prepare except the thing you already know, and nothing to gain from anyone else's words in your mouth.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**A milestone worth naming: Big Idea 4 is now finished.** Between Weeks 19, 20, and 21, the base course has covered both topics that Big Idea 4 tests at the level the exam asks for. That is 11 to 15 percent of the multiple choice, complete. It is the first big idea to be finished.

One thing to keep straight, because it looks like it belongs here and does not: topic 4.3, Parallel and Distributed Computing, is not part of this. That is about splitting work across several processors or machines, and our course covers it in Week 29. Splitting a computation is a different idea from routing a packet.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies. Finish the internet portion of the unit, the lessons that tie the pieces together into how the web works end to end. Then stop; the cybersecurity lessons in that unit belong with our Week 28. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`. Finish it. Three weeks of our course have mapped onto this one unit, so if you have been keeping up you should be able to complete it now.

**A self-audit, and this one is worth the twenty minutes.**

Open `ap-track/AP-CSP-Topic-Coverage.md` and read the whole table, all five big ideas. You are halfway through the course, so mark each of the 35 topics as one of three things: solid, shaky, or not covered yet.

Most of Big Idea 3 should be solid, since Unit 3 was the heart of it. Big Idea 4 should now be solid. Big Ideas 2 and 5 will have real gaps, and that is expected; the data topics land in Week 25 and the impact topics in Week 30. Bring your shaky list to class.

**Extra practice if you want it.**

- Write out the whole trace as a numbered list and mark, next to each stage, which of the four layers from last week it belongs to: physical, IP, TCP, or application. Some stages will not fit any of them. Work out why, and what that tells you about the four-layer picture being a simplification.
- The exam loves a scenario question of the form "the following component fails, what happens?" Write three of your own about the trace, with answers, and bring them in. Good ones distinguish between failures that are invisible to the user, failures that are slow, and failures that are total.
- Work through any trace problems you have not done in `ap-track/AP-Pseudocode-Bridge.md`. From Week 22 the coding gets bigger and the pseudocode practice is entirely on you, so a steady twenty minutes a week from here is worth more than a cram in April.
