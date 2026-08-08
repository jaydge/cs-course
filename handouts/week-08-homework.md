# Week 8 Homework: Inside the Case, and Text as Data

This week you took a computer apart and learned what makes one faster than another, and you found out that a string is really a list of characters. Plan on about 40 minutes.

## 1. Two written answers

- Why does a computer need both RAM and storage? Answer in two or three sentences. The word "power" should show up somewhere in your answer.
- Your friend is buying a laptop and says "this one has a higher gigahertz number so it is faster." Give one reason that might not be true.

## 2. Order the hierarchy

Put these five in order from fastest to slowest, and write next to each one whether it holds a little or a lot:

registers, RAM, cache, SSD, mechanical hard drive

Then answer: what gets bigger as you go down your list, and what gets worse?

## 3. Find the parts

Pick one of these two:

- **Option A.** Find the specifications of a computer at home (on a Mac: the Apple menu, then About This Mac; on Windows: Settings, then System, then About). Write down the processor, the number of cores if it tells you, the amount of RAM, and the storage size and type.
- **Option B.** Find a photo online of the inside of a desktop PC and label five components: CPU or its cooler, RAM, storage drive, power supply, and motherboard.

Either way, write one sentence about anything that surprised you.

## 4. Slicing on paper

No computer for this one. Given:

```python
s = "keyboard"
```

Write down what each of these gives:

- `s[0]`
- `s[3]`
- `s[-1]`
- `len(s)`
- `s[0:3]`
- `s[3:]`
- `s[:3]`
- `"board" in s`

Then check your answers in Thonny. Mark any you got wrong and write one sentence about why.

## 5. Finish the text analyzer

Get your program from class working: it asks for a sentence and prints the character count, the word count, and the vowel count.

Then add one thing to it: a check for whether a word the user types is a palindrome, meaning it reads the same backwards. Ask for a single word, compare it to its reverse, and print whether it is one. Try it on "racecar", "level", and "python".

Careful with capital letters. "Racecar" should still count.

Save it into your CS Class folder.

## 6. Watch, if you want (optional)

Crash Course Computer Science, Episode 9 ("Advanced CPU Designs") and Episode 19 ("Memory and Storage"). Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

Being honest again this week: none of the hardware is on the AP exam. Clock speed, cache, pipelines, SSDs, and GPUs are simply not tested. The exam's Big Idea 4 is about the internet, not about what is inside a case, and we cover that later in the year. The one genuinely AP-tested thing today is strings, topic 3.4, so that is where the slice points.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 2, Programming. Stay in the programming unit and work the strings lessons. Same instruction as last week: keep going in the programming unit, because our systems content this week is not on the exam. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** this one does not map cleanly, and it is better to say so than to send you somewhere useless. The csp-2025 edition has no strings unit. The closest material is the string handling inside Unit 4, Variables, Conditionals, and Functions, at `https://studio.code.org/courses/csp-2025/units/4`, and the traversal lessons in Unit 6, at `https://studio.code.org/courses/csp-2025/units/6`, because traversing a string works exactly like traversing a list. If you have already done both units, skip this and do the practice below instead.

**Extra practice if you want it.**

- The official AP pseudocode has no slicing and almost no string tools; questions build strings by concatenation and pick them apart with loops. Rewrite your palindrome checker in AP pseudocode using only a loop and concatenation, with the tables in `ap-track/AP-Pseudocode-Bridge.md` for the loop and procedure notation.
- Write a function that takes a string and returns it with all the spaces removed, using a loop and building a new string one character at a time. No `.replace()`. Doing it the long way is exactly how the exam expects you to think about strings, since AP pseudocode has no convenience methods.
- Count how many times a specific letter appears in a sentence, using a traversal and a counter. Then do the harder version: find which letter appears most often.
