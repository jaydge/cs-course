# Week 17 Homework: The Machine Underneath

This week you met the operating system and opened a terminal for the first time. None of the ideas are hard; the terminal is just picky about spelling. Keep your command card next to you. Plan on about 40 minutes.

## 1. Navigate, and write down what you see

Open a terminal on your own computer. Mac: Terminal, in Applications, Utilities. Windows: Windows Terminal, Ubuntu profile.

Run these one at a time and write down the output of each. If a command gives an error, write down the error too; that counts as an answer.

```bash
pwd
whoami
cd ~
ls
cd ~/cs-sandbox
ls -la
cd ..
pwd
```

Then answer these in a sentence each:

1. What did `pwd` print the very first time you ran it?
2. What is the difference between what `ls` shows and what `ls -la` shows?
3. What did `cd ..` do to where you were?
4. Press the Up arrow at the prompt. What happens, and why is that useful?

## 2. Read a permission line

Run `ls -l` inside `cs-sandbox` and copy one line exactly as it appears. Then explain it piece by piece:

1. What does the very first character tell you?
2. What may the owner of this file do to it?
3. What may everybody else on the machine do to it?
4. Who owns it?

Then find a folder in the listing (or run `ls -ld ~`) and say what is different about the first character on that line.

## 3. Count what is running

Open Activity Monitor on a Mac, or Task Manager on Windows.

1. How many processes are running right now?
2. How many of those did you personally start?
3. Pick one process you do not recognize and write down its name. Do not quit it. We will talk about a few of these in class.

Then do the same thing from the terminal with `ps aux | head -20` and write down one line from the output.

## 4. Extend the directory lister

Open Thonny and start from the program we wrote in class:

```python
from pathlib import Path

folder = Path.home() / "cs-sandbox"

for item in sorted(folder.iterdir()):
    kind = "dir " if item.is_dir() else "file"
    print(kind, item.name, item.stat().st_size)
```

Change it so that it does one of the following. Pick whichever you like; one, done properly, is enough.

- Print only the items whose name ends in `.txt`.
- Print the total size of everything in the folder, added up.
- Print how many items are folders and how many are files.

Save it into your CS Class folder as `list_folder.py`.

## 5. One paragraph

In your own words, three or four sentences: what is a process, and why can your computer appear to run twenty programs at once when it only has a handful of cores?

## 6. Watch, if you want (optional)

Crash Course Computer Science, Episode 18 covers operating systems and Episode 20 covers files and file systems. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

## A safety note, and it is a real one

Two rules for the terminal, starting now:

- Anything you delete from the terminal does not go to the Trash or the Recycle Bin. It is gone. Read a delete command twice before pressing Return.
- If anyone anywhere, a website, a video, a message, a person you do not know, tells you to paste a command starting with `sudo` into your terminal, do not do it. Bring it to class instead. That is one of the oldest tricks there is.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

This especially applies to the terminal. Typing a command you do not understand teaches you nothing and occasionally deletes something. Understand it, then type it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**An honest note first: none of this week is on the AP exam.** Operating systems, processes, threads, file permissions, and the command line are not in the AP CSP framework at all. Big Idea 4 is about the internet, and that starts in our Week 19. So there is no unit that matches today, and pretending otherwise would waste your time.

**What to do with this week instead.** Pick one.

- **Project STEM (the AP spine):** nothing matches. Use the week to finish anything you left unfinished, most likely in Unit 2, Programming. The nearest topical unit is Unit 6, Innovative Technologies, which covers the internet and cybersecurity, but that lines up with our Weeks 19 to 21 and there is no advantage to starting it two weeks early. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** also no match. If you are caught up, this is a good week to start Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`, early. That unit is where our next three weeks live, and Week 19 throws a lot of acronyms at you in two hours. Arriving already knowing what IP, DNS, and a packet are will make that session much easier.

**Extra practice if you want it.**

- The one real AP idea in today's session is abstraction: the exam asks what an abstraction hides and why hiding it helps. Write one paragraph on this: your Python program never touches the disk, it asks the operating system to. What does that hide from you, and name one thing that becomes possible because it is hidden.
- Find out what your machine's total memory is from the terminal (`vm_stat` on a Mac, `free -h` on Ubuntu) and compare it to what Activity Monitor or Task Manager says. They will not agree exactly. Work out why.
- Rewrite your directory lister so that it searches every folder inside `cs-sandbox` too, not just the top level. Look up `rglob` in the `pathlib` documentation at `https://docs.python.org/3/library/pathlib.html`.
