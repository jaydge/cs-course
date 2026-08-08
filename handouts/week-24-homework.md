# Week 24 Homework: Finish Your Page

You built a web page out of three files today. This finishes it. You will use this same page again in Week 25, when a Python program starts serving it, and again in Week 26, when it becomes something you can install on a phone. So make it one you do not mind looking at for three weeks. Plan on about 45 minutes.

Two rules that do not change:

- Serve the page, do not open the file. From your `personal-page` folder, run `python3 -m http.server 8000` and visit `http://localhost:8000`. If your address bar says `file://`, you are doing it the way that breaks in two weeks.
- First names only. No last name, no address, no school name, no photos of people. This page is not going on the public internet, and it still follows that rule.

## 1. Finish the page

Your page is done when all of these are true:

- It has a `<header>`, a `<main>`, and a `<footer>`.
- It has one `<h1>`, at least two `<h2>` headings, and at least two paragraphs.
- It has a list of at least three things with `<ul>` and `<li>`.
- The stylesheet is attached and the page clearly looks styled: a font that is not the default, a `max-width` so the text does not stretch across the whole screen, and two colors that are readable together.
- The button works.

Commit each piece as you finish it, with a real message. You should end up with at least three commits.

```bash
git add .
git commit -m "Add the projects section"
```

## 2. Learn one new CSS property on your own

Go to MDN (`https://developer.mozilla.org`) and find one CSS property we did not use in class. Some good ones to look up: `border-radius`, `box-shadow`, `text-align`, `letter-spacing`, `background-image`, `opacity`.

Use it on your page. Then add a comment above the rule in your stylesheet saying what it does, in your own words:

```css
/* border-radius rounds the corners of the box */
.card {
  border-radius: 8px;
}
```

The skill being practiced here is looking something up in the documentation, not the property itself. You will do this for the rest of your life.

## 3. Make the page do one more thing

Pick one:

- **A second button** that changes something else on the page. Changing a color from code looks like this: `document.getElementById("fact").style.color = "crimson";`
- **A counter.** Add a `let count = 0;` at the top of your script, add one to it inside the click handler, and show the total on the page. This is the first time you will have kept track of something in JavaScript across multiple clicks.

Either is fine. One that works beats two that half-work.

When it does not work, and it will not on the first try, open the browser console before you do anything else. Right-click, Inspect, Console tab. In JavaScript, a broken button does not shout at you like Python does; it just quietly does nothing, and the explanation is sitting in the console.

## 4. Walk the pipeline in your own words

Write a short paragraph, five or six sentences, answering this: you type an address and press return. The HTML arrives. What does the browser do between receiving that text and showing you pixels?

Use these words correctly: DOM, render tree, layout, paint.

Then answer one more question in two sentences: when your button changes the text on the page, which part of that pipeline has to run again, and why does the page not reload?

## 5. Inspect a real site

Open any website you use. Right-click something on it and choose Inspect.

1. In the Elements panel, find the element you clicked and look at what is wrapped around it. How many levels deep is it?
2. Double-click some text in the Elements panel and change it. Take a screenshot of the changed page.
3. Reload. Write one sentence explaining why your change disappeared.
4. Open the Network panel and reload again. How many separate requests did that one page make? Write the number down.

Bring the number to class. We will compare.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. Web code is everywhere online and it is very easy to paste something you cannot explain. If you get stuck, MDN is the right place to look, and bringing a written-down question to class is always allowed. Stuck is normal; it is where the learning is.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**Straight answer first: this week is mostly not on the AP exam.** HTML and CSS are not tested. The DOM is not tested. JavaScript syntax is not tested, and the exam is deliberately written so that it does not matter what language you code in. If you were studying only for the score, today would be a skip.

We teach it because it is how real software gets built, and because next week depends on it. Next week is the strongest AP week of this whole unit, so if your AP time this week is limited, save it.

Two things from today that do connect honestly:

- Separating structure, presentation, and behavior into three files is abstraction, which the exam does care about, just not in this form.
- Event-driven programming, where your code waits for a click instead of running top to bottom, is exactly how CodeAI's App Lab works, and app design does show up in the exam's questions about program purpose and user interfaces.

**Your unit for this week.** There is no clean match, so pick whichever of these fits your situation. Do only that slice.

- **Project STEM (the AP spine):** nothing in the course matches today. The best use of an AP hour this week is to keep going in whatever unit you are currently working, or to go back and close a gap from an earlier week. Do not go looking for a web unit; there is not one, and hunting for it wastes the hour. If the unit numbering on your account does not match what your instructor gave you, ask; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`. In Week 22 you were pointed at the design-process lessons in that unit. This week, do the App Lab programming lessons instead. You build screens with buttons that respond to clicks, which is the same idea as today's page in a different environment.

**Extra practice if you want it.**

- Add a media query to your stylesheet so the page looks different on a narrow screen, then test it by dragging your browser window narrow. This is the first step toward what Week 26 is about.
- Run Lighthouse on your page. It is built into Chrome's developer tools. Read the accessibility section and fix one thing it complains about. Accessibility is a real and underrated part of Big Idea 5's beneficial-effects material, and it is one of the few places today's work touches the exam at all.
- Ask an honest question and write down your answer: your page has three separate files that a browser has to fetch separately. Why would anyone split it up that way instead of putting everything in one file? Then find out what a browser cache is and revise your answer.
