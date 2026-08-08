# Week 24 Teacher Guide

## 1. Header

- **Week:** 24 of 32
- **Unit:** 5, Building Modern Software
- **Theme question:** What is a web page actually made of?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Name the three languages of a web page and say what each one is responsible for: structure, presentation, behavior.
- Describe what the browser does between receiving bytes and showing pixels, in the right order.
- Explain what the DOM is and why it is a tree in memory rather than the file on disk.
- Write a valid HTML page from scratch with a head, a body, headings, a list, and semantic sections.
- Style that page with an external stylesheet using selectors, properties, and values.
- Attach a JavaScript event listener to a button and change the page from code.
- Serve the page locally over HTTP and inspect it with browser developer tools.

## 3. Where this sits

Unit 4 explained how bytes get from a server to a browser. It stopped at the moment the bytes arrive. Today picks up exactly there and follows them to the screen, which closes the year's central question of how a button press becomes something useful for the web half of the course.

The readiness guide flags this week honestly as a difficulty spike: three new notations arrive at once, and the mitigation it recommends is to scope down, doing HTML and CSS properly and keeping JavaScript light. Follow that. One button, one event listener, one line of the page changing is a complete and sufficient JavaScript outcome for today. Students who want more can have more in the homework.

Continuity in both directions matters this week. Everything built today lives in a Git repository from the first minute, using last week's skills for real rather than as an exercise. The page built today becomes the Flask template next week and the installable Progressive Web App in Week 26. Say that out loud at the start; students work harder on a thing that is going somewhere.

One deliberate omission: no frameworks, no build tools, no `npm`. Three files and a browser. Students should see the platform before anyone hands them an abstraction over it.

## 4. Materials and setup

- Each student's laptop with VS Code, Python, Git, and both Chrome and Firefox.
- Projector at a large font, with VS Code and a browser side by side on the demo machine. Practice the window arrangement in advance; this session is unteachable if the class cannot see both at once.
- Whiteboard with the theme question, and a clear area for the pipeline diagram, which stays up all session.
- A real, content-heavy web page bookmarked for the view-source and DevTools demonstration. A news site or a school page works. Verify it loads on the classroom network before class.
- Printed one-page reference sheet with the HTML skeleton, five CSS properties, and the JavaScript event-listener pattern, one per student. Write it from the code in Section 6.
- Printed Week 24 homework handout, one per student.

## 5. Pre-class prep checklist

- Build the complete three-file page yourself in a scratch folder and get it running under `python3 -m http.server`. Keep it open in a second window during class as your reference. (25 min)
- Practice the DevTools sequence on the demo machine: Inspect, edit text in the Elements panel, reload to show the edit vanish, then Network and Console. If you have not used the Elements panel before, spend fifteen minutes here; the live-edit moment is the one students remember. Developer tools change between browser releases; verify the panel names against the version installed. (20 min)
- Decide your content boundary and be ready to state it in one sentence: no last names, no addresses, no school name, no photographs of people, and nothing that is going on the public internet today. (5 min)
- Check that Chrome or Firefox on the fleet is not blocking `localhost` through the DNS filter or a proxy setting. Test `python3 -m http.server` on a student machine, not just yours. (10 min)
- Write and print the reference sheet, and print homework handouts. (15 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up, view source (0:00 to 0:10)

- **You do:** Pose the theme question. Then open the bookmarked real page and, before anything else, use View Page Source. A wall of text appears. Let the groan happen.
- **You do:** Say the honest thing: this is not written by hand and nobody reads it this way, but every single character of it is one of the three things we are learning today, and by the end of the session they will recognize all three.
- **You do:** Find and point at exactly three things in the source: an `<h1>` or similar tag, a `<link rel="stylesheet">`, and a `<script src=...>`. Say what each one is. Then close it.
- **You do:** Homework check by show of hands: who pushed to GitHub, who caused and resolved a conflict. Note the gaps for follow-up, and move on.

### Segment 2: From bytes to pixels (0:10 to 0:32), Systems strand

1. **Restate where Unit 4 stopped.** Draw the line on the board: DNS, TCP, TLS, HTTP request, response arrives. Everything left of that line was last unit. Everything right of it is today.
2. **State the division of labor before any syntax.** Write three columns on the board and fill them as you go: HTML is structure, the nouns, what things are. CSS is presentation, the adjectives, what things look like. JavaScript is behavior, the verbs, what happens when someone does something. Say that keeping these three separate is the single organizing idea of the whole web platform, and that mixing them is the technical debt of front-end work.
3. **Say the thing students are never told.** HTML is not a programming language. It has no variables, no conditionals, and no loops; it cannot compute anything. It is a markup language, a way of labeling text with what it is. CSS is not a programming language either. JavaScript is one. This distinction matters and it will come up again in the AP discussion.
4. **Draw the pipeline as one line across the board,** and walk it left to right:
   - **Bytes to characters to tokens to nodes.** The browser reads the HTML text and builds objects out of it.
   - **The DOM.** Those objects are assembled into a tree, with `html` at the root, `head` and `body` as children, and every element nested underneath. Draw the tree for a four-element page.
   - **The CSSOM.** The stylesheets get parsed into their own tree of rules.
   - **The render tree.** The two get combined into what is actually going to be drawn. Note that elements with `display: none` are in the DOM but not here.
   - **Layout.** The browser computes where every box goes and how big it is. This step depends on the window size, which is why resizing redoes it.
   - **Paint and composite.** Pixels get filled in, in layers, and the layers get stacked.
5. **Land the key idea about the DOM,** because it is the one that unlocks JavaScript later: the DOM is a live tree of objects in memory. It is built from the file but it is not the file. Code can change the tree, and when the tree changes the browser redoes layout and paint. That is how a page changes without reloading.
6. **Prove it with DevTools, in four moves.** Right-click the real page and choose Inspect. First, hover over nodes in the Elements panel and watch the highlight move on the page, showing that the tree and the pixels are two views of one thing. Second, double-click a headline's text, type nonsense, and press return. The page changes. Third, reload. The nonsense is gone, because you edited the tree in memory, never the file on the server. That single demonstration teaches the DOM better than any diagram. Fourth, open the Network panel and reload, and point out that one page is many separate requests: the HTML, then each stylesheet, each script, each image.
7. **One sentence on why any of this matters for speed.** A page that makes ninety requests and forces layout repeatedly is slow, and that is a design decision, not a fact of nature.

### Segment 3: HTML from scratch (0:32 to 1:02), Coding strand part 1

1. **Set up the project, with Git from the first minute:**

   ```bash
   cd ~/cs-sandbox
   mkdir personal-page
   cd personal-page
   git init
   code .
   ```

   Create three empty files in the Explorer: `index.html`, `style.css`, `script.js`. Say why `index.html` has that exact name: a web server hands out `index.html` when someone asks for a folder, and that convention is older than most of the internet.
2. **State the content boundary out loud, before anyone writes a word.** First names only. No last names, no address, no school name, no photographs of people, no anything they would not read out to a stranger. This page runs on their laptop today and is not being published. Do not skip this.
3. **Build the skeleton at the projector, line by line, naming each part.** Type it; do not paste.

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <title>Ada's Page</title>
     <link rel="stylesheet" href="style.css">
   </head>
   <body>
   </body>
   </html>
   ```

   Name them: `<!DOCTYPE html>` says this is modern HTML. `lang="en"` tells screen readers and translators what language this is. `charset="utf-8"` is why accented characters and emoji do not turn into garbage, and it is the same character-encoding story from Week 2. The viewport line is what makes the page usable on a phone, and Week 26 depends on it. `<title>` is the tab label, not anything on the page. The `<link>` pulls in the stylesheet, which does not exist yet, and that is fine.
4. **Explain a tag once, properly.** An element is an opening tag, content, and a closing tag: `<h1>Ada</h1>`. Some elements have no content and no closing tag, like `<meta>` and `<br>`. Attributes go in the opening tag as `name="value"`. Elements nest, and they must nest cleanly, like brackets in Python, never crossing.
5. **Fill the body together:**

   ```html
   <body>
     <header>
       <h1>Ada</h1>
       <p>Things I am working on this year.</p>
     </header>

     <main>
       <section>
         <h2>Projects</h2>
         <ul>
           <li>A text adventure in Python</li>
           <li>A five-bit binary converter</li>
         </ul>
       </section>

       <section>
         <h2>One fact</h2>
         <p id="fact">Click the button.</p>
         <button id="fact-button">Show me a fact</button>
       </section>
     </main>

     <footer>
       <p>Built from scratch, Week 24.</p>
     </footer>

     <script src="script.js"></script>
   </body>
   ```

   Two things to name deliberately. First, `<header>`, `<main>`, `<section>`, and `<footer>` are semantic: they say what a chunk of the page is for, which matters to screen readers and search engines, and they are why professional HTML is not a pile of anonymous `<div>` tags. Second, the two `id` attributes exist so that JavaScript can find those elements later. Nothing else needs an id.
6. **Serve it over HTTP rather than opening the file.** From the project folder:

   ```bash
   python3 -m http.server 8000
   ```

   Then visit `http://localhost:8000` in the browser. They did this in Week 20. Say why it matters and not just that it works: opening the file directly gives a `file://` address, which behaves differently from a real page in ways that will bite them in Weeks 25 and 26. Get in the habit now. Stop the server with Control-C.
7. **Look at the unstyled page.** It is black text on white with default fonts, and it is a completely functional web page. Say so. Everything from here is decoration and behavior on top of a thing that already works, which is the right order.
8. **Students do:** Build their own version with their own content. Minimum: a heading, two paragraphs, a list of at least three items, and the two elements with ids. Then commit:

   ```bash
   git add .
   git commit -m "Add the page structure"
   ```

### Segment 4: Stretch (1:02 to 1:07)

### Segment 5: CSS (1:07 to 1:32), Coding strand part 2

1. **Name the three parts of a rule** before typing one: a selector picks elements, and inside the braces each declaration is a property and a value separated by a colon and ended with a semicolon.
2. **Write the stylesheet at the projector, reloading after every block** so the class watches the page change:

   ```css
   body {
     font-family: system-ui, sans-serif;
     max-width: 40rem;
     margin: 2rem auto;
     padding: 0 1rem;
     line-height: 1.5;
     color: #222;
     background: #fdfdfb;
   }

   h1 {
     color: #1b4965;
     border-bottom: 2px solid #1b4965;
   }

   #fact {
     font-style: italic;
     min-height: 2rem;
   }

   button {
     font-size: 1rem;
     padding: 0.5rem 1rem;
     cursor: pointer;
   }
   ```
3. **Explain three selector types and stop there.** `body` and `h1` are element selectors, matching every element of that kind. `#fact` is an id selector, matching the one element with that id. A class selector looks like `.warning` and matches every element with `class="warning"`, which is the one they should reach for when several elements need the same treatment. Three kinds is enough for today.
4. **Teach the box model with a real box.** Every element is a rectangle with content in the middle, then padding, then a border, then margin outside it. Show it in DevTools: select an element, find the box-model diagram in the styles pane, and hover over each ring to see it highlighted on the page. That diagram answers most CSS questions students will have for the next year.
5. **Explain `max-width: 40rem; margin: 2rem auto`** because it is the single most useful line in the file: it stops the text from stretching to the full width of a large monitor and centers the column. Ask why long lines are hard to read. Then resize the window and watch it adapt.
6. **Colors, briefly, and connect it to Week 2.** `#1b4965` is three bytes in hexadecimal: red, green, blue, each from 0 to 255. This is the same binary-and-place-value idea from Week 2 wearing a different costume. Have them change one hex pair and reload.
7. **Students do:** Style their own page. Requirement is deliberately low: change the font, set a max width, and pick two colors that are actually readable together. Then use DevTools to change one value live, find a version they like, and copy it back into the file. That workflow, experiment in the browser then save to the file, is how front-end work is actually done.
8. **Commit:** `git add . && git commit -m "Style the page"`

### Segment 6: JavaScript and the DOM (1:32 to 1:52), Coding strand part 3

Keep this light and complete rather than broad. One button that works beats five things half-explained.

1. **Set expectations in a sentence.** They know one programming language well. This is a second one, and today they are getting a tourist's view of it, enough to make one thing on the page respond to a click.
2. **Put this translation table on the board and leave it up:**

   | Idea | Python | JavaScript |
   |---|---|---|
   | Make a variable | `name = "Ada"` | `const name = "Ada";` |
   | A variable that changes | `count = 0` | `let count = 0;` |
   | Print for debugging | `print(x)` | `console.log(x);` |
   | A list | `[1, 2, 3]` | `[1, 2, 3]` |
   | Length | `len(items)` | `items.length` |
   | Equality test | `a == b` | `a === b` |
   | Block boundaries | indentation | curly braces |

   Call out the three things that trip Python programmers: braces instead of indentation, semicolons at the end of statements, and the triple equals for comparison. Tell them `===` exists because JavaScript's `==` does surprising conversions, and that the rule is to always use three.
3. **Write the script at the projector:**

   ```javascript
   const facts = [
     "A commit stores the whole project, not just the changed lines.",
     "Five binary cards can make any number from 0 to 31.",
     "The internet and the web are not the same thing."
   ];

   const button = document.getElementById("fact-button");
   const paragraph = document.getElementById("fact");

   button.addEventListener("click", function () {
     const pick = Math.floor(Math.random() * facts.length);
     paragraph.textContent = facts[pick];
   });
   ```
4. **Read it out loud in four moves, in this order.** `document` is the DOM tree from Segment 2, available to code as an object. `getElementById` walks that tree and hands back one node, which is why those ids were added. `addEventListener` says: when this thing happens to that element, run this function. Setting `.textContent` changes the tree, and the browser redoes layout and paint on its own, which is the loop from the pipeline diagram closing.
5. **Name the new idea explicitly, because it is genuinely new.** Every Python program they have written ran top to bottom and stopped. This one sets something up and then waits. That is event-driven programming, and it is how every interface they have ever used works.
6. **Connect the random line to Week 4.** `Math.random()` returns a decimal between 0 and 1, multiplying scales it to the list length, and `Math.floor` chops off the decimal. It is `random.randint` built from parts, and it also shows what a language without a batteries-included standard library feels like.
7. **Students do:** Get one button working on their own page. That is the whole requirement.
8. **Show the Console panel** when the first error appears, and it will. A JavaScript error does not stop the page or show a traceback on screen; it prints to the console and everything just silently does nothing. Say that plainly: in JavaScript, nothing happening is the error message, so open the console first, always.
9. **Commit:** `git add . && git commit -m "Add the fact button"`

### Segment 7: Wrap and homework (1:52 to 2:00)

- **You do:** Point at the pipeline diagram and have the class walk it back: their file, the DOM, the render tree, layout, paint, and then a click that changed the tree and made the whole tail of it run again.
- **You do:** Say where this is going. Next week a Python program serves this page and fills it with live data from the internet. In Week 26 it becomes something installable on a phone.
- **You do:** Hand out homework and walk through it, including the Extra Credit AP Track section, and note out loud that this week's AP section is thin on purpose and why.

## 7. Key scripts and analogies

- **The three languages:** "HTML is the nouns, CSS is the adjectives, JavaScript is the verbs. A page with only HTML is a plain list of true statements. It still works."
- **HTML is not programming:** "HTML cannot decide anything, count anything, or repeat anything. It labels text with what that text is. That is not a criticism; it is the job."
- **The DOM:** "Your file is a recipe. The DOM is the meal. The browser cooks the recipe once, into a tree of objects in memory, and from then on everything, including your JavaScript, works on the meal."
- **Why editing in DevTools does not stick:** "You changed the meal, not the recipe. Reload and the browser cooks the recipe again."
- **Layout:** "Before it can draw anything, the browser has to decide where every rectangle goes and how big it is. Change one thing near the top and it may have to redo the whole page."
- **The box model:** "Every element is a box. Content, then padding inside the border, then the border, then margin holding other boxes away. Nine out of ten CSS questions are actually box-model questions."
- **Semantic tags:** "`<div>` says nothing. `<header>` says what this is. Somebody using a screen reader, and every search engine on earth, can only work with the version that says something."
- **Event-driven code:** "Every program you have written so far ran to the bottom and quit. This one sets a trap and waits. That is what an app is."
- **Silent JavaScript failure:** "In Python, a mistake shouts at you. In JavaScript, a mistake means the button just does not do anything. Open the console; that is where it went."

## 8. Differentiation

- **Younger or newer students:** This is the scope-down week the readiness guide calls for. Give them a printed, complete `index.html` skeleton and have them fill in only their own content, then do the CSS segment fully, which is the most immediately rewarding part of the day. For JavaScript, give them the entire script file working and have them change only the strings in the `facts` list and the button's label. Reading working code and modifying it is a real outcome. Pair them with a partner for the terminal steps.
- **Extensions for advanced or AP-track students:** Add a second button that changes a CSS property, using `element.style.background = "..."`. Add a counter with `let` that increments on each click and displays how many facts have been shown, which is the first JavaScript state they will have written. Make the page responsive with a media query and test it by narrowing the window. Use `querySelectorAll` and a loop to change every list item at once. Run the browser's built-in Lighthouse audit and read the accessibility section. The strongest can push the repository to GitHub and turn on GitHub Pages, with your approval and the content rules enforced, since that publishes to the public internet.

## 9. Common pitfalls

- **Opening the file instead of serving it.** The address bar says `file://`. It mostly works today and breaks in Weeks 25 and 26. Insist on `python3 -m http.server` and check address bars as you circulate.
- **The stylesheet is not loading.** Nearly always a wrong `href`, a misspelled filename, or the file saved in a different folder. Teach the diagnosis rather than the fix: open the Network panel and look for the 404.
- **Unclosed or crossed tags.** The browser will not complain; it will silently guess and render something strange. Use VS Code's auto-closing and its bracket highlighting, and show the Elements panel as the way to see what the browser actually built.
- **The script tag placed in the head.** The script then runs before the elements exist, `getElementById` returns null, and the listener line throws. Keep the script tag at the bottom of the body as written, and if a student moves it, use it as the teaching moment.
- **Mismatched ids.** `fact-button` in the HTML and `factButton` in the JavaScript. Silent failure. First thing to check when a button does nothing.
- **Not opening the console.** Students conclude their code "does not work" without ever looking at the one place the error went. Make opening the console the first debugging move, the same way reading the traceback is in Python.
- **CSS specificity confusion.** A student writes a rule and something else overrides it. Do not teach specificity today; show them the Styles pane, where the losing rule appears with a line through it, and let that be the answer.
- **Personal information on the page.** Enforce the boundary from Segment 3 as you circulate. Nothing published today, and nothing identifying even locally.
- **JavaScript overrun.** Segment 6 will try to eat the whole session if a student asks a good question about `let` versus `const`. Answer in one sentence and keep moving.

## 10. Homework

Full details in `handouts/week-24-homework.md`. In summary: finish the personal page to a stated definition of done and commit each piece separately; add one CSS rule they did not use in class and say what it does; add a second button or a counter; a short written walk of the rendering pipeline in their own words; a DevTools exercise on a real site. The handout closes with an Extra Credit AP Track section, which is deliberately light this week.

## 11. Assessment

Observational and completion-based, against the weekly-labs rubric, plus the Git history: `git log --oneline` in each student's `personal-page` repository should show at least three commits with sensible messages, which is last week's skill being used rather than practiced.

Three specific things to check by watching:

1. The page is being served from `http://localhost:8000`, not opened as a file.
2. The stylesheet is actually attached, verified by the page looking different rather than by the student saying so.
3. The button works, and the student can say which line finds the element and which line changes it.

The verbal check that matters: ask a student to point at the page and then at the Elements panel and say which one is the DOM. A student who says the file is the DOM has the misconception this whole session exists to fix.

## 12. AP alignment

Say this plainly to students rather than dressing it up. **This week is largely not AP CSP content.** HTML and CSS are not on the exam. The DOM is not on the exam. JavaScript syntax is not on the exam, and the exam is deliberately language-agnostic. A student optimizing purely for the AP score would skip today.

We teach it anyway for two good reasons. It is how the software people actually use gets built, and this course exists to explain the world, not only to pass a test. And it is the load-bearing prerequisite for the next two weeks, one of which, Week 25, is the strongest AP week in the entire unit.

The honest partial connections, offered as connections and not as coverage:

- The layered separation of structure, presentation, and behavior is abstraction in the sense Big Idea 3 uses the word, and the browser is an abstraction layer over the operating system in the sense Big Idea 4 uses it.
- Event-driven programming, where code waits for a user action rather than running top to bottom, is the model CodeAI's App Lab uses throughout its app-design unit, so students who work that unit will recognize today's button immediately.

**AP-track self-study for this week, and only this week's slice.** There is no clean match this week, so the honest options are these, and either is fine:

- **Project STEM (the AP spine):** no unit matches today's content. The best use of an AP hour this week is to keep working whichever unit you are currently in, or to close a gap from an earlier week. Do not go hunting for a web unit; forcing the match wastes the hour. Verify unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 3, Intro to App Design, at `https://studio.code.org/courses/csp-2025/units/3`, and this week specifically the App Lab programming lessons rather than the design-process ones done in Week 22. They build event-driven screens in a JavaScript-flavored environment, which is genuinely the same idea as today's button listener, in a form the exam's app-design questions do use.

Nothing here is required of non-AP students. Next week is the one to save energy for.

## 13. Resources used this week

- The full three-file build: complete inline in Segments 3, 5, and 6. Nothing external needs to be open during class.
- **Prep note:** run the DevTools sequence in Segment 2 once yourself before teaching it, specifically the live text edit followed by a reload. It is the demonstration the whole DOM concept rests on, and the panel layout differs between browsers and versions.
- MDN Web Docs, the reference to use for your own prep and to point students at for the homework: `https://developer.mozilla.org`. Specifically the HTML element reference and the CSS properties reference. MDN is the correct answer whenever a student asks where to look something up.
- Python's built-in web server, used to serve the page: `python3 -m http.server 8000`, already familiar from Week 20. Documentation at `https://docs.python.org/3/library/http.server.html`. It is a development tool and is not suitable for anything public.
- Browser developer tools: built into Chrome and Firefox, nothing to install. Panel names and layout change between releases; verify against the fleet's installed version.
- CodeAI CSP Unit 3, Intro to App Design (the nearest AP-track fit, App Lab lessons): `https://studio.code.org/courses/csp-2025/units/3`
- Why this week is scoped down for newer students: `student-prep/Younger-Student-Readiness-and-Prep.md`, the web-stack row of the risk table.
- Web development extra-credit project track, for students who want to keep going: Section 9 of `curriculum/CS-Curriculum-and-Setup.md`.
