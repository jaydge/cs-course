# Week 21 Teacher Guide

## 1. Header

- **Week:** 21 of 32
- **Unit:** 4, Operating Systems and the Internet
- **Theme question:** What happens when you open google.com?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Trace a web request end to end, from the finger on the key to the photons reaching the eye, naming the major stages in order and saying what each one does.
- Identify which layer is responsible for a given step, and say what that layer hides from the layer above it.
- Predict what would fail, and how it would appear to the user, if a named stage stopped working.
- Connect to a remote machine over SSH, run commands there, and say why the first connection asked them to verify a fingerprint.
- Clone a Git repository from the class server and inspect its contents and history.
- Demonstrate the mid-year systems model on the "trace the button press" milestone.
- Demonstrate Unit 4 mastery on the systems concept check.

## 3. Where this sits

This is the pivot point of the course and the most important assessment in the first half of it.

Everything from Week 1 has been building toward one sentence a student can say out loud. Unit 1 gave them programs. Unit 2 gave them the machine and the twelve-stage key-press relay in Week 10, which was explicitly described then as the first half of today's path. Unit 3 gave them enough programming maturity to know what an application actually is. Unit 4 has spent four weeks on the operating system, the shell, the network, and the protocols. Today all of it becomes one continuous story with no gaps in it, and then students are asked to tell that story back.

Section 3 of the curriculum calls the mid-year trace "the single best measure of whether the systems model landed," and pairs it with the end-of-Unit-4 systems concept check as 15 percent of the grade. Treat it that way. Build it carefully, run it unhurried, and use the oral follow-up rather than only the written, because the oral is both a better measure and the course's main defense against work that is not the student's own.

The SSH lab is the practical send-off for Unit 4 and the bridge to Unit 5. It is the first time students touch a machine that is not in front of them. The `git clone` is deliberately a first taste and nothing more: Git is formally taught in Week 23, VS Code arrives in Week 22, and today's clone is there so that when Git is taught properly it is not the first time they have seen the word. Do not teach commits, branches, or pushes today.

## 4. Materials and setup

- The classroom network from Weeks 19 and 20, rebuilt and working: switch, router, cables, everyone connected.
- **The MacBook class server**, powered, plugged into the switch, with Remote Login enabled and the seeded repository in place. Full setup steps are in Section 5.
- The class server's hostname and IP address written on the board.
- Whiteboard, and this is the one week where board space genuinely matters. You need the Week 19 network diagram and the Week 20 four-layer stack still visible, plus a long clear run of board for the trace itself. If you photographed the Week 10 stack board as that guide suggested, print it and pin it up.
- Sticky notes or index cards for the trace build, roughly 30, plus markers.
- Printed mid-year trace assessment sheet, one per student. Contents in Section 11.
- Printed Unit 4 concept check, one per student. Contents in Section 11.
- Printed Week 21 homework handout, one per student.
- A camera or phone to photograph the finished trace board. You will want it for the final project in Weeks 31 and 32.

## 5. Pre-class prep checklist

- **Set up the class server for SSH. Do this several days ahead, not the night before.** (45 min the first time)
  1. On the MacBook acting as the server, log in as an administrator and open System Settings, General, Sharing, and turn on Remote Login. Note the line it displays telling you how to connect, which includes the machine's hostname, typically something ending in `.local`.
  2. Decide on accounts. One account per student is better, because it makes the permissions lesson real and lets you show `who` with several people logged in. A single shared account is acceptable if time is short. Create the accounts as standard, non-admin users with simple passwords you will write on the board; nothing sensitive lives on this machine.
  3. Under Remote Login's settings, confirm which users are allowed to connect and that your student accounts are included.
  4. From your own machine, on the same network, test the connection before class: `ssh studentname@csserver.local`. If the `.local` name does not resolve, use the IP address instead and write that on the board rather than the name.
- **Set the default branch name on the server before you create anything.** Git's own default was `master` for years and is `main` in current versions, but the setting is per machine and an older installation or an inherited config will still say `master`. If the clone in the next step lands on `master` and you then push `main`, the push fails with "src refspec main does not match any" and you will lose ten minutes of prep to it. Set it explicitly:

  ```bash
  git config --global init.defaultBranch main
  git config --global --get init.defaultBranch
  ```
  The second line should print `main`. (2 min)
- **Create and seed the class Git repository on the server.** (20 min)

  ```bash
  mkdir -p /Users/Shared/repos/hello-class.git
  cd /Users/Shared/repos/hello-class.git
  git init --bare -b main
  ```

  Then seed it with something worth cloning:

  ```bash
  cd /tmp
  git clone /Users/Shared/repos/hello-class.git seed
  cd seed
  echo "# Hello from the class server" > README.md
  mkdir puzzles
  echo "print('You cloned this over the network.')" > puzzles/hello.py
  git add .
  git commit -m "Initial class repository"
  git push origin main
  ```

  **If that last line is rejected,** the branch you are standing on is not called `main`. Run `git branch --show-current` to see what it is actually called. If it says `master`, rename it and push again:

  ```bash
  git branch -m master main
  git push origin main
  ```
  If it prints nothing at all, the commit did not happen; check the output of `git commit` before going further.

  Then make sure students can read it:

  ```bash
  chmod -R a+rX /Users/Shared/repos
  ```

  Verify by cloning it from a different machine as a student user before class. Note that `git init -b` also requires a reasonably current Git; if your version rejects the flag, drop it, then use `git branch --show-current` and the rename above to get to `main`.
- **Check the client side on the Windows machines.** The OpenSSH client ships with Windows and also exists in WSL Ubuntu; either works, but Git may need installing inside Ubuntu (`sudo apt install git`). Confirm from a student account that both `ssh` and `git` run. Also confirm whether `.local` names resolve from the Windows machines; often they do not, in which case those students use the IP address. (20 min)
- **Write and print the mid-year trace assessment sheet and the Unit 4 concept check,** using the contents specified in Section 11. Write both answer keys at the same time. This is the largest prep item of the week and it is the one that matters most. (60 min)
- **Read the full expected trace in Section 7 out loud, once, start to finish, before class.** It takes about four minutes. You are going to build it in front of students and you want the ordering automatic. (10 min)
- **Schedule the oral follow-ups.** Decide now when each student's five-minute oral will happen and tell them the times when you hand out the assessment. See the protocol in Section 11. (10 min)
- **Prepare the board.** Rebuild the network diagram and the four-layer stack if they were erased, and clear a long horizontal run for the trace. Have a plan for covering or erasing the trace before Segment 5. (15 min)
- Rebuild the classroom network and print everything. (20 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and framing the day (0:00 to 0:10)

- **You do:** Quick homework check. Ask two students what happened when they tried to reach their home server from a phone, and one to state what TLS does not hide.
- **You do:** Set the day out honestly, because students will be anxious otherwise. Say exactly what is coming: thirty-five minutes building the whole path together, then the SSH lab, then a written trace, then the Unit 4 concept check, and then a five-minute conversation with each of them scheduled over the next week. Say what the assessment is for: not to catch anyone out, but to find out whether the model that has been built since September actually holds together. Say that there is nothing to cram, because it is all a story they have already lived.
- **You do:** Pose the theme question and take the first answer nobody can give properly. Type `google.com` on the projector, press Return, and let the page appear. Then ask: how many distinct things just happened? Take a number from three students. The numbers will be wildly different and all too low. Say that by the end of the next half hour the board will hold the answer.

### Segment 2: Build the whole path (0:10 to 0:45), Systems strand

Do not lecture this. The students supply the stages; you order them, fill the gaps, and hold the pace. The full expected path with the mechanism for each stage is in Section 7, and that is your answer key. Use it to prompt, not to recite.

1. **Set up the board.** Draw a long horizontal line across the whole board. Mark the far left "finger" and the far right "eyes." Say that everything goes in between and that they are going to fill it.
2. **Hand out sticky notes,** three or four per student, and give them four minutes in pairs to write one stage per note, anywhere along the path. Tell them to write the mechanism, not just the name: not "DNS" but "name turns into an address."
3. **Collect and place them, out loud, in rounds.** Take the notes and stick them on the line roughly where they belong, saying each one as you go. Cluster duplicates. Do not correct order yet; just get everything up.
4. **Now walk the line from left to right and fix it as a class,** in five acts. Announce each act as you reach it and draw a vertical divider on the board. The acts are the memory structure students will use in the assessment, so name them clearly.
   - **Act 1, into the machine.** Finger and switch, keyboard matrix, controller and scancode, USB report, host controller and interrupt, driver, OS event queue, focused application. Say: this is Week 10, unchanged. Move through it briskly; they know it.
   - **Act 2, the application decides.** The browser reads the text, works out that it is a hostname rather than a search, builds a URL, and decides it needs a document from another machine. Add the layer underneath: the browser is itself a program made of machine instructions, running through fetch, decode, execute on the CPU, with its data in RAM and the hot parts in cache. This is Unit 2 arriving in the middle of a network story, and that juxtaposition is the point.
   - **Act 3, out to the world.** Cache check, DNS resolution, the ARP lookup for the gateway's hardware address, the packet handed to the network card, the switch, the router, NAT rewriting the source address, the ISP, routers across the internet each making a local decision, arrival at the far side. Then, at the destination, the TCP handshake and the TLS handshake, and only then the HTTP request itself. Point out the ordering fact students find surprising: nothing about the actual page has been asked for yet, and several round trips have already happened.
   - **Act 4, the server side.** The request arrives at a load balancer, which picks one of many machines. A web server takes it. Application code runs, in some language, on some operating system, on some CPU, on a machine in a building somewhere. It probably queries a database. The result is assembled into an HTTP response with a status code and headers and a body. Ask the question that lands the symmetry: how different is that machine from this one? It is not different at all. It is the same story again, on the other end.
   - **Act 5, back and onto the screen.** Response packets return, possibly by a different route, TCP reassembles them in order, TLS decrypts them, the browser parses the HTML, discovers it needs more files and fires off more requests, builds the DOM, computes the layout, paints it, hands it to the GPU to composite, the frame lands in the framebuffer, the display controller scans it out to the panel, pixels change, light travels to the eye.
5. **Count it.** Ask how many stages are on the board. Somewhere over twenty. Compare that to the numbers offered in Segment 1.
6. **Ask the timing question.** All of that, typically in a few hundred milliseconds. Ask which part takes the longest. The answer is usually the network round trips, and specifically waiting: the DNS lookup, the TCP handshake, the TLS handshake, and the time for the response to travel back. Almost none of the time is computation. Say the consequence, which is a genuine professional insight: most of making a website fast is about doing fewer round trips, not about faster code.
7. **Ask the abstraction question, which is the real assessment target.** Walk the line and ask, at three or four points, what the layer above this one had to know about it. Almost nothing, every time. The person who wrote the web page knew nothing about ARP. The person who wrote the browser knew nothing about the keyboard matrix. Write the word abstraction on the board one more time and say that this line is the best picture of it in the whole course.
8. **Then break it, four times, and make them predict.** This is the part that separates memorization from understanding, and the written assessment will ask the same kind of question, so rehearse the move here rather than springing it. Ask each of these and take answers before confirming:
   - DNS is down. What does the user see? A quick failure, an error saying the site cannot be found, and it looks identical to the site not existing.
   - The router in this room loses power. What does the user see? Everything local still works, and nothing outside does.
   - One packet of the response is lost. What does the user see? Almost certainly nothing, because TCP resends it. Perhaps a slight delay.
   - The server's database is down but the web server is up. What does the user see? A page that loads but shows an error, or a partly filled page, which is a very different symptom from the first three and is a genuinely useful diagnostic distinction.
9. **Photograph the board,** then leave it up for the SSH lab and cover or erase it before Segment 5. Tell students you are going to cover it, and why: the written trace is theirs, not the board's.

### Segment 3: SSH into the class server, and clone from it (0:45 to 1:10), Systems strand

Run this from the steps below. The server addresses and the account names should already be on the board.

1. **Frame it in one sentence.** Everything today has been about a request travelling to a machine somewhere else. The class server is a machine somewhere else, sitting on that table, and they are about to get a shell on it.
2. **Connect.** Each student, from their own terminal:

   ```bash
   ssh yourname@csserver.local
   ```
   Use the IP address instead of the name if `.local` does not resolve on your fleet.
3. **Handle the fingerprint prompt properly, because it is a real lesson and not an obstacle.** The first connection prints an unfamiliar message asking whether they are sure, and showing a fingerprint. Stop the room here. Explain what is being asked: the client has never seen this server before and has no way to know whether it is the real one or an impostor sitting in the middle. It is asking the human to vouch for it, once, and it will remember the answer. Point at the padlock conversation from last week: a website solves this same problem with a certificate signed by somebody the browser already trusts, and SSH solves it by asking you and remembering. Two answers to one question. Then have them type `yes`.
4. **Warn them about the password before they type it.** The password prompt shows nothing at all as they type. No dots, no asterisks, nothing. Say this before it happens or half the room will conclude their keyboard has stopped working.
5. **Prove where they are.** Once connected, have them run:

   ```bash
   whoami
   hostname
   uname -a
   pwd
   ls
   ```
   Ask what is different from their own machine. The hostname is not theirs. The home folder is not theirs and is nearly empty. Say the thing that makes it click: their terminal window looks exactly the same as it did five minutes ago, and every character they type is now travelling across the room, being executed on a different computer, and the output is travelling back. Nothing about the window tells them that. Ask what would be a really bad idea to forget, and steer them to the answer: which machine you are actually typing into.
6. **Show that other people are there too.**

   ```bash
   who
   ```
   Every student who is connected appears. Then have them look at each other's presence on one shared machine. If you created per-student accounts, have them try to write into another student's home folder and watch it be refused; that is Week 17's permission model, enforced across a network, and it is the best possible demonstration of why it exists.
7. **Leave properly.**

   ```bash
   exit
   ```
   The prompt changes back. Have them run `hostname` again to confirm they are home. Say the habit out loud: always know which machine your prompt belongs to.
8. **Now clone the repository, from their own machine, not from the server.** Make sure everyone has exited first.

   ```bash
   cd ~/Documents/"CS Class"/sandbox
   git clone yourname@csserver.local:/Users/Shared/repos/hello-class.git
   cd hello-class
   ls
   ```
   The files are there. Say what just happened in one sentence: `git` opened an SSH connection, asked the server for the whole project, and wrote it to their disk.
9. **Look at the history, and stop there.**

   ```bash
   git log --oneline
   ```
   One entry. Say the one sentence about Git that is useful today and no more: it does not just copy files, it copies the whole history of how those files got that way. Then say plainly that Git is Week 23, that today was a first taste so the word is not brand new when it arrives, and that they should not go looking for commit and push yet.
10. **Run the file they cloned,** because it is satisfying:

    ```bash
    python3 puzzles/hello.py
    ```
11. **Close with the connection back to Segment 2.** Ask which parts of the morning's trace were involved in the clone they just did. Nearly all of Act 3 and Act 4, with SSH in place of HTTPS and a git process in place of a web server. The story generalizes, which is the whole reason for learning it as a story.

### Segment 4: Stretch (1:10 to 1:15)

Cover or erase the trace board during the break, in front of them, as you said you would.

### Segment 5: Mid-year milestone, the written trace (1:15 to 1:40)

- **You do:** Hand out the trace sheet. Say the framing one more time, briefly: this is the assessment the whole first half of the course was pointing at, it is worth real weight, and it is also a conversation, so anything they cannot get onto paper they will have a chance to say out loud in their scheduled oral.
- **You do:** State the ground rules. Twenty-five minutes, individually, no laptops, no notes, board covered. Names on the sheet.
- **You do:** Tell them how it is scored, because knowing the rubric is not cheating and it makes for better answers. Say the four things you are looking for: the major stages present, in a sensible order, with a few words on what each one actually does, and correct answers to the "what breaks" questions at the end. Say explicitly that naming twenty stages with no mechanism scores worse than naming twelve stages and saying what each one does.
- **Students do:** Write.
- **You do:** Circulate quietly. Do not answer content questions. Do note who stalls and where; that tells you what to probe in the oral.

### Segment 6: Unit 4 concept check (1:40 to 1:55)

- **Students do:** Complete the concept check individually, no laptops, about fifteen minutes. Contents in Section 11.
- **You do:** Collect both papers together. Hand out the homework as students finish, and hand each student a slip with their scheduled oral time on it.

### Segment 7: Wrap and close of Unit 4 (1:55 to 2:00)

- **You do:** Uncover the trace board. Let them look at it once more now that they have written their own version.
- **You do:** Close the unit and the half-year deliberately. Point along the line and name what they can now do that they could not in September: they can say what is inside the computer, what the operating system is for, what happens in a terminal, how a message finds one machine out of billions, what protocols are, and what encryption does and does not hide. Say that the second half of the course builds things on top of this instead of opening things up: VS Code and real project structure next week, Git the week after, then the web, then APIs, then AI.
- **You do:** Photograph the board again if it changed.

## 7. Key scripts and analogies

### The full expected trace, which is your answer key

Twenty-two stages in five acts. A student is not expected to produce all of these. Section 11 defines what is expected at each score band.

**Act 1, into the machine.**

1. The finger closes a physical switch under the key. It is the same kind of switch they wired on a breadboard in Week 6.
2. The keyboard's matrix registers which row and column closed, and the controller debounces it and emits a scancode, which is a position, not a letter.
3. The scancode is packaged into a USB report and sent to the computer when the host asks for it.
4. The host controller receives it and raises an interrupt. The CPU stops what it was doing.
5. The OS runs the keyboard driver, translates the scancode into a character using the current layout, and puts an event on a queue.
6. The OS delivers the event to the window that has focus, which is the browser.

**Act 2, the application decides, and the machine underneath it.**

7. The browser accumulates the typed characters, and on Return decides this is a hostname and builds a URL from it.
8. The browser is itself a program: machine instructions being fetched, decoded, and executed by the CPU, with its data in RAM and the hot parts in cache. Every stage in this whole trace is happening as machine instructions somewhere.
9. The browser checks its own cache and the OS cache to see whether it already knows the address, and whether it already has the page.

**Act 3, out to the world.**

10. DNS: if the address is not cached, the machine asks its resolver, which asks a root server, then a `.com` server, then the authoritative server for the domain, and gets back an IP address. Caching means most of this is usually skipped.
11. The OS decides whether the destination is on the local network. It is not, so the packet goes to the default gateway.
12. ARP: the machine needs the gateway's hardware address to put a frame on the wire, so it asks the local network who has that IP, and remembers the answer.
13. The network card turns the frame into electrical or optical signals on the wire.
14. The switch forwards the frame to the port the router is on. The router receives the packet, decrements its time-to-live, consults its routing table, and forwards it onward.
15. NAT: the router rewrites the source address to its own public address and records the translation so it can reverse it for the reply.
16. The packet crosses the ISP and then many independent routers, each making a purely local decision, until it reaches the destination network.
17. TCP: a three-way handshake establishes a connection with the server, so that both sides know the other is there and agree on numbering.
18. TLS: a second handshake, in which the server presents a certificate, the browser verifies it against an authority it already trusts, and the two agree on a shared secret key.
19. HTTP: only now does the browser send the actual request, a few lines of text saying which path it wants, encrypted inside the TLS session.

**Act 4, the server side.**

20. A load balancer receives the request and hands it to one of many identical servers. A web server process takes it. Application code runs, probably queries a database over its own network connection, and gets rows back. A response is assembled: a status code, headers, and a body of HTML. All of this is the same story again on a machine in a different building.

**Act 5, back and onto the screen.**

21. The response is split into packets and travels back, possibly by a different route. TCP reassembles them in order and requests any that went missing. TLS decrypts. The browser parses the HTML, discovers it needs stylesheets, scripts, and images, and issues more requests for each. It builds the DOM, computes layout, and paints.
22. The GPU composites the finished frame into the framebuffer. The display controller scans it out to the panel. Pixels change state, emit light, and the light reaches the eye. Total elapsed time, typically a few hundred milliseconds, most of it spent waiting for round trips rather than computing.

### Analogies and lines worth having ready

- **The whole trace:** "Twenty-plus stages, several thousand packets, machines on two continents, run by organizations that have never spoken to each other, and it happens in less time than it takes you to blink."
- **On the ordering surprise:** "Notice that nothing about the actual page has been asked for yet, and we are already four round trips in. The waiting is most of the internet."
- **On the server:** "That machine is not special. It has an operating system, a CPU, memory, and a network card, and something is running a program on it. It is this room's story, told again, four hundred miles away."
- **On abstraction, one last time:** "Point at any stage on this line and ask what the stage above it had to know about it. The answer is almost always nothing. That is why any of this can be built by people who will never meet."
- **On SSH:** "Your terminal window looks exactly the same as it did a minute ago and every key you press is now going to a different computer. Always know which machine you are typing into."
- **On the fingerprint prompt:** "The client has never met this server and has no way to be sure it is the real one, so it asks you, once, and then remembers. A website solves the same problem with a certificate signed by someone the browser already trusts. Two answers to one question."
- **On what breaks:** "A site that will not resolve looks exactly like a site that does not exist. A server that is up with a broken database looks like a page that loads and then apologizes. Learning to tell those apart from the symptom is real diagnostic skill."

## 8. Differentiation

- **Younger or newer students:** The trace is a story, and stories are the easiest thing in this unit for a newer student to hold. Give them the five act names in advance, on paper, and tell them that getting all five acts in the right order with two or three stages in each is a genuinely good result. Say that out loud to them individually before the assessment, because the anxiety is the thing most likely to hurt their performance. In the oral, ask them to tell it as a story rather than as a list, and prompt with "and then what?" rather than with terminology. In the SSH lab, pair them, and give them the exact command written down; the fingerprint prompt and the invisible password are the two places they will stall.
- **Extensions for advanced or AP-track students:** In Segment 2, have them add the stages nobody mentioned: TCP slow start, HTTP redirects, the browser's preload scanner, or the fact that a modern browser opens several connections at once. In the assessment, the "what breaks" questions are where they show depth, so tell them to spend their extra time there rather than adding more stage names. In the SSH lab, have them try `scp` to copy a file up to the server, look at `~/.ssh/known_hosts` to find the fingerprint their machine recorded, or run `git log --stat` and work out what it is showing. The strongest can be asked, in the oral, the question that separates the top band: what does each layer hide, and name one thing that changed at a lower layer during their lifetime without anything above it noticing.

## 9. Common pitfalls

- **Turning Segment 2 into a lecture.** It is the most tempting session of the year to just tell, because you know the story and it is a good one. Do not. Students who watched a trace being narrated cannot reproduce it; students who supplied the sticky notes can. If you are talking for more than ninety seconds at a stretch, hand it back.
- **The board becoming the answer key for the assessment.** Cover or erase it, in front of them, and say why. The Section 11 written prompt also includes probe questions that cannot be copied from a board, which is deliberate.
- **Assessment anxiety.** This one is bigger than the unit checkpoints and students will feel it. The mitigations that work: tell them the format a week ahead, which the Week 20 handout does; tell them the rubric before they start; and tell them the oral exists as a second chance to show what they know, not as a second hurdle.
- **Running out of time for the concept check.** Segment 2 will expand. Hard stop it at 0:45 and hard start the written trace at 1:15 whatever else is happening. If something must be cut, cut the last part of the SSH lab, not the assessments.
- **The class server not being reachable.** The single most likely technical failure. Test it from a student account, on the classroom network, before class. Have the IP address as a fallback for the hostname, and have a plan to run the lab as a demonstration on the projector if the network misbehaves.
- **The invisible password.** Say it before they type. Otherwise half the room will report a broken keyboard within thirty seconds of each other.
- **Students left logged into the server.** Someone will forget to `exit`, then run a destructive command believing they are on their own machine. Make step 7 mandatory and make `hostname` the habit.
- **Git scope creep.** Somebody will ask about committing and pushing. Answer honestly that it is Week 23, that it is a genuinely good question, and that doing it badly today would make the real lesson harder. Hold the line.
- **Treating the milestone as a memory test.** If your marking rewards the longest list of stage names, students will learn to produce lists. The rubric in Section 11 weights mechanism and the "what breaks" reasoning above coverage for exactly this reason. Mark it that way.
- **Skipping the orals because the week is busy.** They are the most informative twenty-five minutes you will spend all term, and they are the AI-policy enforcement mechanism the curriculum's Section 10 describes. Schedule them before you hand out the assessment, not after.

## 10. Homework

Full details in `handouts/week-21-homework.md`. It is deliberately light, because two assessments happened in class and the orals are still to come. In summary: prepare for the oral by telling the trace out loud to somebody at home and writing down the two stages that were hardest to explain; one short written comparison of the SSH fingerprint prompt and the browser padlock; explore the cloned repository and answer three questions about it; a half-year reflection naming three things they can now explain that they could not in September; the optional Crash Course episode on the World Wide Web. The handout closes with an Extra Credit AP Track section that finishes the CodeAI internet unit and includes a Big Idea 4 self-audit.

## 11. Assessment

This is the heaviest assessment session of the first half of the course, and it has three parts: the written trace, the oral trace, and the Unit 4 concept check.

### A note on grading buckets, worth resolving before you mark anything

Section 3 of the curriculum assigns 15 percent jointly to "the mid-year trace the button press (oral or written) and an end-of-Unit-4 systems concept check," and separately assigns 20 percent to six unit checkpoints. Unit 4's checkpoint and the end-of-Unit-4 systems concept check are the same instrument in practice. Decide which bucket it counts in and do not count it in both. The recommendation here: score the trace, written and oral combined, as the mid-year milestone, and score the concept check as Unit 4's entry in the unit-checkpoint slice. Adjust the 15 percent to reflect the trace alone if you take that route, and note the decision in your gradebook so next year's version is consistent.

### Part 1: the written trace (in class, Segment 5, 25 minutes)

The sheet has two parts and both are required.

**Part A, the trace.** One prompt, stated plainly: "You press Return on the address bar with google.com typed in it, and a moment later the page is on your screen. Describe everything that happens, in order, from your finger to your eyes. For each stage, say briefly what it does, not just its name. You will not remember everything, and you are not expected to. Depth on the stages you do name is worth more than a longer list of names." Give a page and a half of space and a note that a numbered list is fine and a diagram is welcome.

**Part B, four probe questions.** These cannot be answered from memorized order and they are where the top band is decided. Use these four or write your own in the same shape:

1. Name two things that happen before the browser sends the actual request for the page, and say why each is necessary.
2. Your friend's page will not load and the error says the site cannot be found. Name the most likely stage that failed and say how you would test your guess with one command.
3. One packet of the response is lost on the way back. What does the user see, and what makes that so?
4. Pick any one stage on your trace. Say what the stage immediately above it has to know about how it works, and what that tells you about why large systems can be built by people who never meet.

### Part 2: the oral trace (5 minutes per student, scheduled)

**Why it is separate.** It is a better measure than the written for most students at this age, it is the course's main check that the understanding is the student's own, and it lets you probe exactly where the written was thin. It cannot fit inside the session, so schedule it: five minutes per student in the week following, in your optional catch-up slot, before or after the Week 22 session, or by appointment. Give each student their slot on a slip when you collect the written sheet.

**Protocol, and keep to it so students are assessed on the same thing.**

1. Open the same way for every student: "Tell me what happens when you open google.com. Start at your finger and end at your eyes. Take your time, and it is fine to say you are not sure."
2. Do not interrupt for the first two minutes, even for a wrong ordering. Note it and come back.
3. When they finish or stall, ask exactly two probes chosen from the bank below, picked to target where their written sheet was weakest.
4. Close with the same question for every student: "Which part of that are you least sure about?" Honest self-assessment is a real signal and the answers are consistently useful for planning Unit 5.
5. Take notes during, not after. Score within the hour.

**Probe bank.** Pick two.

- What is the difference between the address and the name, and who translates one into the other?
- What is a packet, and why not just send the whole thing at once?
- Where in your trace does encryption start, and what exactly is hidden after that point?
- You said the router forwards it. How does the router know where to forward it to?
- Which parts of what you described are also happening on the server's machine?
- What is the slowest part of the whole thing, and why?
- If I unplugged this room's router right now, which parts of your trace would still work?
- Name one stage where the layer above had no idea what the layer below was doing.

### The rubric, for the trace (written and oral together)

Five dimensions, scored 0 to 4 each, for 20 points. Score the written and the oral against the same rubric and take the higher of the two per dimension, since the two formats favor different students and the goal is to find out what the student understands rather than which format suits them.

| Dimension | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|
| **Coverage** | All five acts present with several stages in each; nothing major missing | All five acts present, some thin | Three or four acts; a whole phase missing, usually the server side or the display end | One or two acts; mostly the parts most recently taught | Nothing usable |
| **Ordering** | Correct throughout, including the non-obvious ordering of DNS, TCP, TLS, then HTTP | Correct overall with one or two local slips | Broadly right shape, several stages out of place | Sequence largely arbitrary | No discernible order |
| **Mechanism** | Says what each stage does and why, in their own words, not memorized phrasing | Mechanism given for most stages | Mechanism for some; several stages are bare names | Names only | None |
| **Layers and abstraction** | Identifies layer boundaries unprompted and can say what a layer hides and why that matters | Identifies boundaries when asked | Vague sense that there are layers | No layer awareness | None |
| **Probes and repair** | Answers both probes correctly, and self-corrects earlier errors when they notice them | Answers one fully and one partly; accepts correction and builds on it | Answers thinly; needs substantial prompting | Cannot engage with the probes | Not attempted |

**Bands.** 18 to 20, the model landed completely. 14 to 17, solid; the systems story holds with gaps at the edges. 10 to 13, the shape is there and the middle is thin; give this student the trace to redo as an extra-credit written piece and re-check in Week 26. 6 to 9, significant gaps; sit down with them individually before Unit 5 gets going, because Weeks 24 and 25 assume this. Below 6, the model did not land, and the right response is a conversation with the student and the parent rather than a grade.

**A floor worth naming.** A trace that includes all of these eight, in order, with mechanism, is a 3 on coverage and ordering at minimum: key press, the OS delivers it to the browser, name turns into an address, the request travels through the local network and out through the router, it crosses the internet by hops, a server processes it and answers, the response comes back and is reassembled, the browser draws it and the screen changes.

### Part 3: the Unit 4 concept check (in class, Segment 6, 15 minutes)

Six areas, short answers, no laptops.

1. **Operating systems.** What is a process, in one sentence, and what is one difference between a process and a thread? One question on why one program cannot read another's memory.
2. **Files and permissions.** Given a line of `ls -l` output, say who may read it and who may change it. Give the command that moves you to the parent directory.
3. **The shell.** Say in one sentence what the `|` character does. Given a goal such as "count the lines in a file that mention the word error," write the one-line pipeline.
4. **Networking vocabulary.** Match five terms to five definitions: IP address, MAC address, DNS, DHCP, NAT. Then one short answer on the difference between a switch and a router.
5. **Protocols.** One question on what TCP guarantees that UDP does not, and one situation where UDP is the better choice. One question giving three status codes to interpret. One short answer naming one thing TLS hides and one thing it does not.
6. **Ordering.** Eight scrambled stages of a page load, to be put in order. Use a short version of the Section 7 path, and choose stages that are not simply the first eight, so that it is not a subset of the trace sheet.

Score against the unit-checkpoint component. Read it diagnostically too: weakness in areas 1 through 3 predicts trouble with VS Code and Git in Weeks 22 and 23, and weakness in 4 and 5 predicts trouble with APIs in Week 25.

## 12. AP alignment

This session consolidates **AP CSP topic 4.1 The Internet** and **topic 4.2 Fault Tolerance**, and it is the best AP session of Unit 4 in one specific respect: the exam's Big Idea 4 questions are overwhelmingly about how the pieces relate rather than about any single piece, and the trace is precisely a test of how the pieces relate. The "what breaks" probes are the same reasoning the exam asks for when it presents a scenario and asks what the consequence of a failure would be.

The concept check's networking and protocol sections are 4.1 and 4.2 directly. The operating system, shell, and permissions sections are not AP content, as Weeks 17 and 18 said plainly; they are in the concept check because they are in our course, not because they are on the exam.

Two clarifications so nobody over-claims. **Topic 4.3, Parallel and Distributed Computing, is not covered in Unit 4.** It is Week 29. And the TLS and certificate material connects to **topic 5.6 Safe Computing**, which is properly covered in Week 28, not here.

With Week 21 complete, Big Idea 4 is fully covered by the base course. That is worth telling AP-track students, because it is the first big idea to be finished and it is a real milestone.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies. Finish the internet portion of the unit, the lessons tying the pieces together into how the web works end to end. Then stop and leave the cybersecurity lessons for our Week 28. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`. Finish the unit. Three weeks of our course have mapped onto this one unit, so a student who has been following along should be able to complete it now, and completing it means Big Idea 4 is genuinely covered from both sides.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The trace build, the assessment, and the rubric: Segments 2 and 5 and Section 11 are complete on their own. **Read the Section 7 trace aloud once during prep**; it is the one thing in this guide that you need at your fingertips rather than on the page.
- The SSH and clone lab: Segment 3 is complete on its own, provided the Section 5 server setup is done in advance. The one model-specific thing to confirm is where Remote Login lives in your macOS version's System Settings, since Apple reorganizes that pane regularly.
- Apple's documentation on Remote Login and SSH access to a Mac, worth checking against your current macOS version during prep: `https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac`
- Git documentation for `git clone` and `git init --bare`, for your reference while setting up the server repository: `https://git-scm.com/docs`
- Crash Course Computer Science, Episode 30 ("The World Wide Web"), optional homework viewing and the last new episode of the unit. It draws the internet-versus-web distinction the AP exam tests, which is exactly the distinction the trace makes concrete. Episodes 28 and 29 were assigned in Weeks 19 and 20; a student preparing for the oral may find them useful again, but say plainly that those are a re-watch and not new work. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Unit 2, The Internet (AP-track reinforcement, completed this week): `https://studio.code.org/courses/csp-2025/units/2`
- The mid-year milestone definition and the grading weights discussed in Section 11: Section 3 of `curriculum/CS-Curriculum-and-Setup.md`.
- The AI-use policy and the "explain your work" enforcement mechanism the oral implements: Section 10 of `curriculum/CS-Curriculum-and-Setup.md`.
- The first half of today's path, taught as the human relay in Week 10: `lessons/week-10-teacher-guide.md`, Segment 3. If you photographed that board, pin the photo up today.
- AP topics 4.1 and 4.2, now complete: `ap-track/AP-CSP-Topic-Coverage.md`.
