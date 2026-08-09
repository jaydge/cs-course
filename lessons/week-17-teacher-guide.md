# Week 17 Teacher Guide

## 1. Header

- **Week:** 17 of 32
- **Unit:** 4, Operating Systems and the Internet
- **Theme question:** Who is actually in charge of the computer?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Define a process, say what makes a thread different from a process, and find both on their own machine.
- Explain in plain language why every process believes it has the whole memory to itself, and connect that to the swapping idea from Week 16.
- Open a terminal on their own machine, whether macOS zsh or WSL Ubuntu, and navigate the filesystem with `pwd`, `ls`, and `cd`.
- Point at the same folder in three places at once: a graphical file browser, a terminal, and a path written as text.
- Read the owner, group, and permission bits from one line of `ls -l` output and say who may read, write, and execute that file.
- Write a short Python program that lists the contents of a directory using `pathlib`.
- Say in one sentence why macOS and Linux feel similar in the terminal and Windows does not.

## 3. Where this sits

Unit 4 opens here and the systems narrative resumes after six weeks of almost continuous coding. Unit 2 ended at the hardware boundary: transistors, the CPU, memory, and the key-press path. Unit 3 lived entirely inside Thonny. This week is the layer between them, the operating system, and it is the week students leave the editor for the first time.

The terminal is the single biggest difficulty spike in the first half of the course. The readiness guide flags it explicitly, alongside the networking acronyms coming in Week 19, as the two places a newer student is most likely to feel lost. Nothing about it is conceptually hard; it is unforgiving about spelling and it has no buttons, and those two things together are what make it intimidating. Plan accordingly: everything typed this week is typed slowly, on the projector first, and every student leaves with a printed command reference.

Week 18 lives entirely in the shell and adds pipes, searching, and scripts. Weeks 19 through 21 build the network on top of these same commands. If a student cannot get to a prompt and run `ls` today, they will be lost for four weeks, so protect Segment 3.

## 4. Materials and setup

- Every student laptop charged and logged in, with the terminal reachable. On Macs that is Terminal in Applications, Utilities. On the Windows machines that is Windows Terminal with the Ubuntu profile, which requires WSL2 to have been installed and initialized already (see Section 5).
- Printed command reference card, one per student, double sided. Contents are listed in Section 5; hand-writing it once and photocopying is fine.
- Projector, with the demo machine's terminal font size raised to something readable from the back of the room. Do this before students arrive, not during Segment 3.
- A second machine of the other kind on or near the projector if you can manage it, so macOS and Ubuntu can be seen literally side by side. If you only have one projector, a Mac showing Terminal in one window and a WSL Ubuntu shell in another window works nearly as well.
- Whiteboard with the theme question written large, plus space for a filesystem tree that stays up all session.
- Printed Week 17 homework handout, one per student.
- Optional: eight index cards labeled with process names for the unplugged scheduler in Segment 2.

## 5. Pre-class prep checklist

- **Verify WSL2 and Ubuntu actually work on every Windows machine, from the student account, not yours.** This is the item most likely to sink the session. Open Windows Terminal, choose the Ubuntu profile, and confirm you reach a `$` prompt without a first-run setup wizard. If Ubuntu has never been launched it will ask for a new UNIX username and password on first run, which eats ten minutes per machine; do that during prep. (20 min, more the first time)
- On each Mac, open Terminal once from the student account and confirm a `%` prompt appears. Raise the profile font size on the demo machine. (10 min)
- Give every machine the same starting point inside the folder students have already used since Week 1, the `CS Class` folder in Documents. Add three empty files and one subfolder so there is something worth listing. You can do this from the terminal in ten seconds per machine:

  ```bash
  mkdir -p ~/Documents/"CS Class"/notes
  cd ~/Documents/"CS Class"
  touch alpha.txt beta.txt gamma.txt
  ```
  Note the quotation marks. `CS Class` has a space in it, and without them the shell reads it as two separate arguments. Segment 3 teaches that explicitly, so type it the same way here. Do not invent a separate practice folder; the point of Segment 5 is that the folder they already know and the path the terminal prints are the same thing. (10 min)
- **Write the command reference card and print it.** Keep it to one page, two columns: `pwd`, `ls`, `ls -l`, `ls -la`, `cd <folder>`, `cd ..`, `cd ~`, `cd -`, `mkdir`, `touch`, `cat`, `clear`, `whoami`, `open .` (macOS) and `explorer.exe .` (WSL), plus the four navigation facts: Tab completes, Up-arrow recalls, Control-C stops, and `~` means your home folder. Add a line saying that the shell is case sensitive and that spaces in filenames need quotes. (20 min)
- Run the Segment 6 Python program on the classroom Python and confirm the output. Check whether Thonny on your machines is using the same Python you get from `python3` in the terminal; if they differ, say so out loud in class rather than letting a student discover it alone. (10 min)
- Decide pairings. Pair any student flagged on the readiness diagnostic with a confident typist for Segment 3. (5 min)
- Print homework handouts and command cards. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Collect the Unit 3 checkpoints from anyone who finished at home, and take a show of hands on the text adventures that reached the definition of done. Follow up individually with anyone who did not.
- **You do:** Pose the theme question by asking a smaller one first: you have written maybe twenty programs this year, and not one of them asked permission to use the screen, the keyboard, or memory. Who gave them those things? Take answers. Somebody will say the operating system; ask them what that actually is.
- **You do:** Set the shape of the day out loud: what the OS does, then the terminal on both platforms, then permissions, then a little Python, then one mystery.
- **Purpose:** Names the layer the whole unit is about, and makes clear that today's answer was invisible all year.

### Segment 2: What an operating system actually does (0:10 to 0:30), Systems strand

Run this from the steps below. It is short and mostly physical.

1. **Human scheduler, three minutes.** Bring one volunteer to the front as the CPU. Hand four other students an index card each with a process name on it: `browser`, `music`, `thonny`, `backup`. Tell the CPU it may work with exactly one card at a time. Then tell it the rule: every two seconds, put the current card down and pick up a different one. Run it for twenty seconds while the class watches.
2. **Ask the question that lands it.** From the outside, how many of these looked like they were running? All four. How many were actually running at any instant? One. Name it: the operating system's scheduler switches between processes fast enough that they appear simultaneous. Then add the honest correction, since students met multi-core CPUs in Week 8: a real machine has several cores, so a handful genuinely run at once, but there are always far more processes than cores, so the switching is still what makes it work.
3. **Define a process, then a thread.** A process is a running program with its own memory, its own open files, and its own identity number. A thread is one line of execution inside a process, and several threads in one process share that process's memory. Use the analogy in Section 7. Do not go further than this; threads return properly in Week 29.
4. **Show it on a real machine.** On the demo Mac, open Activity Monitor (Applications, Utilities). Sort by CPU. Count the processes; there will be several hundred. Ask how many of those the student started. Almost none. Then show the same thing in the terminal so they see that the graphical tool is just a face on the same data:

   ```bash
   ps aux | head -20
   ```
   Point at the PID column and name it. On Windows, the equivalents are Task Manager's Details tab and, inside WSL Ubuntu, the same `ps aux`.
5. **Memory, in ninety seconds.** Every process is handed what looks like a private, complete range of memory addresses, and the OS plus the memory-management hardware quietly maps those onto the real RAM chips from Week 8. Two consequences worth stating: one process cannot read another's memory by accident, which is a security feature, and when the real RAM runs out the OS starts parking pages on the SSD, which is exactly the swapping that made the old laptop feel stuck in Week 16's Mystery Day.
6. **Files and permissions, as a promise.** The OS is also the only thing that actually touches the disk. Your program never writes to a platter or a flash cell; it asks the OS, and the OS decides whether you are allowed. Hold that thought; Segment 5 is where they see the decision being made.

**Purpose:** Four abstractions (process, thread, memory, file) get named with a physical referent for each, before any of them appear as terminal output.

### Segment 3: Two terminals, side by side (0:30 to 1:00), Systems strand

This is the protected segment of the day. Go slowly and let nobody fall behind.

1. **Open a terminal on the projector and say what you are looking at.** The prompt is the shell waiting for you. Point at the parts: the machine name, the current folder, and the symbol at the end. Say plainly that macOS ends the prompt with `%` because its shell is zsh, and Ubuntu ends it with `$` because its shell is bash, and that this difference will not matter to anything you do this year.
2. **Hand out the command cards now,** before the first command, so nobody is trying to memorize.
3. **Type three commands, one at a time, with the class typing along.** Wait for every hand to go up after each before moving on.

   ```bash
   pwd
   ls
   whoami
   ```
   Read the `pwd` output aloud slowly, one slash at a time: `/Users/student` on macOS, `/home/student` on Ubuntu. Say what a path is: a set of directions from the top of the filesystem down to one place, with the slashes as the turns.
4. **Draw the tree on the board and leave it up.** Root at the top as a single `/`. Under it, `Users` on macOS or `home` on Ubuntu, then the student's own folder, then `Documents`, then `CS Class`, then `notes`. Mark the student's home folder with `~` and say the shorthand out loud: the tilde means "my home folder," and it saves typing every time. Point at `CS Class` on the tree and say, without dwelling on it yet, that this is the folder they have been saving work into since Week 1; Segment 5 comes back to it properly.
5. **Navigate the tree physically.** Have students run these in order, checking the tree on the board after each:

   ```bash
   cd ~/Documents/"CS Class"
   pwd
   ls
   cd notes
   pwd
   cd ..
   pwd
   cd ~
   pwd
   ```
   Say the two navigation words as they use them: `..` is the folder above this one, `~` is home. Then say the third thing, because it is the first place the shell's literalness bites: `CS Class` has a space in it, so it goes inside quotation marks. Without them the shell reads the space as a separator, sees two arguments, and tries to enter a folder called `CS`. The quotes are how you tell the shell that a space is part of a name rather than a gap between things.
6. **Teach Tab completion right now, not later.** Have them type `cd ~/Documents/CS` and press Tab. It finishes the name and handles the space for them. Say why this matters more than it looks: it is the cure for the number one terminal frustration, which is typos in long names, and it also proves the thing exists before you press Return. Then teach Up-arrow to recall the last command and Control-C to abandon whatever is running.
7. **Show `ls` with flags and name the grammar.** Run `ls`, then `ls -l`, then `ls -la` in the CS Class folder. Say the general shape of every command they will meet this year: the command name, then options starting with a dash, then the things to act on. Point out that `-la` is just `-l` and `-a` written together, and that `-a` reveals the dotfiles the graphical browser hides.
8. **Split the room for five minutes.** Mac students and Windows students each run steps 3 through 7 on their own machine, then physically walk over and look at a machine of the other kind. Ask them to find one thing that is different. Answers: the prompt symbol, `/Users` versus `/home`, and the color scheme. That is nearly the whole list, and that is the point.
9. **Show the one WSL fact Windows students need.** From inside Ubuntu, the Windows C: drive is mounted at `/mnt/c`. Have them run:

   ```bash
   ls /mnt/c/Users
   ```
   Say what this means: WSL2 is a real Linux running alongside Windows, and `/mnt/c` is the door between the two filesystems. Tell them to keep their coursework in the Linux home folder, not on `/mnt/c`, because file access across that door is slow.

**Purpose:** Every student reaches a prompt and moves around the filesystem on purpose. Nothing else this week matters if this does not happen.

### Segment 4: Stretch (1:00 to 1:05)

### Segment 5: One folder, three views, and who is allowed (1:05 to 1:25), Systems strand

1. **Name the folder they already have, in terminal terms.** Do this before opening anything. Say it plainly: the `CS Class` folder they have been saving work into since Week 1 is the folder the terminal calls `~/Documents/CS Class`. Not a copy of it, not a second folder that looks like it. Finder shows it as an icon with a name; the terminal shows it as a path; there is one folder on the disk. Have them prove it themselves rather than take it from you:

   ```bash
   cd ~/Documents/"CS Class"
   ls
   ```
   Their own work from earlier in the year is listed. Give it a beat. For most students this is the moment the terminal stops being a strange new place and becomes a second window onto a familiar one, which is the whole argument of this segment.
2. **Put the same folder on screen twice.** With the terminal still in `~/Documents/"CS Class"`, run:

   ```bash
   open .
   ```
   A Finder window opens on exactly that folder. Windows students run `explorer.exe .` from Ubuntu and get File Explorer. Arrange the two windows side by side and say the sentence out loud: this is not two folders, it is one folder and two windows onto it.
3. **Prove it in both directions.** Create a file in the terminal with `touch delta.txt` and watch it appear in the graphical window without anyone clicking refresh. Then create a folder in the graphical window and run `ls` in the terminal.
4. **Show the path in the graphical tool.** On macOS, View, Show Path Bar puts the same path along the bottom of the Finder window. On Windows, File Explorer's address bar shows it if you click into it. Say the honest thing: the graphical browser has been hiding the path from you on purpose, because most people do not want it, and from now on you do.
5. **Teach the drag trick, which students love.** Drag any folder from Finder onto a Terminal window and its full path is typed for you. Drag the CS Class folder specifically, and point out that Finder puts in the escaping for the space without being asked. This is the fastest way out of a "where am I" problem all year.
6. **Now permissions.** Run `ls -l` in the CS Class folder and put one line on the board, character by character:

   ```
   -rw-r--r--  1 student  staff  0  Jan  5 10:00  alpha.txt
   ```
   Read it left to right. The first character is the type: a dash for an ordinary file, a `d` for a directory. Then three groups of three: what the owner may do, what the group may do, and what everyone else may do. In each group, `r` is read, `w` is write, `x` is execute, and a dash means not allowed. Then the owner name and the group name.
7. **Make them predict, then check.** Ask what `-rw-r--r--` means for a classmate on the same machine. Answer: they can read it and cannot change it. Then run `ls -ld ~` and ask why a directory needs an `x` bit at all. Answer: on a directory, execute means "you may enter it," which is a genuinely surprising and memorable detail.
8. **Change one and watch it change.** In the CS Class folder:

   ```bash
   chmod 600 alpha.txt
   ls -l alpha.txt
   ```
   Then put it back with `chmod 644 alpha.txt`. Explain the three digits as owner, group, other, with read worth 4, write worth 2, and execute worth 1. Two numbers cover almost everything: 644 for a normal file, 755 for something runnable. Week 18 needs 755 for their script, so this is not trivia.
9. **Connect it to their own laptop, honestly.** Their student account is deliberately a standard, non-admin account. That is the same permission system, one level up. Ask what `sudo` does and answer it plainly: it asks the OS to run one command as the administrator, and it asks for a password because otherwise the whole system would be pointless. Tell them they will not need `sudo` in this course except where a lab explicitly says so, and that a stranger telling them to paste a `sudo` command they do not understand is one of the oldest attacks there is.

### Segment 6: Files and paths in Python (1:25 to 1:45), Coding strand

- **You do:** Make the connection first. They just learned that a path is text. Python treats it as text too, and the standard library has a small module for handling it properly.
- **You do:** Build this at the projector, running after each addition:

  ```python
  from pathlib import Path

  folder = Path.home() / "Documents" / "CS Class"
  print(folder)

  for item in folder.iterdir():
      print(item.name)
  ```
  Name the two new ideas: `Path.home()` is the same thing as `~`, and the slash operator joins path pieces without you having to worry about whether the separator is `/` or `\`. Say why that matters: this exact program runs unchanged on both fleets, which is the whole reason `pathlib` exists. Point at `"CS Class"` and note the contrast worth ten seconds: the space needs no quoting trick here, because it is already inside a Python string. Quoting in the shell and quoting in Python are solving the same problem in two different places.
- **You do:** Add the parts that make it useful:

  ```python
  for item in sorted(folder.iterdir()):
      if item.is_dir():
          kind = "dir "
      else:
          kind = "file"
      print(kind, item.name, item.stat().st_size)
  ```
- **Students do:** Run it, then extend it in one of three ways of their choosing: print only the files whose name ends in `.txt`, print the total size of everything in the folder, or count how many items are directories. Every one of those is a loop with a condition, which is Unit 1 material, so this is a systems topic riding on skills they already have.
- **You do:** Circulate. The predictable problems are a wrong folder name, which raises `FileNotFoundError`, and confusion between `item` (a Path object) and `item.name` (a string). Both are worth reading the error message for out loud.
- **Purpose:** The filesystem stops being a thing the terminal does and becomes data a program can work with. This is also the setup for Week 18's file reading and writing.

### Segment 7: Mystery Day, why are macOS, Windows, and Linux different? (1:45 to 1:55), Systems strand

Ten tight minutes. It is a history question with a technical payoff.

1. **Ask for theories first** and write them up without judging. Expect "different companies," "Apple is more locked down," and "gaming."
2. **Give the family tree, briefly.** Unix was written at Bell Labs starting in 1969. Its design, small tools, a hierarchical filesystem, and everything treated as a file, spread through universities and industry for two decades. Linux, begun by Linus Torvalds in 1991, is a from-scratch kernel built to work like Unix. macOS is descended from NeXTSTEP, which was built on BSD, which is a genuine branch of the Unix family. So the Mac and the Ubuntu machine in this room are cousins with a common ancestor, which is why the commands they just typed are identical on both.
3. **Then Windows.** Windows NT, the line every modern Windows descends from, was designed in the late 1980s by a team led by Dave Cutler, who came from Digital's VMS, not from Unix. Different ancestor, different design decisions: backslashes instead of forward slashes in paths, drive letters instead of one single tree, a registry instead of text configuration files, and a completely different set of system calls underneath.
4. **Land the practical consequence.** This is exactly why WSL2 exists. Microsoft's answer to "developers want Unix tools" was not to rewrite Windows; it was to run a real Linux kernel alongside it. The Windows machines in this room are literally running two operating systems at once, and `/mnt/c` is the seam.
5. **Close with the honest nuance.** None of these is better. They made different bets in different decades for different customers, and the bets are now expensive to unmake. Verify any dates or version details you plan to state confidently; potted computing history is easy to get slightly wrong.

### Segment 8: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out the homework and walk through it, including the Extra Credit AP Track section at the end. Tell AP-track students plainly that operating systems are not on the AP exam and that this week's pointer says so.
- **You do:** Exit question at the door, asked individually: what does `cd ..` do? Anyone who cannot answer gets paired deliberately next week.

## 7. Key scripts and analogies

- **What an OS is:** "It is the program whose entire job is to manage the other programs. Nothing you have written this year asked permission for memory or the screen, because something was quietly granting it every time."
- **Process versus thread:** "A process is a household: its own house, its own front door, its own stuff. A thread is a person in that household. Two people in one house share the kitchen. Two households do not, and if one burns down the other is fine."
- **Scheduling:** "One cook, four orders. The cook works on one at a time and switches so fast that all four diners think they have the kitchen to themselves."
- **Virtual memory:** "Every program is told it has the whole building. The OS quietly hands out rooms and keeps a map, and nobody ever finds out."
- **A path:** "Directions from the front door of the filesystem to one specific thing, with each slash a turn. The graphical window is a photo of where you are; the path is the address."
- **Finder and the shell:** "Two windows onto one folder. Neither one is the real one. The real one is on the disk, and both of these are asking the OS about it."
- **Permissions:** "Nine characters that answer one question three times: what may the owner do, what may their group do, what may everybody else do."
- **`sudo`:** "It means: I know I am not allowed, do it anyway, here is the password. If a stranger on the internet tells you to type it, that is the attack."
- **Why the three OSes differ:** "Two of them are cousins from a 1969 family, and one comes from a different family entirely. That is why two of them speak the same language at the prompt and the third had to have Linux bolted on to join the conversation."

## 8. Differentiation

- **Younger or newer students:** The barrier here is typing accuracy, not the ideas. Pair them with a confident typist and have them each type every command themselves rather than watching. Insist on Tab completion from the first minute, because it removes most of the failures. It is a complete success for these students if they can reach a prompt, run `pwd`, `ls`, and `cd`, and find their CS Class folder from the terminal; permissions can stay at "these letters say who is allowed to do what" without the numeric `chmod`. In Segment 6, give them the working program and have them change only the folder name and run it.
- **Extensions for advanced or AP-track students:** Have them find their machine's total RAM and current free memory from the terminal (`vm_stat` on macOS, `free -h` on Ubuntu) and reconcile it with what Activity Monitor or Task Manager reports. Have them run `ls -la ~` and work out what three of the dotfiles are for. In Python, have them write a recursive version of the directory lister using `folder.rglob("*")` and report the largest file under their home folder. AP-track students should read this week's Extra Credit AP Track section for the honest note that this material is off-syllabus.

## 9. Common pitfalls

- **WSL not initialized on a Windows machine.** First launch demands a new UNIX username and password and can take several minutes. Do it in prep. If it happens in class anyway, move that student to a Mac and sort the machine out afterwards.
- **Typing errors read as conceptual failure.** A student who types `Cd` or `ls -1` and gets an error concludes they do not understand the terminal. They understand it fine. Say early and repeatedly that the shell is case sensitive and completely literal, that this is the same lesson as the Week 1 robot maze, and that Tab completion exists precisely because everyone mistypes.
- **Spaces in filenames.** This bites on the very first `cd`, because the class folder is called `CS Class`. A student who types `cd ~/Documents/CS Class` without quotes gets a confusing error, because the shell reads it as two arguments. Teach `cd ~/Documents/"CS Class"` or, better, Tab completion, which handles the space for them.
- **Getting lost.** Students will end up somewhere unexpected and panic. Give them the reset before they need it: `cd ~` always goes home, and `pwd` always answers "where am I." Write both on the board.
- **The demo font is too small.** Nobody will tell you. Fix it in prep.
- **Confusing the Thonny shell with the system shell.** They look similar and are not the same thing. Thonny's shell runs Python; the terminal runs shell commands. Say it explicitly and show what happens when you type `ls` into Thonny.
- **`sudo` curiosity.** Someone will discover it. Get ahead of it in Segment 5 with the honest explanation rather than a prohibition.
- **Overrunning Segment 3.** If the clock is tight, cut Segment 7's Mystery Day to five minutes and protect the navigation practice. The mystery is interesting; the navigation is load-bearing for four more weeks.

## 10. Homework

Full details in `handouts/week-17-homework.md`. In summary: a short terminal navigation exercise done on their own machine with the answers written down; read one `ls -l` line and explain every character; extend the `pathlib` directory lister; a short written answer on what a process is, prompted by a look at Activity Monitor or Task Manager; optional Crash Course episodes on operating systems and files. The handout closes with an Extra Credit AP Track section, which for this week states plainly that operating systems are not AP CSP content and gives AP students a useful alternative.

## 11. Assessment

Observational and low-stakes. The one thing to actually check, student by student, during Segment 3 is whether each student reached a prompt and navigated to their CS Class folder unaided. Keep a list. Anyone who did not needs deliberate pairing in Week 18, when the shell is the entire session.

The exit question (`cd ..`) is the second check. The homework is scored for completion against the weekly-labs rubric, with the `ls -l` interpretation item being the one worth reading carefully, since permissions reappear in Week 18's script and Week 21's SSH lab.

Nothing this week is a checkpoint. The Unit 4 checkpoint and the mid-year milestone are both in Week 21, and it is worth telling students that now so the unit has a visible destination.

## 12. AP alignment

**This session covers no AP CSP topics, and that is worth saying plainly rather than dressing up.** Operating systems, processes, threads, filesystem permissions, and the command line are not in the AP CSP framework. Big Idea 4, Computer Systems and Networks, is about the internet, and it starts in Week 19. Do not tell AP-track students that today was exam preparation, because it was not.

There is one genuine and non-trivial connection: layered abstraction. The exam does ask what an abstraction hides and why hiding it is useful, and "your program asks the OS instead of touching the disk" is one of the cleanest examples of that idea in the whole course. Make that point; do not stretch it further.

**AP-track self-study for this week, and only this week's slice.** Since there is no matching unit, the honest advice is one of two options, and either is extra credit rather than required work:

- **Project STEM (the AP spine):** nothing in the sequence matches this week. Use the time to finish anything outstanding from earlier units, most likely Unit 2, Programming. The nearest topical unit is Unit 6, Innovative Technologies, which covers the internet and cybersecurity, but that belongs with our Weeks 19 through 21 and starting it now gains nothing. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** likewise no match. A student who is caught up may begin Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`, two weeks early. That unit is the AP home for our Weeks 19, 20, and 21, so anything done now is work banked rather than wasted, and arriving at Week 19 already fluent in the vocabulary is a real advantage given how acronym-heavy that session is.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Terminal navigation, permissions, and the Finder comparison: Segments 3 and 5 are complete on their own. No external source needs reviewing.
- Apple's Terminal user guide, for your own reference on defaults and profile settings: `https://support.apple.com/guide/terminal/welcome/mac`
- Microsoft's WSL documentation, worth reading during prep if you have not set up WSL2 before, particularly the first-run username and password step and the `/mnt/c` filesystem note: `https://learn.microsoft.com/windows/wsl/`. Verify the current install command and requirements before a fleet rollout; Microsoft changes them.
- Python `pathlib` documentation, for your reference: `https://docs.python.org/3/library/pathlib.html`
- Crash Course Computer Science, Episode 18 ("Operating Systems") and Episode 20 ("Files and File Systems"), assigned as optional homework viewing. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- Machine configuration, including the standard-versus-admin account design that Segment 5 explains: Section 8 of `curriculum/CS-Curriculum-and-Setup.md`.
- Why the terminal is a flagged difficulty spike, and the supports available: Section 1 and Section 4 of `student-prep/Younger-Student-Readiness-and-Prep.md`.
- Unit 4 outline and the Week 21 milestone this unit builds toward: Sections 3 and 5 of `curriculum/CS-Curriculum-and-Setup.md`.
