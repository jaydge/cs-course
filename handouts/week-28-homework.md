# Week 28 Homework: Locks, Hashes, and Your Own Front Door

This week you broke a cipher, exchanged a secret in public, found a flipped card you never saw flip, and traced the actual defenses on the classroom network. Now do the same trace at home. Plan on about 45 minutes.

## 1. Crack this

Below is a message encrypted with a Caesar cipher. The shift is not 3, and nobody is going to tell you what it is.

```text
WKH ORFN LV RQOB DV JRRG DV WKH NHB VSDFH
```

Write down three things:

1. The decrypted message.
2. The shift you found.
3. How you found it. If you tried every shift until one worked, say that and say how many you had to try. If you used letter frequency, say which letter you guessed first and why.

## 2. Trace your own house

Draw the stack for your home network the way we drew the classroom's on the board. Start at the internet and end at you. Your list will not be identical to the classroom's, and that is the point.

For each layer, write one line for each of these:

- What it stops.
- What it does not stop.
- What would happen if it quietly failed and nobody noticed.

Then answer this in a short paragraph: which layer in your list is the weakest, and why? There is no wrong answer as long as your reason is specific.

## 3. Hashing in Python

Open `hashing.py` from class.

1. Hash your first name. Then hash your first name with a capital letter changed. Paste both hashes into your answer file and say in one sentence how many characters differ.
2. Hash a whole paragraph of text. How long is the output? Compare it to the length of the hash of a single letter.
3. Answer in writing: a website has been breached and the attacker has stolen the table of password hashes. They cannot reverse a hash. Explain, in three or four sentences, how they crack most of the passwords anyway, and what salting does to make that harder.

## 4. Audit your own passwords, with a parent

Do this part with a parent, not alone.

1. Count how many accounts you have that use the same password, or a small variation of one password.
2. Pick your most important account, the one that could be used to reset the others. That is usually email. Check whether it has multi-factor authentication turned on. If it does not, ask a parent whether you should turn it on.
3. Write down, without writing any actual passwords anywhere: how many reused passwords you found, and what one change you are going to make.

Never write a real password in a homework file.

## 5. Keep the project moving

Your proposal came back with a scope note. Do the thing it says. If it said "too big," cut it down this week and write two sentences describing the smaller version. If it said "right," start writing code.

## 6. Watch, if you want (optional)

Crash Course Computer Science, Episodes 31, 32, and 33, cover cybersecurity, cyber attacks, and cryptography. Episode 33 is the one that matches the cipher and key-exchange work directly: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

**A reminder on getting help.** AI assistants are now permitted on homework builds and side projects, under the three rules from last week: verify everything, never turn in code you cannot explain, and put a comment at the top saying what you asked for and what you changed.

If you are submitting an AP Create Performance Task, your project stays completely AI-free. That is a College Board rule and it holds until you submit.

One more thing specific to this week: never try any of today's attacks on a system that is not yours. Not a school site, not a friend's account, not a site that looks badly built. Unauthorized access is a crime, and "it was easy" and "I was curious" are not defenses. If you want to practice attacking things legally, that is what picoCTF exists for; see the extra-credit section below.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

This week maps to the exam more cleanly than almost any other week of the course. Topic **5.6 Safe Computing** is essentially today's lesson, and it sits inside Big Idea 5, which is 21 to 26 percent of the multiple-choice exam.

Things the exam expects you to be able to do, all of which you did today:

- Say what personally identifiable information is and give an example of why it is worth protecting.
- Explain the difference between symmetric encryption and public-key encryption.
- Say what a certificate authority does and what a digital certificate proves.
- Explain multi-factor authentication in terms of what you know, have, and are.
- Identify phishing, keylogging, rogue access points, and malware, and say what each one is after.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, and specifically its cybersecurity and safe-computing lessons. Stop before the impact and ethics material; that is Week 30's slice and you will want it then. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 8, Cybersecurity and Global Impacts, at `https://studio.code.org/courses/csp-2025/units/8`. Do the cybersecurity half of the unit and stop. Save the global-impacts half for Week 30.

**Create Task reminder.** Your Create Task remains entirely your own work with no AI at any stage, including planning and debugging. This week's milestone: have a file that runs, even if it barely does anything yet. A program that runs and does one small thing on Week 28 becomes a finished project on Week 31. A program that does not exist yet on Week 28 usually does not.

**Extra practice if you want it.**

- Write a Caesar cipher in Python: one function to encrypt with a given shift, one to decrypt, and one that prints all 25 possible decryptions so you can eyeball the right one. `ord`, `chr`, and the modulo operator are all you need.
- Do the real Diffie-Hellman arithmetic with small numbers. Public base 5, public modulus 23. You and a partner each pick a secret exponent, compute base to the power of your secret modulo 23, and swap the results. Then each of you raises what you received to your own secret, modulo 23. You should land on the same number. Then work out what an eavesdropper would have to solve.
- Try the beginner challenges at picoCTF, `https://picoctf.org`, now under Carnegie Mellon's CyLab Security Academy, so check the current sign-up route. It is a legal, deliberately vulnerable playground and it is the Starter tier of the cybersecurity extra-credit track.
