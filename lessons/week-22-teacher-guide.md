# Week 22 Teacher Guide

## 1. Header

- **Week:** 22 of 32
- **Unit:** 5, Building Modern Software
- **Theme question:** How do teams build software that does not fall apart?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Name the phases of the software development life cycle and say what each one produces.
- Explain the difference between building everything before showing anyone and building a little and showing it often, and give one honest advantage of each.
- Define technical debt in their own words and point at a concrete example of it in code.
- Open a folder as a project in VS Code, select a Python interpreter, and run a program from the integrated terminal.
- Create a Python virtual environment and explain what it isolates.
- Restructure a single-file program into a project with a package folder, a `main.py`, a `README.md`, a `.gitignore`, and a `requirements.txt`, and say what each file is for.

## 3. Where this sits

Unit 4 ended with the class server, SSH, and a first `git clone` as a taste. Unit 5 now assembles everything into working software: process this week, version control next week, the web the week after, then APIs and data, then mobile. The single largest change today is the tool. Students have used Thonny for twenty-one weeks. Thonny was correct for those weeks because it hides everything; VS Code is correct from here because the rest of the unit needs a real editor, an integrated terminal, a Git panel, and multi-file projects.

Do not treat the switch as a small administrative step. It is the coding strand for the day, and it costs a full forty minutes to do properly. A student who leaves today unable to open a folder, pick an interpreter, and run a file will be lost in Week 23 and stranded in Week 25.

The process material is not filler. AP topics 1.1 Collaboration and 1.3 Program Design and Development are genuinely covered here, and technical debt gives students the vocabulary to talk about the difference between code that runs and code that can be changed. That vocabulary pays off next week when they review each other's commits.

## 4. Materials and setup

- Each student's laptop with VS Code and Python installed (Section 8 of the curriculum; the provisioning script installs both). Verify VS Code launches on every machine before class, not during it.
- Projector, with VS Code already open on the demo machine at a comfortable font size. Increase it now; the default is unreadable from four feet away.
- Whiteboard with the theme question written large, and a clear column for the SDLC phase list.
- Index cards, roughly twenty per team, and markers, for the sprint simulation.
- A prepared "messy" program and a prepared "clean" version of the same program, on the demo machine (see Section 5).
- Each student's Week 16 text adventure, findable on their machine. It was saved into the `CS Class` folder in Documents, which is where every piece of student work has lived since Week 1 and where today's project goes too. Confirm this in the warm-up; the coding strand restructures it.
- Printed Week 22 homework handout, one per student.

## 5. Pre-class prep checklist

- Verify VS Code opens and runs a Python file on at least two student machines, one Mac and one Windows. If the Python extension is missing, install it on all machines now. Extension names and marketplace entries change; verify the current publisher before a wide install. (20 min)
- Write the messy program and its clean twin. The messy one should be the Week 4 calculator with copy-pasted arithmetic blocks, one-letter variable names, repeated literal numbers, and no functions. The clean one should do the same job with a small dispatch dictionary and one formatting function. You will ask the class to add a feature to each. (20 min)
- Run through the VS Code segment once on the demo machine, deleting the `.venv` afterward so you can demonstrate creating it live. (10 min)
- Prepare the sprint simulation: count out index cards into team piles and decide your three vague customer wants and the one mid-simulation change of mind. (10 min)
- Confirm every student has a working GitHub account and can sign in, ahead of next week. This is the single most common cause of a wasted Week 23. Chase stragglers with parents this week, not next. (10 min)
- Print homework handouts. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and framing (0:00 to 0:10)

- **You do:** Pose the theme question. Then ask a concrete version of it: your text adventure is one file that only you have ever opened. What breaks first if four people have to work on it and it has to still work in two years?
- **Students do:** Locate their Week 16 text adventure file in the `CS Class` folder in Documents and leave it open. Anyone who cannot find it gets paired now, not later.
- **You do:** Set the shape of the day out loud: an hour on how software actually gets built, then a new editor and a real project layout.

### Segment 2: The software development life cycle (0:10 to 0:25), Systems strand

1. **Ask what happens before code and after code.** Take answers and sort them into a phase list on the board: requirements, design, implementation, testing, deployment, maintenance.
2. **State what each phase produces,** because a phase with no artifact is a phase nobody can check. Requirements produce a written description of what the thing must do. Design produces a plan of the pieces. Implementation produces code. Testing produces evidence. Deployment produces a running system someone else can use. Maintenance produces changes to a thing already in use.
3. **Say the unpopular truth about maintenance.** It is the longest and most expensive phase by a wide margin. Most professional programming is changing code that already exists and already has users.
4. **Draw waterfall.** One arrow down the six phases, each finished before the next begins. Ask what it assumes. Answer: that the requirements were right at the start.
5. **Ask when that assumption holds.** It genuinely does hold sometimes, and say so: a bridge, a pacemaker, a spacecraft. Do not caricature waterfall. It is the right shape when changes are catastrophic and the requirements really are known.
6. **Leave the alternative unnamed** for now. Segment 3 makes students invent it.

### Segment 3: Two sprints, unplugged (0:25 to 0:50), Systems strand

Run this entirely from the steps below. No materials beyond index cards and markers.

1. **Form teams of two or three.** Give each team a stack of index cards and a marker. Announce that you are the Customer and that they are a software team building a school lunch ordering app. The cards are screens.
2. **State three vague wants.** Say them once, conversationally, and refuse to repeat them in more detail: students should be able to order lunch, you want to know what has been ordered, and it should be quick. Vagueness is the point.
3. **Backlog, three minutes.** Each team writes one feature per card, as many as they can think of. Then they lay the cards in a single column, most valuable at the top. Tell them explicitly: order by value to the Customer, not by what is easiest or most fun.
4. **Sprint 1, seven minutes.** Each team may build only the top two cards. Building means drawing the screen on the back of the card, with the buttons and text labeled. Nothing else may be touched. Hold the line on this.
5. **Review, four minutes.** Visit each team for about a minute. Have them show you the two screens and say what they do. React honestly as a customer would.
6. **Change your mind, on purpose, in front of everyone.** Announce one reversal and one addition: the ordering screen must show prices, which nobody built, and you no longer care about the feature most teams put second. Teams reorder their backlog on the spot.
7. **Sprint 2, seven minutes.** Same rule, top two cards only, from the reordered backlog.
8. **Debrief, four minutes, and name the thing.** Ask the killer question: what would have happened if you had drawn all twelve screens before showing me anything? Answer it together, that most of the work would have been wasted. Then write the vocabulary on the board against what they just did: backlog, iteration or sprint, review, and the phrase working software over documentation. Tell them the name of the family of methods is Agile, and that what they just experienced is the entire reason it exists.
9. **Give the honest counterweight in one sentence.** Short iterations are not free: they cost meeting time, they can drift with no plan, and they are a poor fit when the thing being built must be correct on the first try.

**Purpose:** Agile lands as something students discovered under time pressure rather than a list of ceremonies to memorize.

### Segment 4: Technical debt (0:50 to 1:05), Systems strand

1. **Put the messy program on the projector.** Do not apologize for it or explain it. Just say it works, and run it to prove that it does.
2. **Ask for a change.** Add a remainder operation, and make every result print to two decimal places. Have the class direct you, out loud, to every place you must edit. Count the places on the board as you go.
3. **Open the clean twin.** Make the same change. It touches one or two places. Run it.
4. **Name the term.** Technical debt is a shortcut taken now that charges interest later, and the interest is paid in the time every future change takes. Both programs work. Only one of them can be changed cheaply.
5. **Make the distinction that matters.** Some debt is deliberate and sensible: ship it now, write down what you skipped, fix it after the deadline. Some debt is careless: nobody decided, nobody wrote it down, and the interest compounds until a small feature takes a week. The problem is rarely the shortcut; it is the shortcut nobody recorded.
6. **Name the repayment.** Refactoring is changing the shape of code without changing what it does. They have done it already, in the Week 5 homework, when they pulled a chunk out into a function.
7. **Close the loop to the sprint game in one line.** Iterating fast is how debt accumulates, and deliberate refactoring is how a fast team stays fast. Both halves are the job.

### Segment 5: Stretch (1:05 to 1:10)

### Segment 6: VS Code (1:10 to 1:40), Coding strand part 1

Do every step on the projector first, then have students repeat it. Go slowly. This is the tool for the rest of the course.

1. **Say why we are leaving Thonny.** Thonny was right because it hid everything: one file, one run button, a visible shell. From here we need many files at once, a terminal in the same window, and a Git panel. That is what VS Code is. Add that Thonny stays installed and is still the better tool for a quick one-file experiment.
2. **Open a folder, not a file.** This is the single most important idea of the segment. In VS Code choose File, then Open Folder, and open their `CS Class` folder inside Documents, the one they have saved work into since Week 1 and navigated to from the terminal since Week 17. Say plainly: VS Code works on a folder, and the folder is the project. Opening a lone file gives up half the tool. There is one student folder for the whole course and this is it; nobody needs a second one.
3. **Tour four things and nothing more.** The Explorer sidebar on the left is the folder. The editor area holds tabs. The integrated terminal opens with Control and backtick, and it is the same zsh or Ubuntu shell they have used since Week 18, just living in the editor. The Command Palette opens with Shift, Command, P on a Mac or Shift, Control, P on Windows, and it can reach every command by name. Resist the urge to show anything else today.
4. **Install the Python extension** if the provisioning did not. Extensions view in the sidebar, search Python, install the Microsoft one. Verify the publisher; marketplace listings change.
5. **Create the virtual environment in the terminal, live:**

   ```bash
   mkdir -p ~/Documents/"CS Class"/adventure
   cd ~/Documents/"CS Class"/adventure
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Point at the quotation marks and say why they are there, because this is the same rule from Week 17: `CS Class` has a space in it, and without the quotes the shell reads it as two separate arguments. `~/Documents/CS\ Class/adventure` works just as well, and Tab completion writes the escaping for them.

   On the Windows fleet inside WSL2 Ubuntu the commands are identical. In PowerShell it is `python -m venv .venv` then `.venv\Scripts\Activate.ps1`.
6. **Explain what it isolates, briefly.** A virtual environment is a private box of installed libraries belonging to this project. Without it, every project on the machine shares one pile of libraries and two projects that need different versions of the same library cannot both work. Point at the changed shell prompt as the visible evidence it is active.
7. **Select the interpreter.** Command Palette, type Python: Select Interpreter, choose the one inside `.venv`. Show the interpreter name now displayed in the status bar. Say what goes wrong if it is unset: the editor and the terminal disagree about which Python is running, which produces the most confusing error class of the whole unit.
8. **Run a file two ways.** Once with the run button, once by typing `python3 main.py` in the terminal. Point out that the run button just types that command for them, and that knowing the command is what lets them run code on a server later.
9. **State the AI rule for this tool, explicitly.** Do not install Copilot or any AI coding extension. The no-AI phase runs through Week 26 and unlocks in Week 27 with a lesson attached. If an AI assistant appears in a student's editor, it gets turned off in front of you.

### Segment 7: Project structure (1:40 to 1:55), Coding strand part 2

1. **Ask the question first.** Your text adventure is 120 lines in one file. At what length does one file stop working? Take answers, then say the real answer: at the point where you cannot find things, which is sooner than they expect.
2. **Build this layout on the board, then in the Explorer:**

   ```
   adventure/
     README.md
     .gitignore
     requirements.txt
     main.py
     game/
       __init__.py
       world.py
       player.py
     tests/
       test_player.py
   ```
3. **Say what each thing is, one line each.** `main.py` is the entry point, the file you run. `game/` is a package, a folder of related modules, and `__init__.py` is the empty file that tells Python the folder is one. `world.py` holds the rooms dictionary. `player.py` holds the `Player` class. `README.md` says what the project is and how to run it. `requirements.txt` lists the libraries this project needs. `.gitignore` lists files that should never be saved into version control.
4. **Students do the move.** First bring the game in. Their Week 16 text adventure is a single file sitting in `CS Class`, one level above the new `adventure` folder, so copy it in and rename the copy `main.py`:

   ```bash
   cd ~/Documents/"CS Class"/adventure
   cp ../adventure.py main.py
   ```

   Substitute whatever they actually called the file in Week 16. Copy rather than move, so a broken refactor never costs them the working original. Then cut the rooms dictionary into `game/world.py` and the `Player` class into `game/player.py`, and make `main.py` import them:

   ```python
   from game.world import rooms
   from game.player import Player
   ```

   Warn before they hit it: `player.py` also needs `from game.world import rooms`, because the class used the map as a global. Run from the project root with `python3 main.py`, not from inside `game/`, or the import fails.
5. **Write the `.gitignore` together.** Four lines, and say why each is there:

   ```
   .venv/
   __pycache__/
   *.pyc
   .DS_Store
   ```

   The virtual environment is rebuildable from `requirements.txt` and is enormous, so it never goes in. `__pycache__` and `.pyc` are generated. `.DS_Store` is Finder clutter. Tell them next week is when this file starts earning its keep.
6. **Write a three-line `README.md`.** What it is, how to run it, one known limitation. Say that a README is the first thing any other programmer reads and the last thing most students write.

### Segment 8: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out homework and walk through it, including the Extra Credit AP Track section. Flag two items out loud: play at least the first few levels of Oh My Git before next week, and confirm your GitHub sign-in works, because next week does not have time to fix accounts.
- **Exit question at the door:** name one thing in your project that should never be committed to version control, and why.

## 7. Key scripts and analogies

- **Why process exists:** "One person writing one program for themselves needs no process at all. Every rule we are about to learn exists because of a second person, a second year, or a second version."
- **Waterfall:** "Design the whole bridge, then build the bridge. That is the right answer for a bridge. It is a poor answer for anything where you learn what you actually wanted by using it."
- **Iteration:** "Build a slice, show it, find out you were wrong, adjust. Being wrong early is cheap. Being wrong at the end is the expensive kind."
- **Technical debt:** "It is a loan. You get the feature today and you pay interest on every change from now until someone cleans it up. Borrowing is not the sin. Borrowing without telling anyone is."
- **Refactoring:** "Changing the shape of the code without changing what it does. Same behavior, better building."
- **Open the folder:** "Thonny worked on files. VS Code works on projects. If you open a single file you have brought a Formula One car to a parking lot."
- **Virtual environment:** "A private shelf of libraries for one project. Without it, every project on the machine shares one shelf and eventually two of them want the same slot."
- **The README:** "The note you leave for the next person to open this folder. That person is usually you, in six months, remembering nothing."

## 8. Differentiation

- **Younger or newer students:** The tool switch is the risk today, not the concepts. Pair them for Segment 6 and give a printed four-line cheat sheet: open folder, Control-backtick for the terminal, Select Interpreter, run. For Segment 7, let them create the folder layout and move only the `Player` class, leaving the rooms dictionary in `main.py`. Half the refactor with imports that actually work beats the whole layout broken. If a student's text adventure never ran, hand them a working copy to restructure; the objective today is structure, not the game.
- **Extensions for advanced or AP-track students:** Have them move their Week 15 tests into `tests/test_player.py` and run them from the terminal. Have them write a real `requirements.txt` by running `pip freeze > requirements.txt` inside the activated environment and then explain why the file is nearly empty. Have them write the README as if for a stranger, including a limitations section. The strongest can research and describe, in five sentences, what a pull request is, ahead of next week.

## 9. Common pitfalls

- **The interpreter is not selected.** The editor uses one Python and the terminal uses another, imports work in one place and fail in the other, and nobody can explain it. Check the status bar on every machine as you circulate. This is the number one time sink of the day.
- **Running `main.py` from inside `game/`.** The import fails with `ModuleNotFoundError: No module named 'game'`. The fix is `cd` back to the project root. Say this before it happens and again when it does.
- **A missing `__init__.py`.** Modern Python often tolerates its absence, which is worse than failing, because behavior differs between machines. Have everyone create the empty file.
- **Smart quotes in the terminal.** Students copying commands from a notes app get invisible curly quotes. Have them type commands, as with code.
- **Forgetting to activate the venv.** They install a library and it lands in the system Python, then the project cannot see it. Teach them to check for the prompt prefix before any `pip install`.
- **The sprint simulation becoming an art project.** Teams will decorate. Hold the seven-minute timer hard and say aloud that running out of time is part of the exercise.
- **Treating technical debt as a synonym for bad code.** It is not. The distinction is deliberate versus careless. Correct this if you hear it.
- **GitHub accounts left until next week.** Do not. Chase them today.

## 10. Homework

Full details in `handouts/week-22-homework.md`. In summary: finish restructuring the text adventure into the project layout and get it running from the terminal; write the README and `.gitignore`; a short written piece identifying one piece of technical debt in their own earlier code and what it would cost to change; play at least the first few levels of Oh My Git as preparation for next week; confirm the GitHub sign-in works. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice.

## 11. Assessment

Observational and completion-based this week, against the weekly-labs rubric. Three specific things to check as you circulate, because each one blocks a later week:

1. The student can open a folder in VS Code and run a file from the integrated terminal without help.
2. The interpreter in the status bar points inside `.venv`.
3. The restructured project actually runs from the project root.

For the process material, the check is verbal. Ask three students at random to define technical debt in their own words and to point at an example in their own code. A student who can only repeat the phrase has not got it.

Record who needed pairing on the VS Code switch. That list is the pairing list for next week's Git lab, where the cost of tool confusion is much higher.

## 12. AP alignment

This session covers AP CSP topics 1.1 Collaboration and 1.3 Program Design and Development. Those two are genuine matches, not stretches: the sprint simulation is collaboration with defined roles and iteration, and the SDLC discussion is exactly what 1.3 describes as designing, developing, and refining a program with input from others. Technical debt itself is not an AP topic, but it is the vocabulary that makes 1.3 concrete.

Note for planning: 1.3 is also assessed indirectly through the Create Performance Task's written responses, where students must describe their development process and any collaboration. What students did today is the honest raw material for that answer in April.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 1, Intro and Computational Thinking. Work only the lessons on the program development process and collaboration, then stop; the computational-thinking basics earlier in that unit are already covered by Units 1 through 3 of our course. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`. This is the closest match in the whole CodeAI course to today: it runs a design process with user input, iteration, and collaboration roles. Do the design-process and collaboration lessons; the App Lab programming lessons in that unit are optional and use JavaScript rather than Python.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The two-sprint simulation: fully inline in Segment 3. No external source needs reviewing, and no materials beyond index cards and markers.
- Technical debt demonstration: the two programs are yours, written during prep. The term originates with Ward Cunningham's debt metaphor if you want the background for your own framing.
- VS Code, for your own reference before teaching Segment 6: `https://code.visualstudio.com/docs/python/python-tutorial`. Worth twenty minutes during prep if you have not set up a Python project in VS Code before, specifically to be fluent with Select Interpreter, since that is where students get stuck. Interface details and extension names change between releases; verify against the version installed on the fleet.
- Python virtual environments, for your reference: `https://docs.python.org/3/library/venv.html`
- Oh My Git, assigned as this week's preparation for next week: `https://ohmygit.org`. Free and open source, and it installs locally. Verify it is installed or downloadable on the fleet before assigning it. See also `student-prep/Younger-Student-Readiness-and-Prep.md`, which flags Git as a difficulty spike and recommends this game first.
- CodeAI CSP Unit 3, Intro to App Design (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/3`
- Laptop software stack and the provisioning scripts, if a machine is missing VS Code or Python: Section 8 of `curriculum/CS-Curriculum-and-Setup.md`.
- Account requirements and the age-13 note for GitHub: Section 12 of `curriculum/CS-Curriculum-and-Setup.md`.
