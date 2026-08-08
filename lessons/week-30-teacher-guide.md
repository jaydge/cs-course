# Week 30 Teacher Guide

## 1. Header

- **Week:** 30 of 32
- **Unit:** 6, The Future of Computing
- **Theme question:** Who does this help, who does it hurt, and who gets to decide?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Name a beneficial and a harmful effect of the same computing innovation, and explain why harmful effects are usually unintended rather than designed (AP 5.1).
- Explain the digital divide along access, quality, and skill, and name a cause other than individual choice (AP 5.2).
- Identify three places bias can enter a computing system, and explain why a system built with no intent to discriminate can still discriminate (AP 5.3).
- Explain what crowdsourcing is, give two real examples, and name one thing that goes wrong with it (AP 5.4).
- Explain copyright as it applies to software, say what an open-source license actually does, and describe Creative Commons in one sentence (AP 5.5).
- State the strongest argument on more than one side of a genuinely contested question, in a form the other side would accept as fair.
- Show measurable progress on the final project or Create Task.

## 3. Where this sits

This is the richest AP week in the entire course. Big Idea 5, Impact of Computing, is 21 to 26 percent of the multiple-choice exam, and five of its six topics are covered today: 5.1, 5.2, 5.3, 5.4, and 5.5. The sixth, 5.6 Safe Computing, was Week 28. A student who genuinely absorbs these two weeks has the whole of Big Idea 5.

It is also the week most likely to go wrong, in a way none of the other 31 weeks can. The subject matter includes live political and economic arguments that reasonable, informed adults disagree about, taught to a room of 8th through 11th graders by one instructor whose opinion carries disproportionate weight. The design decision throughout this guide is therefore that **you teach the structure of the arguments and the students supply the positions**. Where a question is genuinely contested, the guide gives you the strongest case on more than one side and a protocol for running the disagreement. It does not give you a conclusion to deliver, because delivering one would be the wrong lesson and would also be worse AP preparation: the exam asks students to identify effects and tradeoffs, not to hold approved views.

Week 27 previewed the bias topic by showing that a model's behavior comes from its training data. Today asks where the data came from. That is the load-bearing connection of the unit, so make it explicitly.

Twenty-five minutes of protected project time closes the session. Do not sacrifice it; it is part of the nine-hour Create Task allocation and Week 31 depends on students arriving with working code.

## 4. Materials and setup

- Whiteboard with the theme question written large, plus three permanent columns drawn and labeled: **What we agree on**, **What we disagree on**, **What we would need to know**. These stay up all session and get filled in continuously.
- Printed discussion protocol card, one per student, with the five steps from Segment 1.
- Printed tryout dataset for the bias activity, one per pair. Twelve fictional athletes, each with: years on a club team, coach rating out of 10, timed sprint, and a note on whether they have played before. Build it so that "years on a club team" correlates strongly with the coach rating and weakly with the sprint time. Details in Segment 4.
- Printed debate briefs, one per pair, each carrying one contested question and three bullet points for each side. Write these yourself from Segment 7 so they match your students.
- Each student's laptop for the project work block.
- Projector.
- Printed Week 30 homework handout, one per student.

## 5. Pre-class prep checklist

- **Decide, in advance and in writing, how you will handle your own opinions today.** The recommended stance is that you do not state them during the debate segment, and that if a student asks directly you either decline or answer once and label it clearly as one person's view rather than the class conclusion. Whatever you choose, choose it before you are asked in front of the room. (10 min)
- Build the tryout dataset. It takes twenty minutes and the activity does not work with invented-on-the-spot numbers, because the correlation has to actually be in the data for students to find it. (20 min)
- Write the debate briefs. Two contested questions is the realistic number for the time available; pick from the four in Segment 7 based on what your students will engage with. For each, write three genuine bullet points per side. **Write the side you personally disagree with first**, and write it well enough that someone holding it would recognize it. If you cannot, that question is not ready to teach. (25 min)
- Read AP topics 5.1 through 5.5 in `ap-track/AP-CSP-Topic-Coverage.md` and confirm you know which specific things the exam expects for each. (10 min)
- Decide what the project work block will produce, per student, and write yourself a list of who is behind. (10 min)
- Print the protocol cards, datasets, briefs, and homework handouts. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and the discussion protocol (0:00 to 0:10)

1. **Pose the theme question** and say what today is: the one session of the course where the right answer is not in the room and will not be by the end.
2. **Hand out the protocol card and read it aloud.** Say that it applies to every discussion today, and that you will interrupt anyone who skips a step.
   - **One.** Write before you talk. Two minutes of silence, on paper, before any discussion opens.
   - **Two.** State the other side first. Before you argue your position, say what the best version of the opposing argument is. Someone who holds that position has to accept your summary as fair before you may continue.
   - **Three.** Separate facts from values. Ask which part of the disagreement is about what is true and which part is about what matters. Most arguments are jammed because nobody has separated these.
   - **Four.** Name what would change your mind. If nothing would, say that honestly, and notice what it means.
   - **Five.** No vote. The session does not end by taking a poll. It ends with the three columns on the board filled in.
3. **Say the reason for step two out loud, once.** If you can only argue against a weak version of the other side, you do not understand the disagreement, you only understand your own position. That skill is the point of the day and it transfers to everything.

### Segment 2: Beneficial and harmful effects, AP 5.1 (0:10 to 0:24), Systems strand

1. **Start with a computing innovation nobody argues about.** GPS navigation. Ask for benefits: nobody gets lost, ambulances arrive faster, delivery is efficient. Fill the list generously.
2. **Now ask for the costs,** and let them find them: people cannot navigate without it, the traffic reroutes through residential streets, the location data is collected and sold, and an outage strands people who never learned the roads.
3. **Name the pattern that the exam actually tests.** Write it on the board: harmful effects of computing innovations are usually unintended, and they are often discovered only after wide adoption. The people who built GPS navigation were not trying to erode anyone's sense of direction.
4. **Do a second one quickly, in pairs, two minutes.** Assign different innovations to different pairs: online maps, recommendation feeds, translation, ride-hailing, smart doorbells, spellcheck. Each pair produces two benefits and two costs and reads them out.
5. **Add the nuance the exam expects.** The same effect can be beneficial to one group and harmful to another at the same time, and an innovation's effects depend on how people actually use it rather than on what it was designed for. Get an example of each from the pairs' lists.
6. **Put the first entries in the three columns on the board.** Usually "every innovation has unintended effects" goes under agreement immediately, which is a good start.

### Segment 3: The digital divide and crowdsourcing, AP 5.2 and 5.4 (0:24 to 0:40), Systems strand

1. **Define the digital divide in three dimensions,** because students usually know only the first.
   - **Access.** Whether there is a connection and a device at all.
   - **Quality.** Whether it is fast and reliable enough to actually do the thing. A phone with a data cap is not the same as home broadband when the assignment is a video call.
   - **Skill and support.** Whether there is anyone around who knows how to fix it when it breaks.
2. **Ask what causes it, and push past the first answer.** Students say "money." Push: why is rural broadband worse than urban broadband even for people with money? Get to the infrastructure economics, that laying cable to a sparse area costs the same and serves fewer customers. Then add the other causes the exam names: geography, age, disability, and language.
3. **Make it concrete and close to home.** Ask what would happen to their own coursework this year if the home connection went out for a month. Then ask what would happen to a student whose school assumes everyone has one and who never had one at all. Keep this at the level of systems rather than asking any student to disclose their own situation.
4. **Name the exam's framing:** the digital divide affects both individuals and whole groups, it is caused by socioeconomic, geographic, and demographic factors, and unequal access to computing means unequal access to the opportunities that computing creates.
5. **Pivot to crowdsourcing, AP 5.4, which is the same theme viewed from the other end:** what becomes possible when very large numbers of people contribute a little each.
6. **Give three examples and name what each one gets from the crowd.** Wikipedia gets writing and fact-checking. OpenStreetMap gets mapping. Citizen-science projects get classification work that no funded team could afford. Distributed computing projects get spare processor time. Reviews and ratings get judgment at a scale no editor could match.
7. **Ask what goes wrong with it,** and let them generate the list: vandalism and deliberate manipulation, unpaid labor producing something someone else monetizes, quality that varies wildly by topic, and the fact that the crowd represents whoever showed up rather than everyone. That last one is the bridge to the next segment, so say it as the bridge.

### Segment 4: Computing bias, AP 5.3 (0:40 to 0:58), Systems strand

1. **Run the activity before defining anything.** Hand each pair the tryout dataset and this task: you are writing the ranking rule for team selection. Using only the columns in the data, write a rule that picks the top six. You may weight the columns however you like. Five minutes.
2. **Collect the rules on the board.** Most pairs will weight the coach rating heavily, because it looks like the most informative column, and several will weight years on a club team because it looks like a measure of commitment.
3. **Now reveal what is in the data.** Point out the correlation you built in: club-team years and coach rating track each other closely, and both track weakly or not at all with the actual sprint time. Ask what club teams cost to join. Let the room work out that the rule they just wrote selects heavily on who could afford club fees, dressed up as a measure of ability.
4. **Ask the crucial question, and let it be uncomfortable for a moment.** Did anyone in this room intend to select on family income? Nobody did. Ask whether that changes what the rule does. It does not. That gap between intent and effect is the whole topic.
5. **Now define the three sources of bias, on the board, mapping each to what just happened.**
   - **Bias in the data.** The data reflects a world that is already unequal, so a system trained on it reproduces that inequality. This is the club-fee column.
   - **Bias in the design.** Which columns were collected, which were left out, what counts as success. Nobody put "improvement over the season" in the dataset, and that choice was made before any rule was written.
   - **Bias from the builders.** The assumptions of the people writing the system, both intentional and, far more often, unnoticed. A team of people who all played club sports would not have thought to question that column.
6. **State the exam's key sentence and have them write it down:** computing bias can be embedded at every stage of development, whether intentionally or not, and a system that treats everyone by the same rule is not therefore fair, because the rule itself may encode a difference.
7. **Connect it to Week 27 explicitly, in two sentences.** Three weeks ago they watched a perceptron find its own numbers from four labeled examples, and nobody wrote a rule. Now ask where the labels came from. Every model, including the largest ones, is a rule discovered from a dataset that somebody chose.
8. **Then give the honest, contested part rather than a tidy ending.** Ask what to do about it. Take answers, and note the real difficulty as you go: removing the biased column often does not help, because other columns predict it. Measuring fairness requires collecting the very attribute you were trying not to use. And there are several mathematical definitions of fairness that cannot all be satisfied at once, so "make it fair" is not a single well-defined instruction. Put this under "what we would need to know" rather than resolving it.

### Segment 5: Stretch (0:58 to 1:03)

### Segment 6: Copyright, licensing, open source, and privacy, AP 5.5 (1:03 to 1:20), Systems strand

1. **Start with the default, because students assume the opposite.** Anything a person writes, including code, is automatically copyrighted by the author the moment it exists. There is no filing step. The default is that nobody else may copy it.
2. **Ask what that would mean for the internet,** where copying is the basic operation. Then introduce licenses as the answer: a license is the author keeping the copyright and giving specific permissions in advance.
3. **Walk the licensing spectrum in four stops,** briefly, on the board.
   - **All rights reserved.** The default. Ask before using.
   - **Permissive open source,** for example MIT. Do what you like, including selling it, but keep the copyright notice.
   - **Copyleft open source,** for example GPL. Do what you like, but anything you build on it must carry the same freedoms.
   - **Public domain.** No rights reserved at all.
4. **Give Creative Commons one clean sentence** and show the building blocks: attribution, non-commercial, no-derivatives, share-alike, mixed and matched. It is the same idea as software licensing applied to writing, images, and music, and the exam expects them to know it exists.
5. **Make it real with their own repositories.** Every student has a GitHub repo from Week 23 and a project in progress. Ask what license their project has. The answer for most is none, which means all rights reserved by default, which means nobody may legally use their code. Have them think about whether that is what they want, and note that they will add a license file in Week 31.
6. **Now privacy and surveillance, and set it up as a tradeoff rather than a villain.** Start with the classroom itself: the NextDNS logs they saw in Week 28 exist to keep the network safe and they also record what everyone looked at. Both are true simultaneously. That is the shape of every privacy question.
7. **Name the mechanisms without moralizing.** Data collected for one purpose gets used for another. Aggregation makes anonymous data identifiable, and a small number of "anonymous" facts about a person is usually enough to name them. Data persists far longer than the reason for collecting it. Convenience and privacy trade against each other in almost every product decision.
8. **Give the exam's framing and stop there.** Personally identifiable information is valuable and is collected constantly, often in exchange for a free service; the exchange is real and it is not always a bad deal; and users are frequently unaware of what they are trading.
9. **Add deepfakes as the current sharp edge,** four sentences. Synthetic images, audio, and video have made "I saw it" and "I heard their voice" much weaker evidence than they were. The genuinely hard consequence is not just that fakes get believed, it is that real recordings can now be dismissed as fakes. Note the legitimate uses too, in film, accessibility, and translation, because a topic taught only through its worst case does not stick.

### Segment 7: Structured debate, steelman rounds (1:20 to 1:42)

Pick two of the four questions below. Run each for about ten minutes with the protocol from Segment 1. Your job is to run the protocol, not to referee the content.

**The four contested questions, each with the honest case on both sides.** These are written so you can hand out briefs; add your own bullets.

**Question A: Should public spaces use automated video surveillance?**
- The case for: it deters and solves violent crime, it is impartial in a way a human guard is not, victims of crimes in public places overwhelmingly want the footage to exist, and the alternative is not "no observation," it is unreliable human memory.
- The case against: it changes behavior even when nobody is watching, it errs in ways that fall unevenly across groups, the footage outlives its purpose, and a capability built for one use gets used for others without a new decision being made.
- The honest middle that students often find: this depends almost entirely on who holds the footage, for how long, and who may request it, which are policy questions rather than technology questions.

**Question B: Is automation destroying jobs, or moving them?**
- The case that it is a serious problem: automation has repeatedly eliminated specific occupations, the replacement jobs often require different skills and appear in different places, and telling a 50-year-old that the economy will adjust over twenty years is not a useful answer to them.
- The case that it is not: employment has not trended down across two centuries of mechanization, new categories of work appear that nobody predicted, and automating dangerous or crushing work is a real gain rather than a loss.
- The steelman that improves the discussion: both sides are frequently arguing about different time horizons, and both may be right about theirs. Push students to notice that.

**Question C: Should training an AI model on published work require permission or payment?**
- The case for permission: people made that work, the model's ability comes directly from it, the model competes with them commercially, and no other industry gets to use an input for free simply because using it was technically easy.
- The case against: reading things and learning from them has never required a license, humans learn from copyrighted work constantly, a per-work permission regime is impossible at scale and would hand the field to whoever already owns the largest archive, and the model does not store or reproduce the originals.
- Where it actually sits: this is being litigated and legislated right now, in several countries, with different answers emerging. Tell students that honestly. "Currently unresolved" is the correct state of knowledge and it is a valuable thing for a student to be able to say.

**Question D: Should social platforms be responsible for what their users post?**
- The case for: the platform chooses what to amplify, that choice is an editorial act, and the harm is real and measurable.
- The case against: the volume makes accurate judgment impossible, mistakes in both directions are inevitable, and giving a small number of companies the job of deciding what may be said is itself a serious concentration of power.

**Running it.**

1. Announce the question and give two minutes of silent writing. Enforce the silence.
2. Round one is the steelman round only. Each pair states the best version of the position they do **not** hold. Nobody argues yet. Take three or four and ask the room whether each summary was fair.
3. Round two: open discussion. Interrupt anyone who attacks a version of the argument that nobody in the room holds.
4. Round three, two minutes: what would change your mind? Take answers around the room. Accept "nothing" and ask the student to say why.
5. Fill the three columns on the board and read them back. That is the ending, and there is no vote.
6. Say the closing line and mean it: they should leave able to argue both sides of both questions. If they can only argue their own, they came in with an opinion and are leaving with the same one, which is not what the last twenty minutes were for.

### Segment 8: Final project and Create Task work time (1:42 to 1:57), Coding strand

- **You do:** Before anyone opens a laptop, restate the Create Task rule for the third time this unit: for students submitting a Create Performance Task, no AI at any stage, including planning, code, and debugging, and including today. Everyone else works under the rule you set in Week 27.
- **Students do:** Work. Silently, on the project, for the full fifteen minutes.
- **You do:** Circulate with your list of who is behind and conference with them first, thirty seconds each. The single question that helps most: what is the next thing you are going to type? A student who cannot answer that is stuck on scope, not on code, and needs the project cut down today rather than in Week 31.
- **You do:** Log this time. It counts toward the AP Create Task's nine protected hours, and you will need the total.

### Segment 9: Wrap (1:57 to 2:00)

- **You do:** Point at the three columns and note how much sits under "what we would need to know." Say that this is what an honest position on a hard question looks like. Hand out homework, noting the Extra Credit AP Track section, which is the biggest one of the year.

## 7. Key scripts and analogies

- **On unintended effects:** "Nobody set out to make people worse at reading a map. The harmful effects of a technology are almost never the ones anybody planned, which is exactly why they are hard to catch in advance."
- **On the digital divide:** "It is not one line with people on either side. It is access, then quality, then whether anyone in your house can fix it. A phone with a data cap is not the same thing as broadband, even though both are technically 'online'."
- **On crowdsourcing:** "A million people doing one minute of work each is something no company can buy. It is also a million people who chose to show up, which is not the same as everybody."
- **On bias:** "Nobody in this room decided to select on family income. The rule you wrote does it anyway. What a system does is a separate question from what its authors meant, and only one of those two things affects anybody."
- **On removing the biased column:** "Take out the obvious column and the other columns quietly rebuild it. Zip code predicts a great many things nobody put in the data."
- **On copyright defaults:** "Your code is copyrighted the moment you write it, with no paperwork. That means the default answer to 'may I use this?' is no. A license is you saying yes in advance, in writing, to everybody."
- **On open source:** "It is not 'free code lying around'. It is code with a legal document attached telling you exactly what you may do with it. Read the document."
- **On privacy tradeoffs:** "You are not being robbed, you are making an exchange. The question worth asking is whether you know what you are handing over and what it is worth, and mostly the answer is no."
- **On deepfakes:** "The dangerous part is not that people will believe fakes. It is that real footage can now be waved away as fake, which is a much cheaper thing to do."
- **On the steelman rule:** "If the other side's argument sounds stupid to you, you are not hearing their argument, you are hearing your version of it. Go find the version a smart person holds and argue with that one."
- **On not resolving things:** "Three columns, and the third one is the longest. That is not a failure of the discussion. That is what the honest state of a hard question looks like."

## 8. Differentiation

- **Younger or newer students:** Keep the examples concrete and close to their own lives, and steer away from the more abstract policy framing. The tryout activity works at every age and is the anchor; make sure they get through it. In the debate, give them the steelman round and let them stop there rather than pushing them into open argument, since stating the other side well is the harder and more valuable half anyway. Note that the debate briefs are written for the room, so pick the two questions that are age-appropriate for your youngest student, not your oldest.
- **Extensions for advanced or AP-track students:** Have them find two current news stories on the same contested question with opposite conclusions and identify exactly where the two accounts disagree, separating factual disagreement from value disagreement. Have them read one real open-source license end to end, MIT because it is short, and write a plain-language summary. Have them write the fairness question up properly: pick two definitions of fairness for the tryout dataset, show that satisfying both at once is impossible with that data, and explain what that means for anyone claiming a system is "unbiased."

## 9. Common pitfalls

- **The instructor's opinion becomes the class conclusion.** The largest risk of the day. In a small class with one adult, an offhand remark settles a question that should stay open. Decide your stance during prep, and if you do share a view, label it clearly as yours and invite disagreement immediately.
- **Teaching the contested questions as settled.** Every one of these has serious people on both sides. A student who leaves able to recite one position has learned less than a student who leaves genuinely unsure, and the exam rewards the second one more.
- **Straw-manning, in both directions.** This is what the protocol exists to prevent. Enforce the steelman round even when it slows things down, especially when the room agrees, because unanimous rooms produce the worst arguments.
- **Bias treated as an accusation.** If "bias" is heard as "the programmers were bad people," students stop thinking. The tryout activity fixes this by making them the ones who wrote the biased rule, so run the activity before the definitions and never in the other order.
- **The tryout dataset without a real correlation in it.** If you invent numbers on the spot, students will not find the pattern and the reveal will feel like a trick. Build the data during prep.
- **The debate eating the project time.** It will if you let it. Hard stop at 1:42, every time. The project block is part of the protected Create Task hours and Week 31 depends on it.
- **A student discloses something personal about their home situation.** Plausible in the digital divide segment. Keep the discussion at the level of systems and groups rather than individuals, do not follow up publicly, and follow up privately if something concerning comes out.
- **Everything drifts to AI.** Students will pull every topic back to AI because it is the most vivid current example. Two of the four debate questions are already about it, which is enough; use the others deliberately.
- **The Create Task rule quietly lapses.** By the third repetition it starts sounding like a formality. Say it anyway, at the top of the work block, every time.

## 10. Homework

Full details in `handouts/week-30-homework.md`. In summary: a benefit-and-cost analysis of one innovation the student chose; a written steelman of the position they disagree with on one of the class questions; a bias walkthrough of a described system; a licensing decision for their own project repository; and substantial project work, which is now the priority. The handout closes with an Extra Credit AP Track section that is the largest of the year, because five AP topics land today.

## 11. Assessment

Two things are assessed, and they are unusual for this course.

**The steelman writing task in the homework is the graded artifact of the week,** and it is scored on one criterion: would a person who actually holds that position accept the summary as fair and complete? Not on whether the student agrees, and explicitly not on which side they took. Say that to the class when you hand it out, because otherwise students write what they think you want.

**Participation in the protocol** is observational and is the one week where the participation component of the grade genuinely earns its 5 percent. What you are watching for is whether a student can hold a position and represent its opposite accurately at the same time.

For AP purposes, note that these five topics are examined through multiple-choice questions asking students to identify effects, causes, and tradeoffs, not to argue positions. The homework's benefit-and-cost item is the closest thing to exam-shaped practice this week, so mark it against that standard.

Finally, record where every student's project stands at the end of Segment 8. This is your last data point before Week 31, and any student without running code needs an intervention this week rather than next.

## 12. AP alignment

**This is the highest-yield AP session in the course.** Five of the six topics in Big Idea 5 are covered today: **5.1 Beneficial and Harmful Effects**, **5.2 Digital Divide**, **5.3 Computing Bias**, **5.4 Crowdsourcing**, and **5.5 Legal and Ethical Concerns**. Big Idea 5 is 21 to 26 percent of the multiple-choice exam, and it is the big idea students most often neglect because it does not look like programming. Tell them the percentage; it changes how they treat the week.

Specific things the exam expects, by topic:

- **5.1:** that innovations have both beneficial and harmful effects, that harmful effects are usually unintended, and that a single effect can be beneficial to one group and harmful to another.
- **5.2:** that the divide covers access, quality, and skill, and is driven by socioeconomic, geographic, and demographic factors rather than by individual choice.
- **5.3:** that bias can be embedded at every stage, intentionally or not, and that it frequently comes from the data rather than from the code.
- **5.4:** what crowdsourcing is, that it enables work at a scale otherwise impossible, and that citizen science is a standard example.
- **5.5:** copyright as the default, licensing as granted permission, open source and Creative Commons as license families, and the privacy implications of data collection and aggregation.

One structural note for your own planning: **Practice 6, Responsible Computing, is assessed only through the Create Performance Task, not on the multiple-choice exam.** Today's discussion work is therefore practice for the Create Task and for life, while the exam-facing part of the week is the factual content above. Both matter; they are assessed in different places.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, and specifically its impact-of-computing lessons, which cover beneficial and harmful effects, the digital divide, bias, crowdsourcing, and legal and ethical concerns. Students who did the cybersecurity portion in Week 28 now finish the unit. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 8, Cybersecurity and Global Impacts, at `https://studio.code.org/courses/csp-2025/units/8`. Do the global-impacts half of the unit, which was deliberately left for this week. Its innovation, bias, and digital divide lessons are the closest match in the free curriculum to today's session.

This is also the week to point AP-track students at the whole of `ap-track/AP-CSP-Topic-Coverage.md`, since with today's five topics plus Week 28's 5.6, the framework is complete.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The discussion protocol, the tryout bias activity, and the four debate questions are complete in Section 6. The tryout dataset must be built during prep; the activity depends on a correlation that is genuinely present in the numbers.
- **AP topics 5.1 to 5.5, with the exam's specific expectations:** `ap-track/AP-CSP-Topic-Coverage.md`. Read this during prep so you know which of today's many ideas are the tested ones.
- Official AP CSP Exam Reference Sheet, for AP-track students: `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`
- Open-source license texts, for the licensing segment and the advanced extension: `https://choosealicense.com` gives plain-language summaries of MIT, GPL, and Apache side by side, and links the full texts. Creative Commons license chooser: `https://creativecommons.org/choose/`. Both are worth two minutes of prep so you can answer the "which one should I use?" question that Week 31 will produce.
- The classroom's own DNS logging and filtering, used as the privacy example: Section 8 of `curriculum/CS-Curriculum-and-Setup.md`, and the Week 28 demonstration.
- Crash Course Computer Science, Episode 39 ("Educational Technology") and Episode 40 ("The Singularity, Skynet, and the Future of Computing"), optional homework viewing and a reasonable closing pair for the unit. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Unit 8, Cybersecurity and Global Impacts (AP-track reinforcement, global-impacts half): `https://studio.code.org/courses/csp-2025/units/8`
- AP Create Performance Task rules and the current year's deadline: AP Central, `https://apcentral.collegeboard.org/courses/ap-computer-science-principles`. Verify before relying on any date or requirement stated in these guides; College Board changes both.
