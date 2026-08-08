# Week 29 Homework: Somebody Else's Computer

One session, four big topics, and one ladder on the board that ties them together. This homework checks the ladder, the arithmetic, and whether you can apply any of it to your own project. Plan on about 40 minutes.

## 1. Speedup problems

Show your working. The formula is `speedup = sequential time / parallel time`.

1. A job takes 90 seconds run sequentially. Split across processors it takes 30 seconds. What is the speedup?
2. A program has one part that takes 40 seconds and cannot be split up at all, and another part that takes 120 seconds and can be split perfectly across 4 processors. How long does the whole program take now, and what is the speedup?
3. Five independent tasks take 12, 9, 20, 7, and 15 seconds. They are run at the same time on five processors. How long until all five are finished? Explain your answer in one sentence, because the number is not the interesting part.
4. In question 2, suppose you get 100 processors instead of 4. What is the shortest the program could possibly take, and why can it never go below that?

## 2. Put these on the ladder

The ladder from class, from most to least that you manage:

```text
Your own hardware
Virtual machine
Container
Serverless function
```

For each situation below, say which rung you would pick and give one sentence of reasoning. There is more than one defensible answer for some of them, and the reasoning is what is being marked.

1. A hobby website that gets about ten visitors a day and must cost as close to nothing as possible.
2. A school that needs to run a piece of old software that only works on Windows Server 2012.
3. A team of six developers who keep breaking each other's setups because everyone has slightly different Python versions installed.
4. A function that resizes a photo, called maybe twenty times a day, at completely unpredictable moments.

## 3. Your project at scale

Imagine a thousand people used your final project at the same time. In a short paragraph each:

1. What part of it would break first? Be specific about which part, not just "the server."
2. Name one thing from today's session that would help with that, and say why.
3. Would your project need more than one copy of its data? If it did, name one thing that could go wrong that cannot go wrong today with one copy.

You do not have to build any of this. The question is whether you can see it coming.

## 4. The CAP scenario

A messaging app keeps three copies of your chat history on three servers. The network between two of them fails for thirty seconds.

1. If the app chooses to stay correct, what does the user see during those thirty seconds?
2. If the app chooses to stay available, what does the user see instead, and what has to happen afterward?
3. Which choice would you make for a messaging app? Which would you make for a bank transfer? Give one sentence each.

## 5. Keep the project moving

By the end of this week you should have a file that runs. Not finished, not good, just running and doing one thing. If you do not have that yet, that is this week's actual homework and the rest is secondary.

---

**A reminder on getting help.** AI assistants are permitted on homework builds and side projects, under the three rules: verify everything, never turn in code you cannot explain, and put a comment at the top saying what you asked for and what you changed.

If you are submitting an AP Create Performance Task, your project stays completely AI-free at every stage until you submit it. College Board's rule, not ours.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**An honest note about this week.** Of the four topics covered in class, exactly one is on the AP exam: **4.3 Parallel and Distributed Computing**. Cloud, containers, serverless, CDNs, and blockchain are not in the AP framework at all. Do not study them for the exam. Study them because you now know what those words mean, which is worth more than four exam points anyway.

Question 1 of your homework above is the AP-tested part of this week. If you got all four right, you have this topic.

What 4.3 expects of you:

- Tell a sequential solution from a parallel one from a distributed one.
- Calculate speedup as sequential time divided by parallel time.
- Recognize that the part which cannot be parallelized sets a floor on how fast the whole thing can get.
- Recognize that adding more processors gives less and less benefit each time.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, and specifically its parallel and distributed computing lessons. That portion only. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** there is no cloud or distributed-systems unit, so this week does not map cleanly and it is better to say so than to send you somewhere wrong. The nearest useful thing is Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`, and specifically its redundancy and fault-tolerance lessons, which are the same idea underneath today's replication material. If you already did Unit 2 in the fall, reread those lessons rather than starting something new.

**Create Task reminder.** Still entirely your own work, still no AI at any stage. Milestone for this week: your program should run and do one real thing. Also decide now, and write it down, which procedure you are going to screen-capture for your Personalized Project Reference. It needs to be one you wrote yourself, it needs at least one parameter, and it needs both an if and a loop inside it. If your program does not have a procedure like that yet, that is what to build next.

**Extra practice if you want it.**

- Write a Dockerfile for your Week 25 Flask app. You need four lines: a base image, a working directory, a copy of your files, and the command to run. Get it building if you have Docker; get it written even if you do not.
- Work this harder speedup problem, which is closer to what the exam sometimes asks: a program spends 20 percent of its time in a part that cannot be parallelized. If the parallel part could be made infinitely fast, what is the best possible speedup for the whole program? (The answer is 5, and working out why is the exercise.)
- Look up which cloud region is physically closest to you, then `ping` a service hosted there and one hosted on another continent, and write down the difference in milliseconds. Then work out roughly how much of that difference is just the speed of light.
