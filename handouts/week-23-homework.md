# Week 23 Homework: Your Own Repository

In class you worked in the class book with everyone else. This week you do it alone, on your own project, on GitHub, and you break it on purpose one more time. Plan on about 50 minutes.

Keep your Git cheat sheet next to you. Nobody memorizes these commands in one week.

## 1. Put your project on GitHub

Your `adventure` project is already a repository on your laptop from Segment 3 in class. Now give it a home on the internet.

1. On `github.com`, signed in, create a new repository named `adventure`. Do not let GitHub add a README, a `.gitignore`, or a license; you already have those, and adding them makes a mess on the first push.
2. From the page of setup commands GitHub shows you, use the "push an existing repository" ones:

   ```bash
   cd ~/Documents/"CS Class"/adventure
   git remote add origin <the URL GitHub gave you>
   git branch -M main
   git push -u origin main
   ```
3. Reload the GitHub page. Your files are there.

Then check one thing, which is the actual point of the exercise: is there a `.venv` folder in the file list? There should not be. If there is, your `.gitignore` is not doing its job, so bring it to class.

## 2. Branch, change, merge

1. Make a branch: `git switch -c experiment`
2. On that branch, change something you are not sure about. Make it genuinely risky if you like; that is what branches are for.
3. Commit it, with a message that says what changed and why, in one line:

   ```bash
   git add .
   git commit -m "Add the cellar's locked door"
   ```

   Rule for the message: someone reading your log a year from now should be able to tell whether the change they are hunting for is in that commit. "stuff" and "update" fail that test.
4. Run `git switch main` and look at your files. Your change is gone. It is not lost, it is on the other branch. Sit with that for a second; that is the whole idea.
5. Run `git log --oneline --graph --all` and find both branches in the picture.
6. Merge it in: `git merge experiment`, then `git push`.

## 3. Cause a conflict, alone

You need two branches that change the same line. Here is the recipe:

1. `git switch main`, then `git pull`.
2. Open your `README.md` and add a line at the bottom that says `Status: unfinished`. Commit it on `main`.
3. `git switch -c cleanup`. On this branch, change that same line to `Status: works, mostly`. Commit it.
4. `git switch main`. Change that same line again, to `Status: playable`. Commit it.
5. `git merge cleanup`.

You should get `CONFLICT (content): Merge conflict in README.md`. Take a screenshot of it before you touch anything, save the screenshot in your `CS Class` folder, and bring it to class.

Now finish it. Run `git status` and read it. Open the file, find the `<<<<<<<`, `=======`, and `>>>>>>>` lines, and edit it so it has exactly one status line, the one you actually want, with all three marker lines deleted. Then `git add README.md`, `git commit`, and `git push`.

If you get lost at any point, `git merge --abort` puts everything back exactly as it was. Using it is not failing.

## 4. Explain it in your own words

Two short answers, a few sentences each. Write them in a file or on paper.

1. What is a commit, and what does it contain? Say why "a list of the lines I changed" is not quite right.
2. A merge conflict happens. Is anything broken? What is Git actually asking you for, and how do you answer it?

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

One extra thing about Git: when a command fails, read the error. Git's messages usually name the exact next command to run.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**Straight answer first: Git is not on the AP exam.** No question will ask you what a commit is or how to resolve a merge conflict. Nobody should study Git for the exam.

What is on the exam is topic 1.1 Collaboration, and today was a genuine example of it. When the exam asks why programs are developed collaboratively, or what reviewing another programmer's work is for, you now have a real answer instead of a memorized one. The same is true of the Create Performance Task written response, which asks about collaboration if you had any.

The other reason to care: if you do the Create Task in the spring, your program will exist for weeks before it is finished. Putting it in a repository is how a dead laptop stops being a catastrophe.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 1, Intro and Computational Thinking, and only the collaboration lessons. This is a thin slice, and if you already worked it last week then there is genuinely nothing new here. In that case, spend the hour getting ahead in Unit 2, Programming, instead. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`. Work only the collaboration lessons.

**Extra practice if you want it.**

- Open a real pull request. Pair with someone in the class, give each other access to your GitHub repositories, push a branch to your partner's repository, and open a pull request from it. Leave a review comment in the web interface, then have your partner merge it. This is exactly what professional teams do all day, and the web view makes the review conversation visible in a way sticky notes do not.
- On GitHub, find any open source project you have heard of and read its most recent ten commits. Ask yourself which of the messages actually tell you what changed.
- Find out what `git rebase` does and write three sentences on why this class uses `git merge` instead. There is a real tradeoff and there is no single right answer.
