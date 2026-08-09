# Week 18 Homework: Living in the Shell

This week you did real work at the prompt: making and finding files, piping tools together, and running Python without pressing a Run button. The homework practices all of it. Plan on about 45 minutes.

Everything below happens inside `~/Documents/"CS Class"/sandbox`. Stay in the sandbox, and remember the rule: `rm` does not use the Trash. Remember the quotation marks too, or use Tab completion, which puts them in for you.

## 1. Shell tasks

Do each of these and write down both the command you used and what it printed. If you get an error, write the error down too; that is a real answer and we will look at it in class.

1. Make a folder called `homework18` inside the sandbox and move into it.
2. Create a file called `list.txt` containing the line `apples` (use `echo` and `>`).
3. Add three more lines to it, one at a time, without erasing what is already there. Then show the whole file.
4. Copy `list.txt` to `backup.txt`, then rename the copy to `list-old.txt`.
5. Count how many lines are in `list.txt`.
6. From your home folder, find every file anywhere in the sandbox whose name ends in `.txt`.

## 2. Build two pipelines

Use the `access.log` file in the sandbox's `logs` folder. Each of these is one line with at least one `|` in it. Write down the command and the answer.

1. How many lines in the log mention `404`?
2. How many different users appear in the log? (The username is the fifth field on each line. You will need `awk '{print $5}'`, then something to remove duplicates, then something to count.)

Then answer in a sentence: in your own words, what does the `|` character actually do?

## 3. Improve your script

Open `report.sh` from the sandbox's `logs` folder in Thonny (as a text editor, not to run it). Add one new line that reports something the script does not report yet: how many requests returned 404, how many different users there were, or the very first line of the log.

Save it, then run it from the terminal with `./report.sh` and write down the output. If it says "permission denied," you know what to do and why.

## 4. Python, from the terminal

Write a program called `find_lines.py` and save it in the `homework18` folder you made in task 1.

It should:

1. Read `access.log` from the sandbox's `logs` folder.
2. Print every line that contains the text `404`, without the extra blank line between them.
3. Write those same lines into a new file called `errors.txt`.
4. At the end, print how many it found.

Run it from the terminal with `python3 find_lines.py`, not from Thonny's Run button. Then use `cat errors.txt` and `wc -l errors.txt` to check that the file has what you expect.

A hint if you get stuck on step 2: every line you read from a file still has its newline on the end, and `print` adds another one.

## 5. One short answer

Two or three sentences. You now know two ways to work with files: the Finder or File Explorer, and the shell. Name one job where the graphical one is clearly better, and one job where the shell is clearly better. Say why for each.

## 6. Watch, if you want (optional)

Crash Course Computer Science, Episode 22, is about keyboards and command line interfaces, and explains why the prompt exists at all: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

The shell rule from last week still stands, and it matters more now that you know more commands: never run a command you do not understand, and never one that a stranger handed you.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**Another honest note: the shell is not on the AP exam either.** Pipes, scripts, `grep`, and running Python from a terminal are all outside the AP CSP framework. Two more weeks of this and then Week 19 lands squarely on Big Idea 4, which is genuinely tested.

**What to do with this week.** Pick one.

- **Project STEM (the AP spine):** no matching unit. Finish anything outstanding from earlier units. Hold off on Unit 6, Innovative Technologies; it covers the internet and cybersecurity and works much better alongside our Weeks 19 to 21 than ahead of them. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** no matching unit. If you are caught up, spend the week on Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`. This is the best use of the next two weeks for an AP-track student. Everything in it is on-topic for Weeks 19, 20, and 21, and next week alone throws IP, MAC, DNS, DHCP, NAT, routers, and switches at you in two hours.

**Extra practice if you want it.**

- The pipeline is decomposition, which is one of the computational thinking practices the exam does test. Write one paragraph explaining `grep alice access.log | wc -l` to someone who has never used a terminal, using the word "decomposition" honestly rather than as decoration.
- Add an argument to your shell script so that `./report.sh alice` reports only on one user. Inside a bash script, `$1` is the first argument given on the command line.
- Write a small version of `grep` in Python: a program that takes a filename and a word as command-line arguments (`sys.argv`) and prints every line of that file containing that word. Then run yours and the real `grep` on the same file and check that you get the same lines. Yours will be slower. That is worth thinking about.
