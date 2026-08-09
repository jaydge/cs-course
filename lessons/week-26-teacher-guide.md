# Week 26 Teacher Guide

## 1. Header

- **Week:** 26 of 32
- **Unit:** 5, Building Modern Software
- **Theme question:** Why does the same app exist five different ways?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Name the three main ways to build a mobile app, native, cross-platform, and Progressive Web App, and give one real advantage and one real cost of each.
- Explain why a company might rationally choose any of the three, given a described situation.
- Describe what a phone gives an app that a laptop does not: sensors, GPS, push, permissions, offline storage, and cloud sync.
- Explain what an app permission is and why the operating system, not the app, controls it.
- Convert their Flask web app into a Progressive Web App by adding a manifest and a service worker.
- Explain what a service worker is, and why it only runs over HTTPS or on localhost.
- Demonstrate Unit 5 mastery on the checkpoint.

## 3. Where this sits

This closes Unit 5 and the "build something real" arc. Weeks 22 through 25 assembled process, version control, the web, and live data. Today adds the last layer, which is how that software reaches a phone, and then converts their own app to prove the point rather than just describing it.

The systems half is a guided tour and should be treated as one: broad, honest, no code, ending in a judgment students can actually make. The coding half is the PWA conversion, which is genuinely the cheapest possible route from "a web page" to "a thing on a home screen," and that fact is itself the lesson.

Unit 6 opens next week with AI, and it is also the week the no-AI phase ends. For AP-track students, February and the nine-hour Create Task window open in Unit 6 too, so today's Extra Credit AP Track section moves Create Task planning from orientation to a concrete choice of idea.

Give the checkpoint fifteen protected minutes at the end. It is the last checkpoint before the final project.

## 4. Materials and setup

- Printed Unit 5 checkpoint, one per student. See Section 11 for what it covers.
- Each student's laptop with their working `weather` Flask project from Week 25, VS Code, Git, and Chrome. Chrome specifically: its Application panel is the clearest tool for this lab, and its install flow is the most predictable. Verify before class.
- Two placeholder PNG icons, 192 by 192 and 512 by 512 pixels, distributed to every student or committed to the class-server repository. Do not spend class time making icons.
- Projector, with Chrome DevTools open on the demo machine and the Application panel already found.
- Your own phone, and optionally one classroom test device, for the install demonstration. See the caution in Section 5.
- Whiteboard with the theme question, and a four-column area for the approach comparison.
- Printed Week 26 homework handout, one per student.

## 5. Pre-class prep checklist

- **Write and print the Unit 5 checkpoint.** Cover the six areas in Section 11 and keep it to about fifteen minutes of work. Write the answer key at the same time. (35 min)
- **Do the entire PWA conversion yourself, on the demo machine, and install it.** Then delete the service worker and cache, and do it again from scratch, because you will need to un-stick at least one student's cached service worker during class and the unregister flow is worth having in your fingers. (30 min)
- **Decide the phone story before class, because this is where the lab bites.** Service workers only run over HTTPS or on `localhost`. Flask on `http://127.0.0.1:5000` qualifies, so the whole lab works on the laptop. A phone reaching the laptop over the classroom network at `http://192.168.x.x:5000` does not qualify, and the service worker will silently refuse to register. Pick one: do the install demonstration on laptops only, which is the recommended default; or run a single instructor-led phone demonstration using Chrome's remote-debugging port forwarding from `chrome://inspect`, which does make the phone treat the address as localhost. Do not attempt twelve phones. (20 min)
- Prepare the two placeholder icons and get them onto every machine. (10 min)
- Confirm every student's Week 25 Flask app still runs, and confirm the project actually contains `templates/index.html`, `static/style.css`, and `static/script.js`. That third file is the one that goes missing, because a page renders perfectly well without it, and today's service worker precaches it by name and fails its whole install if it is absent. If a student's project has no `static/script.js`, copy theirs across from their Week 24 `personal-page` folder now and add the `<script src="{{ url_for('static', filename='script.js') }}"></script>` line to the template. Fix broken apps before class if you can; a student with no working app cannot do the lab. (20 min)
- Refresh yourself on the current state of PWA support, which genuinely changes year to year, particularly on iOS. Verify anything you plan to state as fact about what a PWA can and cannot do on each platform. (15 min)
- Print the checkpoint and homework handouts. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and framing (0:00 to 0:10)

- **You do:** Pose the theme question. Then make it concrete: pick a large service everyone knows and list where it exists. An iPhone app, an Android app, a website, and possibly a desktop app and a watch app. Ask the class whether that is one program or five. Take answers; do not resolve it yet.
- **You do:** Quick homework check. Who has a Flask app that runs, and whose page still loads when the network is off? Anyone whose app is broken pairs up now.
- **You do:** Set the shape of the day: forty-five minutes on how mobile software actually works, thirty-five minutes turning their own app into something installable, then the Unit 5 checkpoint.

### Segment 2: Three ways to build the same app (0:10 to 0:38), Systems strand

1. **Start with what a phone actually is.** A computer with a small screen, a battery that matters, an always-on radio, a pile of sensors, and an operating system that is far more controlling than a laptop's. Every difference below flows from those five facts.
2. **Build this table on the board as you talk, one column at a time.** Do not hand it out finished; the class fills it with you.

   | | Native | Cross-platform | Progressive Web App |
   |---|---|---|---|
   | What it is | Written per platform in the platform's own language | One codebase compiled or run on both | A web page with extra parts |
   | Tools | Kotlin with Android Studio; Swift with Xcode | Flutter (Dart), React Native (JavaScript), .NET MAUI (C#) | HTML, CSS, JavaScript |
   | Codebases | Two | One | One |
   | Hardware access | Everything, immediately | Most things, sometimes late | Limited, varies by platform |
   | Distribution | App store | App store | A URL |
   | Update speed | Store review, days | Store review, days | Instant |
   | Best when | Performance and deep OS integration matter | Budget matters and the app is mostly screens and data | Reach and update speed matter most |

3. **Native, honestly.** Android apps in Kotlin using Android Studio and Jetpack Compose; iOS apps in Swift using Xcode and SwiftUI. Full access to every capability the moment the platform ships it, the best performance, and interfaces that feel correct because they use the real system components. The cost is real and large: two codebases, two languages, two toolchains, and often two teams, for one product. Note that Xcode runs only on macOS, which is a hard constraint on who can build for iOS at all.
4. **Cross-platform, honestly.** One codebase, both stores. Explain the two different strategies in one line each, because the difference matters: Flutter draws every pixel itself with its own rendering engine, so it looks identical everywhere and slightly unlike either platform; React Native drives the platform's real components from JavaScript, so it looks native and inherits both platforms' quirks. .NET MAUI is the same idea for teams already living in C#. The cost is a layer of indirection: when something new or unusual is needed, you are waiting for someone to bridge it, and debugging crosses the boundary.
5. **Progressive Web App, honestly.** A web page with two additions: a manifest file that says it is an app, and a service worker that lets it work offline. It installs from a URL with no store involved, updates the instant you deploy, and runs on anything with a modern browser. The costs are genuine: less access to hardware, capability differences between platforms that shift year to year, no presence in the store where people look for apps, and a ceiling on performance for anything graphics-heavy. Say clearly that platform support for PWA features changes often enough that any specific claim should be checked rather than remembered.
6. **Mention the fourth thing in one sentence** so students recognize the word later: a hybrid app wraps a web app inside a native shell with a bridge to device features, using tools like Capacitor. It is a middle position, not a fourth philosophy.
7. **Now make them choose.** Read four scenarios and take a vote and a reason on each. This is the segment's actual assessment.
   - A bank with a large budget, strict security requirements, and a need for Face ID and secure storage. (Native is defensible; the deep OS integration is the whole point.)
   - A four-person startup with one JavaScript developer and eight weeks of runway. (Cross-platform or a PWA; two native codebases would eat them alive.)
   - A restaurant that wants customers to see today's menu and order. (A PWA; nobody installs an app to read a menu once, and the URL is the distribution.)
   - A studio building a 3D game with real-time physics. (Native, or a game engine that compiles to native; the performance ceiling is the deciding factor.)
8. **Land the general rule.** The right answer depends on the team you have, the money you have, how deep into the hardware you need to go, and how fast you need to ship changes. Nobody picks a technology because it is the best technology; they pick it because it fits those four constraints. That is engineering judgment, and it is a different skill from programming.
9. **Add the constraint students never think of: the store is a gatekeeper.** Both major stores take a cut of purchases, review every submission, can reject an app for reasons the developer cannot appeal well, and control what may be distributed at all. For some companies that is the single deciding factor in favor of the web. Flag it as something Unit 6's ethics week comes back to.

### Segment 3: What the phone gives an app (0:38 to 0:55), Systems strand

1. **Permissions, and who is really in charge.** An app does not decide it can use the camera. The operating system does, and it asks the user. Demonstrate on your own phone: open the settings for one app and show the list of switches. Name the model: apps are sandboxed, meaning each one is walled off and cannot read another app's data or the whole filesystem, and anything outside the wall requires a permission the user grants at runtime and can revoke later. Ask the good question: why ask at the moment of use rather than at install time? Because a request in context is one a person can actually judge.
2. **State the principle and connect it forward.** Least privilege: ask for the minimum you need, at the moment you need it. An app requesting contacts, location, and the microphone to show a bus timetable is telling you something, and Unit 6's ethics week will come back to exactly that.
3. **Sensors, quickly.** Accelerometer for movement and orientation, gyroscope for rotation, magnetometer as a compass, ambient light for screen brightness, barometer on some devices, plus camera and microphone. Ask what a step counter is actually made of: an accelerometer plus an algorithm looking for a repeated pattern. Most sensor features are a cheap sensor plus clever software, not a magic sensor.
4. **GPS, in four sentences.** Satellites broadcast the time continuously. The phone hears several of them, and because the signals took different amounts of time to arrive, it can solve for its own position. It needs several satellites at once, which is why it fails indoors. Phones cheat by also using known Wi-Fi network locations and cell towers, which is why a position appears indoors and why it is sometimes confidently wrong.
5. **Push notifications, and the surprise in them.** The server does not contact the phone. It cannot; the phone moves networks and is usually asleep. The app's server sends the message to the platform's push service, Apple's or Google's, which holds a single persistent connection to the device and delivers it. Ask why the platform insists on being in the middle. Battery: one connection for all apps instead of one per app. Add the consequence, which is real: the platform can see that a message was sent and can refuse to deliver it.
6. **Offline storage.** A phone is offline constantly, in lifts, tunnels, and dead zones, so an app that needs the network for every action is unusable. Apps keep a local copy: a small database on native platforms, and in the browser the Cache API and IndexedDB, which is what the lab uses next.
7. **Cloud sync, and the callback that lands this whole unit.** If the phone has a local copy and the server has a copy and both change while offline, you have two versions of the same thing. Ask the class what that is. It is a merge conflict, from Week 23, and the resolution strategies are the same family: take the newest, take the server's, take the user's, or ask a human. Say the honest version: most apps quietly pick "the last write wins" and occasionally lose someone's work because of it.

### Segment 4: Stretch (0:55 to 1:00)

### Segment 5: Convert the app to a PWA (1:00 to 1:35), Coding strand

Students work in their Week 25 `weather` project at `~/Documents/"CS Class"/weather`. Everything runs against `http://127.0.0.1:5000`, which counts as a secure context, so service workers will register.

Before anyone types anything, have every student run `ls static templates` in the project and read the result out. They should see `index.html` in `templates/`, and `style.css` and `script.js` in `static/`. All three came across from Week 24 during last week's Segment 3. The service worker written in step 6 names two of those files by path and will refuse to install if either is missing, so spending thirty seconds here saves the lab.

1. **State the definition first.** Three things turn a web page into an installable app: it must be served over HTTPS or localhost, it must have a manifest describing it, and it must register a service worker. Nothing else is required.
2. **Say what a service worker is, before writing one,** because the mental model is the hard part. It is a JavaScript file the browser keeps running in the background, separately from any page, and it sits between the page and the network. Every request the page makes goes through it first, and it decides whether to answer from a local cache or go out to the network. Draw it on the board as a box between the page and the internet. Add the two rules that explain every confusing thing about them: it has no access to the page's DOM, and it keeps running after the tab is closed.
3. **Create the manifest** at `static/manifest.json`:

   ```json
   {
     "name": "My Weather Page",
     "short_name": "Weather",
     "start_url": "/",
     "display": "standalone",
     "background_color": "#fdfdfb",
     "theme_color": "#1b4965",
     "icons": [
       { "src": "/static/icon-192.png", "sizes": "192x192", "type": "image/png" },
       { "src": "/static/icon-512.png", "sizes": "512x512", "type": "image/png" }
     ]
   }
   ```

   Name two fields specifically. `display: standalone` is what removes the browser's address bar so it looks like an app rather than a page. `start_url` is what opens when the icon is tapped. Copy the two placeholder icons into `static/`.
4. **Link the manifest** in the `<head>` of `templates/index.html`:

   ```html
   <link rel="manifest" href="{{ url_for('static', filename='manifest.json') }}">
   <meta name="theme-color" content="#1b4965">
   ```
5. **Serve the service worker from the root, and explain why.** A service worker can only control pages at or below its own path, which is called its scope. Served from `/static/sw.js` it would control only `/static/`, which is useless. Add `send_from_directory` to the import line already at the top of `app.py`, so it reads:

   ```python
   from flask import Flask, render_template, send_from_directory
   ```

   Then add a second route, below the existing `home()` route:

   ```python
   @app.route("/sw.js")
   def service_worker():
       return send_from_directory("static", "sw.js", mimetype="application/javascript")
   ```

   This is the single most common reason a first PWA does not work, so make them say the word scope out loud.
6. **Write the service worker** at `static/sw.js`:

   ```javascript
   const CACHE_NAME = "weather-v1";
   const PRECACHE = [
     "/",
     "/static/style.css",
     "/static/script.js",
     "/static/offline.html"
   ];

   self.addEventListener("install", function (event) {
     event.waitUntil(
       caches.open(CACHE_NAME).then(function (cache) {
         return cache.addAll(PRECACHE);
       })
     );
   });

   self.addEventListener("activate", function (event) {
     event.waitUntil(
       caches.keys().then(function (names) {
         return Promise.all(
           names.filter(function (n) { return n !== CACHE_NAME; })
                .map(function (n) { return caches.delete(n); })
         );
       })
     );
   });

   self.addEventListener("fetch", function (event) {
     event.respondWith(
       fetch(event.request)
         .then(function (response) {
           const copy = response.clone();
           caches.open(CACHE_NAME).then(function (cache) {
             cache.put(event.request, copy);
           });
           return response;
         })
         .catch(function () {
           return caches.match(event.request).then(function (cached) {
             return cached || caches.match("/static/offline.html");
           });
         })
     );
   });
   ```

   Before running it, read the `PRECACHE` list against the project on screen and account for all four entries: `/` is the Flask home route, `/static/style.css` and `/static/script.js` came over from Week 24, and `/static/offline.html` gets written in step 8. If any one of those four is missing or misspelled, `cache.addAll` rejects and the entire service worker fails to install, silently.

   Read the three event handlers out loud as three jobs. **Install** runs once when the service worker is new, and it fills the cache with the files the app needs to exist at all. **Activate** runs when a new version takes over, and it deletes the old caches, which is why the cache name has a version number in it. **Fetch** runs on every single request the page makes: try the network first, save a copy of whatever comes back, and if the network fails, serve the saved copy, or the offline page if there is no saved copy.
7. **Say why this app is network-first rather than cache-first.** It shows live weather. A cache-first app would be faster and would show yesterday's temperature confidently, which is worse than being slow. The caching strategy is a design decision that depends on what the data is, and that is the real lesson of the file.
8. **Create `static/offline.html`**, a plain page with a heading saying the app is offline and a line explaining that any weather shown may be old. Two sentences is enough.
9. **Register it** by adding this to the bottom of `static/script.js`, the same file that holds their Week 24 fact button:

   ```javascript
   if ("serviceWorker" in navigator) {
     window.addEventListener("load", function () {
       navigator.serviceWorker.register("/sw.js")
         .then(function (reg) { console.log("Service worker ready, scope:", reg.scope); })
         .catch(function (err) { console.log("Service worker failed:", err); });
     });
   }
   ```

   Point at the `if`: the check exists because not every browser has one, and an app should degrade rather than break. Point at the `.catch`: without it, a failed registration is completely silent, which is the worst possible failure mode for a beginner.
10. **Test it in four moves,** all in Chrome's DevTools Application panel. This is the part students should be able to repeat unaided:
    - **Manifest.** Open Application, then Manifest. The name, icons, and colors should be listed with no errors.
    - **Service Workers.** It should say activated and running. If it does not, the console has the reason.
    - **Cache Storage.** Expand it and see the actual files sitting in `weather-v1`. This is the moment it becomes real for most students.
    - **Offline.** Tick the Offline checkbox in the Service Workers section and reload. The page still loads. Turn off the laptop's Wi-Fi entirely and reload again. Still loads.
11. **Now ask the uncomfortable question.** The page loaded offline, but what temperature is it showing? An old one, from whenever it was last cached, presented as if it were current. Ask what an honest app would do. The answer is to show the time of the reading and to say plainly that it is stale. Have them add that line to their offline page. This is a two-minute exercise that teaches more about engineering integrity than an hour of lecture.
12. **Commit:**

    ```bash
    git add .
    git commit -m "Convert the weather app to a PWA"
    ```

### Segment 6: Install it, and the HTTPS rule (1:35 to 1:42)

1. **Install on the laptop.** In Chrome at `http://127.0.0.1:5000` there is an install control in the address bar or in the browser menu. Install it. It opens in its own window with no address bar, and it appears in the applications list like anything else. It is their Python program, in a window, with an icon.
2. **State the HTTPS rule and why it exists.** Service workers require HTTPS, with `localhost` as the single deliberate exception so that development is possible. The reason is that a service worker can intercept and rewrite every request a site makes, so anyone able to inject one over an unencrypted connection could rewrite the entire site for that user permanently. Connect it straight back to Unit 4's TLS lesson.
3. **Say what that means for phones, plainly.** Reaching the laptop from a phone over the classroom network uses a plain IP address, which is not a secure context, so the service worker will refuse to register and the install option will not appear. This is not a bug in their code. Getting it onto a phone properly means deploying it to a real host with a certificate, which is the cloud extra-credit track in the curriculum.
4. **Optional instructor demonstration, if prepared:** use Chrome's remote-debugging port forwarding from `chrome://inspect` on the demo machine to make the phone treat the address as `localhost`, then install it on the phone in front of the class. Impressive and worth the two minutes if it is already set up. Do not troubleshoot it live.

### Segment 7: Unit 5 checkpoint (1:42 to 1:57)

- **Students do:** Complete the checkpoint individually, no laptops, about fifteen minutes.
- **You do:** Collect it. Hand out homework as students finish, noting the Extra Credit AP Track section and saying out loud that AP-track students should read it this week rather than next, because the Create Task window opens in Unit 6.

### Segment 8: Wrap (1:57 to 2:00)

- **You do:** Close the unit deliberately. Five weeks ago they had a Python file in Thonny. They now have a versioned project, served by a web server they wrote, pulling live data from another company's computer, styled, and installable as an app. Every layer of that was built by them, and nothing in it is magic.
- **You do:** Tell them what changes next week. Unit 6 opens with AI, and it is the week AI tools stop being off-limits, with a lesson attached about using them without letting them do the thinking.

## 7. Key scripts and analogies

- **Why five versions exist:** "It is not one program written five times because someone was being thorough. It is five products with a shared idea, and every one of them is a bet about which users matter most."
- **Native versus cross-platform:** "Native is a bespoke suit for each platform. Cross-platform is one good suit that fits both occasions nearly as well, for a fraction of the price. Neither answer is wrong; the question is what the occasion is."
- **PWA:** "A web page that asked to be treated as an app and was believed. The whole trick is a manifest saying what it is and a service worker so it works with the network off."
- **Choosing a technology:** "Nobody picks the best technology. They pick the one that fits the team they have, the money they have, the hardware access they need, and how fast they need to ship. That is engineering."
- **The store as a gatekeeper:** "Two companies decide what software three billion phones are allowed to run. Whatever you think of that, it is a fact you have to build around."
- **Permissions:** "The app asks. The operating system decides who to ask, and it asks you. That is the whole design, and it exists because apps could not be trusted to ask honestly."
- **Sandboxing:** "Every app lives in its own walled garden and cannot see over the wall. Everything outside the wall needs permission, one item at a time."
- **Push notifications:** "Your app's server does not phone your phone. It phones Apple or Google, who already have your phone on the line, and they pass the message along. One line for everyone, because a thousand open connections would flatten the battery by lunchtime."
- **A service worker:** "A little program that sits between your page and the internet and answers the door. Sometimes it goes out to the network, sometimes it hands over something it already had in the cupboard."
- **Cache-first versus network-first:** "Ask what your data is. A menu can be a day old. A temperature cannot. The caching strategy is a decision about honesty, not about speed."
- **Sync conflicts:** "Two copies of the same thing changed while nobody was looking. You have seen this. It is a merge conflict, and most apps resolve it by quietly letting the last one win."

## 8. Differentiation

- **Younger or newer students:** The systems half needs no adjustment; the scenario vote is the right level for everyone. For the lab, give them the complete `manifest.json`, `sw.js`, and `offline.html` files and have them do only the wiring: copy the files in, add the `<link>` to the head, add the Flask route, paste the registration block, then get it working and inspect it in the Application panel. Reading and installing working code is a real outcome and the inspection steps are where the understanding lives. Pair them.
- **Extensions for advanced or AP-track students:** Change the fetch handler to cache-first and observe what breaks about the weather display, then explain why. Add a version bump to `CACHE_NAME` and watch the activate handler clear the old cache in Cache Storage. Show the app's own last-updated time on the page so a stale cached copy is honest about itself. Investigate what the Notification and Geolocation APIs would require and write four sentences on why a browser makes both of them ask permission. The strongest can look at what deploying this to a real host with HTTPS would involve, which is the cloud extra-credit track in Section 9 of the curriculum.

## 9. Common pitfalls

- **The service worker is served from `/static/` and controls nothing.** The scope trap. The Flask route in step 5 exists for this. If a student skipped it, the registration succeeds and the caching silently never applies to the page.
- **`cache.addAll` fails if any one URL in the list 404s,** and it fails the entire install with an unhelpful message. The usual culprits are a missing `static/script.js`, which should have come across from Week 24 during Week 25's Segment 3, and an `offline.html` saved under a different name. Check the file list against the `PRECACHE` array first when debugging, and check it for the whole room before starting rather than one student at a time.
- **A stale service worker.** The old one stays in control until every tab is closed, so students change the file and see no effect. Teach the fix once and put it on the board: in the Application panel, tick Update on reload while developing, and use Unregister to start clean.
- **Testing over `http://192.168.x.x`.** No secure context, no service worker, no install prompt, and no obvious error. Anticipate it; a student will try it with their phone.
- **Opening the file directly instead of through Flask.** A `file://` address is not a secure context either, and this is why Week 24 insisted on serving the page.
- **No icons, or wrong sizes.** The manifest reports an error and the install option does not appear. Hand out the placeholder icons rather than letting anyone make their own in class.
- **Silent registration failure.** Without the `.catch`, nothing appears anywhere. It is in the code for that reason; make sure nobody deleted it.
- **Believing offline data is current.** The engineering-honesty point in step 11. Do not skip it; it is the best thing in the lab.
- **Treating PWA capability claims as permanent.** What a PWA can do on each platform genuinely shifts year to year. Teach students to check rather than to remember, and check yourself before stating anything specific.
- **The systems tour overrunning.** The mobile discussion is enjoyable and will eat the lab if allowed. Start the lab at 1:00 regardless.
- **Checkpoint time.** Start it at 1:42 even if half the room is still debugging. The lab can be finished at home; the checkpoint cannot.

## 10. Homework

Full details in `handouts/week-26-homework.md`. In summary: finish the PWA so it installs and loads offline, with an honest staleness message and a short written defence of the network-first caching choice; a written comparison choosing an approach for three described products with reasons; a permissions audit on their own phone or a family device. The handout closes with an Extra Credit AP Track section, which this week is mostly Create Task planning, since Unit 6 and the February window open next week.

## 11. Assessment

**Unit 5 checkpoint**, administered in Segment 7 and covering six areas:

1. **Process.** Name two phases of the software development life cycle and what each produces. Define technical debt in one sentence, with an example. One short judgment item: given a described project, argue for building it all at once or in short iterations.
2. **Version control.** What does a commit contain, and why is "the lines I changed" not quite right? What is a branch, in one sentence? Given a short block of text containing conflict markers, say which side came from `main` and which from the incoming branch, and describe what to do next. One item naming what `git add` does that `git commit` does not.
3. **The web.** Given the three filenames of a web page, say which is responsible for structure, presentation, and behavior. Explain what the DOM is, and why editing text in the browser's Elements panel does not survive a reload. One short find-the-bug item on an HTML snippet with a crossed or unclosed tag.
4. **APIs and JSON.** Given a small JSON document, write which Python type each part becomes. Given a response, write the expression that reads one nested value. What do status codes 200 and 404 mean? One item asking why a program that depends on an API must decide in advance what to do when the API is unreachable.
5. **Data.** Given a small table of ten rows, one filter question, one count question, one metadata question about units or time window, and one question asking what this data cannot tell you. That last item is the AP 2.3 check and it is the most important item on the paper.
6. **Mobile.** Given two described products, choose native, cross-platform, or PWA and justify each in one sentence. Name two things a PWA gives up compared with a native app. One item on why the operating system, not the app, controls permissions.

Score it against the unit-checkpoint component of the grade. It is diagnostic as much as evaluative. A weak result on area 5 matters most, since 2.3 and 2.4 are not covered again in the course; follow up individually with those students before the Create Task window. A weak result on area 2 predicts trouble in the final project, where every student's work lives in a repository.

Also assess the PWA lab against the weekly-labs rubric, with one addition: the student should be able to point at the fetch handler and say, in their own words, what happens to a request when the network is down.

## 12. AP alignment

Be straight with students. **Mobile development is not AP CSP content.** Native versus cross-platform, app stores, push notifications, and service workers are not on the exam. Nothing in today's coding half is tested.

The week is still worth AP-track students' attention for two reasons, and both are honest rather than stretched.

**First, it previews Big Idea 5, Impact of Computing, which is 21 to 26 percent of the exam,** more than any other big idea except algorithms. Three things discussed today are squarely in it, and Week 30 covers them properly:

- Permissions, sandboxing, and what apps can see about their users are 5.6 Safe Computing and part of 5.5 Legal and Ethical Concerns.
- The app stores as gatekeepers deciding what software may exist is 5.1 Beneficial and Harmful Effects and 5.5.
- The fact that a PWA runs on a cheap phone with a browser while a large native app may not is 5.2 Digital Divide, and it is one of the clearest concrete examples of that topic available anywhere in the course.

Note the framing for the exam: it rewards answers that name both a benefit and a harm of the same innovation, and today's material is full of those pairs.

**Second, the Create Task window opens next week.** February, in Unit 6, with nine protected hours of class time and a submission deadline in late April. Verify the current year's deadline on AP Central rather than trusting any date printed here. Students who started an idea list in Week 25 should narrow it to one this week, so that the first protected hour is spent building rather than deciding. The handout carries the specifics of what the task requires.

**AP-track self-study for this week, and only this week's slice.** There is no direct content match, so the honest options are these:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, is the nearest fit, and it is a loose one. It covers how computing innovations work and their effects, which is the frame today's mobile tour used. Work only the lessons on innovations and their impacts. If the Create Task idea is not yet chosen, that is a better use of the hour than this unit. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** two options and neither is a content match for the lab. Unit 8, Cybersecurity and Global Impacts, at `https://studio.code.org/courses/csp-2025/units/8`, covers the Big Idea 5 material previewed above and is the better choice if the student wants exam content. Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`, is the better choice if the student is ready to plan the project, and this is the week it stops being orientation and becomes real preparation.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The PWA conversion: complete inline in Segment 5, including the manifest, the service worker, the Flask route that fixes the scope problem, the registration snippet, and the DevTools test sequence. Nothing external needs to be open during class.
- **Prep note:** do the full conversion and install on the demo machine before teaching it, then unregister the service worker and clear the cache and do it a second time. The un-sticking flow is the one you will need live, and reading about it is not the same as having done it.
- **Prep note:** verify the current state of PWA support before class, particularly anything you plan to say about what works on iOS. This changes year to year more than almost anything else in the course.
- MDN Progressive Web Apps guide, for your own reference: `https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps`. The service worker and Cache API pages under the same domain are the authoritative references. Verify against current browser behavior; this area moves.
- Chrome DevTools Application panel, used for all testing: built in, nothing to install. Panel names change between releases; verify against the fleet's version.
- Placeholder icons: prepare two square PNGs at 192 and 512 pixels during prep and distribute them. Do not spend class time on icon creation.
- Native and cross-platform toolkits, named in Segment 2 for accuracy and not used in class: Android with Kotlin at `https://developer.android.com`, iOS with Swift at `https://developer.apple.com/swift`, Flutter at `https://flutter.dev`, React Native at `https://reactnative.dev`, .NET MAUI at `https://dotnet.microsoft.com/apps/maui`. Verify names and current status before quoting any of them as fact; this list changes.
- CodeAI CSP Units 8 and 9 (AP-track Big Idea 5 preview and Create Task preparation): `https://studio.code.org/courses/csp-2025/units/8` and `https://studio.code.org/courses/csp-2025/units/9`
- AP Create Performance Task requirements and the current year's deadline: AP Central, `https://apcentral.collegeboard.org/courses/ap-computer-science-principles`. Deadlines and requirements change annually; verify before relying on anything here.
- Mobile and cloud extra-credit project tracks, for students who want to go further: Section 9 of `curriculum/CS-Curriculum-and-Setup.md`.
- Unit 5 outline and the checkpoint's place in the grade: Sections 3 and 5 of `curriculum/CS-Curriculum-and-Setup.md`.
