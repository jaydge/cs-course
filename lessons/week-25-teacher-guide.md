# Week 25 Teacher Guide

## 1. Header

- **Week:** 25 of 32
- **Unit:** 5, Building Modern Software
- **Theme question:** How do programs talk to other programs?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Explain what an API is in one sentence, and give the difference between a page meant for a person and an endpoint meant for a program.
- Read a JSON document, name its four building blocks, and map each one onto the Python type it becomes.
- Call a public API with the `requests` library and pull a specific value out of the response.
- Build and run a small Flask application that serves a page filled with live data.
- Load a CSV file in Python, report how many rows and columns it has, and name its columns and units.
- Filter a dataset, count within it, and find one pattern that was not visible in the raw file.
- Display a summary as a simple text chart.
- Say what a dataset does not contain, and why that matters as much as what it does.

## 3. Where this sits

This is the payoff week of Unit 5 and the strongest AP week in it. Everything the course has built converges: Unit 4's HTTP request and response, Week 22's project structure and virtual environment, Week 23's repository, Week 24's HTML page, and Unit 3's dictionaries and loops. Almost nothing today is a new idea. It is old ideas plugged into each other, and it is worth saying that out loud around the halfway mark.

Two AP topics are covered properly here and nowhere else in the course: 2.3 Extracting Information from Data and 2.4 Using Programs with Data. The coverage map lists the Week 25 data lab as the sole source for 2.3. That is why the data lab gets a protected thirty-five minutes and must not be cut for more Flask time. If the session is running behind, shorten the Flask styling, never the data lab.

Week 26 converts today's Flask app into an installable Progressive Web App, so what students build today needs to still run next week. Tell them.

This is also the week AP-track students should start letting a Create Task idea form. The Create Task window opens in February, in Unit 6, and needs nine protected hours. The Extra Credit AP Track section of the handout carries the orientation; mention it out loud rather than leaving it in print.

## 4. Materials and setup

- Each student's laptop with VS Code, Python, and Git, plus a working internet connection. Test the connection to the API from a student machine before class, not from yours.
- The prepared offline fallback files on a USB drive or in the class-server repository: one saved API response as JSON and one saved CSV dataset. If the network fails or the API is down, the entire session still runs from these.
- Projector at a large font, with VS Code, a terminal, and a browser visible.
- Whiteboard with the theme question, and a clear area for the JSON-to-Python mapping table.
- Printed one-page reference: the JSON building blocks, the `requests` pattern, the Flask skeleton, and the `csv.DictReader` pattern. One per student.
- Printed Week 25 homework handout, one per student.

## 5. Pre-class prep checklist

- **Run the API call yourself and save the response.** In a browser, open the endpoint in Segment 2 and confirm it returns JSON. Then save one response to `data/sample_weather.json` for the offline fallback. Public API terms, parameters, response field names, and rate limits change without notice; verify the endpoint works and re-read the current terms of use before relying on any of this in class. (20 min)
- **Download the CSV dataset** and save a copy for the fallback. The USGS earthquake feed described in Section 13 is the one the lab is written around. Open it and confirm the column names still match what Segment 5 expects; feed formats do change. (15 min)
- **Install the libraries on one machine and time it.** Inside an activated virtual environment: `pip install flask requests`. If the classroom network is slow or filtered, pre-download the wheels or pre-install on the fleet during prep. Twelve students running `pip install` simultaneously on a school connection is a real risk. (20 min)
- Build and run the complete Flask app yourself, including the template, and leave it open in a second window during class. (25 min)
- Write and run the whole data lab yourself against the real file, and note the actual numbers you get so you can tell whether a student's answer is plausible. (20 min)
- Print the reference sheet and homework handouts. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and framing (0:00 to 0:10)

- **You do:** Pose the theme question. Then a concrete version: a weather app on a phone did not measure the weather. Where did the number come from, and how did it get in there?
- **You do:** Homework check by show of hands on the personal page, and confirm everyone can still serve it. Anyone whose page is broken pairs up now; today's work builds on it.
- **You do:** Set the shape of the day: thirty-five minutes building a web app that fetches live data, then thirty-five minutes pulling answers out of a real dataset. Say that both halves are the same skill wearing different clothes: a program using data it did not create.

### Segment 2: APIs and JSON (0:10 to 0:30), Systems strand

1. **Define it in one sentence and write it up.** An API is a documented way for one program to ask another program for something. Not a page for a human to read, a door for software to knock on.
2. **Make the distinction visible.** Open a normal weather website. It is HTML, styled for eyes, full of navigation and advertisements. Now open the API endpoint in the same browser:

   ```
   https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current=temperature_2m,wind_speed_10m&temperature_unit=fahrenheit
   ```

   Same information, no decoration, machine-readable. Say the difference plainly: one is for people, one is for programs, and this is why scraping a web page is a fragile last resort while calling an API is not.
3. **Read the URL out loud as its parts,** connecting straight back to Unit 4: the scheme, the host, the path, and then the query string after the question mark, which is a list of `name=value` pairs joined by ampersands. Those pairs are the arguments to the request. Change the latitude and longitude live and reload to prove it.
4. **Note the absence of a key, and say why we chose it that way.** This API needs no account and no key. That is deliberate: API keys belong to a person, usually require a payment method, and generally have terms that do not suit minors. Where the course does use a paid or keyed service later, the key is instructor-owned. Note also that free APIs have rate limits and terms of use, and that hammering one from twelve laptops is both rude and a good way to get the classroom address blocked.
5. **Teach JSON with the response on screen.** Four building blocks and nothing else: objects in curly braces holding `"key": value` pairs, arrays in square brackets holding an ordered list, and the primitives, which are strings in double quotes, numbers, `true`, `false`, and `null`.
6. **Put the mapping table on the board and leave it up:**

   | JSON | Python |
   |---|---|
   | object `{ }` | dictionary |
   | array `[ ]` | list |
   | string | `str` |
   | number | `int` or `float` |
   | `true` and `false` | `True` and `False` |
   | `null` | `None` |

   Say the useful consequence: once JSON is parsed, it is dictionaries and lists, and they have been working with those since Week 11. There is nothing new to learn about using the data, only about getting it.
7. **Point out the two double-quote rules students break:** JSON keys are always in double quotes, and JSON has no trailing comma after the last item. Both produce parse errors that read badly.
8. **Call it from Python, live, in the shell.** Activate the environment first, then:

   ```bash
   pip install requests
   python3
   ```

   ```python
   import requests
   url = "https://api.open-meteo.com/v1/forecast"
   params = {"latitude": 40.71, "longitude": -74.01,
             "current": "temperature_2m", "temperature_unit": "fahrenheit"}
   response = requests.get(url, params=params, timeout=10)
   print(response.status_code)
   data = response.json()
   print(data["current"]["temperature_2m"])
   ```

   Four things to name as you go. `requests.get` sends the same HTTP GET the browser sends, which they watched in Wireshark in Week 20. `status_code` of 200 means success, and 404 and 500 mean the two failure kinds they already know. `.json()` parses the text into Python objects. And `data["current"]["temperature_2m"]` is a dictionary inside a dictionary, exactly like the rooms map from Week 16.
9. **Say the AP name for the library idea in one line.** `requests` is a library: code somebody else wrote, imported and reused. That is AP topic 3.14, and they first met it in Week 4 with `import random`.

### Segment 3: The Flask app (0:30 to 1:05), Coding strand part 1

1. **Frame the shape before the code.** So far the browser has asked a server for files, and Python has asked an API for data. Flask makes their Python program be the server. Draw three boxes: the browser, their Flask program, and the weather API. The arrows go browser to Flask, Flask to API, and back again. Their program is in the middle, which is exactly what a backend is.
2. **Create the project with the Week 22 layout:**

   ```bash
   cd ~/cs-sandbox
   mkdir weather
   cd weather
   git init
   python3 -m venv .venv
   source .venv/bin/activate
   pip install flask requests
   mkdir templates static
   code .
   ```

   Add the same four-line `.gitignore` from Week 22 before the first commit. Say why the `.venv` matters here more than it did then: it now contains hundreds of installed library files.
3. **Write `app.py` at the projector, in three stages, running after each.** Stage one, the smallest thing that works:

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route("/")
   def home():
       return "Hello from my own server."

   if __name__ == "__main__":
       app.run(debug=True, port=5000)
   ```

   Run it with `python3 app.py` and open `http://127.0.0.1:5000`. Stop and let that land: they wrote a web server. Name the two new pieces. The `@app.route("/")` line is a decorator, and the only thing they need to know today is that it maps a URL path to the function underneath it. `debug=True` reloads the code on every save and shows real errors in the browser, and it must never be used for anything public.
4. **Stage two, add the API call:**

   ```python
   from flask import Flask, render_template
   import requests

   app = Flask(__name__)

   URL = "https://api.open-meteo.com/v1/forecast"
   PARAMS = {
       "latitude": 40.71,
       "longitude": -74.01,
       "current": "temperature_2m,wind_speed_10m",
       "temperature_unit": "fahrenheit",
   }

   @app.route("/")
   def home():
       response = requests.get(URL, params=PARAMS, timeout=10)
       data = response.json()
       now = data["current"]
       units = data["current_units"]
       return render_template(
           "index.html",
           temperature=now["temperature_2m"],
           temp_unit=units["temperature_2m"],
           wind=now["wind_speed_10m"],
           observed=now["time"],
       )

   if __name__ == "__main__":
       app.run(debug=True, port=5000)
   ```

   Have students set the latitude and longitude to their own town, which they can find from any maps application. Note the `timeout=10`: without it, a slow API hangs the whole server, and that is a real lesson about depending on somebody else's computer.
5. **Stage three, the template.** Copy last week's `index.html` into `templates/` and `style.css` into `static/`, then change two things. The stylesheet link becomes:

   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
   ```

   And add a weather section using the placeholders:

   ```html
   <section>
     <h2>Right now</h2>
     <p>{{ temperature }} {{ temp_unit }}, wind {{ wind }}.</p>
     <p><small>Observed at {{ observed }} UTC.</small></p>
   </section>
   ```

   Explain the double braces in one line: Flask fills them in before sending the page, so by the time the browser sees it, it is ordinary HTML with numbers in it. Prove it with View Page Source in the browser: the braces are gone. That single demonstration is what separates server-side rendering from client-side JavaScript in students' heads, and it costs thirty seconds.
6. **Break it on purpose, twice, and fix it.** First, unplug the network or change the host name to something invalid and reload. The page dies with a connection error. Second, misspell a key in the dictionary lookup and reload to get a `KeyError`. Then add the handling:

   ```python
   @app.route("/")
   def home():
       try:
           response = requests.get(URL, params=PARAMS, timeout=10)
           response.raise_for_status()
           data = response.json()
       except requests.RequestException:
           return render_template("index.html", temperature="unavailable",
                                  temp_unit="", wind="unknown", observed="never")
   ```

   Say the principle: any time your program depends on another computer, that computer will be down at some point, and deciding what your program does then is part of writing it, not an extra.
7. **Students do:** Get it running with their own location, then commit:

   ```bash
   pip freeze > requirements.txt
   git add .
   git commit -m "Serve live weather from a Flask app"
   ```

   Point at `requirements.txt` and say what it is now good for: another person can rebuild the exact environment from it, which is why the `.venv` folder itself never needs to be committed.

### Segment 4: Stretch (1:05 to 1:10)

### Segment 5: The data lab (1:10 to 1:45), Coding strand part 2

Protect this segment. It carries AP topics 2.3 and 2.4 for the whole course. Students work in the same `weather` project, in a separate file, with the CSV in a `data/` folder.

1. **Set the question first, before any code.** Put a real question on the board that the dataset might answer, for example: how many earthquakes happened in the last day, where were they, and is there any pattern to when they happen? Say that data work always starts with a question, because a dataset with no question attached is just a big file.
2. **Look at the raw file first, in the editor.** Open the CSV in VS Code. It is text, with a header row and one record per line, fields separated by commas. Say why CSV survives despite being primitive: everything can read it.
3. **Read the metadata before reading the data.** This is AP topic 2.3 and it is the step everyone skips. Ask and answer six questions on the board:
   - **Who published it and when?** A government scientific agency, updated continuously.
   - **What is one row?** One detected earthquake, not one place and not one day.
   - **What time window?** The last twenty-four hours, which means this file is different tomorrow, which means a result without a date attached is meaningless.
   - **What are the units?** Depth in kilometers, magnitude on a logarithmic scale, times in UTC. Stress the time zone; a student who reads the hour column as local time will find a pattern that is not there.
   - **How was it collected?** By seismometers, which exist in some places and not others.
   - **What is not in it?** No damage, no injuries, no population, no cost. Ask what questions this file therefore cannot answer, and get them to say "how bad was it" out loud.
4. **Load it and describe it in code.** New file `explore.py`:

   ```python
   import csv

   with open("data/quakes.csv", newline="", encoding="utf-8") as f:
       reader = csv.DictReader(f)
       rows = list(reader)
       columns = reader.fieldnames

   print("Rows:", len(rows))
   print("Columns:", len(columns))
   print(columns)
   print(rows[0])
   ```

   Explain `DictReader` in one line: it uses the header row to give every record as a dictionary keyed by column name, so `row["mag"]` works. Note that everything comes back as a string, always, which is the Week 2 `input` trap in a new costume.
5. **Filter, and hit the real-data problem on purpose:**

   ```python
   big = []
   for row in rows:
       if row["mag"] and float(row["mag"]) >= 2.5:
           big.append(row)

   print("Magnitude 2.5 or greater:", len(big))
   ```

   Some rows have an empty magnitude. Remove the `if row["mag"] and` guard and let it crash with a `ValueError`, then put it back. Name the lesson: real data has holes, and every real analysis contains a decision about what to do with them. Ask what dropping those rows does to the answer.
6. **Count into a dictionary,** which is the Week 11 and Week 16 pattern doing real work:

   ```python
   counts = {}
   for row in rows:
       region = row["place"].split(", ")[-1]
       counts[region] = counts.get(region, 0) + 1

   top = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
   for region, n in top[:10]:
       print(n, region)
   ```

   If `lambda` is unfamiliar to the group, give it as a one-line recipe rather than teaching it: it says sort by the second thing in each pair.
7. **Find a pattern that was invisible in the file:**

   ```python
   by_hour = {}
   for row in rows:
       hour = int(row["time"][11:13])
       by_hour[hour] = by_hour.get(hour, 0) + 1

   for hour in range(24):
       n = by_hour.get(hour, 0)
       print(f"{hour:02d} " + "*" * n)
   ```

   The text bar chart is the same asterisk histogram from the Week 16 dice simulation, deliberately. Ask what shape they expected and what they got.
8. **Now do the hard part, which is the actual AP skill: interpret it honestly.** Earthquakes should be roughly uniform across the hours of a day. If the chart is not flat, the candidate explanations are worth arguing about: too few rows for the noise to average out, detection differing by time of day, or the window not being a clean twenty-four hours. Push students to say which explanations the data itself can settle and which it cannot. Then land the general rule: a pattern in a chart is a question, not an answer.
9. **Name the collection bias explicitly,** because it is the most exam-relevant idea in the segment. Regions with dense sensor networks record many more small events than regions with few sensors. So a count by region measures where the sensors are at least as much as where the earthquakes are. Ask for one other dataset where the same trap would apply. Reported crime and app-store ratings both work well.
10. **Students do:** Answer three questions of their own from the file and print the results. One filter, one count, one chart. Then commit.

### Segment 6: Share out and the AP framing (1:45 to 1:55)

- **Students do:** Three or four students say, in one sentence each, one thing they found and one thing the dataset cannot tell them. Insist on the second half of the sentence.
- **You do:** Name what they just did in the exam's own words, and write the four steps on the board, because this is exactly what 2.3 tests: get the data, clean or filter it, transform or aggregate it, and then interpret the result, including its limits. Add the fifth thing the exam cares about, which is that a program made the analysis possible at a scale no person could do by hand. That is topic 2.4.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Hand out homework and walk through it, including the Extra Credit AP Track section, and say out loud that this week's AP slice is the strongest of the unit and that the section also carries the first real Create Task orientation.
- **You do:** Tell them to keep the `weather` project working, because next week turns it into something installable.
- **Exit question at the door:** name one thing your dataset cannot tell you.

## 7. Key scripts and analogies

- **What an API is:** "A restaurant has a dining room for people and a service window for the kitchen next door. A web page is the dining room. An API is the service window, and it is much easier to order through when you are also a machine."
- **Why not scrape the page:** "You can read the number off a web page with code, and it will work until they move a button. The API is a promise; the page is a coincidence."
- **JSON:** "Curly braces are dictionaries, square brackets are lists, and everything else is a string or a number. You already know how to use all of it. The only new part is where it came from."
- **Flask:** "Until now your program asked servers for things. Now your program is the thing being asked."
- **The route decorator:** "That line above the function is a label saying: when someone visits this address, run this function and send back whatever it returns."
- **Templates:** "The template is a form letter with blanks. Flask fills the blanks and mails it. By the time the browser sees it, there were never any blanks."
- **Depending on other computers:** "The moment your program needs somebody else's server, you have inherited their outages. Deciding what your page says when they are down is part of building it."
- **Metadata:** "Read the label before you eat it. What is one row, what are the units, what time zone, who collected it, and what did they not collect?"
- **Missing data:** "Real data has holes. What you do about the holes is a decision you make, and it changes your answer, so say out loud which decision you made."
- **Collection bias:** "A map of recorded earthquakes is partly a map of earthquakes and partly a map of seismometers. Every dataset is partly a map of who was counting."
- **Patterns:** "A bump in a chart is a question, not an answer."

## 8. Differentiation

- **Younger or newer students:** The readiness guide recommends treating APIs as a demonstration for these students, and that is the right call if time is tight. Give them a complete, working `app.py` and have them change only the latitude, longitude, and the template text, then confirm it runs. That is a real outcome and it teaches reading code. For the data lab, give them the loading code complete and have them do only the count-into-a-dictionary step and the asterisk chart, which is the same pattern they already ran in Week 16. The metadata discussion in step 3 is verbal and everyone should be in it; it needs no code and it is the part the exam actually tests.
- **Extensions for advanced or AP-track students:** Add a second Flask route, `/about`, with its own template. Add a form so the user can type a city's coordinates and see the weather for it, using `request.args`. Cache the API response for ten minutes so a page reload does not hit the API every time, and explain why that is polite. In the data lab, compute the mean and median magnitude and explain which is more honest for this data and why. Cross-reference two columns, such as depth against magnitude, and say whether anything looks related and how they would tell the difference between a real relationship and a coincidence. The strongest can install `matplotlib` in the virtual environment and produce a real chart, then say what the asterisk version did just as well.

## 9. Common pitfalls

- **`pip install` outside the activated environment.** The libraries land in the system Python, Flask is "not installed," and nobody can see why. Check for the prompt prefix. This is the most common failure of the day.
- **Twelve simultaneous installs on a slow network.** Pre-install during prep if there is any doubt.
- **The API is down, blocked, or has changed its response shape.** This is why the prep checklist saves a sample response. Have the offline path ready and treat an outage as a live demonstration of why the error handling in step 6 exists.
- **A `KeyError` on the response.** Almost always a changed or misspelled field name. Teach the diagnosis: `print(data)` and look at what actually came back, rather than guessing.
- **Port 5000 already in use.** Something else on macOS may hold it. Change to `port=5001` and move on; do not spend class time on it.
- **Editing `index.html` in the old `personal-page` folder** instead of the new `templates/` folder, then wondering why nothing changes. Check which file is open.
- **Everything from a CSV is a string.** `row["mag"] > 3` compares strings and gives nonsense without raising an error, which is worse than crashing. Show it once.
- **Empty fields in real data.** Deliberately crashed in step 5 so it is a lesson rather than a mystery.
- **Time zones.** The timestamps are UTC. A student who treats them as local time will confidently report a false pattern. Say it twice.
- **Committing the dataset.** A small CSV is fine. Say the general rule anyway: large data files do not belong in a repository, which is why the file lives in a `data/` folder that can be added to `.gitignore` when it grows.
- **Letting Flask eat the data lab.** Watch the clock. At 1:10 the data lab starts, finished Flask app or not.

## 10. Homework

Full details in `handouts/week-25-homework.md`. In summary: get the Flask app running and committed, with the error-handling path working when the API is unreachable; answer four questions from the dataset in code and write up the answers; a written metadata description of the dataset including what it cannot tell them; one paragraph on collection bias. The handout closes with an Extra Credit AP Track section carrying this week's AP slice, which is the strongest of the unit, and the first real Create Task orientation.

## 11. Assessment

Observational and completion-based, against the weekly-labs rubric, plus the written data write-up, which is the closest thing this unit has to an AP free-response answer and should be read carefully.

Four things to check by watching:

1. The Flask app runs and shows a number that came from the internet.
2. The student can point at the line that makes the request, the line that parses it, and the line that puts the value into the page.
3. The data lab prints a count that is plausible against the numbers you got in prep.
4. The student can say what one row of the dataset represents.

The verbal check that matters most, and the one that is actually AP 2.3: ask what the dataset cannot tell them. A student who can only describe what is in the file has done the mechanical half. Note anyone in that position, because 2.3 and 2.4 are not covered again.

## 12. AP alignment

This is the strongest AP session in Unit 5 and one of the strongest in the course. It directly covers:

- **2.3 Extracting Information from Data.** The whole data lab. The exam expects students to know that data must often be cleaned or filtered before use, that a program lets you find patterns at a scale a person cannot, that metadata is data about the data, and that a correlation found in a dataset is not a cause. All four came up today.
- **2.4 Using Programs with Data.** Both halves of the session. The exam frames this as using a program to process information to gain insight, and specifically mentions filtering and cleaning.
- **3.14 Libraries.** `requests`, `flask`, and `csv` are three libraries used for real, which is a much stronger instance of the topic than Week 4's `import random`.

Two exam details worth saying out loud, since they cost nothing today and are easy points in May. Metadata is data about data, and changing metadata does not change the underlying data. And a larger dataset is not automatically a better one; if the collection was biased, more of it is more bias.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 5, Big Data. This is the cleanest single-unit match in the whole course. Work the lessons on extracting information from data, on metadata, and on the limits of data, then stop; the material on large-scale systems goes beyond what we need this week. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 5, Data, at `https://studio.code.org/courses/csp-2025/units/5`. Note for planning: Data moved to Unit 5 in the `csp-2025` edition from Unit 9 in older editions, so older guides and forum posts will point at the wrong number. This unit is the direct match for today: cleaning, filtering, visualizing, and drawing conclusions responsibly.

**Create Task orientation starts now, and it is orientation only.** The Create Performance Task window opens in Unit 6, in February, with nine protected hours of class time and a submission deadline in late April. Verify the current year's deadline on AP Central rather than trusting a date printed here. The reason to raise it today rather than in February is that a good project idea needs weeks to form, and today's session is the most common source of one: a program that fetches or loads data and does something useful with it fits the task requirements naturally. The handout carries the details.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The Flask app and the data lab: complete inline in Segments 3 and 5, including the template changes and the error handling. Nothing external needs to be open during class.
- **Prep note:** actually run the API call and download the CSV during prep, and save both to local files as the offline fallback. This is the one week where an external service can take the session down, and the fallback is what prevents that.
- **Weather API, no key required:** Open-Meteo, `https://open-meteo.com`. The forecast endpoint used in class is `https://api.open-meteo.com/v1/forecast` with `latitude`, `longitude`, and `current` parameters. Chosen because it needs no account, no key, and no payment method, which matters when the users are minors. Free-tier terms, rate limits, and response field names change; verify the current terms and the response shape before class each year. If it becomes unsuitable, any keyless JSON endpoint works with the same code, and if you switch to a keyed service the key stays instructor-owned per Section 12 of the curriculum.
- **Dataset for the data lab:** the USGS earthquake feeds, `https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php`. The lab is written around the past-day, all-magnitudes CSV. It is public domain, small, genuinely messy in useful ways, and it has real metadata worth reading. Verify the column names before class; feed formats change. Any small CSV with a date column, a numeric column, and a category column will support the same lab.
- Flask, for your own reference: `https://flask.palletsprojects.com`. The quickstart covers routes, templates, and static files. Note that `debug=True` and the built-in server are for development only.
- Requests, for your own reference: `https://requests.readthedocs.io`
- Python's `csv` module: `https://docs.python.org/3/library/csv.html`
- CodeAI CSP Unit 5, Data (AP-track reinforcement, the direct match this week): `https://studio.code.org/courses/csp-2025/units/5`
- AP Create Performance Task requirements and the current year's deadline: AP Central, `https://apcentral.collegeboard.org/courses/ap-computer-science-principles`. Deadlines and requirements change annually; verify before relying on anything here.
- Account and API-key policy, including why keys stay instructor-owned: Section 12 of `curriculum/CS-Curriculum-and-Setup.md`.
