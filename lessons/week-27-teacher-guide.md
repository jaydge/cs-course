# Week 27 Teacher Guide

## 1. Header

- **Week:** 27 of 32
- **Unit:** 6, The Future of Computing
- **Theme question:** What is actually happening inside an AI?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Sketch the arc from rule-based AI and search to machine learning to today's large language models, and say what changed at each step.
- Build and train a tiny perceptron in Python, explain what the weights and the bias do, and show why it cannot learn XOR.
- Explain in plain language what an embedding is and why "meaning as a list of numbers" makes search and similarity possible.
- State the difference between training and inference, and why that difference explains cost, speed, and the fact that a model does not learn from your chat.
- Explain what a hallucination is, why the design of a next-token predictor makes it inevitable rather than a bug, and what that implies for using the tool.
- State the course's new AI policy accurately: what is now permitted, what is still forbidden, and the separate College Board rules that govern the Create Performance Task.

## 3. Where this sits

Unit 6 opens here. Everything from Week 1 to Week 26 built the stack underneath this topic: bits and encoding in Unit 1, hardware and the GPU in Unit 2, lists and dictionaries and loops in Unit 3, the network in Unit 4, and APIs and JSON in Unit 5. An LLM API call is a Week 25 request with a very expensive server on the other end, and students should be told that explicitly, because it makes AI a system rather than magic.

This is also the policy hinge of the whole course. From Week 1 the rule has been no AI assistance, and students have been told repeatedly that the rule changes here. It changes today, deliberately, in a taught session rather than by drift. Section 10 of the curriculum is the governing document; read it before you teach this.

The single most important thing to get right today is the carve-out. AI becomes available for ordinary coursework and side projects. It does not become available for the AP Create Performance Task, which students begin or continue this week and which is governed by College Board rules, not by ours. Two things start on the same day and pull in opposite directions, so name both clearly and repeat the second one every week from here to Week 32.

## 4. Materials and setup

- Each student's laptop with VS Code and Python; projector for live coding.
- Whiteboard with the theme question written large, and clear space for the perceptron diagram, which stays up all session.
- Printed Week 27 homework handout, one per student.
- Printed one-page AI policy card, one per student, stating the three phases in a form they can tape inside a notebook. Draft it from Section 6, Segment 6 below.
- The instructor machine with an LLM API key already configured in an environment variable, if you are running the API demo. The key stays on your machine; see the note in Section 5.
- Printed Create Task proposal form, one per student. One page: working title, what the program does, what a user does with it, what list or collection it manages, what procedure the student will write, and what would make it "done."
- Optional for the younger-student alternate: a browser open to TensorFlow Playground on a spare machine.

## 5. Pre-class prep checklist

- **Read Section 10 of `curriculum/CS-Curriculum-and-Setup.md` end to end, and write out the three sentences you will say when you unlock AI and the three sentences you will say when you carve out the Create Task.** Do not improvise this part. (15 min)
- **Read the current College Board policy on plagiarism and AI use for the AP CSP Create Performance Task on AP Central.** This changes, and you are about to make a binding statement to students about it. Verify it this year rather than trusting anything printed here. (20 min)
- Type and run the perceptron code from Segment 3 yourself, including the XOR failure, so you know exactly what the printed output looks like at each epoch. (15 min)
- If running the API demo: install the provider SDK on your machine only, set the key as an environment variable, and run the script in Segment 5 once. **Look up the current model identifier on the provider's model list and write it into the placeholder in the Segment 5 script, then print your filled-in copy and teach from that.** Confirm your account has credit and note the per-call cost so you can state it honestly. Provider SDKs, model names, and pricing change frequently; verify all three the week you teach this. (20 min)
- Prepare one deliberately hallucinated code sample for Segment 6. The easiest reliable method is to write it yourself: take real Python and invent a plausible method that does not exist, for example `my_list.sort_descending()` or `requests.get_json(url)`. You want it to look completely reasonable. Print several spare copies on paper: the same sample is the non-AI alternative for homework item 4, for any student whose family has not cleared AI use. See Section 11. (10 min)
- Print the homework handout, the policy card, and the Create Task proposal form. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up (0:00 to 0:08)

- **You do:** Pose the theme question and take the room's existing theories about how AI works. Write them on the board without correcting any of them. Common answers: it searches the internet, it copies answers, it thinks, it has a giant database. Leave them up; you will return and mark each one at the end of Segment 5.
- **You do:** Set the shape of the day out loud: a history, a thing they build, a look at the modern machine, and then a change to the class rules that they have been waiting on since September.

### Segment 2: From rules to search to learning (0:08 to 0:30), Systems strand

1. **Start with the oldest idea: AI as rules.** Early AI was hand-written rules, an expert system, a long chain of if-statements written by a human who already knew the answer. Ask what breaks: nobody can write enough rules for the real world, and the rules cannot handle a case the author never imagined.
2. **Second idea: AI as search.** Draw a small game tree on the board, three levels of tic-tac-toe. Explain that a chess program does not "understand" chess; it explores possible futures and scores the leaves. Deep Blue beating Kasparov in 1997 was mostly this, at enormous scale, plus expert-written scoring. Land the point: search plus a scoring function gets you superhuman play without anything resembling understanding.
3. **Ask the question that forces the third idea.** How do you write the scoring function for "is this photo a cat?" Let them try. They cannot, and neither can anyone else, and that is exactly why the field changed.
4. **Third idea: machine learning.** Instead of writing the rules, show the program many labeled examples and let it adjust its own numbers until it gets them right. Define the three words on the board: **training data** (the examples), **parameters** (the numbers the program adjusts), **training** (the adjusting).
5. **Give the honest timeline in four beats.** The perceptron in 1958, an early neuron model that worked and then hit a wall. A long quiet period. Around 2012, deep neural networks plus GPUs plus large datasets suddenly beat everything else at image recognition. Then 2017 onward, the transformer architecture, and language models scaling far past what anyone expected.
6. **Name why now and not 1980, in one sentence each.** More data, because the internet exists. More compute, because GPUs turned out to be perfect for the arithmetic involved. Better architectures. Connect the GPU point straight back to Unit 2: a GPU is thousands of simple units doing the same arithmetic in parallel, which is what training a network is.

### Segment 3: Build a perceptron (0:30 to 1:05), Coding strand

1. **Do it with humans first, three minutes.** Two students hold up cards showing 0 or 1. A third student is the neuron and holds two cards with numbers written on them, the weights, starting at 0 and 0, plus a third card for the bias. The rule: multiply each input by its weight, add them, add the bias, and if the total is above zero say 1, otherwise say 0. Run it once. It is wrong. Then give the learning rule: if you said 0 and should have said 1, add a little to the weight of every input that was 1. Run it again. It gets closer. That is training, done by hand.
2. **Now go to the machines.** Draw the same thing on the board as a diagram: two inputs, two weights, a sum, a bias, a threshold, one output.
3. **Students type this, in a new file `perceptron.py`.** Have them type it rather than paste it.

   ```python
   weights = [0.0, 0.0]
   bias = 0.0
   rate = 0.1

   training = [
       ([0, 0], 0),
       ([0, 1], 0),
       ([1, 0], 0),
       ([1, 1], 1),
   ]

   def predict(inputs):
       total = bias
       for i in range(len(inputs)):
           total = total + inputs[i] * weights[i]
       if total > 0:
           return 1
       return 0

   for epoch in range(20):
       wrong = 0
       for inputs, target in training:
           guess = predict(inputs)
           error = target - guess
           if error != 0:
               wrong = wrong + 1
               for i in range(len(inputs)):
                   weights[i] = weights[i] + rate * error * inputs[i]
               bias = bias + rate * error
       print("epoch", epoch, "weights", weights, "bias", round(bias, 2), "wrong", wrong)
   ```

4. **Read the output together.** The `wrong` count drops to 0 and then stays there. Point at the weights and say what just happened: nobody wrote the rule for AND. The program found numbers that produce AND, by being corrected four examples at a time. That is the entire idea of machine learning, in twenty lines and no libraries.
5. **Students do:** Change the four target values to OR (`0, 1, 1, 1`) and rerun. It learns that too, with different weights. Then change them to NOT on a single input if they want a third case.
6. **Now break it on purpose.** Change the targets to XOR (`0, 1, 1, 0`) and rerun. The `wrong` count never reaches 0; it oscillates forever. Let them watch it fail for a full minute before you explain.
7. **Explain the failure geometrically, not algebraically.** Draw the four input pairs as four dots on a small grid. For AND and OR you can separate the 1s from the 0s with one straight line. For XOR you cannot, no matter where you put the line. One perceptron is exactly one straight line, so XOR is not merely hard for it, it is impossible.
8. **Land the historical payoff.** This exact limitation stalled the field for years. The fix is to stack perceptrons in layers, so the second layer draws lines on the output of the first. That is what "deep" in deep learning means: more layers. Every model they have heard of is this, with billions of weights instead of two.

### Segment 4: Stretch (1:05 to 1:10)

### Segment 5: Embeddings, transformers, and what an LLM actually does (1:10 to 1:35), Systems strand

1. **Embeddings first, because they are the most useful idea and the least known.** Ask how a program could know that "king" and "queen" are more related than "king" and "bicycle". Take answers. Then give the move: represent every word as a list of numbers, a few hundred of them, positioned so that related things sit near each other. That list is an embedding, and "near" means the arithmetic distance between two lists.
2. **Make it concrete with a two-number version on the board.** Put four words on a grid with axes you invent, for example "how animal" and "how large": dog at (0.9, 0.4), cat at (0.9, 0.2), whale at (0.9, 1.0), truck at (0.1, 0.9). Ask which two are closest. Then say the real thing has hundreds of axes, nobody labels them, and the model discovers them during training.
3. **Say what this buys you, in three examples they use daily.** Search that finds the right result when you did not use the right word. Recommendations. Duplicate detection. All three are "find the nearest list of numbers."
4. **Transformers, conceptually and briefly.** Do not do the math. Say this: the key trick is called attention, and it lets the model, when processing one word, look at every other word in the input and weight how much each one matters right now. In "the trophy did not fit in the suitcase because it was too big," attention is how the model connects "it" to "trophy" instead of "suitcase." Everything else about the architecture is plumbing around that idea.
5. **What an LLM does, stated flatly.** It predicts the next chunk of text, over and over, given everything so far. That is the whole job. It was trained by being shown enormous amounts of text with the next chunk hidden, and adjusting billions of weights until its guesses got good. There is no lookup, no database of answers, and no search of the internet unless a tool has been bolted on to do that.
6. **Training versus inference, on the board as two columns.** Training happens once, costs a very large amount of money and electricity, and produces a fixed set of weights. Inference is running those frozen weights to answer one prompt, and it is comparatively cheap and fast. Draw the consequence students most often get wrong: your conversation does not train the model. The weights do not change when you talk to it. Anything it appears to remember within a conversation is text being fed back in, not learning.
7. **Hallucinations, framed correctly.** A model that predicts plausible next text will produce plausible text whether or not it is true, because plausibility is what it optimizes and truth is not something it has direct access to. It is not lying, and it is not broken. It is doing the thing it does, and the thing it does is not fact retrieval. That is why a confident, well-formatted, completely fictional answer is the characteristic failure mode.
8. **Optional API demo, instructor machine only.** Run this on the projector. State clearly that the key is yours, that it stays on your machine, that it costs real money per call, and why: provider terms generally restrict minors from holding their own accounts, per Section 12 of the curriculum.

   ```python
   import os
   import anthropic

   client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

   # Placeholder, not a real model name. During prep, either set CLASS_MODEL_ID
   # in your environment or type the current identifier in on the line below.
   model_id = os.environ.get("CLASS_MODEL_ID", "PUT-THE-CURRENT-MODEL-ID-HERE")

   try:
       message = client.messages.create(
           model=model_id,
           max_tokens=200,
           messages=[{"role": "user", "content": "Explain a perceptron in two sentences."}],
       )
       print(message.content[0].text)
   except Exception as error:
       print("The call failed. Check the model identifier first:", model_id)
       print(error)
   ```

   **The model line is deliberately a placeholder rather than a real identifier, and the call is wrapped so that a wrong one fails readably.** Model names are retired on short notice, and a stale one printed in a guide fails live in front of the class with an unhelpful error. Get the current identifier from the provider's model list during prep, put it in the environment variable or type it in, and run the filled-in script once before class. If it does fail in front of the class, the printed identifier and error message are the demonstration: read them out loud, which is exactly the habit Segment 6 is about to ask of them. Point at the shape of it and connect it to Week 25: this is an HTTP POST with a JSON body and a JSON response. The API key is the same idea as the API keys from the weather app. The only new thing is what is on the other end. Verify the SDK name, the model name, and the pricing before class; all three change.
9. **Return to the board from Segment 1** and mark each of the students' opening theories as right, wrong, or partly right. This takes ninety seconds and is the highest-retention move of the session.

### Segment 6: Using AI as a coding tool, and the policy change (1:35 to 1:55)

Hand out the policy card at the start of this segment and work through it with them.

1. **State the change plainly.** From today, AI assistance is permitted on ordinary coursework, homework builds, and personal projects. The Week 1 rule has done its job: they can write, read, and debug Python without help, which means they are now in a position to supervise a tool instead of being replaced by one.
2. **State the reason for the old rule, now that it is over.** You cannot supervise something you could not do yourself. That was the entire point, and it is why the rule was not negotiable in September.
3. **Give the three rules that replace it, and write them on the board.**
   - **Verify everything.** Run it. Read the error. Check the function actually exists in the documentation.
   - **Never ship code you do not understand.** If you cannot explain a line out loud, it does not count as yours, and it will not count for a grade.
   - **Disclose.** Any submitted work that used AI carries a comment at the top saying what you asked for and what you changed. Not a punishment; a professional habit.
4. **Demonstrate a hallucinated API live.** Put your prepared sample on the projector, the one with the invented method. Ask the class whether it looks right. It will. Run it. It fails with an `AttributeError`. Then look up the real method in the Python documentation together. Say the general form of this: the failure mode is not gibberish, it is confident, plausible, well-formatted, and wrong.
5. **Show the harder case, which is the subtle bug rather than the crash.** Describe or display a function that runs, returns a number, and is off by one at the boundary. A crash tells you there is a problem. A wrong answer does not. This is why "it ran" is not verification and why the Week 15 testing habits now matter more, not less.
6. **Name the over-reliance trap directly.** The risk is not that the tool is bad. The risk is that reaching for it before thinking removes the exact struggle that builds skill. Give them a working rule: try it yourself first, for a set amount of time, then ask. And a second one: if you find yourself accepting suggestions you do not follow, stop and go read the code.
7. **Mention agentic tools, briefly and accurately.** Claude Code is an example of the next step up: a tool that can read your files, run commands, and make multi-file edits rather than just returning a snippet. Say the obvious consequence out loud: the more it does on its own, the more the human's job becomes review, and the less excuse there is for not reading the diff. If you demonstrate it, demonstrate reviewing its output, not just accepting it.
8. **Now the carve-out, and give it its own beat.** Slow down here. The AP Create Performance Task is not covered by anything you just said. It is governed by College Board's own originality and AI rules, it must be the student's own work, and students sign an attestation to that effect. Our class rules cannot and do not override that. For any student who is submitting a Create Task, the Create Task stays under the Week 1 rule for the rest of the year.
9. **Say the practical version so nobody has to interpret it.** Write it on the board and leave it there:
   - AI is allowed on: homework builds, side projects, extra-credit tracks, and non-AP final projects.
   - AI is not allowed on: the AP Create Performance Task, in any form, at any stage, including planning, code, and the written pieces.
   - If you are unsure whether something is Create Task work, it is, and the answer is no.
10. **Close the loop for non-AP students.** A student not submitting a Create Task still builds the final project, and you are still setting the rule for it. The recommendation is to keep the core logic of the final project AI-free so the demo and the writeup are honest, and to allow AI for setup, environment problems, and debugging. Whatever you decide, decide it today and put it in writing on the handout, because ambiguity in Week 31 is a much worse problem than a strict rule in Week 27.

### Segment 7: Create Task kickoff and wrap (1:55 to 2:00)

- **You do:** Hand out the Create Task proposal form. Tell every student, AP track or not, that the final project starts now and not in Week 31, and that the proposal is due as part of this week's homework.
- **You do:** Give the one sentence that shapes good proposals: the best project is small, finishable, and something the student actually wants to exist.
- **You do:** Hand out the homework, noting the Extra Credit AP Track section and the fact that the "no AI" footer on the handout has changed for the first time all year.

## 7. Key scripts and analogies

- **Why machine learning exists:** "Nobody can write down the rules for what a cat looks like. So we stopped writing rules and started showing examples. That is the whole pivot, and everything since is scale."
- **Weights:** "A weight is how much this input matters to this decision. Training is the process of the program arguing with itself about how much each thing matters until it stops being wrong."
- **The perceptron limit:** "One perceptron is one straight line. If you cannot separate your answers with one straight line, one perceptron will never do it, no matter how long you train. Stacking them is what buys you curves."
- **Embeddings:** "Meaning as coordinates. Once every word is a point in space, 'related' becomes 'close', and 'close' is just arithmetic. Computers are extremely good at arithmetic."
- **Attention:** "When you read 'it', you look back at the sentence to figure out what 'it' means. Attention is the model doing that, for every word, all at once."
- **What an LLM is:** "An extremely well-read autocomplete. That sounds dismissive and it is not. Autocomplete at that scale turns out to do things nobody predicted."
- **Training versus inference:** "Training is writing the textbook, once, at enormous cost. Inference is looking something up in it. Talking to the model does not edit the textbook."
- **Hallucination:** "It is not lying to you. It has no idea what true means. It is producing the most plausible-looking next thing, and plausible and true overlap most of the time, which is exactly what makes the misses dangerous."
- **On the policy change:** "You were not allowed to use the calculator until you could do the arithmetic. You can do the arithmetic now. Here is the calculator, and here is the one exam where it is still not allowed."
- **On the Create Task carve-out:** "This is not our rule and we cannot bend it. College Board sets it, you sign it, and it holds for the rest of the year."

## 8. Differentiation

- **Younger or newer students:** Use the Section 11 alternate. Skip the weighted-sum arithmetic and put them on TensorFlow Playground or Teachable Machine, where they train a classifier by clicking and watch the decision boundary move. The objective is the same: they should be able to say that the program adjusted its own numbers until it stopped being wrong. If they are typing the perceptron, give them the full file and have them change only the four target values and describe what happens.
- **Extensions for advanced or AP-track students:** Add a hidden layer by hand and get XOR working, or use `scikit-learn`'s `MLPClassifier` on the same four rows and compare. Compute the distance between two invented three-number embeddings by hand and rank which pairs are closest. Read the Anthropic or OpenAI documentation page for the API call in Segment 5 and describe the request as an HTTP request, naming the method, headers, and body, connecting it to Week 20 and Week 25.

## 9. Common pitfalls

- **The policy change swallows the session.** Students will want to talk about AI opinions all period. Protect Segments 2 through 5 and hold the discussion for Segment 6 and for Week 30, where it has a proper protocol.
- **The Create Task carve-out gets heard as a suggestion.** It will, if you say it once at 1:52 while handing out papers. Give it its own moment, put it on the board, put it on the policy card, and put it on the handout. Then repeat it in Weeks 30, 31, and 32.
- **Students conclude the model is "just autocomplete, so it is useless."** The opposite over-correction of thinking it is magic, and just as wrong. The honest framing is that a very large next-token predictor does genuinely useful work and also fails in a specific, predictable way.
- **Students believe their chats train the model.** Extremely common and worth killing explicitly. Note separately that some providers may use conversations for training under their terms, which is a privacy question and a different question from whether the weights change while you type.
- **The perceptron never converges even for AND.** Check `rate` is not enormous and that `predict` uses `> 0` rather than `>= 0`. Also check that the student did not indent the training loop inside the `predict` function.
- **XOR is treated as a bug in their code.** Say before they run it that it is supposed to fail, or half the room will spend ten minutes debugging correct code.
- **API keys on student machines.** Do not let this happen even once. The key is instructor-owned per Section 12, it costs real money, and the terms generally restrict minors. If a student wants API access for an extra-credit project, mediate it with a parent and your key, and set a spend limit.
- **Cost surprise.** If you run the demo repeatedly with long outputs, it adds up. Set `max_tokens` low and check your usage dashboard afterward.

## 10. Homework

Full details in `handouts/week-27-homework.md`. In summary: get the perceptron learning AND and OR, run the XOR case and explain the failure in writing; a short written piece on training versus inference and on hallucinations; the Create Task or final project proposal, which is the real deliverable this week; and an optional supervised exercise in catching an AI-generated error, which carries an equivalent non-AI version on the printed sample for families who have not cleared AI use. The handout's help-policy footer changes this week, and the Extra Credit AP Track section carries the Create Task rules in full.

## 11. Assessment

Observational and one written artifact.

The perceptron is assessed against the weekly-labs rubric, with the "works and can explain" level requiring the student to point at a weight and say what it does. Do not accept "it learns" as an explanation.

The written homework piece is where you check the two ideas most likely to be misremembered: that training and inference are different events, and that a hallucination is a predictable consequence of the design rather than a malfunction.

**The AI-using exercise, homework item 4, is optional and is never required of any student.** Some families will decline, and some services have an age floor, so plan for it rather than improvising. The equivalent non-AI version is the printed hallucinated sample from Segment 6: hand it to the student on paper and have them work steps 1 to 3 of item 4 against it unchanged, checking every function and method in the Python documentation, then running it and testing an empty list, a zero, and a negative number. Assess both versions identically, against the same thing: did the student check the claims against documentation, and did they test the edges rather than accepting that it ran. Nothing in the grade turns on whether a student prompted a model, and do not record the difference anywhere that reads as a deficit.

**The proposal is the graded item that matters.** It is the first component of the final project, which is 20 percent of the course grade. Read every proposal before Week 28 and return it with a scope judgment: too big, too small, or right. Most first proposals are too big. Sending a student into Week 31 with an unfinishable idea is the single most avoidable failure of the last six weeks.

Also record, per student, which AI policy applies to them from here: Create Task submitters are AI-restricted for their project, and everyone else follows the rule you set in Segment 6, step 10. Write it down. You will need it when you grade in Week 32.

## 12. AP alignment

**Be honest with students about this week: AI and machine learning are not an AP CSP framework topic.** There is no Big Idea for neural networks, no exam question on transformers, and no pseudocode for training a model. Today's content is here because it is essential to understanding the computing world they live in, not because it is on the exam. Saying that plainly is better than implying an alignment that does not exist.

Three genuine AP connections do exist and are worth naming:

- **5.3 Computing Bias, previewed.** Where a model's behavior comes from, namely its training data and the choices of the people who built it, is the mechanism behind the bias topic that Week 30 covers properly. Today's "the model found the numbers, nobody wrote the rule" is the setup for that week's "so where did the numbers come from?"
- **3.14 Libraries and 2.4 Using Programs with Data,** touched lightly by the API call and by using someone else's trained model as a component.
- **Practice 6, Responsible Computing.** Note for your own planning that this practice is assessed only through the Create Performance Task, not on the multiple-choice exam. Today's policy session is practice for it.

The real AP value of this week is momentum on the Create Performance Task, which begins now.

**Announce the standing AP hour today.** College Board requires nine hours of supervised in-class time for the Create Task, and the regular sessions contain only about two hours forty minutes of it (the count is in the Week 31 guide, Section 3). The course covers the rest with a scheduled, supervised hour immediately after class each week from this week through submission, plus office hours by arrangement. Attendance is required only for students submitting the Create Task, is logged with dates, and costs everyone else nothing. Say this out loud when the proposal form goes home, so families can plan for the extra hour on class days.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, is the nearest match, and its lessons on emerging technology and computing innovations line up with today. Work only that portion. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** there is no AI unit in the CSP course, so do not pretend one matches. Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`, was unlocked in Week 26 and students may already be inside it, so this week continues that work rather than starting it. This week's slice is one specific piece of the unit and no more: the opening lessons that set out the task overview, what the finished submission must contain, and how it is scored. That is the piece that shapes a good proposal, which is this week's deliverable. **Stop before the planning and project-development lessons.** Unit 9 is spread deliberately across four weeks so that no single week becomes "work on Unit 9": the written-response and Personalized Project Reference lessons are Week 30's slice, the planning and build lessons are Week 31's, and whatever remains is finished in Week 32. Lesson names and ordering inside the unit change between course versions, so check the unit's lesson list and take only the portion described.

Nothing here is required of non-AP students.

## 13. Resources used this week

- **Section 10 of `curriculum/CS-Curriculum-and-Setup.md`, the AI-use policy.** Read this during prep. It is the governing document for Segment 6 and the guide does not restate all of it.
- **College Board guidance on plagiarism and AI use for the Create Performance Task:** AP Central, `https://apcentral.collegeboard.org/courses/ap-computer-science-principles`. Review the current year's version during prep. This policy changes and you are making a binding statement to students based on it.
- Perceptron lab: complete in Segment 3, nothing external needed.
- TensorFlow Playground, for the younger-student alternate and for a good visual of hidden layers: `https://playground.tensorflow.org`. Teachable Machine, for a no-code training demo: `https://teachablemachine.withgoogle.com`. Both are free and need no account.
- LLM API documentation, for the Segment 5 demo: Anthropic at `https://docs.anthropic.com` or OpenAI at `https://platform.openai.com/docs`. Verify SDK names, model names, and current pricing the week you teach this; all three change often. The key is instructor-owned per Section 12 of the curriculum.
- Claude Code, the agentic example mentioned in Segment 6: `https://docs.anthropic.com/en/docs/claude-code`. Only demonstrate it if you have used it yourself; a fumbled agentic demo teaches the wrong lesson.
- Crash Course Computer Science, Episodes 34 ("Machine Learning and Artificial Intelligence") and 36 ("Natural Language Processing"), optional homework viewing. Episode 36 is the better pairing for the language-model half of this session than Episode 35, "Computer Vision," which this course does not assign. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- Younger-student neural-network alternate: Section 11 of `curriculum/CS-Curriculum-and-Setup.md`.
- AI and machine learning extra-credit track: Section 9 of `curriculum/CS-Curriculum-and-Setup.md`.
