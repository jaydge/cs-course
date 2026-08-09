# Week 26 Homework: Make It an App

This finishes Unit 5. Five weeks ago your code was a single Python file in Thonny. It is now a versioned project, served by a web server you wrote, pulling live data off the internet, and installable with an icon. Plan on about 50 minutes.

## 1. Finish the PWA

Your app is done when all of these are true:

- From `~/Documents/"CS Class"/weather`, `python3 app.py` runs it and `http://127.0.0.1:5000` loads.
- The Application panel in Chrome shows your manifest with no errors.
- The Application panel shows a service worker that is activated and running.
- Cache Storage contains your files.
- With the Offline box ticked, or with Wi-Fi off entirely, the page still loads.
- Chrome offers to install it, and when installed it opens in its own window with no address bar.

Two things that catch nearly everyone:

- If nothing changes when you edit `sw.js`, the old service worker is still in charge. In the Application panel, tick "Update on reload," or click Unregister and reload.
- If the service worker never installs, check that every file listed in `PRECACHE` exists at that exact path. One wrong filename fails the whole thing, quietly.

Commit when it works:

```bash
git add .
git commit -m "Finish the PWA conversion"
```

## 2. Make it honest about being offline

Your app loads with the network off, which is the good news. It also shows an old temperature with nothing telling the user that. Fix it: add a line to your offline page, or to the main page, saying clearly that the reading may be out of date, and give the time it was taken. Software that quietly presents stale information as current is software that lies.

Then write two or three sentences on the design decision underneath it. Your service worker tries the network first and falls back to the cache only when that fails. Why is that the right way round for a weather app, and what kind of app would be better off the other way round?

## 3. Choose the approach, with reasons

For each of these, say whether you would build it native, cross-platform, or as a PWA, in one or two sentences, and name the single constraint that decided it: budget, performance, hardware access, distribution, or update speed. There is more than one defensible answer; the reasoning is the whole assignment.

1. A local library wants people to search the catalog and see whether a book is on the shelf.
2. A company is building a video editing app that has to handle 4K footage smoothly on a phone.
3. Two people with a small budget are building a habit tracker that syncs across devices and sends a daily reminder.

## 4. Audit the permissions on a real device

On your own phone, or a family device with permission from whoever owns it, open the settings screen that lists app permissions.

1. Pick two apps. Write down what each one is allowed to access.
2. Find one permission that surprised you, where you cannot immediately explain why that app needs that thing. Write two or three sentences on it: what is it allowed to do, what is the most generous explanation for why, and what is the least generous one?

Do not change anyone else's settings without asking them.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. That changes next week, when Week 27 covers AI properly and it becomes permitted on non-exam work. One more week unaided. MDN is the right reference for service workers, and bringing a written question to class is always allowed.

Unit 5 is finished, so this matters more than usual: be ready to point at your fetch handler and say out loud what happens to a request when the network is down. If you can explain it, you own it.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**Straight answer first: mobile development is not on the AP exam.** Native versus cross-platform, app stores, push notifications, and service workers are not tested. Nothing in the coding half of today's class will appear in May.

But two parts of the discussion genuinely will.

**Big Idea 5, Impact of Computing, is 21 to 26 percent of the exam,** which is more than anything except algorithms. Three things from today sit right in the middle of it, and Week 30 covers them properly:

- Permissions and sandboxing, and what an app can learn about you, are topics 5.6 Safe Computing and 5.5 Legal and Ethical Concerns.
- App stores deciding what software is allowed to exist is 5.1 Beneficial and Harmful Effects and 5.5.
- A PWA running fine on a cheap phone that cannot handle a large native app is 5.2 Digital Divide, and it is one of the clearest real examples of that topic in the whole course.

The exam rewards answers that name a benefit and a harm of the same thing. Today gave you several pairs. Practice writing one: pick app store review, and in four sentences give the strongest case for it and the strongest case against it.

**The Create Task window opens next week.** This is the part to read carefully.

Starting in Unit 6, in February, you get nine protected hours of class time for the AP Create Performance Task, and it is submitted in late April. Check the exact deadline for your year on AP Central; College Board moves it, and a handout is not a reliable source for a date.

What the task actually is: a program you design and build yourself, a video of it running, and written responses about how it works and how you developed it. The program has to include a list or similar collection used for something meaningful, a procedure you wrote yourself that takes a parameter and does something with it, and an algorithm inside that procedure using both selection and iteration.

**Your job this week is to pick one idea.** In Week 25 you were asked to write down three. Now narrow to one, so that the first protected hour in February is spent building instead of deciding.

Answer these four questions in writing about the idea you pick:

1. What does the program do, in two sentences?
2. What is the list or collection, and what is in it? Where does the data come from, a file you make, a CSV, or an API?
3. What is the procedure you will write, what parameter does it take, and what does it return?
4. What decision does it make (selection) and what does it repeat (iteration)?

If you cannot answer all four, the idea is not ready, and it is much cheaper to find that out now than in March.

Two things to keep in mind. Your Week 25 data lab is very close to the right shape already, and reusing that pattern with data you care about is a legitimate and sensible plan. And the Create Task must be your own work: the College Board's rules about copied code and about AI apply to it, and they still apply after AI unlocks for everything else next week.

**Your unit for this week.** No unit matches today's content, so pick by what you need.

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, is the nearest fit and it is a loose one. It is about how computing innovations work and what effects they have, which is the frame today used. If your Create Task idea is not settled, do that instead; it is worth more. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 8, Cybersecurity and Global Impacts, at `https://studio.code.org/courses/csp-2025/units/8`, if you want exam content, since it covers the Big Idea 5 material above. Or Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`, if you are ready to plan. Last week you were told to skim Unit 9 and not start it. This week you may start it.

**Extra practice if you want it.**

- Unit 5 is finished. Open `ap-track/AP-CSP-Topic-Coverage.md` and look at 1.1, 1.3, 2.3, 2.4, and 3.14. Those are the five topics this unit was responsible for. Mark each one solid, shaky, or not yet, and bring the shaky ones to class. Be honest about 2.3 and 2.4 in particular; the course does not come back to them.
- Write your Create Task procedure in AP pseudocode before you write it in Python, using `ap-track/AP-Pseudocode-Bridge.md`. Writing it twice is not wasted work; the written responses ask you to explain that procedure, and you will explain it better having said it two ways.
