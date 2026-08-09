# Week 20 Homework: Reading the Wire

This week you became a web server, read a real HTTP request byte by byte, and then found out you could not read the next one because it was encrypted. Plan on about 45 minutes.

**One thing that is deliberately not in this homework: Wireshark.** Packet capture stays in class, on the classroom network, with the rules we agreed on. Do not run captures at home, on anyone else's network, or on traffic that is not yours. Everything below works without it.

## 1. Be a server at home

Put two or three files (a text file and anything else) into the `sandbox/site` folder inside your CS Class folder, and serve it:

```bash
cd ~/Documents/"CS Class"/sandbox/site
python3 -m http.server 8080
```

Then:

1. Visit `http://localhost:8080` in a browser on the same machine. Write down what you see.
2. Find your machine's IP address on your home network (you did this last week). From a phone, tablet, or another computer on the same Wi-Fi, visit `http://<that address>:8080`. Write down whether it worked. If it does not work, do not spend more than five minutes on it: a firewall refusing an incoming connection is a real and correct answer.
3. Copy down two lines of the log printed by the terminal the server is running in.
4. Request a file that does not exist, for example `http://localhost:8080/nope.txt`. What does the browser show, and what does the server's log say?

Press Control-C in the terminal to stop the server when you are done.

## 2. Four short questions

1. Name one thing TCP guarantees that UDP does not. Then name one situation where you would deliberately choose UDP anyway, and say why.
2. What are the three messages of the TCP handshake, in order, and what does the exchange accomplish?
3. An IP address gets a message to the right machine. What does a port number add, and why is the address alone not enough?
4. What do these status codes mean: 200, 404, 500?

## 3. Fetch with Python

Start your server again. Then write a program `fetch.py` that:

1. Requests three different paths from your own server: one file that exists, one file that exists with a different name, and one that does not exist.
2. Prints the path and the status code for each, one per line.
3. For the one that exists, also prints the `Content-Type` header and the first 50 characters of the body.

Use `requests` if it is installed, or `urllib.request` if it is not. Run it from the terminal with `python3 fetch.py`.

While it runs, watch your server's terminal. Write down what appeared in the log.

## 4. What HTTPS does and does not do

Someone tells you: "The padlock means nobody can see anything I do on that site."

Write four or five sentences correcting them. Be specific. Say what is genuinely hidden, name at least two things that are still visible to someone watching the network, and say what the padlock does and does not tell you about the site itself.

## 5. Watch, if you want (optional)

Crash Course Computer Science, Episode 29, "The Internet." Episode 30 is next week's, so save it: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

## Looking ahead to next week

Next week is the whole thing end to end: what happens when you open google.com, from your finger to the pixels and back. It is also the mid-year assessment and the Unit 4 checkpoint.

It is not a memory test and there is nothing to cram. The best preparation is to be able to tell the story out loud, so try explaining one piece of it to somebody at home this week: how a name becomes an address, or why a message gets split into packets, or what the padlock means.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

And the rule from class again, because it is the important one this week: your own machine and your own network, always. Anything else, ask first.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

This week continues AP topic 4.1 The Internet, specifically the protocol half of it. What the exam actually cares about from today is narrower than what you did in class, so here is the honest version:

- A protocol is an agreed set of rules. The internet works because independent organizations follow the same rules, not because anyone runs it.
- Protocols are layered. HTTP rides on TCP, which rides on IP, which rides on whatever the physical network is. Each layer only deals with the one below it.
- TCP resends what gets lost and puts things back in order. That is fault tolerance implemented in software, which is a different mechanism from last week's redundant paths, and both count.
- Encryption protects the content of a message in transit. It does not hide that the message happened.

The exam does not ask about Wireshark, the handshake by name, or port numbers. Those were for understanding, not for the test.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies. Continue the internet lessons you started last week, specifically the ones on protocols and data transmission. Still stop before the cybersecurity material; that lines up with our Week 28. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`. Pick up where you stopped last week and do the lessons on protocols, HTTP, and the web. Pay attention to the distinction that unit draws between the internet and the World Wide Web. The exam tests it and most people get it wrong.

**Extra practice if you want it.**

- Write, in AP pseudocode, a procedure that takes a list of URLs and returns a list of the ones that came back with status 200. You will not be able to actually make requests in pseudocode, so assume a `FETCH_STATUS(url)` procedure exists. This is a real exam skill: reasoning about a procedure whose insides are given to you as an abstraction. Use `ap-track/AP-Pseudocode-Bridge.md` for the syntax.
- In one paragraph, explain why layering lets the internet change without being rewritten. Give one concrete example: something that changed at one layer while the layers above it carried on unaware. Wi-Fi replacing cables is a good one, and so is IPv6.
- Look at your own browser's `User-Agent` string (search for "what is my user agent" or read it from the capture you saved in class). Write down everything it reveals about you, then find one thing on the list you would rather it did not send.
