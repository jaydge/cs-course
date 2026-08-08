# Younger-Student Readiness and Prep Guide

A companion to the main course plan, focused on students who are newer to computers (some new to the internet itself) so that the pace never leaves them lost. It covers:

1. Where younger students may get lost (mapped to the course)
2. Summer preparation plan
3. Readiness diagnostic (not a gate)
4. During-course supports
5. Supplemental video and interactive resources
6. Recommended books from recognized authors

The guiding idea: the biggest risk for a true beginner is not the computer science. It is the foundation underneath it, the everyday computer fluency the course quietly assumes. Build that first and most of the rest follows.

---

## 1. Where younger students may get lost

Ranked by how likely it is to trip a beginner, with the mitigation already available in the course.

| Risk area | Where | Why it is hard for a beginner | Mitigation |
|---|---|---|---|
| Basic computer fluency (typing, files and folders, windows, browser, accounts) | Assumed from Day 1 | Entirely new if a student has barely used a computer; nothing else can land until this does | Summer prep, Essential tier (Section 2) |
| The first programming leap: variables, loops, functions | Unit 1, W3 to W5 | The hardest cognitive jump in the course; code as abstract instructions that run line by line | Summer block-coding pre-loads the concepts so only syntax is new |
| Binary conversion arithmetic | Unit 1, W2 | Depends on comfort with place value and powers of 2 | Place-value scaffold (course Section 11 alternate); Khan video |
| Objects and classes | Unit 3, W11 to W12 | A large abstraction: data and behavior bundled together | Slow concrete examples, pairing, preview video |
| Data structures by hand (stacks, queues, linked lists) | Unit 3, W13 | Abstract structures with no physical referent | CS Unplugged activities with physical objects |
| Sorting and searching, Big-O | Unit 3, W14 | Algorithms must be seen step by step; Big-O adds growth-rate math | Physical sorting (Section 5), visualizers, Big-O alternate (course Section 11) |
| The terminal and command line | Unit 4, W17 to W18 | Intimidating, unforgiving, no buttons to click, exact spelling required | Pre-build file-system fluency in summer; guided cheat sheet; pairing |
| Networking acronyms (IP, DNS, TCP, packets) and Wireshark | Unit 4, W19 to W20 | Jargon-heavy and abstract; packet captures look overwhelming | Watch the Code.org internet films first; lean on analogies |
| Git and version control | Unit 5, W23 | The commit and branch model confuses adults too | The "Oh My Git!" game, GitHub Desktop before the command line, preview video |
| Web stack (HTML, CSS, JavaScript together) and APIs | Unit 5, W24 to W25 | Three new notations at once, then data formats on top | Scope down: HTML and CSS first, JavaScript light, APIs as a demo |
| Neural network math (perceptron) | Unit 6, W27 | Weighted sums and linear algebra | Visual-tool alternate (course Section 11); 3Blue1Brown for older students |
| Public-key cryptography | Unit 6, W28 | Two keys, one locks and the other unlocks, is counterintuitive | Locked-mailbox analogy; Computerphile video |

The two that deserve the most pre-emptive attention are the first row (computer fluency) and the terminal, because both are about comfort with the machine rather than CS ideas, and both can be softened a lot before the course even begins.

---

## 2. Summer preparation plan (optional)

There is no required pre-course class. Treat everything in this section as optional and voluntary, for families who want a head start. The essential fluency is covered for all students in the brief in-course intro (see the Course Intro: Computer Basics guide). This section is most useful for the students the readiness diagnostic flags, and for the single highest-value item any family can do in advance: typing practice.

Two tiers. The Essential tier is for any student new to computers and is the difference between keeping up and drowning in Week 1. The Bonus tier is for eager students or those with more time.

### Essential

1. **Typing.** Use typing.com or keybr.com, about 15 minutes a day. A comfortable target is roughly 20 to 25 words per minute with reasonable accuracy. They do not need to be fast, just to stop hunting for every key, because all coding depends on it.
2. **Computer basics.** Be able to: create a folder, save a file into it, close it, then find and reopen it; recognize a file extension and say what it means; have two windows open and switch between them; copy text from one place to another; take a screenshot.
3. **Internet basics.** Open a browser, use tabs, run a search and judge results, understand what a link and a URL are, and set a bookmark. Important for students new to the internet.
4. **First account and password.** With a parent, set up a Code.org account and create one strong password. This previews both account setup later in the course and the password ideas in the cybersecurity unit.
5. **Block-coding on-ramp (the highest-value item).** Work through Code.org's Express Course or CS Fundamentals, or build in Scratch. The goal is not Python; it is to internalize sequence, loops, conditionals, and events in a friendly, drag-and-drop setting. When Python arrives in Unit 1, the ideas are already familiar and only the typing of syntax is new.

### Bonus

6. Build one small Scratch project, such as a sprite that moves with the arrow keys or a two-sprite chase.
7. Watch three or four short "how computers and the internet work" videos to build vocabulary (see Section 5).
8. Light math refresh: place value, the powers of 2 (1, 2, 4, 8, 16, 32, 64, ... up to 1024), and remainders. These feed binary and the MOD operator.
9. Read, or be read to from, the first several chapters of "CODE" by Charles Petzold, or the gentler "But How Do It Know?" by J. Clark Scott (see Section 6).

---

## 3. Readiness diagnostic

This is a diagnostic, not an entrance exam. Nobody is excluded by it. Its only job is to tell you, per student, where to spend the summer. Administer it informally a month or two before the course.

### Part A: Practical computer skills

Watch the student attempt each task, or have a parent confirm it. Mark Ready or Needs practice.

- Type two or three sentences without hunting for most keys.
- Create a folder, save a file into it, close the program, then find and reopen the file.
- Point to a file's extension and say roughly what it means.
- Open two windows or tabs and switch between them; copy text from one to the other.
- Open a browser, search for something, and open a result in a new tab.
- Explain what a password is for and create a strong one.

Any "Needs practice" marks point straight to the Essential tier items 1 through 4.

### Part B: Logical reasoning (no coding required)

Short written questions. These predict programming readiness better than any tech knowledge does.

1. Write down, one step per line, exactly how to make a peanut butter sandwich, as if explaining to someone who has never done it. (Looking for: ordered, complete, unambiguous steps.)

2. Follow these rules in order, starting with the number 3:
   - Add 4.
   - If the result is greater than 5, subtract 2; otherwise add 10.
   - Double the result.
   What is the final number?

3. What are the next two numbers? 1, 2, 4, 8, 16, ___, ___

4. When you divide 17 by 5, what is the remainder?

5. These instructions are supposed to draw a square. Find the mistake:
   1. Draw a line going right.
   2. Turn 90 degrees.
   3. Draw a line going down.
   4. Turn 90 degrees.
   5. Draw a line going left.
   6. Stop.

**Answers and what they tell you:**

- Q1: there is no single right answer; look for clear sequencing and no skipped steps. Weakness here means more Scratch and Code.org plus unplugged logic this summer.
- Q2: 10. (3, then +4 is 7, then since 7 is greater than 5 subtract 2 to get 5, then double to 10.) This tests following a sequence with a condition. The core skill of tracing code.
- Q3: 32 and 64. Also previews powers of 2 for binary.
- Q4: 2. Previews the MOD operator.
- Q5: it only draws three sides; it is missing a fourth turn and a fourth line (and never returns to start). Spotting the incomplete instruction is early debugging instinct.

### Reading the results

- Weak on Part A: prioritize computer basics and typing this summer.
- Weak on Part B sequencing (Q1, Q2, Q5): prioritize the block-coding on-ramp and unplugged logic.
- Weak on the math items (Q3, Q4): do the place-value and powers-of-2 refresh.

---

## 4. During-course supports

So a student does not fall behind once the course is moving.

- **Concept-preview videos.** The week before a difficulty spike, assign one short video so students arrive with the vocabulary. Suggested pairings: Code.org internet films before W19 networking; an "Oh My Git!" session before W23 Git; a sorting visualizer before W14; a public-key analogy video before W28.
- **CS Unplugged activities** (csunplugged.org, free). Teach the abstract topics physically before any code. Sort students by height or sort a shuffled deck to teach sorting step by step; flip cards to teach binary; pass objects down a line to teach a queue. This directly answers the "sorting needs to be explained step by step" concern.
- **Pair programming.** Pair a younger student with an older one for selected labs. Both benefit; explaining cements the older student's understanding.
- **A running glossary.** Each student keeps a personal list of terms and plain-language definitions as the course goes. Owning the vocabulary reduces the lost feeling.
- **A "stuck" protocol.** Try for a set number of minutes, then check notes and documentation, then ask a peer, then ask the instructor. This teaches productive struggle without letting anyone drown.
- **Section 11 alternates.** Use the younger-student alternates from the main plan (Big-O without logarithms, the visual neural-network tool, the binary conversion scaffold) only for students who need them.
- **An optional weekly catch-up or extension slot.** Fifteen to twenty minutes where students who are behind get reinforcement and students who are ahead get an extra-credit nudge.

---

## 5. Supplemental video and interactive resources

Curated, not exhaustive. Verify current availability before relying on any one of them.

### Whole-course and foundations
- Crash Course Computer Science (already in the course plan): a 40-episode tour of the whole stack, good for guided-tour days.
- Code.org short films ("How Computers Work," "How the Internet Works"): beginner-friendly, a few minutes each, narrated by well-known technologists. Ideal vocabulary builders for newer students.

### Programming on-ramp
- Code.org and Scratch tutorials: the gentlest entry, block-based.
- The Coding Train (Daniel Shiffman): energetic, beginner-friendly creative coding.
- "Automate the Boring Stuff with Python" by Al Sweigart: free companion videos and book for practical Python.

### Hardware and how a computer works
- Ben Eater: builds a working computer on breadboards, the best deep visual for what is happening inside.
- Computerphile: short single-topic explainers across many CS subjects, great for Mystery Days.

### Binary, sorting, and algorithms
- Khan Academy: binary and number systems at a calm pace.
- Sorting visualizers: visualgo.net and similar, where students watch a sort happen step by step and control the speed.

### Networking
- Code.org's internet film series: how data moves, in plain language.
- Ben Eater's networking series and Computerphile: deeper but still accessible.

### Git
- "Oh My Git!": a free open-source game that teaches version control visually. Excellent for younger students.

### AI and cryptography
- 3Blue1Brown's neural network series: the clearest visual explanation of how neural networks work, better suited to older students because of the math.
- Computerphile: strong, short cryptography explainers for the public-key topics.

---

## 6. Recommended books from recognized authors

Trade books from notable authors, not textbooks, chosen to support the course narrative. For each: what it is, where it fits, and who it suits.

- **"CODE: The Hidden Language of Computer Hardware and Software" by Charles Petzold.** The closest thing to a single book for this entire course. It builds from simple codes and electrical switches all the way to a working computer, exactly the arc of the class. Use it as the spine reference, read aloud or excerpt the early chapters for younger students. Suits everyone; younger students may need the first chapters paced slowly. Supports Units 1 and 2.

- **"The Pattern on the Stone: The Simple Ideas That Make Computers Work" by W. Daniel Hillis.** A short, elegant explanation of how computers work conceptually, written by a renowned computer architect. A gentler, faster read than CODE and a fine alternative for students who find CODE dense. Supports Units 1 and 2.

- **"But How Do It Know? The Basic Principles of Computers for Everyone" by J. Clark Scott.** The most approachable explanation of how a CPU actually works at the bit level. Good for a student who wants the hardware story without heavy prose. Younger-friendly. Supports Unit 2.

- **"The Code Book" by Simon Singh.** A gripping history of cryptography from ancient ciphers to modern encryption, by a celebrated science writer. Pairs perfectly with the cybersecurity unit and makes public-key ideas feel like a story rather than math. Suits most students. Supports Unit 6.

- **"You Look Like a Thing and I Love You" by Janelle Shane.** A funny, genuinely clarifying look at how machine learning works and the strange ways it fails, by a well-known AI researcher and writer. Demystifies AI without math. Younger-friendly. Supports Unit 6.

- **"Algorithms to Live By: The Computer Science of Human Decisions" by Brian Christian and Tom Griffiths.** Explains core algorithmic ideas through everyday decisions. Better for older or more curious students. Supports Unit 3.

- **"Automate the Boring Stuff with Python" by Al Sweigart.** Leans instructional rather than narrative, but it is by a recognized author, beloved, project-based, and free to read online, which makes it a strong practical companion for the Python work. Suits students who want more hands-on Python. Supports Units 1, 3, and 5.

A practical way to use these: keep CODE as the through-line, pull the others in when their unit arrives, and offer the narrative titles (The Code Book, You Look Like a Thing and I Love You) as enjoyable extra-credit reads rather than required reading.
