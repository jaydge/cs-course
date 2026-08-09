# Week 25 Homework: Live Data, and What It Will Not Tell You

Today you wrote a program that is a web server, and you pulled answers out of a file of real measurements. This homework finishes both. Plan on about 50 minutes.

Keep the `weather` project working. Next week it becomes something you can install on a phone.

Start by activating your virtual environment. If your prompt does not show `.venv`, nothing you install lands where you think it did. The quotation marks are the Week 17 rule, because `CS Class` has a space in it.

```bash
cd ~/Documents/"CS Class"/weather
source .venv/bin/activate
```

## 1. Finish the Flask app

Your app is done when all of these are true:

- Running `python3 app.py` starts it, and `http://127.0.0.1:5000` shows your page.
- The temperature shown is for a place you chose, not the one from the demo.
- Your Week 24 styling is applied, through `static/style.css`.
- Your Week 24 fact button still works, which means `static/script.js` came across into this project too. Check it. Next week's lab will not run without that file.
- It shows the observation time, and the page says somewhere that the time is UTC.
- When the API cannot be reached, the page still loads and says so instead of crashing.

Test that last one properly. Turn off your Wi-Fi and reload the page. If you get a wall of error text, your `try` and `except` are not doing their job. If instead you get a page saying "Internal Server Error", your `home()` function reached the end without returning anything, which usually means the successful `return render_template(...)` ended up indented inside the `try` block. It belongs after it.

Then commit:

```bash
pip freeze > requirements.txt
git add .
git commit -m "Finish the weather app with offline handling"
```

## 2. Answer four questions from the dataset

Use the earthquake CSV in your `data/` folder. Write the code in `explore.py`. Print each answer with a label so the output explains itself.

1. How many rows are in the file, and how many columns?
2. How many events had a magnitude of 4.0 or greater? What percentage of the total is that?
3. Which five regions appear most often? Print them with their counts.
4. Make one text chart. Either the count by hour from class, or a count by rounded magnitude, which is more interesting than it sounds.

Two traps from class. Everything read out of a CSV is a string, so `float()` it before comparing, and some rows have an empty magnitude, so check for that before converting.

## 3. Describe the data before you trust it

Write this out. Five short answers, one or two sentences each.

1. Who published this data, and when was this copy of it made?
2. What does one row represent? Be precise. It is not one place and it is not one day.
3. What are the units for the `depth` column and the `mag` column?
4. What time zone are the timestamps in, and what would go wrong if you assumed otherwise?
5. Name three things that are **not** in the file, and one question people would obviously want answered that this data therefore cannot answer.

Question 5 is the important one. Most of the mistakes people make with data are answering a question the data was never able to answer.

## 4. One paragraph on bias

Regions with a lot of seismometers record far more small earthquakes than regions with almost none.

So when you counted events by region in section 2, what were you actually measuring? Write a paragraph, and name one other kind of data where the same trap applies. Reported crime, restaurant reviews, and potholes reported to a city are all worth thinking about.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly starting in Week 27. The official Flask and `csv` documentation is genuinely good, and bringing a written-down question to class is always allowed. Stuck is normal; it is where the learning is.

One more thing specific to this week: when your program talks to somebody else's server, that server will sometimes be slow, wrong, or down. That is not your bug. Handling it is your job.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**This is the strongest AP week of the whole unit.** Today covered three real exam topics properly:

- **2.3 Extracting Information from Data.** Cleaning and filtering, finding a pattern with a program that you could not find by hand, reading metadata, and knowing that a pattern is not a cause.
- **2.4 Using Programs with Data.** Using a program to process information and get insight out of it.
- **3.14 Libraries.** `requests`, `flask`, and `csv` are all libraries: code somebody else wrote that you imported and used.

Two exam facts that are easy points in May and cost you nothing to learn now:

- Metadata is data about data. Changing the metadata does not change the underlying data.
- A bigger dataset is not automatically a better one. If the way it was collected was biased, collecting more of it just gives you more bias.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 5, Big Data. This is the cleanest match between our course and Project STEM all year. Work the lessons on extracting information from data, on metadata, and on the limits of data, then stop. The large-scale systems material goes past what we need. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 5, Data, at `https://studio.code.org/courses/csp-2025/units/5`. One warning: Data used to be Unit 9 in older editions of this course, so older guides and forum posts will send you to the wrong place. Unit 5 is the right one in the current edition. It covers cleaning, filtering, visualizing, and drawing conclusions responsibly, which is exactly today.

**Create Task orientation. Start thinking, not building.**

The AP Create Performance Task is the project half of the AP CSP score. You design and build a program yourself, record a video of it running, and answer written questions about it. It starts in February, in Unit 6, and you get nine protected hours of class time for it. It is submitted in late April. Check the exact deadline for your year on AP Central; College Board moves it, and a handout is not a reliable source for a date.

Why this is in front of you now, in Week 25, rather than in February: a good idea takes weeks to arrive, and today is the single most likely source of one. A program that loads data, or fetches it from an API, and then does something useful with it fits the task requirements naturally. It needs a list or similar collection, a procedure you wrote yourself with a parameter, and some algorithm involving selection and iteration. Your data lab today has most of those bones already.

Three things to do about it this week, none of which involve writing project code:

1. Write down three ideas. One sentence each. Bad ideas are fine; the point is to start the list.
2. For each one, say what data it uses and where that data comes from.
3. Skim CodeAI Unit 9, Create PT Prep, at `https://studio.code.org/courses/csp-2025/units/9`, for twenty minutes, just to see what the finished thing looks like. Do not start it.

Keep the list. We will come back to it next week and again in February.

One rule that will not change: the Create Task must be your own work, and the College Board's rules about AI and about copied code apply to it even after AI tools unlock for the rest of the course in Week 27.

**Extra practice if you want it.**

- Write, in AP pseudocode, the loop that counts your earthquakes by region. Pseudocode has no dictionary, so you will have to solve it with lists, which is genuinely good practice at working inside the exam's limits. Use `ap-track/AP-Pseudocode-Bridge.md`.
- Find a second dataset that interests you, from a government or university source, and answer the same metadata questions about it before writing a single line of code.
- Read the Big Idea 2 section of `ap-track/AP-CSP-Topic-Coverage.md` and mark 2.1 through 2.4 as solid, shaky, or not yet. This week was the course's main coverage of 2.3 and 2.4, so be honest about it.
