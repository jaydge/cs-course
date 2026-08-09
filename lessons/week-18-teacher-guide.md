# Week 18 Teacher Guide

## 1. Header

- **Week:** 18 of 32
- **Unit:** 4, Operating Systems and the Internet
- **Theme question:** Why would anyone choose to type instead of click?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Create, copy, move, rename, and delete files and folders from the shell, and say why deletion there is permanent.
- Search inside files with `grep` and search for files with `find`.
- Explain what a pipe does and build a three-stage pipeline that answers a question no single command answers.
- Redirect a command's output into a file with `>` and `>>`, and say the difference.
- Write, make executable, and run a short shell script.
- Run a Python program from the terminal with `python3`, and read a command-line argument with `sys.argv`.
- Read a text file and write a text file from Python using `with open(...)`.

## 3. Where this sits

Week 17 got everyone to a prompt and taught them to move around. This week they do work there. The session is deliberately the most hands-on of the unit, because shell fluency is a compounding skill: it pays off in Week 19's networking commands, Week 21's SSH lab, Week 22's VS Code terminal, and Week 23's Git, and a student who is still fighting the prompt in Week 21 will struggle in all four.

The pipe is the conceptual centerpiece. It is the single idea that explains why the Unix design has outlived every operating system it competed with, and it is also a genuinely new shape of thinking for students: small tools, each doing one thing, composed into an answer. That is the same decomposition idea from Week 5's functions, arriving from a completely different direction, and it is worth saying so out loud.

The Coding strand leaves Thonny's Run button for the first time. Students discover that a Python file is just a file, that something has to be told to run it, and that Thonny was quietly doing that for them all year. File reading and writing arrives here for the same reason: they now know what a file actually is.

## 4. Materials and setup

- Student laptops with working terminals, verified in Week 17. Anyone who never reached a prompt last week gets paired today.
- The Week 17 command reference cards. Bring spares.
- A printed challenge sheet for Segment 3, one per student, listing the numbered challenges from that segment so students can work at their own pace without watching the projector. This is the one printed item that genuinely saves time.
- A prepared data file for the pipe work, described in Section 5, placed on every machine.
- Projector with a large terminal font.
- Whiteboard with the theme question, plus space for the pipeline diagram.
- Printed Week 18 homework handout, one per student.

## 5. Pre-class prep checklist

- **Create the practice data on every machine.** The pipe segment needs something with enough lines to be interesting. Put a folder `~/Documents/"CS Class"/sandbox/logs` on each machine containing a file `access.log` of roughly 200 lines, each line looking like `2026-01-14 10:32:07 GET /index.html 200 alice`, with a mix of four or five usernames, a mix of paths, and a mix of status codes including some 404s. Generate it once with a five-line Python script and copy the file to every machine. From the terminal, the folder is made with:

  ```bash
  mkdir -p ~/Documents/"CS Class"/sandbox/logs
  ```
  Note the quotation marks again. Everything this week lives inside the same `CS Class` folder students have used since Week 1, in a new `sandbox` subfolder, so that the destructive commands in Segment 3 have somewhere safe to happen. Do not create a separate practice folder elsewhere; Week 17's whole argument was that there is one folder and the terminal is just another window onto it. (20 min the first time)
- Run every command in Segment 3 yourself, on both a Mac and a WSL Ubuntu machine, and confirm the output matches what the challenge sheet claims. Small differences exist; `grep --color` behavior and `find` argument order are the usual culprits. (20 min)
- Write and print the challenge sheet. It is the numbered list from Segment 3, nothing more, with a blank line under each for the answer. (15 min)
- Write and test the shell script from Segment 5 and the two Python programs from Segment 6 on the classroom machines. Confirm `python3` works from the terminal on both fleets and note which version it reports, since Thonny may be using a different one. (15 min)
- Decide the sandbox rule and be ready to state it: all destructive commands happen inside `~/Documents/"CS Class"/sandbox` and nowhere else. Consider making a fresh copy of the sandbox folder on each machine so a mistake costs nothing. (5 min)
- Print homework handouts and challenge sheets. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Ask three students to read out one line of `ls -l` output from their homework and interpret it. Correct anything shaky about the permission bits now; the script in Segment 5 depends on it.
- **You do:** Pose the theme question honestly, as a challenge. The Finder is easier for one file. Ask: how would you find every file on this laptop that mentions the word "binary," anywhere inside it, including files you have forgotten about? Let them describe doing it by hand. Then say that the answer is one line and they will write it in forty minutes.
- **Purpose:** Establishes the actual argument for the shell, which is not "it is faster to type" but "some questions have no clicking answer."

### Segment 2: The grammar of a command (0:10 to 0:25), Systems strand

1. **Write the shape on the board and leave it there:** `command  -options  arguments`. Every command they meet this year fits it.
2. **Demonstrate with one they know.** `ls` alone. `ls -l` adds an option. `ls -l ~/Documents/"CS Class"` adds an argument. Three forms, same command.
3. **Teach `man`, and teach how to leave it.** Run `man ls`. Say that this is the manual page, that it is dense on purpose, and that nobody reads it top to bottom. Show scrolling with the space bar and, critically, quitting with `q`. Students who cannot get out of `man` or `less` will close their whole terminal. Have every student open `man ls` and press `q` right now.
4. **Show that reading a manual page is a skill.** Find the `-l` line in `man ls` together. Say the honest thing: you will look up flags for the rest of your life, and remembering that the manual exists matters far more than memorizing any flag.
5. **Name the five survival keys** and write them on the board: Tab completes, Up-arrow recalls, Control-C stops a running command, Control-L or `clear` clears the screen, and `q` leaves a pager.
6. **Set the sandbox rule, firmly.** Everything today happens inside `~/Documents/"CS Class"/sandbox`. Say why in one sentence: you are about to learn a delete command that does not use the Trash, and a sandbox means a mistake costs you nothing. Say the quoting point once more while the path is on the projector, because it is the thing that will trip them all morning: `CS Class` has a space in it, so it goes in quotation marks, or the shell reads it as two separate arguments and looks for a folder called `CS`. Tab completion puts the quoting in for them, which is the better habit.

### Segment 3: The challenge course (0:25 to 1:00), Systems strand

Hand out the printed challenge sheet. Students work through it at their own pace, in pairs where you decided to pair. You demonstrate challenges 1, 5, and 8 on the projector before anyone starts; the rest they do from the sheet while you circulate. Announce that reaching challenge 10 is a full result and that 11 and 12 are for anyone who gets there.

1. **Make a workspace.** From your home folder, create a folder `week18` inside the sandbox, move into it, and confirm with `pwd`.

   ```bash
   mkdir ~/Documents/"CS Class"/sandbox/week18
   cd ~/Documents/"CS Class"/sandbox/week18
   pwd
   ```
   Read the `pwd` output aloud. It ends `.../Documents/CS Class/sandbox/week18`, which is the folder they could open in Finder right now if they wanted to.
2. **Make files three ways.** Create an empty file with `touch first.txt`. Create a file with content in it using redirection: `echo "hello from the shell" > second.txt`. Then look at what you made with `cat second.txt`.
3. **Copy and rename.** Copy `second.txt` to `third.txt` with `cp second.txt third.txt`. Rename `first.txt` to `notes.txt` with `mv first.txt notes.txt`. Note the surprising fact: renaming and moving are the same command, because a name is just where a file sits.
4. **Move something into a folder.** Make a folder `archive` and move `third.txt` into it. Confirm with `ls` and `ls archive`.
5. **Delete, carefully.** Delete `third.txt` from inside `archive`:

   ```bash
   rm archive/third.txt
   ```
   Stop the room here and say it once, clearly: there is no Trash, no undo, and no confirmation. Then say the two rules. First, always `ls` before you `rm` so you know what is actually there. Second, never run a delete you do not fully understand, especially one someone else handed you. Do not demonstrate recursive deletion at all.
6. **Look inside a big file three ways.** Move to `~/Documents/"CS Class"/sandbox/logs`. Run `cat access.log` and watch it fly past uselessly. Then run `head access.log`, then `tail access.log`, then `less access.log` and quit with `q`. Ask which of the four they would actually use on a file this size.
7. **Count.** How many lines are in `access.log`?

   ```bash
   wc -l access.log
   ```
8. **Search inside a file.** Find every line mentioning `alice`:

   ```bash
   grep alice access.log
   ```
   Then find every failed request: `grep 404 access.log`. Say what `grep` does in one sentence: it prints the lines that match, and throws the rest away.
9. **Search for files, not inside them.** From your home folder, find every file whose name ends in `.txt`:

   ```bash
   find ~/Documents/"CS Class"/sandbox -name "*.txt"
   ```
   Name the difference out loud, because students conflate these constantly: `grep` looks inside files, `find` looks for files.
10. **Build a pipe.** How many times did alice appear in the log?

    ```bash
    grep alice access.log | wc -l
    ```
    Stop the room and draw it on the board: `grep` produces lines, the `|` hands them to `wc -l` instead of to the screen, and `wc -l` counts them. Say the idea plainly. Each tool does one small job. The pipe is a hose from the output of one to the input of the next. Nobody wrote a "count alice's lines" program, and nobody needs to, because two tools compose into one.
11. **Three stages.** Who used the site the most? The username is the last field on each line:

    ```bash
    awk '{print $5}' access.log | sort | uniq -c | sort -rn
    ```
    Walk it left to right on the board: pull out field five, put identical names next to each other, count each run, then sort by the count, biggest first. Tell them `awk` is a whole language they do not need today and that this is the only incantation from it they will use. The point is the shape of the pipeline, not the tool.
12. **Save an answer.** Send the result into a file and check it:

    ```bash
    awk '{print $5}' access.log | sort | uniq -c | sort -rn > report.txt
    cat report.txt
    ```
    Then run it again with `>>` instead of `>` and `cat` it again. Ask what changed. Name it: `>` replaces the file, `>>` adds to the end. Getting these backwards destroys work, so it is worth ten seconds.

Return to the theme question at the end: the "find every file mentioning binary" problem from Segment 1 is now `grep -r binary ~/Documents/"CS Class"`, and everyone in the room can read that line.

### Segment 4: Stretch (1:00 to 1:05)

### Segment 5: Write a tiny shell script (1:05 to 1:25), Systems strand

1. **Motivate it in one sentence.** They just typed a four-stage pipeline. Nobody wants to type that twice. A script is a file full of commands, and running the file runs the commands.
2. **Create the file.** Say up front that they can use Thonny as a plain text editor for this, which avoids teaching a terminal editor today. In Thonny, File, New, then save it into the `sandbox/logs` folder inside `CS Class` as `report.sh`. Tell them explicitly that Thonny will not run it and that this is fine; it is just a text editor here.
3. **Type the script together, line by line:**

   ```bash
   #!/bin/bash
   echo "Log report for $(date)"
   echo "Total lines:"
   wc -l < access.log
   echo "Busiest users:"
   awk '{print $5}' access.log | sort | uniq -c | sort -rn | head -3
   ```
4. **Explain the first line, because it is genuinely strange.** `#!/bin/bash` is called the shebang. It tells the operating system which program should run the rest of this file. Connect it straight back to Week 17: the OS is the thing that decides how a file gets executed, and this line is how the file tells it.
5. **Try to run it and fail on purpose.** From the terminal, in the `logs` folder:

   ```bash
   ./report.sh
   ```
   It fails with a permission error. Do not fix it yet. Ask what is missing and steer them to last week's `ls -l`.
6. **Look at the permissions and fix them.**

   ```bash
   ls -l report.sh
   chmod +x report.sh
   ls -l report.sh
   ./report.sh
   ```
   The `x` bits appear between the two listings and the script runs. This is the moment Week 17's permissions segment pays off, and it is worth pointing at explicitly.
7. **Explain `./` while they are curious.** The shell does not look in the current folder for commands, on purpose, so that a file named `ls` sitting in a downloaded folder cannot hijack the real one. `./report.sh` means "the one right here, and I mean it."
8. **Students do:** Add one line of their own to the script. Suggestions: count the 404s, print the first line of the log, or print how many distinct users appear (`awk '{print $5}' access.log | sort | uniq | wc -l`).

### Segment 6: Python from the command line, and real files (1:25 to 1:55), Coding strand

- **You do:** Frame the reveal. All year, Thonny's Run button has been doing one thing: handing your file to Python. Today you do it yourself. In the terminal:

  ```bash
  cd ~/Documents/"CS Class"/sandbox/week18
  python3 --version
  ```
  Note the version out loud and compare it to what Thonny reports at the top of its shell. If they differ, say so plainly rather than hiding it; a machine can have several Pythons, and knowing which one you are talking to is a real skill that returns in Week 22.
- **You do and students do:** Write a two-line file in Thonny, save it as `hello.py` in `week18`, and run it from the terminal:

  ```bash
  python3 hello.py
  ```
  Land the idea: a Python program is a text file. Thonny is a convenience, not a requirement. Nothing about their code changes.
- **You do:** Add arguments, which is the piece that makes command-line Python worth doing:

  ```python
  import sys

  print("You gave me", len(sys.argv) - 1, "arguments")
  print("They were:", sys.argv[1:])
  ```
  Run it as `python3 args.py apple banana`. Explain that `sys.argv[0]` is the program's own name, which is why the count is off by one, and connect it straight to the command grammar from Segment 2: this is how `ls -l notes.txt` gets its `-l` and its `notes.txt`. Their program now has the same shape as every command they ran today.
- **You do:** Now file reading, with the log file they already know:

  ```python
  with open("access.log") as f:
      for line in f:
          if "404" in line:
              print(line.strip())
  ```
  Say what `with` does in one sentence: it opens the file and guarantees it gets closed when the block ends, even if something goes wrong. Say what `.strip()` is for: every line read from a file still carries its newline character, and `print` adds another one, so without it everything double-spaces. Let a student discover that if you can.
- **You do:** Then writing:

  ```python
  with open("errors.txt", "w") as out:
      with open("access.log") as f:
          for line in f:
              if "404" in line:
                  out.write(line)
  ```
  Run it, then `cat errors.txt` from the terminal, then open it in Finder. Same file, three views, which is Week 17's idea landing again.
- **Say the caution out loud, because it costs data:** opening a file with `"w"` erases whatever was in it, immediately, before you write anything. `"a"` appends instead. This is the same distinction as `>` and `>>` from Segment 3, and pointing at that parallel makes both stick.
- **Students do:** Write a program that reads `access.log`, counts how many lines mention each of two usernames, and prints both counts. Then have them compare their answer to what the shell pipeline gave in challenge 11. Getting the same number two completely different ways is the satisfying part.
- **Purpose:** Python stops being a thing that happens inside an IDE and becomes a tool that lives alongside the others in the terminal. This is the prerequisite for Week 20's `http.server` and Week 22's project structure.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Ask the theme question again and take a real answer. The one you want: because some questions do not have a clicking answer, and because small tools that combine beat one big tool that almost does what you want.
- **You do:** Hand out homework, noting the Extra Credit AP Track section. Tell them next week the machines get plugged into each other and the room becomes a network.

## 7. Key scripts and analogies

- **Why the shell:** "Clicking is better for one file. Typing is better for a thousand files, or for a question nobody built a button for. You now have both, and choosing well is the skill."
- **Command grammar:** "Verb, adverbs, objects. `ls` is the verb, `-l` is how, and the filename is what. Every command in your life fits that sentence."
- **The pipe:** "A hose. `grep` fills the hose with lines, `wc` counts whatever comes out. Neither one knows the other exists, and that is exactly why they work together."
- **The Unix philosophy:** "Nobody built a program that counts how many times alice appears in a log. They built one that filters and one that counts, and left the hose to you. That decision from 1970 is why your Mac and that Ubuntu machine speak the same language."
- **`grep` versus `find`:** "`grep` looks inside. `find` looks for. Confuse them once, remember it forever."
- **`rm`:** "There is no Trash out here. The Trash is a feature of the graphical program, not of the disk. Look before you delete."
- **The shebang:** "The first line of the script is not for you, it is a note to the operating system saying which program should read the rest of this."
- **`chmod +x`:** "A file does not become a program because of what is in it. It becomes a program when someone says it is allowed to run. That is the permission bit you read last week."
- **`python3 hello.py`:** "The Run button was never magic. It was typing this for you, every time, and not telling you."
- **`with open`:** "It opens the file, does your work, and closes it behind you even if you knock something over on the way out."

## 8. Differentiation

- **Younger or newer students:** Reaching challenge 8 is a complete result; say that to them directly so they are not measuring themselves against the fast pairs. The pipe is the one thing not to skip, so if they are running short, jump them from challenge 8 straight to challenge 10 and skip the file-searching. For the script, give them the finished file and have them only run `chmod +x` and execute it, which still teaches the permission point. In Segment 6, running an existing program from the terminal and reading a file are enough; skip `sys.argv`.
- **Extensions for advanced or AP-track students:** Have them find every `.py` file they have written this year and count the total lines across all of them, in one pipeline (`find ~ -name "*.py" | xargs wc -l` will get them close, and the failure modes are instructive). Have them add an argument to their shell script so `./report.sh alice` reports on one user, using `$1`. In Python, have them write a program that takes a filename and a search word as command-line arguments and prints matching lines, which is a small `grep` and makes the point that these tools are not magic. The strongest can compare their Python `grep` against the real one on a large file and notice the speed difference.

## 9. Common pitfalls

- **Stuck in `man` or `less`.** Teach `q` in Segment 2 and make everyone press it once. Otherwise a student will silently close their terminal and lose their place.
- **`rm` accidents.** Enforce the sandbox rule. Do not demonstrate recursive deletion, do not joke about it, and do not put it on the challenge sheet. If a student asks about `rm -rf`, answer honestly that it deletes a folder and everything in it without asking, that professionals have destroyed real work with it, and that they will not need it in this course.
- **`>` overwriting something they wanted.** Predictable and mostly harmless in the sandbox. Use it as the hook for the `>` versus `>>` distinction rather than preventing it.
- **Quoting.** `grep hello world.txt` searches for `hello` in a file called `world.txt`, which is not what a student who meant to search for "hello world" expected. Teach quotes at the moment it happens.
- **Smart quotes from a document.** Same problem as Week 2, worse here. Never let students paste shell commands from a word processor or a notes app. The challenge sheet is printed for exactly this reason.
- **`./` omitted.** `report.sh` alone gives "command not found" and looks like the script is broken. Segment 5 step 7 exists to pre-empt this.
- **Two different Pythons.** Thonny's Python and the terminal's `python3` may be different installations with different packages. Say it in Segment 6 rather than letting a student hit it silently in Week 20 when `requests` is installed in one and not the other.
- **The challenge course becoming a race.** Some pairs will finish challenge 12 in fifteen minutes and get loud. Have the extension tasks from Section 8 written on the board so they have somewhere to go.
- **`awk` anxiety.** Somebody will want to understand `awk`. Say honestly that it is a full language, that today it is a copied incantation, and that the pipeline shape is what matters. Do not teach it.

## 10. Homework

Full details in `handouts/week-18-homework.md`. In summary: a set of shell tasks with the commands and outputs written down; build two pipelines to answer given questions; extend the shell script with one new line and re-run it; write a Python program that reads a file, filters it, and writes the results to a new file, run from the terminal rather than from Thonny's Run button; a short written comparison of when to use the shell and when to use a graphical file browser. The handout closes with an Extra Credit AP Track section, which again states plainly that the shell is not AP CSP content.

## 11. Assessment

Observational, plus one artifact. During Segment 3, walk the room with the challenge list and note where each student got to. The two things worth recording per student are whether they built a working pipe unaided (challenge 10) and whether they ran their own script after `chmod +x` (Segment 5 step 6). Those two predict how Week 21's SSH lab will go better than anything else.

The homework's Python file-processing program is the graded artifact, scored against the weekly-labs rubric. The specific thing to look for is whether the student ran it from the terminal, which you can ask them to demonstrate in thirty seconds at the start of Week 19.

Also worth a note in your records: any student who still cannot navigate to a folder without help after two full sessions needs a fifteen-minute one-to-one before Week 21, not more class time. The SSH lab assumes this is automatic.

## 12. AP alignment

**Like Week 17, this session covers no AP CSP topics.** The shell, pipes, scripts, and file input and output are not in the framework. Command-line Python is not either. Say so to AP-track students rather than implying that everything in the course is exam preparation.

Two connections are real but indirect, and worth naming for that reason. First, the pipeline is decomposition and abstraction in a new costume, and both are computational thinking practices the exam does assess. Second, file reading is the mechanical foundation of AP topic 2.4, Using Programs with Data, though the exam's version of that topic is about drawing conclusions from a dataset rather than about opening a file, and our course covers it properly in Week 25.

**AP-track self-study for this week, and only this week's slice.** No unit matches, so the advice is the same as last week, and it is extra credit rather than required work:

- **Project STEM (the AP spine):** no matching unit. Finish outstanding work from earlier units. Do not start Unit 6, Innovative Technologies, yet; it is the right home for our Weeks 19 through 21 and is better done alongside them. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** no matching unit either. A caught-up student should use this week to work Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`, ahead of Week 19. Everything in that unit is on-topic for the next three weeks, and doing the vocabulary lessons now takes real pressure off the acronym-heavy Week 19 session.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The challenge course, the shell script, and the Python segment: Segments 3, 5, and 6 are complete on their own. No external source needs reviewing to run them.
- The manual pages on the classroom machines are the reference students should learn to use: `man ls`, `man grep`, `man find`. Worth skimming `man grep` during prep so you can answer flag questions without guessing.
- Python `sys.argv` and the file-object documentation, for your reference: `https://docs.python.org/3/library/sys.html` and `https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`
- Crash Course Computer Science, Episode 22 ("Keyboards and Command Line Interfaces"), optional homework viewing and a good short history of why the command line exists at all. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- "Automate the Boring Stuff with Python" by Al Sweigart, free online, for any student who wants more file-processing practice: recommended in Section 6 of `student-prep/Younger-Student-Readiness-and-Prep.md`.
- Terminal difficulty supports and pairing guidance: Section 4 of `student-prep/Younger-Student-Readiness-and-Prep.md`.
- Unit 4 outline: Section 5 of `curriculum/CS-Curriculum-and-Setup.md`.
