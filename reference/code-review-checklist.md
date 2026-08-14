# Code Exercise Review Checklist

A working inventory of every coding exercise in the course, for a systematic quality pass. One checkbox per exercise, grouped by week, chronological from Week 1 to Week 32.

## What counts as an exercise here

Any code a student is meant to write, run, or fill in: the builds and fill-in-the-blank work in `handouts/week-NN-homework.md`, and anything live-coded in `lessons/week-NN-teacher-guide.md` that a student types or runs themselves (Section 6's minute-by-minute flow and Section 7's scripts). Illustrative fragments in prose that nobody is meant to run are not listed. The halting-problem contradiction sketch in Week 14 is the clearest example of an excluded fragment: `will_it_finish` does not exist and cannot, which is the point of it.

Each week's Extra Credit AP Track section is out of scope for this pass, so the practice problems in those sections are not inventoried.

## Language markers

Most items are Python and run under plain `python3` with the standard library. Items in another runtime are marked, because they are verified differently:

- **[sh]** shell and terminal commands, verified in zsh or bash
- **[git]** git commands, verified against a scratch repository
- **[web]** HTML, CSS, or JavaScript, verified in a browser
- **[pkg]** needs a package beyond the standard library, per that week's own instructions (Week 20 says `requests` if installed or `urllib.request` if not; Week 25 installs Flask and requests into a venv)
- **[hw]** runs on classroom hardware or a hosted service rather than a student laptop
- **[paper]** worked by hand, then optionally checked on a machine

## How to run this pass

Written down so the work can continue from this file alone, on a different machine, with no memory of the thread that produced it.

**Work one exercise per turn, in checklist order.** Do not move to the next exercise in the same turn. Weeks build on each other, so chronological order is the default; skipping ahead means reviewing an exercise whose prerequisites have not been checked yet.

**For each exercise:**

1. Read it as currently written, in its handout and in its teacher guide context where it appears in both.
2. Actually run it. Set up a scratch directory outside the repo, reproduce what the student is asked to type or fill in, and execute it. Confirm it runs clean and produces the output the handout or guide claims. Clean up scratch files afterward; nothing from testing gets committed.
3. Evaluate in this priority order: correctness first; then whether a concept with a well-known teaching form uses that canonical form rather than a clever variant; then single-concept clarity, with boilerplate minimized or handled for the student so the concept stays the visual focus; then a deliberate check against over-engineering; then comments pitched at a first-time programmer.
4. Re-run after any edit.
5. Update every place the teacher guide echoes the exercise: Section 6's flow, Section 7's scripts, Section 10's homework summary.
6. Commit, then check the box here.

**Verify in the matching runtime.** Python items run under `python3` with the standard library only, unless that week says otherwise. Shell items run in bash or zsh. Git items run against a scratch repository, never this one. Web items are checked in a browser. Reasoning about whether code works is not verification.

**Package weeks get their packages installed for real.** Week 20 specifies `requests` if installed or `urllib.request` if not, so test the `urllib` path as the guaranteed one and the `requests` path when available. Week 25 has students install Flask and requests into a virtual environment, so build a scratch venv and run it. Respect exactly what each week specifies rather than assuming a package is present.

**Hardware items are the exception.** `[hw]` items depend on the Apple IIe, the classroom network, or the Raspberry Pi class server and cannot be reproduced on a review machine. Review them by reading, verify whatever part runs locally, and say plainly in the report which part went unverified. W1-1, the Apple IIe BASIC program, is verified by the instructor on the hardware rather than by review.

**What not to change.** An exercise that is already correct, clear, and using a standard pattern needs no change; "no changes needed" is a normal outcome. Do not replace a plain loop with a comprehension, a manual conditional with a clever one-liner, or an explicit pattern with a smarter abstraction. For students who are not experienced programmers, the more explicit and more textbook-proven form is the correct one even where a more compact form exists. Only add sophistication where that sophistication is the actual point of the week's lesson. Do not touch anything outside the current exercise's scope, and do not touch that week's Extra Credit AP Track section or its AP-alignment claims unless a change genuinely forces it.

**Conventions that bind any rewrite** are in the repository README. The two that matter most here: coding exercises prefer skeletons, fill-in-the-blank sections, and "here is the pattern, now apply it" over a complete solution a student could paste in without understanding it; and surrounding prose is plain, with no em dashes, no emojis, and no sales language.

**Commits.** One commit per exercise, or per week where a week's exercises are small and tightly related. Never batch multiple weeks into one commit. Author `JD Smith <jaydge@gmail.com>`. The message says what was tested and what changed, or "verified as-is, no changes" where nothing needed fixing. The checkbox update here can ride along with that commit or be its own.

**If confidence is low,** say so and ask rather than guessing, particularly about whether a claimed pattern really is the canonical one.

---

## Week 1: What is a computer?

- [ ] W1-1: Apple IIe BASIC `10 PRINT "HELLO" / 20 GOTO 10 / RUN` (lessons/week-01-teacher-guide.md, Segment 1) **[hw]**. A typed command becomes machine action.
- [ ] W1-2: first `print("hello")` in Thonny, then edit the string and rerun (lessons/week-01-teacher-guide.md, Segment 4). Running and saving a first program.

## Week 2: Why only 1s and 0s?

- [ ] W2-1: greeting program with `input` and a variable, extended with a second question (lessons/week-02-teacher-guide.md, Segment 3; handouts/week-02-homework.md, item 2). Variables and input.
- [ ] W2-2: the `input` returns a string trap and the `int()` fix, then double a number (lessons/week-02-teacher-guide.md, Segment 6; handouts/week-02-homework.md, item 2). Types and conversion.
- [ ] W2-3: five-bit binary converter skeleton, no loops (lessons/week-02-teacher-guide.md, Segment 6 extension). Place value in code, deliberately repetitive.

## Week 3: How do we tell a computer what to do?

- [ ] W3-1: if/elif/else on age, plus the `=` versus `==` deliberate error (lessons/week-03-teacher-guide.md, Segment 5). Conditionals and indentation.
- [ ] W3-2: positive, negative, or zero, then `and`/`or`/`not` for single digit (lessons/week-03-teacher-guide.md, Segment 5). Three-way branching and boolean operators.
- [ ] W3-3: number-guessing game, fixed secret, three written-out guesses (lessons/week-03-teacher-guide.md, Segment 6). Conditionals as a game.
- [ ] W3-4: trace three conditional snippets on paper (handouts/week-03-homework.md, item 2) **[paper]**. Reading code without running it.
- [ ] W3-5: improve the guessing game with distance-off and a named welcome (handouts/week-03-homework.md, item 3). Absolute difference via `if`.

## Week 4: Loops and borrowed code

- [ ] W4-1: `for i in range(...)` tour, including `range(1, 6)` and `range(5, 0, -1)` (lessons/week-04-teacher-guide.md, Segment 2). Counted iteration and off-by-one.
- [ ] W4-2: `while` loop accumulator, plus the deliberate infinite loop (lessons/week-04-teacher-guide.md, Segment 2). Condition-controlled iteration.
- [ ] W4-3: `import random` and `random.randint(1, 10)` into the guessing game (lessons/week-04-teacher-guide.md, Segment 3). Libraries.
- [ ] W4-4: calculator with an operator choice and a divide-by-zero guard, looping until quit (lessons/week-04-teacher-guide.md, Segment 6; handouts/week-04-homework.md, item 1).
- [ ] W4-5: Rock Paper Scissors against the computer, best of five with a score (lessons/week-04-teacher-guide.md, Segment 6; handouts/week-04-homework.md, item 1).
- [ ] W4-6: trace three loop snippets, one with a missing decrement (handouts/week-04-homework.md, item 2) **[paper]**.

## Week 5: Functions and finding bugs

- [ ] W5-1: `def greet()` then `def add(a, b)` with `return`, define versus call (lessons/week-05-teacher-guide.md, Segment 2). Functions, parameters, return.
- [ ] W5-2: three student functions: print a greeting, return the larger, return whether even (lessons/week-05-teacher-guide.md, Segment 2).
- [ ] W5-3: the three debugging moves on prepared broken programs (lessons/week-05-teacher-guide.md, Segment 3). Tracebacks, print debugging, the Thonny stepper.
- [ ] W5-4: Hangman with `pick_word` and `show_progress` (lessons/week-05-teacher-guide.md, Segment 5; handouts/week-05-homework.md, item 1). Decomposition into functions.
- [ ] W5-5: refactor a Week 4 program by extracting one function (handouts/week-05-homework.md, item 2).
- [ ] W5-6: debug three broken functions: `NameError`, print-instead-of-return, bad indentation (handouts/week-05-homework.md, item 3).

## Week 6: Gates and lists

- [ ] W6-1: list creation, indexing, `len`, assignment, negative index, and the deliberate `IndexError` (lessons/week-06-teacher-guide.md, Segment 6). Lists and zero-indexing.
- [ ] W6-2: a list of five things: print all, print one, change one, print the length (lessons/week-06-teacher-guide.md, Segment 6; handouts/week-06-homework.md, item 3).
- [ ] W6-3: gate lookup table, `and_table[a * 2 + b]`, extended to OR and NOT (lessons/week-06-teacher-guide.md, Segment 6; handouts/week-06-homework.md, item 4). A list as a lookup table.

## Week 7: From gates to a machine, and lists that change

- [ ] W7-1: list methods: `append`, `remove`, `pop`, `sort`, and `in` (lessons/week-07-teacher-guide.md, Coding strand; handouts/week-07-homework.md, item 3). Mutating a list.
- [ ] W7-2: `for item in list` traversal, contrasted with index-based iteration, then a running total (lessons/week-07-teacher-guide.md, Coding strand). Traversal and the accumulator pattern.
- [ ] W7-3: find the largest value with a loop, no `max()` (lessons/week-07-teacher-guide.md, Coding strand; handouts/week-07-homework.md, item 4). The best-so-far pattern.

## Week 8: Inside the case, and text as data

- [ ] W8-1: strings as sequences: index, negative index, `len`, `in` (lessons/week-08-teacher-guide.md, Coding strand).
- [ ] W8-2: slicing `word[0:4]`, `word[4:]`, `word[:4]`, with predict-before-run (lessons/week-08-teacher-guide.md, Coding strand; handouts/week-08-homework.md, item 4).
- [ ] W8-3: iterate the characters of a string, then `upper`, `strip`, `split` (lessons/week-08-teacher-guide.md, Coding strand).
- [ ] W8-4: text analyzer: character count, word count, vowel count (lessons/week-08-teacher-guide.md, Coding strand; handouts/week-08-homework.md, item 5).
- [ ] W8-5: print a word backwards, by loop or by slice (lessons/week-08-teacher-guide.md, Coding strand build two).
- [ ] W8-6: palindrome check added to the analyzer, case-insensitive (handouts/week-08-homework.md, item 5).

## Week 9: The board, the boot, and loops inside loops

- [ ] W9-1: nested `for` loops, the hours-and-minutes model (lessons/week-09-teacher-guide.md, Coding strand).
- [ ] W9-2: multiplication table with `end="\t"` and the deliberately misindented `print()` (lessons/week-09-teacher-guide.md, Coding strand).
- [ ] W9-3: three shapes: 5 by 5 square, left-aligned triangle, right-aligned triangle (lessons/week-09-teacher-guide.md, Coding strand; handouts/week-09-homework.md, item 5).
- [ ] W9-4: trace three nested-loop snippets, including the indentation bug (handouts/week-09-homework.md, item 4) **[paper]**.

## Week 10: From a key press to a pixel

- [ ] W10-1: `dis.dis(add)` on a two-line function, then on one of their own (lessons/week-10-teacher-guide.md, Segment 5; handouts/week-10-homework.md, item 3). Code becomes instructions.
- [ ] W10-2: `dis.dis("x = 2 + 3")` constant folding (lessons/week-10-teacher-guide.md, Segment 5).
- [ ] W10-3: compare the bytecode of a loop with the same work written out three times (lessons/week-10-teacher-guide.md, Segment 5, if time). A loop is a backward jump.

## Week 11: Dictionaries and modeling real data

- [ ] W11-1: dictionary basics: create, look up, add, replace, `del` (lessons/week-11-teacher-guide.md, Segment 3).
- [ ] W11-2: the deliberate `KeyError`, then the `in` guard and `.get()` with a default (lessons/week-11-teacher-guide.md, Segment 3).
- [ ] W11-3: iterate with `.items()` (lessons/week-11-teacher-guide.md, Segment 3).
- [ ] W11-4: five capital cities keyed by country: lookup, add, change, print with a loop (lessons/week-11-teacher-guide.md, Segment 3).
- [ ] W11-5: nested dictionary record, double subscript (lessons/week-11-teacher-guide.md, Segment 4; handouts/week-11-homework.md, item 2).
- [ ] W11-6: contact manager with `add_contact`, `find_contact`, `list_contacts` and a menu loop (lessons/week-11-teacher-guide.md, Segment 6; handouts/week-11-homework.md, item 1).
- [ ] W11-7: predict then run four dictionary snippets, two of which raise (handouts/week-11-homework.md, item 3).

## Week 12: Classes and objects

- [ ] W12-1: the dictionary-plus-loose-function version of a pet, before classes (lessons/week-12-teacher-guide.md, Segment 3). The problem classes solve.
- [ ] W12-2: `Pet` class with `__init__` and `feed`, and two independent instances (lessons/week-12-teacher-guide.md, Segment 3).
- [ ] W12-3: add `play` and `describe`, plus the two deliberate `self` errors (lessons/week-12-teacher-guide.md, Segment 5). Return versus print, and `self.`.
- [ ] W12-4: `Item` class with `total_value`, held in a list and looped over (lessons/week-12-teacher-guide.md, Segment 6; handouts/week-12-homework.md, item 1).
- [ ] W12-5: a second class that holds objects of the first (`Shelter`, `Backpack`, or `Party`) (handouts/week-12-homework.md, item 2).
- [ ] W12-6: trace three class snippets: two counters, a bound method printed without parentheses, a shadowed attribute (handouts/week-12-homework.md, item 3).

## Week 13: Stacks, queues, and the shape of data

- [ ] W13-1: a stack from a list with `append` and `pop` (lessons/week-13-teacher-guide.md, Segment 5).
- [ ] W13-2: a queue from a list with `append` and `pop(0)`, and the empty-list crash (lessons/week-13-teacher-guide.md, Segment 5).
- [ ] W13-3: `push_task` and `pop_task` with an empty guard, and the same shape for the print queue (lessons/week-13-teacher-guide.md, Segment 5; handouts/week-13-homework.md, item 1).
- [ ] W13-4: linked list: `Node` class, three nodes, traversal loop, then splice a fourth in (lessons/week-13-teacher-guide.md, Segment 6).
- [ ] W13-5: indexing drill, including `letters[5]` and the last-index rule (handouts/week-13-homework.md, item 4) **[paper]**.

## Week 14: Searching, sorting, and what cannot be done

- [ ] W14-1: linear search versus binary search race, timed, with a step counter (lessons/week-14-teacher-guide.md, Segment 3; handouts/week-14-homework.md, item 1). The canonical binary search loop.
- [ ] W14-2: bubble sort versus the built-in sort, run from a starter file (lessons/week-14-teacher-guide.md, Segment 3). The canonical bubble sort, watched rather than typed.
- [ ] W14-3: break binary search by shuffling the list first (lessons/week-14-teacher-guide.md, Segment 3). The sorted precondition.

## Week 15: Debugging and testing

- [ ] W15-1: a two-frame traceback from `report([])` calling `average` (lessons/week-15-teacher-guide.md, Segment 3). Reading the call stack.
- [ ] W15-2: `assert` on `is_even`, then break the function so a test fails (lessons/week-15-teacher-guide.md, Segment 5).
- [ ] W15-3: group assertions into `test_is_even()` and call it, including the `is_even(0)` edge case (lessons/week-15-teacher-guide.md, Segment 5).
- [ ] W15-4: write tests for two functions from Weeks 11 and 13, one an edge case (lessons/week-15-teacher-guide.md, Segment 5).
- [ ] W15-5: Tic-Tac-Toe skeleton: `LINES`, `new_board`, `winner`, and the game loop (lessons/week-15-teacher-guide.md, Segment 6; handouts/week-15-homework.md, item 1).
- [ ] W15-6: `test_winner()` with three assertions (lessons/week-15-teacher-guide.md, Segment 6; handouts/week-15-homework.md, item 1).
- [ ] W15-7: read three tracebacks and name the real mistake (handouts/week-15-homework.md, item 2) **[paper]**.
- [ ] W15-8: `is_full` with an early `return True`: write the failing test first, then fix (handouts/week-15-homework.md, item 3).

## Week 16: Finish the world, run the simulation

- [ ] W16-1: `rooms` as a dictionary of dictionaries, with exits as keys (lessons/week-16-teacher-guide.md, Segment 3).
- [ ] W16-2: `Player` class with `move` returning True or False, and `take` left to the student (lessons/week-16-teacher-guide.md, Segment 3).
- [ ] W16-3: the game loop skeleton with `quit` and an unknown-command branch (lessons/week-16-teacher-guide.md, Segment 3; handouts/week-16-homework.md, item 1).
- [ ] W16-4: dice simulation, counts in a dictionary, asterisk histogram with a `bar` divisor (lessons/week-16-teacher-guide.md, Segment 5; handouts/week-16-homework.md, item 2).
- [ ] W16-5: random walk, then 1000 walks counting how many end more than 20 from the start, using `abs()` (lessons/week-16-teacher-guide.md, Segment 5).

## Week 17: The machine underneath

- [ ] W17-1: terminal navigation sequence: `pwd`, `whoami`, `cd ~`, `ls`, quoted path, `ls -la`, `cd ..` (handouts/week-17-homework.md, item 1) **[sh]**.
- [ ] W17-2: read one `ls -l` permission line piece by piece (handouts/week-17-homework.md, item 2) **[sh]**.
- [ ] W17-3: `pathlib` directory lister with `Path.home()`, `iterdir`, `is_dir`, `stat().st_size` (lessons/week-17-teacher-guide.md, Segment 6).
- [ ] W17-4: extend the lister: filter `.txt`, total the sizes, or count directories, saved as `list_folder.py` (lessons/week-17-teacher-guide.md, Segment 6; handouts/week-17-homework.md, item 3).

## Week 18: Living in the shell

- [ ] W18-1: the challenge course: `mkdir`, `echo` with `>` and `>>`, `cp`, `mv`, `wc -l`, `find` (lessons/week-18-teacher-guide.md, Segment 3; handouts/week-18-homework.md, item 1) **[sh]**.
- [ ] W18-2: two pipelines over `access.log`, counting 404s and distinct users with `awk`, `sort`, `uniq`, `wc` (lessons/week-18-teacher-guide.md, Segment 3; handouts/week-18-homework.md, item 2) **[sh]**.
- [ ] W18-3: `report.sh`, made executable, with one line added by the student (lessons/week-18-teacher-guide.md, Segment 5; handouts/week-18-homework.md, item 3) **[sh]**.
- [ ] W18-4: run `hello.py` from the terminal with `python3`, not the Run button (lessons/week-18-teacher-guide.md, Segment 6).
- [ ] W18-5: `sys.argv` argument printer, run as `python3 args.py apple banana` (lessons/week-18-teacher-guide.md, Segment 6).
- [ ] W18-6: read a file with `with open(...)`, filter for `404`, `strip()` the newline (lessons/week-18-teacher-guide.md, Segment 6).
- [ ] W18-7: write matching lines out to `errors.txt`, and the `"w"` versus `"a"` caution (lessons/week-18-teacher-guide.md, Segment 6).
- [ ] W18-8: count how many log lines mention each of two usernames, and check it against the pipeline (lessons/week-18-teacher-guide.md, Segment 6).
- [ ] W18-9: `find_lines.py`, combining read, filter, write, and count (handouts/week-18-homework.md, item 4).

## Week 19: Finding one machine out of billions

- [ ] W19-1: network commands: `ifconfig`, `networksetup`, `netstat -rn`, `ping` (handouts/week-19-homework.md, item 1) **[sh]**.
- [ ] W19-2: `traceroute` to a distant site, reading hops and `* * *` (handouts/week-19-homework.md, item 2) **[sh]**.
- [ ] W19-3: `socket.gethostname()` and `socket.gethostbyname()` (lessons/week-19-teacher-guide.md, Segment 6).
- [ ] W19-4: `ipaddress.ip_network("192.168.1.0/24")`, `num_addresses`, and membership tests (lessons/week-19-teacher-guide.md, Segment 6).
- [ ] W19-5: loop a list of site names, printing each name beside its address, saved as `lookup.py` (lessons/week-19-teacher-guide.md, Segment 6; handouts/week-19-homework.md, item 4).
- [ ] W19-6: time the same lookup twice with `time.time()` and explain the difference (lessons/week-19-teacher-guide.md, Segment 6; handouts/week-19-homework.md, item 4).

## Week 20: Reading the wire

- [ ] W20-1: serve a folder with `python3 -m http.server 8080`, then request a missing file (lessons/week-20-teacher-guide.md, Segment 2; handouts/week-20-homework.md, item 1) **[sh]**.
- [ ] W20-2: `requests.get` printing status code, `Content-Type`, and body (lessons/week-20-teacher-guide.md, Segment 7) **[pkg]**.
- [ ] W20-3: the `urllib.request.urlopen` version for fleets without `requests` (lessons/week-20-teacher-guide.md, Segment 7).
- [ ] W20-4: `fetch.py` requesting three paths including a 404, printing path and status (handouts/week-20-homework.md, item 3) **[pkg]**.

## Week 21: The whole story

- [ ] W21-1: `ssh` to the class server, then `whoami`, `hostname`, `uname -a`, `pwd`, `ls`, `who`, `exit` (lessons/week-21-teacher-guide.md, Segment 3) **[sh] [hw]**.
- [ ] W21-2: `git clone` over SSH, `git log --oneline`, and run the cloned `puzzles/hello.py` (lessons/week-21-teacher-guide.md, Segment 3) **[git] [hw]**.
- [ ] W21-3: explore the cloned repository, including finding `.git` (handouts/week-21-homework.md, item 3) **[sh]**.

## Week 22: A real project, in a real editor

- [ ] W22-1: create and activate a virtual environment, and select the interpreter (lessons/week-22-teacher-guide.md, Segment 6) **[sh]**.
- [ ] W22-2: split the text adventure into `main.py`, `game/world.py`, `game/player.py`, with the package imports (lessons/week-22-teacher-guide.md, Segment 7; handouts/week-22-homework.md, item 1).
- [ ] W22-3: the four-line `.gitignore` (lessons/week-22-teacher-guide.md, Segment 7; handouts/week-22-homework.md, item 2).
- [ ] W22-4: a three-part `README.md` with an exact run command (handouts/week-22-homework.md, item 2).

## Week 23: Your own repository

- [ ] W23-1: `git init`, `status`, `add`, `commit`, `log`, `diff` on the adventure project (lessons/week-23-teacher-guide.md, Segment 3) **[git]**.
- [ ] W23-2: the collaborative lab: clone, branch, commit, push, review, merge, and the rejected push (lessons/week-23-teacher-guide.md, Segment 5) **[git] [hw]**.
- [ ] W23-3: cause and resolve a merge conflict in pairs (lessons/week-23-teacher-guide.md, Segment 6) **[git]**.
- [ ] W23-4: push the adventure project to GitHub and confirm `.venv` is absent (handouts/week-23-homework.md, item 1) **[git]**.
- [ ] W23-5: branch, change, merge, and cause a conflict alone, with `git merge --abort` as the escape (handouts/week-23-homework.md, items 2 and 3) **[git]**.

## Week 24: Finish your page

- [ ] W24-1: HTML skeleton: doctype, `lang`, charset, viewport, title, stylesheet link (lessons/week-24-teacher-guide.md, Segment 3) **[web]**.
- [ ] W24-2: semantic body with `header`, `main`, `section`, `footer`, a list, and two ids (lessons/week-24-teacher-guide.md, Segment 3; handouts/week-24-homework.md, item 1) **[web]**.
- [ ] W24-3: the stylesheet: element, id, and class selectors, the box model, `max-width` and `margin: auto` (lessons/week-24-teacher-guide.md, Segment 5; handouts/week-24-homework.md, item 1) **[web]**.
- [ ] W24-4: the fact button: `getElementById`, `addEventListener`, `textContent`, `Math.floor(Math.random() * n)` (lessons/week-24-teacher-guide.md, Segment 6; handouts/week-24-homework.md, item 1) **[web]**.
- [ ] W24-5: look up one new CSS property on MDN and use it with a comment (handouts/week-24-homework.md, item 2) **[web]**.
- [ ] W24-6: a second button, or a click counter with `let count = 0` (handouts/week-24-homework.md, item 3) **[web]**.

## Week 25: Live data, and what it will not tell you

- [ ] W25-1: the smallest Flask app: `@app.route("/")` returning a string (lessons/week-25-teacher-guide.md, Segment 3) **[pkg]**.
- [ ] W25-2: add the API call and `render_template` with named values (lessons/week-25-teacher-guide.md, Segment 3) **[pkg]**.
- [ ] W25-3: move the Week 24 page into `templates/` and `static/`, with `url_for` and `{{ }}` placeholders (lessons/week-25-teacher-guide.md, Segment 3) **[pkg] [web]**.
- [ ] W25-4: `try` and `except requests.RequestException`, with exactly one return taken (lessons/week-25-teacher-guide.md, Segment 3; handouts/week-25-homework.md, item 1) **[pkg]**.
- [ ] W25-5: `explore.py`: load the CSV with `DictReader`, report rows, columns, and the first record (lessons/week-25-teacher-guide.md, Segment 5; handouts/week-25-homework.md, item 2).
- [ ] W25-6: filter by magnitude, with the empty-value guard and the deliberate `ValueError` (lessons/week-25-teacher-guide.md, Segment 5; handouts/week-25-homework.md, item 2).
- [ ] W25-7: count by region into a dictionary, then sort by count (lessons/week-25-teacher-guide.md, Segment 5; handouts/week-25-homework.md, item 2).
- [ ] W25-8: count by hour from a sliced timestamp and draw the asterisk chart (lessons/week-25-teacher-guide.md, Segment 5; handouts/week-25-homework.md, item 2).

## Week 26: Make it an app

- [ ] W26-1: `static/manifest.json` and the `<link rel="manifest">` (lessons/week-26-teacher-guide.md, Segment 5) **[web]**.
- [ ] W26-2: the `/sw.js` Flask route with `send_from_directory`, and why scope requires it (lessons/week-26-teacher-guide.md, Segment 5) **[pkg]**.
- [ ] W26-3: `static/sw.js` with install, activate, and network-first fetch handlers (lessons/week-26-teacher-guide.md, Segment 5) **[web]**.
- [ ] W26-4: `static/offline.html`, and the honest stale-data line added to it (lessons/week-26-teacher-guide.md, Segment 5; handouts/week-26-homework.md, item 2) **[web]**.
- [ ] W26-5: register the service worker from `static/script.js`, with the feature check and the `.catch` (lessons/week-26-teacher-guide.md, Segment 5) **[web]**.

## Week 27: A machine that learns, and a new rule

- [ ] W27-1: `perceptron.py`: weights, bias, `predict`, and the epoch training loop that learns AND (lessons/week-27-teacher-guide.md, Segment 3; handouts/week-27-homework.md, item 1).
- [ ] W27-2: change the targets to OR, then to XOR, and watch XOR never converge (lessons/week-27-teacher-guide.md, Segment 3; handouts/week-27-homework.md, item 1).

## Week 28: Locks, hashes, and your own front door

- [ ] W28-1: `hashing.py`: a `sha256` helper, and three near-identical inputs showing the avalanche effect (lessons/week-28-teacher-guide.md, Segment 4; handouts/week-28-homework.md, item 3).
- [ ] W28-2: crack a stolen hash by hashing a list of common passwords (lessons/week-28-teacher-guide.md, Segment 4).
- [ ] W28-3: add a salt and watch the same attack fail (lessons/week-28-teacher-guide.md, Segment 4).

## Week 29: Somebody else's computer

No coding exercise this week. The session is systems tours plus the speedup arithmetic in handouts/week-29-homework.md, item 1, which is worked by hand. Listed here so the gap is deliberate rather than an oversight.

## Week 30: Who does this help, and who does it hurt?

No new coding exercise. Segment 8 is protected work time on the final project, and the homework is writing plus project progress.

## Week 31: Finish it

No new coding exercise. The whole session is build time on the student's own final project, under a no-new-features rule.

## Week 32: The last sheet

No coding exercise. Demo day and course close.
