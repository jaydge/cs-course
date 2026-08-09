# Week 29 Teacher Guide

## 1. Header

- **Week:** 29 of 32
- **Unit:** 6, The Future of Computing
- **Theme question:** Where does "the cloud" actually live, and how do a thousand computers agree on anything?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Say what "the cloud" physically is, and name three things a data center has that a laptop does not.
- Explain virtualization, containers, and serverless as three points on one line, and say what each one stops you from having to care about.
- Explain what object storage is and why a CDN makes a video start faster, in terms of the network they learned in Unit 4.
- Distinguish parallel from distributed computing, and compute the speedup of a parallel solution from sequential and parallel run times (AP 4.3).
- Explain replication, and use the CAP framing to say why a distributed system must give something up when the network breaks.
- Give a plain-language account of what a blockchain is, what problem consensus solves, and what a blockchain is genuinely bad at.

## 3. Where this sits

This is the compressed week the curriculum designed on purpose. Cloud infrastructure, containers, distributed systems, and blockchain are four topics that could each take a semester, and they get one session between them, because the time was spent on programming depth in Unit 3 and is about to be spent on the final project. Say that out loud to the class: today is a map, not a territory, and the objective is that no term in it ever sounds like magic again.

It also has the best foundation of any tour in the course. Every idea today is a recombination of something students already own: a server is the class MacBook from Week 21, a container is the process and filesystem isolation from Week 17, a CDN is caching plus the routing from Week 19, and replication is the fault tolerance from the Week 19 packet-routing activity. Teach it as recombination, not as new material.

AP 4.3 Parallel and Distributed Computing is the one genuinely tested topic in the session, and it comes with arithmetic the exam actually asks for. Protect Segment 6.

## 4. Materials and setup

- Projector and instructor machine with a browser.
- The class MacBook server reachable over SSH, and the deployed Flask app from Unit 5 still live.
- Docker installed on the instructor machine if you intend to run the container demo. It is optional; the segment works from the board.
- Whiteboard with the theme question written large, and space for the abstraction ladder, which stays up all session.
- Three composition notebooks or clipboards labeled Node A, Node B, Node C, for the Three Notebooks activity.
- A stack of index cards for the messages in that activity.
- Six sheets of paper for the paper blockchain, pre-ruled with three sections each: "previous page's code," "transactions," "this page's code."
- Printed Week 29 homework handout, one per student.
- Optional: a photograph of a real data center interior, and a photograph of an undersea cable landing station, on screen.

## 5. Pre-class prep checklist

- Decide whether you are running the Docker demo live. If yes, pull a small image and run it once beforehand so nothing downloads in front of the class. If no, the board version in Segment 3 is complete and you lose nothing. (15 min, or 0)
- Have the Unit 5 Flask app running and its URL ready, plus an SSH session to the class server open in a second terminal tab. You will use both as the "one server" baseline. (10 min)
- Work the three speedup problems in Segment 6 yourself and write the answer key. Getting one wrong on the board in front of the class is the fastest way to lose the AP topic of the week. (10 min)
- Rehearse the Three Notebooks activity by walking through the message sequence alone. It has a specific ordering that produces the disagreement, and improvising it produces a muddle. (15 min)
- Pre-rule the six blockchain pages. (5 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up (0:00 to 0:08)

- **You do:** Pose the theme question. Ask where a photo goes when it is "in the cloud." Take answers and write them down. Then ask the follow-up that does the work: name one physical object that photo is sitting on right now.
- **You do:** Frame the day honestly. Four large topics, two hours, no mastery expected. The goal is a map with no blank regions on it.

### Segment 2: Servers, data centers, and virtualization (0:08 to 0:28), Systems strand

1. **Start with the server they already have.** SSH into the class MacBook on the projector. Say plainly: this is a server. It is a computer that is on, has an address, and answers requests. There is nothing else to the definition. A server is a role, not a kind of hardware.
2. **Scale it up in three steps and ask what breaks at each one.** One laptop serving your class. One rack serving a school. A hundred thousand machines serving a country. Take answers on what breaks: power, heat, network, the fact that machines fail.
3. **Describe a data center as the answer to those four problems.** Redundant power feeds and generators and batteries. Enormous cooling, because a rack of servers is a space heater. Redundant network connections, often to multiple providers. And the design assumption that hardware fails constantly, so nothing important lives on one machine. Show the photograph if you have one.
4. **Add the geography.** Regions and availability zones exist because a whole building can lose power, and because the speed of light is finite, so a server in Virginia answers a user in Virginia faster than one in Oregon. Tie back to Week 20's latency observations.
5. **Now virtualization, and motivate it with waste.** A physical server running one small app uses a fraction of its capacity, and the rest is bought and paid for and idle. Ask what to do about it. Steer to the answer: run several independent computers on one physical machine.
6. **Define a virtual machine precisely.** Software called a hypervisor divides one physical machine into several virtual ones, each with its own operating system, each believing it has the hardware to itself. Note that students have already seen this: WSL2 on the Windows fleet is a virtual machine, and Windows students have been running Linux inside Windows since Week 17 without calling it that.
7. **Name what virtualization bought the world:** you can rent a computer by the hour instead of buying one, and you can create and destroy computers with an API call. That is what "cloud" means economically, and it is the whole business.

### Segment 3: Containers and serverless (0:28 to 0:48), Systems strand

1. **Ask what is wasteful about a virtual machine.** Each one carries a full operating system, gigabytes of it, most of which is identical to its neighbors. Booting one takes a minute.
2. **Define a container against that.** A container shares the host's kernel and packages only the application and the specific libraries it needs. It starts in under a second and is measured in megabytes. Connect it straight to Week 17: a container is a process with a restricted view of the filesystem, the network, and the process list. The isolation mechanisms are the OS features they already met.
3. **Name the problem containers actually solve, because it is not mainly efficiency.** Say it as the sentence every developer has heard: "it works on my machine." A container is the machine, shipped along with the code, so it works the same everywhere. Ask whether anyone has hit a version mismatch on their own laptop this year. Several will have.
4. **Docker in three commands, at the board or live.** Keep it to this:

   ```text
   Dockerfile   a recipe: start from this base, copy my code in, run this command
   docker build makes an image from the recipe, once
   docker run   starts a container from the image, as many times as you like
   ```

   Connect image and container to the Week 12 vocabulary: an image is the class, a container is an object made from it. That single line does more work than a live demo.
5. **Optional live demo, two minutes.** Run a prepared container and show it serving something, then run a second copy on a different port. The visible payoff is two identical, isolated copies started instantly.
6. **Serverless, defined by what disappears.** Ask what is still annoying about containers: something has to decide how many are running, keep them patched, and pay for them while idle. Serverless means you upload a function, the provider runs it when a request arrives, and you are billed per invocation. There is still a server; you have just stopped being the one who thinks about it.
7. **Draw the ladder on the board and leave it up.** This is the takeaway of the segment.

   ```text
   Your own hardware    you manage everything
   Virtual machine      you manage the OS and up
   Container            you manage the app and its libraries
   Serverless function  you manage the code
   ```

   Say the pattern out loud: every rung removes one thing you have to care about, and every rung takes away some control. That tradeoff is the whole history of computing infrastructure in one ladder.

### Segment 4: Object storage and CDNs (0:48 to 1:03), Systems strand

1. **Contrast two ways to keep a file.** A filesystem has folders, paths, and the ability to change a byte in the middle of a file, and it is what they have used since Week 1. Object storage has a bucket, a key, and a blob, and you generally replace the whole object rather than editing it.
2. **Ask why anyone would give up folders.** The answer is scale and durability: a flat key-to-blob mapping spread over many machines with many copies is far easier to make enormous and hard to lose than a directory tree. This is where photos, videos, and backups actually live.
3. **Now the distance problem.** Ask how long light takes to cross the Atlantic and back through fiber, roughly. It is tens of milliseconds, and no engineering fixes it. Then ask what you do if your users are everywhere and your data is in one place.
4. **Let them invent the CDN.** They will say "keep copies closer to people." That is it. A content delivery network is a set of caches spread around the world holding copies of the static parts of a site, so the video, the images, and the JavaScript come from a machine near the user while the parts that must be fresh come from the origin.
5. **Demonstrate it, thirty seconds.** Run `ping` and `traceroute` against a large CDN-served site and against the class server, and compare the hop counts and times on the projector. The big site is often physically closer than students expect.
6. **Land the caching principle,** which is one of the few genuinely universal ideas in computing: keep a copy of the expensive thing near where it is used. Note that they have now met it four times, in the CPU cache in Week 8, the DNS cache in Week 19, the browser cache in Week 24, and here.

### Segment 5: Stretch (1:03 to 1:08)

### Segment 6: Parallel and distributed computing, AP 4.3 (1:08 to 1:28), Systems strand

This is the AP-tested segment of the week. Do not compress it.

1. **Define the two terms against each other, on the board.** A **sequential** solution does one step at a time. A **parallel** solution splits the work among processors that share memory in one machine, for example the cores in their laptop. A **distributed** solution splits the work among separate machines that communicate over a network. Parallel is inside one computer; distributed is across many.
2. **Make it physical in one minute.** Ask how long it takes one student to count the books on a shelf, then how long for four students splitting the shelf. Then ask what the four students still have to do at the end: add their four numbers. Name that overhead now, because the exam depends on it.
3. **Give the speedup definition, exactly as the exam uses it.**

   ```text
   speedup = sequential run time / parallel run time
   ```

4. **Work three problems as a class,** on paper, then at the board. These are the exam's question type.
   - A task takes 60 seconds sequentially. Run in parallel it takes 20 seconds. What is the speedup? (3.)
   - A program has a part that takes 30 seconds and cannot be parallelized, and a part that takes 90 seconds and can be split perfectly among 3 processors. What is the total parallel time and the speedup? (30 plus 30 equals 60 seconds; speedup is 120 divided by 60, which is 2.)
   - Four processes take 50, 40, 30, and 20 seconds and are run in parallel across four processors. How long does the whole thing take? (50, the slowest one. The answer is not the average and not the sum, and this is the item students most often miss.)
5. **Draw the conclusion the exam wants.** Adding processors gives less and less benefit, because the part that cannot be split does not shrink and because coordination costs grow. Speedup is never equal to the number of processors in practice, and doubling the processors does not halve the time.
6. **Connect it back up the session.** A data center is distributed computing as a business. Splitting a job across a thousand machines is the reason a web search returns in under a second.

### Segment 7: The Three Notebooks, unplugged (1:28 to 1:45)

Replication, partition, and eventual consistency, made visible. Run it exactly in this order.

1. **Set up.** Three students sit apart, each with a labeled notebook: Node A, Node B, Node C. Each writes the same first line: `balance = 100`. Say what they are: three copies of one database, kept on three machines, which is what replication means. Ask why anyone would want three copies. Take the two right answers: survival if one dies, and speed if they are near different users.
2. **Establish the rule.** Any change written in one notebook must be sent to the other two on an index card, hand-delivered by a runner. Delivery is not instant. Nothing else may be said out loud.
3. **Round one, the happy path.** You tell Node A: a customer deposits 50. Node A writes `balance = 150` and sends two cards. The runner delivers them. All three now agree. Ask what the system looked like during the delivery: the three copies disagreed for a moment, and any customer reading Node C got a stale answer. Name it: eventual consistency. Given no new changes, all copies converge. Given a constant stream of changes, they are never all identical at any instant, and that is normal rather than broken.
4. **Round two, break the network.** Announce that the runner between A and C is down. Now tell Node A that a customer withdraws 100, and at the same time tell Node C that a customer withdraws 80. Both are legal against the balance each of them can see. Both write it. Neither can tell the other.
5. **Stop and ask the question.** Total balance was 150 and 180 has been withdrawn. Ask the class what the system should have done at the moment the network broke. Let them argue for two minutes. There are only two answers and they should find both:
   - Refuse the withdrawals until the nodes can talk again. The system stays correct and stops being usable.
   - Allow them and sort it out later. The system stays usable and is briefly wrong.
6. **Name it.** That is the CAP tradeoff. When the network partitions, and networks do partition, you must choose between consistency and availability. Write on the board: "you do not get to pick all three, because partitions are not optional, they are weather." Ask which choice a bank should make, and which choice a social media feed should make, and get the class to see that both answers are correct for their own system.
7. **Round three, repair.** Restore the runner and have the nodes reconcile. Ask them how to decide which withdrawal wins. Take their proposals: latest timestamp, lowest node number, ask a human. Then tell them all three are used in real systems, and that the last one is why banks have a fraud department.
8. **Close with quorum in one line.** One common middle path is to require a majority of nodes to agree before a write counts. With three nodes, two must agree. The minority side stops accepting writes and stops being wrong.

### Segment 8: Blockchain and consensus (1:45 to 1:57), Systems strand

1. **Frame the problem before the technology,** which is the only way this topic is worth teaching. Everything so far assumed the three notebook-holders are honest and just badly connected. Now assume one of them lies on purpose, and that there is no boss to appeal to. How does a group of strangers, some of whom are dishonest, agree on one shared history?
2. **Build a paper blockchain, five minutes.** Give six students a pre-ruled page each and line them up.
   - Each page has three parts: the previous page's code, the transactions, and this page's code.
   - Page 1 writes `0000` as the previous code, writes two transactions, then computes its own code with a deliberately silly rule you announce, for example the number of letters written on the page.
   - Each following page copies the previous page's code into its top box, writes its own transactions, and computes its own code the same way.
   - Now tamper: quietly change one transaction on page 2. Recompute page 2's code. It no longer matches what page 3 has recorded as "previous," and neither does anything after it.
   - Land it: each page commits to the entire history before it, so changing anything old requires rewriting everything since. That is the chain in blockchain, and the "code" is a cryptographic hash from Week 28.
3. **Add the consensus half in three sentences.** Everyone holds a copy, so a liar has to convince the majority. Making a new page must be expensive or stake something valuable, or a liar could simply make thousands of pages; proof of work makes it computationally expensive, and proof of stake makes it financially costly to cheat. The longest or heaviest valid chain is what everyone accepts as true.
4. **Be honest about the cost and the fit.** State plainly what a blockchain is genuinely good at: agreement among parties who do not trust each other and have no shared authority. Then state what it costs: it is far slower, far more expensive, and far more energy-hungry than a database, because it is buying the removal of a trusted middleman and nothing else.
5. **Give the diagnostic question and let it sit.** "Would a normal database work here?" If yes, a blockchain is a worse database. Most proposed uses of a blockchain fail that question. Some do not, and reasonable people disagree about which is which; note that Week 30 has the protocol for that kind of argument and this is not the day for it.

### Segment 9: Wrap (1:57 to 2:00)

- **You do:** Point at the abstraction ladder still on the board and say what the whole session was: one long argument about who has to care about what. Hand out homework, noting the Extra Credit AP Track section and that the AP slice this week is small and specific.

## 7. Key scripts and analogies

- **What a server is:** "A computer that is turned on and answering. That is the whole definition. The one in the corner of this room is a server, and the difference between it and Google's is quantity, not category."
- **The cloud:** "It is someone else's computer in a building with very good air conditioning, that you rent by the minute."
- **Virtual machines:** "One physical machine convincingly pretending to be eight, each with its own operating system, each unaware of the others."
- **Containers:** "A virtual machine ships an entire house. A container ships the room you actually use, and borrows the plumbing from the building it lands in."
- **Why containers exist:** "So that 'it works on my machine' becomes a true and useful statement, because your machine is what got shipped."
- **Serverless:** "There is definitely a server. You have just stopped being the person who has to think about it, and you pay by the request instead of by the hour."
- **The ladder:** "Every rung takes away a thing you must manage and a thing you may control. That is the trade, all the way up."
- **CDNs:** "The video did not come from California. It came from a box in a building an hour away that had already been handed a copy, because the speed of light is not negotiable."
- **Parallel speedup:** "Nine people cannot deliver a baby in one month. The part that cannot be split sets the floor, and there is always a part that cannot be split."
- **Replication:** "Three copies means you survive losing one. It also means that for a moment, in the middle of every change, your three copies disagree with each other. That is not a bug, it is the cost of having three."
- **CAP:** "You cannot choose whether the network breaks. You can only choose what you do when it does: be wrong, or be unavailable."
- **Eventual consistency:** "If everyone stops typing, everyone will agree shortly. Nobody stops typing."
- **Blockchain:** "It is a shared history that is expensive to rewrite, run by people who do not trust each other. If the people involved do trust each other, or there is an authority they all accept, a database does the same job for a thousandth of the cost."

## 8. Differentiation

- **Younger or newer students:** The abstraction ladder is the one thing to secure; the rest can be a good story. Give them a printed copy of the ladder with the four rungs and have them fill in the "what you manage" column during Segment 3. In Segment 6, do the first speedup problem with them individually and skip the third. In the Three Notebooks activity, put them in the node roles rather than the analysis role; being the node that could not reach the others is a strong memory.
- **Extensions for advanced or AP-track students:** Have them write a Dockerfile for their Unit 5 Flask app and, if Docker is available, get it running in a container. Have them work an Amdahl-style problem where the non-parallel fraction is given as a percentage rather than as seconds. Have them look up a real cloud provider's regions and availability zones and explain why the region nearest to them is where it is. Point them at the Section 9 cloud and systems extra-credit track, where deploying a project to a free tier is now a realistic weekend.

## 9. Common pitfalls

- **Trying to teach all four topics properly.** You cannot, and attempting it produces four half-topics and no map. The single deliverable is the abstraction ladder plus AP 4.3. Everything else can be a good story told once.
- **The Docker demo consuming fifteen minutes.** Pull the image beforehand or skip the demo entirely. The board version teaches the concept just as well and cannot fail.
- **Containers described as "lightweight virtual machines."** It is the common shorthand and it hides the actual distinction, which is the shared kernel. Say "a container is a process, a virtual machine is a machine" and it stays straight.
- **The speedup with four unequal parallel processes.** Students average the times or add them. The answer is the maximum. Do that problem deliberately and slowly.
- **Speedup assumed to equal the processor count.** Almost every student's first instinct. Problem two in Segment 6 exists to break it; do not skip it.
- **The Three Notebooks activity turning into chaos.** The rule that nothing may be said out loud is what makes it work. Enforce it hard, and have the runner physically walk the cards.
- **CAP taught as a theorem with three choices.** The useful framing is that partitions are not a choice, so the choice is between consistency and availability during a partition. The "pick two of three" phrasing misleads students and they carry it for years.
- **Blockchain generating a cryptocurrency argument.** Redirect once, using the "would a database work here?" question, and hold the actual debate for Week 30 where there is a protocol for it.
- **Blockchain treated as inherently secure.** The chain makes tampering with history detectable. It does nothing about a lost key, a bad contract, or a lie recorded truthfully in the first place.

## 10. Homework

Full details in `handouts/week-29-homework.md`. In summary: three speedup problems; a short written piece placing four described situations on the abstraction ladder; a written answer on what their own final project would need if a thousand people used it at once; a CAP scenario question; and continued project work. The handout closes with an Extra Credit AP Track section carrying this week's AP slice, which is 4.3 and nothing else.

## 11. Assessment

Observational, plus the written homework.

The speedup problems are the only thing this week with a right answer that matters, and they are the only thing worth checking carefully. Mark them properly and reteach the maximum-of-parallel-times case if more than one student misses it, because it recurs on the exam.

For the rest, the check is vocabulary in use rather than recall. During the Three Notebooks activity, listen for whether students describe the disagreement as a bug or as a tradeoff. That distinction is the entire objective of the second half of the session.

The homework's abstraction-ladder question is scored against the weekly-labs rubric. Also use this week to spot-check final-project progress: by the end of Week 29 every student should have a file that runs.

## 12. AP alignment

**Be straight with students about the mapping this week.** Of the four topics covered, exactly one is an AP CSP framework topic: **4.3 Parallel and Distributed Computing**. Cloud infrastructure, containers, serverless, object storage, CDNs, and blockchain are not in the framework and will not appear on the exam. They are in the course because a computing education that cannot explain what "the cloud" is has a hole in it, not because they are tested.

For 4.3 specifically, the exam expects students to be able to: distinguish sequential, parallel, and distributed solutions; calculate speedup as sequential time divided by parallel time; recognize that the parallel portion is limited by the sequential portion; and recognize that adding processors gives diminishing returns. Segment 6 covers all four directly, and that segment is worth more AP points than the other eighty minutes combined.

One secondary connection: **4.2 Fault Tolerance**, covered in Unit 4, is reinforced by the replication and quorum material. Redundancy in the notebook activity is the same idea as redundant routing in the Week 19 packet activity.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, and specifically its distributed and parallel computing material. Work only the parallel and distributed portion. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** there is no cloud or distributed-systems unit, so the fit here is imperfect and worth saying so. The nearest is Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`, whose redundancy and fault-tolerance lessons are the same idea today's replication material rests on. Students who did Unit 2 in the fall should reread the redundancy lessons rather than starting anything new.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The abstraction ladder, the speedup problems, the Three Notebooks activity, and the paper blockchain are all complete in Section 6. Nothing external needs reviewing to run them.
- Docker's own getting-started page, if you run the optional demo: `https://docs.docker.com/get-started/`. Pull the image during prep, not in class.
- The class server and the Unit 5 Flask app are the concrete "one server" baseline for the session. No new setup beyond having both reachable.
- `ping` and `traceroute`, already used in Week 19, for the CDN latency comparison. Nothing to install.
- AP CSP Exam Reference Sheet, `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`, for AP-track students working the speedup problems in pseudocode terms.
- Packet Routing unplugged activity, for the fault-tolerance callback: `teaching-activities/Unplugged-Logic-Activities.md`.
- Crash Course Computer Science has no episode that fits this session. Cloud infrastructure, containers, distributed systems, and blockchain are outside the series, so **no episode is assigned this week and the handout asks for no viewing.** A student who wants the network layer again may re-watch Episodes 28 ("Computer Networks") and 29 ("The Internet") as optional revision, but those were assigned as new work back in Week 19 and are not being set again. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- Cloud and systems extra-credit track, including deploying to a free tier: Section 9 of `curriculum/CS-Curriculum-and-Setup.md`. Note that free tiers usually require a payment method, so keep those parent-managed per Section 12.
- CodeAI CSP Unit 2, The Internet (the nearest AP-track match this week): `https://studio.code.org/courses/csp-2025/units/2`
