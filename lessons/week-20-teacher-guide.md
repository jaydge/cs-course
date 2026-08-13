# Week 20 Teacher Guide

## 1. Header

- **Week:** 20 of 32
- **Unit:** 4, Operating Systems and the Internet
- **Theme question:** What does a web page actually look like on the wire?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Explain what TCP guarantees, what UDP does not, and give one sensible use for each.
- Describe the three-way handshake in order and say what it is for.
- Say what a port number is and why an address alone is not enough to deliver a message.
- Serve a folder over HTTP with `python3 -m http.server` and reach it from another machine.
- Capture packets in Wireshark, apply a display filter, and follow one TCP stream.
- Read a raw HTTP request and response, naming the method, the path, the status code, and at least two headers.
- Explain what TLS hides and what it cannot hide, having seen both in their own capture.
- Fetch a page from Python with `requests` and inspect the status code, the headers, and the body.

## 3. Where this sits

Week 19 built the road. This week is the traffic on it. Everything today rides on last week's packets: TCP is the agreement about how to turn a stream of packets back into an ordered message, HTTP is the agreement about what to put inside, and TLS is the layer that wraps HTTP so nobody in the middle can read it.

The session is built around one deliberate reveal. Students capture their own traffic to a classmate's plain HTTP server and can read every byte of it, including the request they typed. Then they capture the same kind of request to an HTTPS site and can read nothing at all. That contrast, discovered rather than told, is the most effective way to teach what encryption is actually for, and it is the reason the coding strand's `http.server` comes before the capture rather than after.

Two things about this session need real attention in prep rather than in class. Wireshark needs permission setup on macOS that requires an administrator, and packet capture on a shared network raises a privacy question that deserves an explicit conversation with students rather than a silent policy. Both are handled below.

Week 21 assembles this and everything before it into the end-to-end trace and the mid-year milestone.

## 4. Materials and setup

- The classroom network from Week 19, rebuilt: switch, router, cables, everyone plugged in. Rebuilding it takes five minutes if the cables are labeled and is worth doing before students arrive.
- Wireshark installed on every machine, with capture permissions already working. See Section 5; this cannot be done in class.
- Each machine's IP address, gathered and written on the board before or during Segment 1.
- A small folder of files on each machine to serve: an `index.html`, a `hello.txt`, and one small image. Contents do not matter; visible names do.
- Projector for the Wireshark demonstration. Wireshark's default font is small; raise it in prep.
- Whiteboard with the theme question, the Week 19 network diagram still up, and space for the handshake diagram and the request and response anatomy.
- Printed Week 20 homework handout, one per student.
- Optional but useful: a printed one-page sheet with the four display filters used today and the anatomy of an HTTP request.

## 5. Pre-class prep checklist

- **Set up Wireshark capture permissions on every machine. This is the item that must not slip to class time.**
  - On macOS, capturing requires access to the `/dev/bpf*` devices, which a standard user does not have by default. The Wireshark installer package ships an "Install ChmodBPF" component that installs a small launch daemon to grant that access to members of a group. Run that installer as an administrator, then log out and back in (a reboot is safer), then open Wireshark from the student account and confirm that the interface list on the start screen is populated rather than empty. An empty interface list is the symptom of this not being done.
  - On Windows, Wireshark captures through Npcap, which is bundled with the Wireshark installer and must be installed by an administrator. Confirm from the student account that interfaces appear.
  - **Windows students capture on the Windows host, not inside WSL.** WSL2 sits behind its own virtual network, so a capture taken inside Ubuntu will not show the machine's real traffic. Use Wireshark on Windows.
  - Verify the exact installer wording and permission mechanism against the current Wireshark documentation before your first run; the details have changed across versions and across macOS releases. (45 min the first time, 10 min in later years)
- **Pre-approve Python in the macOS firewall, as an administrator.** The first time `python3 -m http.server` listens on a port, macOS asks whether to allow incoming connections, and a standard student account may not be able to approve that dialog. Either approve it in prep from the admin account, or plan to walk around with the admin password, or turn the firewall off for the lab period on the isolated classroom network and back on afterwards. Decide which and note it. (15 min)
- **Confirm `requests` is available.** It is not in the Python standard library. Check whether the terminal's `python3` can `import requests`, and whether Thonny's Python can too, because they may be different installations. If it is missing, install it during prep (`python3 -m pip install requests`, or in Thonny via Tools, Manage Packages). If installing is awkward on your fleet, use the `urllib.request` fallback given in Segment 7 instead; it needs no installation. (15 min)
- **Create the folder to be served on every machine,** with an `index.html`, a `hello.txt`, and a small image, at `~/Documents/"CS Class"/sandbox/site`. Same folder students have used since Week 1, same `sandbox` subfolder as Week 18, same quoting rule for the space. (10 min)
- **Do a full dry run of the capture yourself:** start a server on port 8080, capture from another machine, filter with `http`, follow the stream, and read the request. Note the exact interface name to select on your fleet, because guessing it in front of the class wastes five minutes. **Use 8080 and not some other spare port.** Wireshark decides whether to dissect a TCP conversation as HTTP by looking at the port number against a built-in list, and 8080 is on that list while 8000 is not. Serve on a port Wireshark does not recognize and the packets appear as plain TCP, the `http` display filter matches nothing, and the pivot of the whole session quietly fails. Confirm during your dry run that the `http` filter actually returns your `GET` line before you rely on it in front of the room. (20 min)
- **Choose the HTTPS comparison target for Segment 6** and confirm the capture looks the way you expect. Any ordinary public site works. (5 min)
- **Prepare the privacy conversation.** Read Segment 1 step 3 and decide how you will phrase the rule for your group. Consider whether parents should be told in advance that the class uses a packet analyzer; it is a reasonable thing to mention proactively. (10 min)
- Rebuild the classroom network and print handouts. (15 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up, and the privacy contract (0:00 to 0:10)

1. **Homework check, briefly.** Ask two students for their traceroute hop counts and for one explanation of `* * *`.
2. **Pose the theme question with a demonstration of ignorance.** Load a page on the projector. Say: last week we followed the packets. Today we open one and read what is inside. Ask what they expect to find.
3. **Have the privacy conversation now, before Wireshark is open, not after.** Do not skip this and do not rush it. The points to make, in this order:
   - The tool you are about to use reads network traffic. That is exactly what it is for, and it is a completely standard tool that network engineers use every day.
   - Today you will capture only your own machine's traffic, only to a target we designate, and nothing else.
   - Do not capture, save, screenshot, or share anyone else's traffic. If something that is not yours appears in your capture, do not read it, and tell me.
   - Even without reading the contents, a capture shows who talked to whom and when. That metadata alone is revealing, which is a point worth sitting with for a moment, because it is the same argument at the center of most real privacy debates.
   - Capturing traffic on a network you do not own or administer is a different thing from what we are doing here, and depending on where you are and what you capture it can be against school policy or against the law. On your own machine, on your own home network, you are fine. Anywhere else, ask first.
   - One reassuring technical fact, which is also a lesson: because this room is wired through a switch rather than a hub, your machine mostly only sees traffic addressed to it in the first place. A switch forwards a frame to the one port that needs it. A hub, which is what these were before switches got cheap, shouted everything at everybody. That change in hardware design is itself a privacy improvement, and it is why casually snooping on a modern wired network is harder than films suggest.
4. **Get an explicit agreement,** verbally, from the room. It takes fifteen seconds and it changes how the next ninety minutes feel.

### Segment 2: Serve a folder (0:10 to 0:28), Coding strand part 1

Doing this first gives the capture in Segment 4 something readable to look at.

1. **Say what is about to happen.** Every website they have ever used is a program sitting on a machine, waiting for requests, and handing back files. They are about to be that. It is one line.
2. **Run it, on the projector first:**

   ```bash
   cd ~/Documents/"CS Class"/sandbox/site
   python3 -m http.server 8080
   ```
   Read the output line it prints: it is serving the current directory on port 8080. Note that the terminal is now busy and will not give a prompt back until you press Control-C, because the program is still running. That surprises students and is worth naming.
3. **Visit it from the same machine.** Open a browser to `http://localhost:8080`. The folder listing appears, or `index.html` if there is one. Then watch the terminal: a log line appeared for the request. Point at it and say that this is a real web server log, the same shape as the `access.log` they pipelined in Week 18.
4. **Explain `localhost` and the port in one move.** `localhost` always means this machine, and it maps to the address `127.0.0.1`, which never leaves the computer. The `:8080` is a port number. Then teach the port properly, because it is a genuinely new idea: an IP address gets you to the right machine, and a port gets you to the right program on it. Use the apartment building analogy in Section 7. Mention that some ports are conventional, notably 80 for HTTP and 443 for HTTPS, which is why browsers do not make you type them. Say why we chose 8080 specifically: it is the long-established stand-in for port 80 when you are not allowed to use 80 itself, and because it is conventional, tools recognize it as HTTP without being told. That matters in forty minutes, when Wireshark has to decide what these packets are.
5. **Students do:** Each student starts their own server in their own `site` folder. Have each write their IP address and port on the board next to their name if it is not already there.
6. **Now visit somebody else's.** Have each student open `http://<a classmate's IP>:8080` in a browser. This is the moment the room becomes the internet in miniature: their laptop is now a server that other machines are fetching files from. Let it land.
7. **Watch your own log fill up.** Each student's terminal now shows requests from other people's machines, with real addresses and real paths. Ask them to find, in their own log, the moment a specific classmate visited.
8. **If a machine refuses connections,** it is almost certainly the firewall, which is the prep item above. Say what is happening rather than just fixing it: the OS is declining to accept incoming connections for that program, which is a security feature doing its job.

### Segment 3: TCP, UDP, ports, and the handshake (0:28 to 0:48), Systems strand

1. **Return to the index cards from Week 19.** The cards arrived out of order and one might not have arrived at all. Ask who fixes that. Nobody did, last week, because the destination student did it by hand. Name the thing that does it in software: TCP.
2. **Write what TCP promises on the board,** four items: everything you sent arrives, it arrives in order, nothing arrives twice, and if something is lost it gets sent again. Then say the price: acknowledgements, buffering, waiting, and retransmission all cost time.
3. **Then UDP, in contrast.** UDP promises almost nothing. It sends the packet and does not check. Ask when on earth that would be preferable, and steer to the answer: when late data is worse than missing data. A video call that pauses for two seconds to recover one lost frame is worse than a video call that drops one frame and keeps going. Give the honest list of what typically uses each: web pages, email, and file transfer over TCP; live voice and video, DNS lookups, and many games over UDP. Add the modern caveat that a lot of web traffic now runs over newer protocols built on UDP, so the clean split is a teaching simplification; verify the current picture before stating specifics.
4. **Act out the three-way handshake with two volunteers.** Give them the lines and have them say them out loud, facing each other:
   - Student A: "Can we talk? Here is my starting number."
   - Student B: "Yes. I got your number. Here is mine."
   - Student A: "Got yours. Starting now."

   Then write the real names next to each: SYN, SYN-ACK, ACK. Ask what the exchange accomplishes. Two things: both sides know the other is really there and really listening, and both sides agree on the numbering that will let them detect a missing piece later. Say that they are about to see these three exact packets in Wireshark in ten minutes, which makes the segment feel like a prediction rather than a lecture.
5. **Draw the stack on the board and leave it up for Week 21.** Bottom to top: the physical wire and the switch, then IP getting a packet to a machine, then TCP getting an ordered stream between two programs, then HTTP saying what is wanted. Four layers. Say the framing that matters: each layer only talks to the one below it and never needs to know how that one works. This is the same abstraction idea from Week 10's key-press relay, and pointing at that is worth doing.
6. **Name HTTP before they see it.** It is a text protocol. The client sends a few lines of plain readable text saying what it wants, and the server sends a few lines back followed by the content. That is genuinely all it is, and they are about to read one.

### Segment 4: Capture the traffic (0:48 to 1:20), Systems strand

Everyone keeps their `http.server` running. Restate the rule from Segment 1 before opening the tool.

1. **Open Wireshark and stop before capturing.** Look at the start screen together. It lists the network interfaces, each with a little activity graph. Have students identify which one is their Ethernet connection; the one with a moving line is usually the right one. Say plainly that if this list is empty, the permission setup did not take, and that is a machine problem to solve now rather than a student problem.
2. **Set a capture filter to keep the noise down.** In the field at the top of the start screen, before starting, have each student type a capture filter naming their chosen partner's address:

   ```
   host 192.168.1.42
   ```
   Say what this does and why it matters ethically as well as practically: it tells Wireshark to record only traffic to and from that one machine, so nothing else is even written down.
3. **Start the capture** by double-clicking the interface. Packets start scrolling.
4. **Generate exactly one thing to look at.** Each student, in a browser, requests one specific file from their partner's server:

   ```
   http://192.168.1.42:8080/hello.txt
   ```
5. **Stop the capture immediately** with the red square. Say why: a capture left running becomes thousands of lines and finding anything in it is miserable. Capture briefly, around one action.
6. **Apply a display filter.** In the filter bar at the top of the main window, type `http` and press Return. Explain the difference from step 2 in one sentence: a capture filter controls what gets recorded, a display filter controls what you are shown from what was recorded.
7. **Find the request.** There should be a line whose Info column reads something like `GET /hello.txt HTTP/1.1`. Have every student find theirs before moving on. If a machine's filter comes back completely empty, see the note in Section 9; it is almost always the port, and it is a two-click fix.
8. **Follow the stream, which is the payoff.** Right-click that packet, choose Follow, then TCP Stream. A window opens showing the entire conversation as text, with the request in one color and the response in the other. Give the room thirty seconds of silence to just read it.
9. **Dissect the request together on the board:**

   ```
   GET /hello.txt HTTP/1.1
   Host: 192.168.1.42:8080
   User-Agent: Mozilla/5.0 ...
   Accept: text/html,...
   Connection: keep-alive
   ```
   Name each part: `GET` is the method, meaning "give me"; `/hello.txt` is the path; `HTTP/1.1` is the version. Then the headers, which are just name and value pairs of extra information. Point at `User-Agent` and say the uncomfortable true thing: their browser volunteered what browser and operating system they are running, to a stranger's machine, without being asked, on every single request.
10. **Dissect the response:**

    ```
    HTTP/1.0 200 OK
    Server: SimpleHTTP/0.6 Python/3.12
    Content-type: text/plain
    Content-Length: 20

    hello from my server
    ```
    Name the status code and give the four families in one line each: 200 means it worked, 301 and 302 mean it moved, 404 means no such thing here, 500 means the server broke. Point at the blank line and say what it is: the boundary between the headers and the content, and the only thing separating them. Then have somebody count the characters in the body and check it against `Content-Length`. Twenty characters, twenty bytes. Say what that header is for: the receiver needs to know where the content ends, and this is how it is told. Their own capture will show whatever their own file actually contains, and a file that ends with a newline counts that newline, so expect their number to be one more than the visible characters.
11. **Now clear the display filter and look at the handshake.** Change the filter to `tcp` and scroll to the top of the conversation. The first three packets are labeled `[SYN]`, `[SYN, ACK]`, and `[ACK]`. Point at each and connect them to the two volunteers from Segment 3. This is the single most satisfying moment of the session: a thing they acted out ten minutes ago, in the actual data, with timestamps.
12. **Count the packets for one small file.** Ask how many packets were involved in fetching one short text file. It is more than they expect: three for the handshake, the request, the response, acknowledgements, and a teardown at the end. Say the consequence out loud: a real web page requests dozens or hundreds of files, so a single page load is thousands of packets.
13. **Save one capture.** Have each student save their capture file with File, Save As, into their sandbox, and remind them that this file contains only their own traffic to their partner's server, which is exactly what the capture filter guaranteed.

### Segment 5: Stretch (1:20 to 1:25)

A short break. Leave Wireshark open; Segment 6 starts a new capture immediately, this time on an outside `https://` site rather than a student's own server.

### Segment 6: What TLS hides (1:25 to 1:45), Systems strand

This is the reveal the whole session was built for. Do not spoil it early.

1. **Ask a leading question.** You just read a classmate's entire request and response as plain text. Ask what that means for everything they have ever typed into a website. Let them be uncomfortable for a moment.
2. **Run the experiment.** Have each student start a fresh capture with no capture filter, or with a capture filter naming an ordinary public website's address, visit an `https://` site, and stop.
3. **Try the same filter.** Type `http` in the display filter. Almost nothing appears. Then type `tls` and the packets are there. Have them follow the TCP stream on one and look at it: unreadable bytes.
4. **Draw the line precisely, because "encrypted" is too vague and the precision is the lesson.** On the board, two columns.

   | Still visible to anyone on the path | Hidden by TLS |
   |---|---|
   | Your IP address and the server's IP address | The path you asked for |
   | The fact that a connection happened, and when | The headers, including cookies |
   | Roughly how much data moved | The content of the page |
   | The port, so the kind of service | Anything you typed or submitted |

   Note that historically the site name was visible during the handshake in a field called SNI, and that newer mechanisms encrypt it, so whether a name is visible depends on the client, the server, and the configuration. Verify the current state before teaching it as settled; this is an actively moving area.
5. **Say what the middle column means in practice.** Someone watching cannot read the message, but they can see who you talked to and when, which is the metadata point from Segment 1 arriving with evidence behind it.
6. **Explain TLS in four sentences, no more.** After the TCP handshake there is a second handshake. The server presents a certificate, which is a document signed by an organization the browser already trusts, saying that this really is that site's key. The two sides then use public-key mathematics to agree on a shared secret key that nobody watching could compute. Everything after that is encrypted with that key. Say the two jobs plainly: TLS proves who you are talking to and hides what you say, and the first job is the one people forget. Then say that public keys and certificates get their proper session in Week 28, and stop.
7. **Show the padlock and read the certificate.** Click the padlock in the browser's address bar and show the certificate details: who it was issued to, who issued it, and when it expires. Say the honest limitation, which students should hear from you rather than from the internet: the padlock means the connection is encrypted and the certificate matches the name in the bar. It does not mean the site is honest, safe, or who you think it is. A convincing fake site can have a perfectly valid certificate.
8. **Close the loop on the theme question.** The wire carries readable text unless somebody wrapped it. It used to be readable almost everywhere, and it took about twenty years of effort to change that. That change is why they could read hello.txt and could not read anything else.

### Segment 7: A request from Python (1:45 to 1:57), Coding strand part 2

- **You do:** Frame it in one sentence. The browser is not special. Anything that can open a TCP connection and send those few lines of text can be a client, and their program can.
- **You do:** At the projector, with a classmate's server still running:

  ```python
  import requests

  response = requests.get("http://192.168.1.42:8080/hello.txt")
  print(response.status_code)
  print(response.headers["Content-Type"])
  print(response.text)
  ```
  Point at each line and name what it corresponds to in the Wireshark stream they read fifteen minutes ago. The status code is the `200 OK` line. The headers are the header block. The text is what came after the blank line. Three lines of Python and one packet capture describing the same event is the connection worth making explicit.
- **You do:** Show what the library did on their behalf:

  ```python
  print(response.request.headers)
  ```
  It sent a `User-Agent` too, and it named itself. Ask what else `requests` did silently: a DNS lookup if the target had been a name, a TCP handshake, TLS if the URL had been `https`, and the parsing of the response. One function call, five layers of work.
- **If `requests` is not installed on your fleet,** use the standard library instead and say why you are:

  ```python
  from urllib.request import urlopen

  with urlopen("http://192.168.1.42:8080/hello.txt") as response:
      print(response.status)
      print(response.read().decode())
  ```
- **Students do:** Fetch two different files from a classmate's server and print the status code for each, including one path that does not exist so they see a `404` from the other side. Watching their own server log the 404 at the same moment is the useful part.
- **Say the caution once,** because it matters from here to the end of the course: writing a program that requests things from other people's servers is normal and fine at this scale, and it becomes rude or worse in a loop. Do not point a loop at a public site. Their own classmate's `http.server` is the right target today.

### Segment 8: Wrap and homework (1:57 to 2:00)

- **You do:** Hand out homework, noting the Extra Credit AP Track section.
- **You do:** Tell them exactly what Week 21 is: the whole path, end to end, plus the mid-year assessment and the Unit 4 checkpoint. Tell them the assessment is a conversation and a written trace, not a memory test, and that the two boards still up (the network diagram and the four-layer stack) are the study guide.

## 7. Key scripts and analogies

- **A port:** "The IP address gets the letter to the right building. The port number is the apartment. Without it the mail carrier is standing in the lobby holding your package."
- **TCP:** "Registered mail. Numbered, tracked, signed for, and resent if it goes missing. It is slower and you know it arrived."
- **UDP:** "A postcard, thrown. Fast, cheap, no promises. For a live video call that is the right trade, because a frame that arrives two seconds late is worse than a frame that never arrives."
- **The handshake:** "Are you there? Yes, are you? Yes. Three messages before anyone says anything useful, so that both sides know the other is really listening and both agree on how to count."
- **Layers:** "The wire moves bits, IP finds the machine, TCP puts the pieces back in order, HTTP says what you want. Four agreements stacked up, and each one only talks to the one below it."
- **HTTP:** "It is just text. A few lines saying what you want, a few lines back saying here it is. You could type it by hand, and people did, for years."
- **The status code:** "A three-digit summary of how it went, sent before anything else. 200 fine, 404 no such thing, 500 I broke."
- **What TLS does:** "It puts your postcard in an envelope. The mail carrier still knows you wrote to that address today, and can weigh it, and cannot read it."
- **The padlock, honestly:** "It means the line is private and the name matches. It says nothing at all about whether the person at the other end is honest."
- **The `User-Agent` header:** "Your browser announced what it is and what operating system it runs on to a stranger's machine, unasked, on every request. Nobody made it do that; it is just how the web grew up."

## 8. Differentiation

- **Younger or newer students:** Wireshark is visually overwhelming, and the readiness guide names it specifically. Three mitigations. First, pair them, and have the pair share one screen for the capture. Second, give them the capture filter and the display filter written down rather than making them type from memory. Third, define success narrowly and tell them what it is: start a capture, find one `GET` line, follow the stream, and read the request out loud. That is the whole learning objective and everything else is detail. In Segment 2 the server is easy and satisfying for them, so let them do it themselves. In Segment 7, running the given three-line program counts as a complete result.
- **Extensions for advanced or AP-track students:** Have them capture a DNS lookup with the display filter `dns` and match the query and the response, connecting it straight to last week's `dig`. Have them find the FIN or RST packets that end a connection and describe the teardown. Have them look at the timestamps on the three handshake packets and work out the round-trip time, then compare it to what `ping` said. Have them serve a folder and fetch it with `requests` in a small loop over several files, printing the status code for each, and then find every one of those requests in a single capture. The strongest can compare an HTTP/1.1 conversation to what a modern browser does to a real site and notice how many connections open at once.

## 9. Common pitfalls

- **Wireshark shows no interfaces.** This is the permission setup, not a student error, and it cannot be fixed quickly in class. Verify on every machine during prep. Have a plan for pairing anyone whose machine fails on the day.
- **Capturing inside WSL.** Windows students who run a capture in Ubuntu see the wrong network. Say it before it happens.
- **The macOS firewall blocking the server.** Handle it in prep. If it appears in class, name what is happening rather than clicking through it.
- **Captures too large to navigate.** Students who leave a capture running for five minutes will have tens of thousands of packets and will give up. Enforce the pattern: start, do one thing, stop.
- **The `http` display filter comes back empty.** The traffic is there but Wireshark has not recognized it as HTTP, which happens when the server is on a port that is not in Wireshark's built-in HTTP port list. Check the server is actually on 8080. If a student has started theirs on some other port, the fix takes ten seconds: clear the filter, right-click any packet in the conversation, choose Decode As, set the TCP port to HTTP, and apply. Then reapply the `http` filter and the `GET` line is there. Worth knowing before class rather than discovering it at 1:05, because this filter is the pivot of the session.
- **Capture filter versus display filter confusion.** They use different syntax, which is a genuine and unhelpful quirk of the tool. `host 192.168.1.42` is a capture filter; `ip.addr == 192.168.1.42` is the display filter equivalent. Say this once, clearly, and put both on the printed sheet.
- **Someone else's traffic appearing.** Broadcast traffic and stray packets will show up. Treat it exactly as you said you would in Segment 1: do not read it, do not save it, move on. How you handle this the first time sets the tone.
- **"So I can read everyone's passwords."** Somebody will say it. Answer it directly rather than deflecting: on a switched network you mostly see only your own traffic, nearly everything worth reading is encrypted now, and attempting it on a network you do not own is a serious matter with real consequences. Then point out that the reason those two facts are true is the twenty years of work Segment 6 described.
- **Overrunning into Segment 6.** The capture is engaging and will expand. Hard stop at 1:20. The TLS contrast is the point of the whole session and cutting it wastes everything before it.
- **`requests` missing, or installed for the wrong Python.** The classic version of this is that it works in Thonny and not in the terminal. Check in prep and use the `urllib` fallback if needed.
- **Teaching too much TLS.** The temptation to explain public-key exchange properly is strong. Resist it; that is Week 28, with the paint-mixing activity to make it land. Four sentences today.

## 10. Homework

Full details in `handouts/week-20-homework.md`. In summary: serve a folder at home on port 8080 and fetch it from a phone or a second device on the same network; four short questions comparing TCP and UDP, explaining ports, and reading status codes; a Python program that fetches three paths from their own server and reports the status codes; a written answer on exactly what TLS hides and what it does not, using the two-column table from class; the optional Crash Course episode on the internet. Wireshark work is deliberately not assigned as homework, for the privacy reasons discussed in class, and the handout says so. The handout closes with an Extra Credit AP Track section continuing the CodeAI internet unit.

## 11. Assessment

Observational, plus one artifact. The single observation worth recording, per student, during Segment 4: could they get to a followed TCP stream and read the `GET` line out of it? That is the whole lab in one check.

The homework's written answer about TLS is the item to read carefully. The misconception to look for is "HTTPS means nobody can see anything," which is both wrong and consequential, and it is worth correcting individually rather than only to the group. The two-column table from Segment 6 is the standard to mark against.

Also note, for Week 21 planning, which students could explain the four-layer stack without looking at the board. Those are the students who will do well on the milestone, and the ones who could not are the ones to give a heads-up to about what the assessment asks.

## 12. AP alignment

This session continues **AP CSP topic 4.1 The Internet**, which is the protocol half of that topic: the idea that a protocol is an agreed set of rules, that protocols are layered, that HTTP sits on TCP which sits on IP, and that this layering is what allows the internet to scale and to change without everything being rewritten. It also touches **topic 4.2 Fault Tolerance** from a different angle than last week, since TCP's retransmission is fault tolerance implemented in software rather than in the network's shape.

The TLS material connects forward to **topic 5.6 Safe Computing**, which our course covers properly in Week 28. Mention the connection, do not claim the topic is covered today.

A word on depth, so nobody over-prepares: the exam does not ask about Wireshark, about the three-way handshake by name, or about port numbers. What it does ask is whether a student understands that protocols are agreements, that they are layered, and that encryption protects content in transit. Today's lab makes those three ideas concrete, which is its real exam value, but the lab itself is well beyond exam depth. That is fine and deliberate; this course is not only exam preparation.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies. Continue the internet lessons started last week, specifically the protocol and data-transmission material. Still stop before the cybersecurity lessons, which belong with our Week 28. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`. Continue where Week 19 stopped: the lessons on protocols, HTTP, and how the web works on top of the internet. The distinction that unit draws between the internet and the web is one the exam does test and one students routinely get wrong.

Nothing here is required of non-AP students.

## 13. Resources used this week

- The server, capture, TLS, and `requests` work: Segments 2, 4, 6, and 7 are complete on their own once the prep in Section 5 is done.
- **Wireshark, and this one genuinely needs reviewing in advance.** The macOS capture-permission mechanism (the ChmodBPF helper installed by the Wireshark package) and the Windows Npcap requirement are both administrator-level setup steps that change between releases. Read the current installation and permission notes before your first run: `https://www.wireshark.org` and the user guide linked from it. Verify against your actual macOS version rather than trusting a remembered procedure.
- Python `http.server`, for your reference and for the security note in its own documentation about not using it in production: `https://docs.python.org/3/library/http.server.html`
- The `requests` library documentation: `https://requests.readthedocs.io`. Standard-library fallback: `https://docs.python.org/3/library/urllib.request.html`
- Crash Course Computer Science, Episode 29 ("The Internet"), optional homework viewing. Episode 28 was Week 19's and Episode 30 ("The World Wide Web") is Week 21's, where it lands better because that session is about the web sitting on top of everything else. One episode per week, no repeats. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Unit 2, The Internet (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/2`
- Wireshark's place in the lab equipment and software stack: Sections 6 and 8 of `curriculum/CS-Curriculum-and-Setup.md`.
- Why Wireshark is a flagged difficulty spike for newer students: Section 1 of `student-prep/Younger-Student-Readiness-and-Prep.md`.
