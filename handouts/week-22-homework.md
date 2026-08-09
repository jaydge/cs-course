# Week 22 Homework: A Real Project, in a Real Editor

This week you moved from Thonny to VS Code and learned how software actually gets built by teams. The homework makes your text adventure into a real project and gets you ready for next week, which is Git. Plan on about 45 minutes.

## 1. Finish the project layout

Your `adventure` folder lives inside your `CS Class` folder in Documents, the same folder you have been saving work into since Week 1. It should end up looking like this:

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
```

Get it running. Open the `adventure` folder in VS Code, open the terminal with Control and backtick, and from the project root type:

```bash
cd ~/Documents/"CS Class"/adventure
python3 main.py
```

The quotation marks are there because `CS Class` has a space in it, which is the Week 17 rule.

If you get `ModuleNotFoundError: No module named 'game'`, you are almost certainly in the wrong folder. Type `pwd` and check that you are in `adventure`, not in `adventure/game`.

Two things to check before you call it done:

- The interpreter shown in the VS Code status bar points inside your `.venv`.
- The game still plays exactly as it did in Week 16. Restructuring is not supposed to change behavior. That is the whole idea of refactoring.

## 2. Write the README and the .gitignore

Your `README.md` needs three things, and three sentences is enough:

1. What this program is.
2. How to run it, as an exact command someone could copy.
3. One thing it does not do yet.

Your `.gitignore` needs these four lines:

```
.venv/
__pycache__/
*.pyc
.DS_Store
```

Be ready to say, out loud, why the `.venv` folder should never be saved into version control.

## 3. Find your own technical debt

Open any program you wrote earlier this year. Pick one that works.

Find one piece of technical debt in it. Something copy-pasted three times, a number typed in five places, a variable named `x`, a function that does four unrelated jobs.

Write a short paragraph answering three questions:

1. What is the shortcut?
2. Suppose you had to make one specific change tomorrow. Name the change, and say how many places in the file you would have to edit.
3. What would you do differently if you rewrote that part now?

You do not have to fix it. Noticing it is the assignment.

## 4. Play Oh My Git, before next class

Next week is Git and version control, which confuses adults, so we are getting a head start.

Install and play "Oh My Git!" (`https://ohmygit.org`), which is free and open source. Get through at least the first few levels, far enough that you have seen a commit and a branch drawn as a picture. You do not have to understand it; you just need the shapes to be familiar rather than new.

## 5. Check your GitHub sign-in

Log in to your GitHub account and confirm it works. If your password is lost, reset it now with a parent, and store the new one in Bitwarden.

Do this before class. Next week's lab does not have time in it to fix accounts, and a broken login means you sit and watch.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. That includes AI extensions inside VS Code: do not install Copilot or anything like it. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

This week maps cleanly onto two real exam topics: 1.1 Collaboration and 1.3 Program Design and Development. The sprint simulation was collaboration with roles and iteration. The SDLC discussion was program design and development. Both show up on the exam, and both also show up in the written responses of the Create Performance Task later on.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 1, Intro and Computational Thinking. Work only the lessons on the program development process and on collaboration, then stop. The computational-thinking basics earlier in that unit are things we covered back in Units 1 through 3. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`. This is the best match in the whole CodeAI course for today. Do the design-process and collaboration lessons. The App Lab programming lessons in that unit are optional; they use JavaScript rather than Python, so treat them as a preview of Week 24 rather than as required work.

**Extra practice if you want it.**

- The exam expects you to know why a program is developed with input from other people, and what a development process gains from iteration. Write four sentences answering that, using the lunch-app simulation as your evidence. Keep the paragraph. It is genuinely useful practice for the kind of written response the Create Task asks for.
- Write a one-page project plan for something you would like to build: what it does, who it is for, the three things it must do, and the two things you would deliberately leave out of the first version. Deciding what to leave out is the skill.
- Read the Big Idea 1 section of `ap-track/AP-CSP-Topic-Coverage.md` and mark 1.1 and 1.3 as solid, shaky, or not yet.
