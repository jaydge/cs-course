# Week 23 Teacher Guide

## 1. Header

- **Week:** 23 of 32
- **Unit:** 5, Building Modern Software
- **Theme question:** How do many people change the same code without destroying it?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Explain what a commit is: a named snapshot of the whole project, with a parent, an author, and a message.
- Initialize a repository, stage changes, commit them, and read `git log` and `git diff`.
- Explain what a branch is and why working on one is safer than working on `main`.
- Clone from the class server, push a branch, and merge it into `main`.
- Read another student's change as a diff and give one specific piece of review feedback.
- Cause a merge conflict, read the conflict markers, and resolve it deliberately.
- Say what `.gitignore` is for, having watched it work.

## 3. Where this sits

Week 21 ended Unit 4 with SSH into the class server and a first `git clone` purely as a taste, with no explanation. Today is the explanation, and it is the hardest single session in Unit 5. The readiness guide flags Git as one of the course's genuine difficulty spikes, and it is right: the commit and branch model confuses working adults, not just fourteen-year-olds.

Three things make it reachable. Students have used a real terminal since Week 18, so typing commands is not the obstacle. They built a `.gitignore` last week without knowing why, and today it earns its keep. And they were assigned Oh My Git as homework, so the graph shapes have been seen once already.

Everything downstream depends on this. Week 24's page, Week 25's Flask app, Week 26's PWA, and the Unit 6 final project all live in repositories. This is also the last week of the unit that is mostly about process rather than product, so protect the lab time.

Worth using in class: this course's own repository is a real repository with real history. Showing `git log` on the material they are holding is the most convincing demonstration available, and it costs two minutes.

## 4. Materials and setup

- The MacBook class server, awake, on the classroom network, with SSH reachable and the seeded `classbook.git` repository in place (see Section 5).
- Each student's laptop with Git installed, VS Code, and their working SSH access from Week 21 verified.
- Every student's GitHub account confirmed working, done last week, not today.
- Projector at a large font, with a terminal and VS Code both open on the demo machine.
- Whiteboard with the theme question, and a large clear area kept free all session for the commit graph. Do not erase it.
- Sticky notes, about ten per student, for the unplugged graph.
- Printed one-page Git command cheat sheet, one per student. Write it from Sections 6 and 7 of this guide.
- Printed Week 23 homework handout, one per student.

## 5. Pre-class prep checklist

- **Set up the class server repository.** On the server, as an admin:

  ```bash
  cd /Users/Shared/repos
  sudo git init --bare -b main --shared=group classbook.git
  sudo chgrp -R staff classbook.git
  sudo chmod -R g+rwX classbook.git
  ```

  This is the same `/Users/Shared/repos` folder used for the Week 21 `hello-class.git` taste, so the path and the SSH accounts are already familiar. Three things matter here. The `-b main` flag avoids a version-dependent surprise where a bare repository defaults to `master`. The `--shared=group` flag plus the group ownership is what allows several students, each on their own SSH account, to push to one repository without permission errors; substitute whatever group your student accounts actually belong to. And if `.local` names did not resolve on the fleet in Week 21, use the server's IP address everywhere below and write it on the board. (25 min)
- **Seed the repository** from your own laptop, so students clone something that already has history:

  ```bash
  git clone yourname@csserver.local:/Users/Shared/repos/classbook.git
  cd classbook
  mkdir facts
  touch facts/.gitkeep
  printf '# The Class Book\n\nOne file per student in facts/.\n\nClass motto: TBD\n' > README.md
  git add .
  git commit -m "Seed the class book"
  git push -u origin main
  ```

  Verify by cloning it a second time into a scratch folder. (15 min)
- **Do the entire merge-conflict sequence yourself, start to finish, from two separate clones on two machines.** Do not skip this. It is the segment most likely to go sideways in front of a room, and doing it once in prep is the difference. (25 min)
- Play the first several levels of Oh My Git yourself if you have not, so you can speak to what students saw. (15 min)
- Verify SSH from at least two student machines to the server, and verify the clone works. Network problems discovered at 0:55 cost the whole lab. (10 min)
- Write and print the one-page command cheat sheet, and print homework handouts. (15 min)
- Set the default branch name on every fleet machine if the provisioning did not: `git config --global init.defaultBranch main`. (5 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and readiness check (0:00 to 0:10)

- **You do:** Pose the theme question. Then ask for a show of hands: who has ever had a file called something like `essay_final_v2_ACTUALLY_final.docx`? Ask what problem that naming scheme is trying to solve, and where it fails. It fails at knowing what changed, at knowing why, at two people editing at once, and at getting back a version from three weeks ago.
- **You do:** Two-minute demonstration on the projector. Open this course's own repository and run `git log --oneline` on it. Say plainly: these lesson materials are a repository, this is its real history, and every line of it was made by the commands you are about to type.
- **You do:** Readiness check, thirty seconds, hands up: SSH into the server worked last time, Oh My Git got played, GitHub sign-in works. Note who is short on which and pair accordingly. Do not fix accounts now.

### Segment 2: The model, unplugged (0:10 to 0:30), Systems strand

Run entirely from these steps. Sticky notes and the whiteboard only.

1. **Define a commit before showing any command.** Write on the board: a commit is a snapshot of the whole project at one moment, with an author, a timestamp, a message, and a pointer to the commit that came before it. Stress "the whole project," because most students assume a commit stores only the lines that changed. The lines-that-changed view is the diff, which is something Git computes for you, not what it stores.
2. **Build the chain physically.** Stick three sticky notes in a row on the board, left to right, each with a short message written on it: "add rooms", "add player", "fix typo". Draw an arrow from each note back to the one before. Say the arrows point backwards on purpose: every commit knows its parent, and the chain is the history.
3. **Add the label.** Put one more sticky note labeled `main` on the rightmost commit. Explain: a branch is nothing but a label that points at a commit, and it moves forward as you commit. That is the whole definition, and it is why branches are cheap.
4. **Branch it.** Add a second label sticky, `add-map`, on the same commit as `main`. Now add two new commits hanging off it and move the `add-map` label along. Point out that `main` never moved and still works. Land the idea: a branch is a place to be wrong safely.
5. **Merge it.** Add a new sticky with two arrows, one back to the tip of `main` and one back to the tip of `add-map`, and move `main` onto it. Say what a merge commit is: one commit with two parents, which is how the two histories become one.
6. **Manufacture the conflict on the board, in advance of doing it in code.** Put two branches on the board that both changed the same line of the same file. Ask the class what Git should do. Take answers. Then give the real answer: Git can combine changes to different parts of a file by itself, but when two people change the same line, there is no correct automatic answer, so Git stops and asks a human. A conflict is not an error. It is Git refusing to guess.
7. **Name the three places a file can be,** because this is the concept that makes `git status` readable: the working directory (your files as they are right now), the staging area (the changes you have chosen to include in the next commit), and the repository (the committed history). `git add` moves things from the first to the second. `git commit` moves the second into the third.

**Purpose:** Every command in the next ninety minutes is a move on this diagram. Leave the diagram up and point at it constantly.

### Segment 3: Git alone, in your own project (0:30 to 0:55), Coding strand part 1

Students work in their own `adventure` project from last week. Type every command yourself on the projector first.

1. **Set identity once per machine:**

   ```bash
   git config --global user.name "Ada Lovelace"
   git config --global user.email "ada@example.com"
   git config --global init.defaultBranch main
   ```

   Say why: the name and email are stamped into every commit forever, and this is how the class book will show who wrote what.
2. **Initialize and look:**

   ```bash
   cd ~/cs-sandbox/adventure
   git init
   git status
   ```

   Read the output together. Everything is untracked. Point at the diagram: these files are in the working directory and nowhere else.
3. **Watch `.gitignore` do its job.** Note that `.venv/` and `__pycache__/` are not in the untracked list. Have one student temporarily rename `.gitignore` and rerun `git status` to see hundreds of files appear, then rename it back. That single moment justifies last week's four lines better than any explanation.
4. **Stage, commit, inspect:**

   ```bash
   git add .
   git status
   git commit -m "First commit of the text adventure"
   git log
   git log --oneline
   ```
5. **Change something and see the diff:**

   ```bash
   # edit one line in game/world.py, then:
   git diff
   git add game/world.py
   git diff
   git diff --staged
   git commit -m "Reword the hall description"
   ```

   The point of running `git diff` twice: after staging, `git diff` shows nothing, because it compares the working directory to the staging area. `git diff --staged` compares the staging area to the last commit. Students find this confusing exactly once, and seeing it beats being told.
6. **Write three commit messages on the board and rank them.** "stuff", "fixed it", "Fix the crash when a room has no exits". Give the rule: say what changed and why, in one line, in the present tense, so that a person reading the log in six months knows whether to look here. Bad commit messages are technical debt in the sense they learned last week.
7. **Show the VS Code Source Control panel** for thirty seconds, so they know the same operations exist as buttons, and say the commands stay primary because commands are what work on a server.

### Segment 4: Stretch (0:55 to 1:00)

### Segment 5: The collaborative lab (1:00 to 1:30), Coding strand part 2

Everyone works in the same class-server repository at the same time. Put the clone URL on the board. Keep the pace brisk and check the room after each numbered step.

1. **Clone:**

   ```bash
   cd ~/cs-sandbox
   git clone yourname@csserver.local:/Users/Shared/repos/classbook.git
   cd classbook
   ls
   git log --oneline
   ```

   Point out the difference from Segment 3: this repository already has history, and it came from somewhere else. That somewhere else has a name, `origin`. Confirm it with `git remote -v`.
2. **Branch:**

   ```bash
   git switch -c add-ada
   ```

   Each student uses their own first name. Say what just happened against the board diagram: a new label was created on the current commit, and nothing else in the world changed.
3. **Do the work.** Create `facts/<yourname>.md` containing one true, boring, verifiable fact about themselves in a single line. Boring is deliberate; nothing personal or identifying beyond a first name.
4. **Stage and commit:**

   ```bash
   git status
   git add facts/ada.md
   git commit -m "Add Ada's fact file"
   git log --oneline --graph --all
   ```
5. **Push the branch:**

   ```bash
   git push -u origin add-ada
   ```

   Explain `-u`: it links your local branch to the one on the server so that later `git push` and `git pull` need no arguments. Note that nothing on `main` has changed yet. Pushing a branch proposes work; it does not deliver it.
6. **Code review, in pairs, six minutes.** Partners swap what they look at, not where they sit:

   ```bash
   git fetch origin
   git diff main origin/add-ben
   ```

   Each student reads their partner's diff and writes two things on a sticky note: one specific thing that is good, and one specific question or suggestion. Give the rule out loud: review the change, not the person, and be specific enough that the author knows what to do. Then swap stickies and let authors amend if they want to.
7. **Merge into `main`:**

   ```bash
   git switch main
   git pull
   git merge add-ada
   git push
   ```
8. **Expect the rejected push, and treat it as the lesson.** Everyone is pushing to the same `main` at once, so most students will see something like:

   ```
   ! [rejected] main -> main (fetch first)
   ```

   Do not let anyone panic or start deleting things. Say what it means: the server's `main` moved while you were working, so your push would erase someone else's commit, and Git refuses. The fix is to catch up first:

   ```bash
   git pull
   git push
   ```
9. **Look at the shape.** Once the room settles:

   ```bash
   git log --oneline --graph --all
   ```

   Everyone is looking at the same history, containing everyone's work, built by twelve people in twenty minutes without anyone emailing a file to anyone.

### Segment 6: Break it on purpose (1:30 to 1:50), Coding strand part 3

This is the segment that makes Git stick. Everybody causes a conflict deliberately.

1. **Pair students, A and B.** Both start clean:

   ```bash
   git switch main
   git pull
   ```
2. **Both branch:**

   ```bash
   git switch -c motto-ada
   ```
3. **Both edit the same line.** In `README.md` there is a line reading `Class motto: TBD`. Each student replaces `TBD` with their own proposed motto. Same file, same line, two different values. That is the entire recipe for a conflict.
4. **Both commit and push:**

   ```bash
   git add README.md
   git commit -m "Propose a class motto"
   git push -u origin motto-ada
   ```
5. **A merges first, and it works:**

   ```bash
   git switch main
   git pull
   git merge motto-ada
   git push
   ```
6. **B merges second, and it does not:**

   ```bash
   git switch main
   git pull
   git merge motto-ben
   ```

   Output:

   ```
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```
7. **Stop the room here and read it out loud.** Nothing is broken, nothing is lost, and no work has been destroyed. Git did what the board diagram predicted: it found two different values for one line and refused to guess.
8. **Look at the state:**

   ```bash
   git status
   ```

   It says "Unmerged paths" and names `README.md`. Then open the file:

   ```
   <<<<<<< HEAD
   Class motto: Read the error message.
   =======
   Class motto: Commit early, commit often.
   >>>>>>> motto-ben
   ```
9. **Decode the markers, exactly.** Everything between `<<<<<<< HEAD` and `=======` is what is already on the branch you are standing on, which is `main`. Everything between `=======` and `>>>>>>>` is what is coming in from the branch you are merging. The three marker lines are not code, not comments, and not magic. They are plain text that Git wrote into your file for you to delete.
10. **Resolve it by hand.** B edits the file so it contains exactly one motto line, invented with A or combining both, and deletes all three marker lines. Say the rule: a resolved file must contain zero `<`, `=`, and `>` marker lines, and it must be a file you would have written on purpose.
11. **Finish the merge:**

    ```bash
    git add README.md
    git commit
    git push
    ```

    `git commit` with no `-m` opens an editor with a merge message already written; saving and closing accepts it. If the editor is unfamiliar, `git commit -m "Merge motto branches"` is fine.
12. **Give them the escape hatch, and make them use it once.** Any student who feels lost mid-conflict can type:

    ```bash
    git merge --abort
    ```

    and be returned exactly to where they were before the merge. Have every student run it once on a second, throwaway conflict, so they know from experience that the panic button exists.
13. **Show the VS Code version, briefly.** Open the conflicted file in the editor and point at the Accept Current, Accept Incoming, and Accept Both buttons. Say they do exactly what the students just did by hand, and that hand-editing first is why they can now be trusted with the buttons.
14. **Look at the finished shape:**

    ```bash
    git log --oneline --graph --all
    ```

    Find the merge commit with two parents on screen and connect it back to the sticky note on the board.

### Segment 7: Hosted Git and wrap (1:50 to 2:00)

- **You do:** One-minute framing of GitHub. It is the same Git they just used, running on someone else's server, with a web page in front of it. The class server and GitHub are interchangeable in every way that matters to the commands.
- **You do:** Name the two words they will hear everywhere: a pull request is a proposal to merge a branch, with a place attached for the review conversation they just had on sticky notes; a fork is your own copy of somebody else's repository. That is enough vocabulary for today.
- **You do:** Hand out homework and walk through it, including the Extra Credit AP Track section. The homework pushes their own project to GitHub, which is why the account check mattered.
- **Exit question at the door:** you get a merge conflict. Is anything broken, and what is Git asking you for? (Answer: nothing is broken; Git is asking you to choose, because two people changed the same line.)

## 7. Key scripts and analogies

- **Why version control:** "Every project you will ever work on has a history. The only question is whether that history is written down somewhere you can use, or lost in a pile of files named final_v2."
- **A commit:** "A photograph of the whole project, with a note attached saying what you just did and why. Photographs are cheap. Take a lot of them."
- **A branch:** "A sticky note with a name on it, stuck to one commit. That is genuinely all it is. Which is why making one costs nothing and why you should make one for anything risky."
- **Why branch:** "A branch is a place to be wrong safely. `main` keeps working while you find out whether your idea was any good."
- **Staging:** "The working directory is your desk. The staging area is the pile you have decided goes in the envelope. The commit is sealing the envelope and mailing it."
- **A conflict:** "Not an error. Git combining two people's work, hitting one line where they disagree, and refusing to guess which of you was right. It is asking a question, and the answer is a human decision."
- **Conflict markers:** "Those angle brackets are not code. Git typed them into your file so you could see both versions. Your job is to delete all three lines and leave the version you actually want."
- **Rejected push:** "Somebody else moved while you were writing. Git will not let you overwrite them. Pull first, then push."
- **Commit messages:** "Write for the person who reads this log in a year with no memory of today. That person is you."

## 8. Differentiation

- **Younger or newer students:** Run them through GitHub Desktop instead of the command line for Segments 3 and 5, then bring them back to the terminal for the conflict in Segment 6, which they can also do in the app. The GitHub Desktop path is: File then Clone Repository for step 1, the Current Branch menu then New Branch for step 2, the Changes tab with a summary box then Commit for step 4, Push Origin for step 5, and Current Branch then Merge into Current Branch for step 7. The vocabulary is identical, which is the point. Also let them keep the Oh My Git graph open on a second window as a visual reference. Do not let a student skip the conflict segment; the conflict is the part that teaches the model.
- **Extensions for advanced or AP-track students:** Have them try `git log --oneline --graph --all` after every operation and narrate the shape. Have them delete a committed file and recover it with `git restore`. Have them look at `git show <hash>` for one of their own commits and identify the parent hash. Have them open a real pull request on GitHub against a partner's repository in the homework, review it in the web interface, and merge it there. The strongest can research the difference between merge and rebase and explain in three sentences why this class uses merge.

## 9. Common pitfalls

- **Accounts and SSH not working.** This is the whole-lab killer, which is why it is checked the week before. If a student is still blocked at 1:00, pair them at a working machine as a co-driver rather than losing them to troubleshooting.
- **The default branch is `master` on some machines.** Mixed branch names in one repository produce baffling push errors. The prep checklist sets `init.defaultBranch` fleet-wide; verify it.
- **Permission denied on push to the class server.** Almost always the bare repository was not created with `--shared=group` or the group ownership is wrong. Fix it during prep, not during class.
- **Committing the `.venv` folder.** If a student's `.gitignore` is missing or misspelled, they will commit thousands of files. Catch it at `git status` before the first `git add .`, which is why step 4 of Segment 3 has them look first.
- **`git add` without `git commit`.** The student swears they saved their work and the log shows nothing. Point at the three-places diagram.
- **Editing a file while on the wrong branch.** Have them check with `git status`, which names the branch on its first line, before they start typing. Say it out loud as a habit: status first, always.
- **Panic at the conflict markers.** Expect at least one student to delete the whole file or try to `rm -rf` the repository. Get `git merge --abort` on the board before Segment 6 starts, and have everyone use it once.
- **Resolving a conflict by leaving a marker line in.** The file then has a stray `=======` in it and the program breaks later in a way nobody connects to Git. Have partners check each other's resolved file.
- **The unmerged branch pile.** By the end there are twenty-odd branches on the server. That is fine and worth pointing at. Cleaning up with `git branch -d` is an optional extension, not required.
- **Time.** Segment 6 must start by 1:30. If Segment 5 runs long, cut the code-review swap to three minutes rather than shortening the conflict.

## 10. Homework

Full details in `handouts/week-23-homework.md`. In summary: push their `adventure` project to a new GitHub repository; make two commits with real messages; create a branch, make a change on it, and merge it; deliberately create and resolve one merge conflict in their own repository; a short written piece explaining a commit, a branch, and a conflict in their own words. The handout closes with an Extra Credit AP Track section carrying this week's AP self-study slice.

## 11. Assessment

Observational and completion-based, against the weekly-labs rubric. The class-server repository is itself the evidence: run `git log --oneline --graph --all` after class and you can see exactly who committed, who merged, and who resolved a conflict. That log is your record for the week.

Four things to verify per student, by watching rather than by asking:

1. Committed something with a message that describes the change.
2. Pushed a branch to the class server.
3. Reviewed a partner's diff and produced one specific comment.
4. Resolved a merge conflict by hand, with the markers gone.

The verbal check is the exit question. A student who says a conflict means something is broken has the wrong mental model and needs a two-minute conversation at the board next week.

## 12. AP alignment

Be honest with students here. Git is not AP CSP content. The exam does not ask about commits, branches, or merges, and no amount of Git fluency shows up on the multiple-choice paper.

What is AP content is topic 1.1 Collaboration, and today was a real instance of it: shared work in one codebase, defined roles, review of another person's contribution, and the resolution of a disagreement about the same line. When the exam asks about the benefits of collaboration, or when the Create Task written response asks what the student's collaborators contributed, today is the experience to draw on. Say that framing out loud rather than pretending Git is tested.

The practical AP value of Git is indirect and real: AP-track students will build the Create Task program over several weeks in the spring, and a repository is what stops a hard-drive failure or a bad afternoon from destroying it.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 1, Intro and Computational Thinking, specifically its collaboration lessons. This is a small slice, and it is the honest one; if you already did it last week, then this week has no new Project STEM work, and using the time to get ahead on the Unit 2 programming material is a better use of an hour. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`. Work only the collaboration lessons, which cover the same ground the exam tests: why programs are developed collaboratively and what reviewing someone else's work is for.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The unplugged commit-graph activity: fully inline in Segment 2. Sticky notes and a whiteboard only.
- The whole Git lab: complete in Segments 3, 5, and 6, including the exact clone URL pattern, the conflict recipe, and the resolution. Nothing external needs to be open during class.
- **Prep note:** run the entire Segment 6 conflict sequence yourself from two clones before teaching it. This is the one part of the week where reading the steps is not a substitute for having done it.
- Oh My Git, assigned as last week's homework and the recommended first exposure for students who need it: `https://ohmygit.org`. Free and open source. Verify availability on the fleet.
- Git reference for your own use: `https://git-scm.com/docs` and the free book at `https://git-scm.com/book/en/v2`. Chapters 2 and 3 are the relevant ones. Command behavior has changed across versions, notably `git switch` and `git restore` replacing older uses of `git checkout`; verify against the Git version installed on the fleet.
- GitHub Desktop, the recommended path for students who struggle with the command line: `https://desktop.github.com`. See `student-prep/Younger-Student-Readiness-and-Prep.md` for why it is offered.
- This course's own repository, used as the live example in Segment 1. The README notes that it is intended to serve exactly this purpose.
- CodeAI CSP Unit 3, Intro to App Design (AP-track collaboration slice): `https://studio.code.org/courses/csp-2025/units/3`
- GitHub account requirements, the age-13 minimum, and parental consent: Section 12 of `curriculum/CS-Curriculum-and-Setup.md`.
