# Week 19 Teacher Guide

## 1. Header

- **Week:** 19 of 32
- **Unit:** 4, Operating Systems and the Internet
- **Theme question:** How does a message find one particular machine out of billions?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Explain what a packet is and why a message is broken into many of them.
- Describe routing as a series of local decisions with no single machine knowing the whole path.
- Say why the internet keeps working when a router fails, and demonstrate it in the unplugged activity.
- Distinguish a MAC address from an IP address and say which one changes when you move to a different network.
- Say in one sentence each what DNS, DHCP, and NAT do.
- Say what a switch does that a router does not.
- Find their own IP address, their MAC address, and their default gateway from the terminal.
- Run `ping` and `traceroute` and read the output.

## 3. Where this sits

This is the week the wires get plugged in. Weeks 17 and 18 stayed inside one machine; from here to Week 21 the subject is what happens between machines. The readiness guide flags the networking acronyms as one of the two biggest difficulty spikes in the first half of the course, alongside the terminal, and for the same reason: nothing here is conceptually hard, but eight new abbreviations arrive in two hours and a student who loses one loses the thread.

The design counters that in two ways. The unplugged Packet Routing activity comes first, before any acronym, so that every abstract term afterwards has a physical memory attached to it. And the physical network build means students meet each acronym while holding the thing it names: this is the switch, this is the cable, this is the address the router just handed you.

This is also the first genuinely AP-tested session of Unit 4. Topics 4.1 The Internet and 4.2 Fault Tolerance are both squarely covered, and the node-drops-out moment in the unplugged activity is 4.2 almost verbatim.

Week 20 adds the protocols that ride on top of this (TCP, UDP, HTTP, TLS) and captures them in Wireshark. Week 21 assembles everything into the end-to-end trace.

## 4. Materials and setup

- The networking kit: the gigabit switch, the old Wi-Fi router, and enough Ethernet cables to reach every machine plus two spares. Count the cables during prep, not in class.
- **USB-C to Ethernet adapters, one per MacBook.** Modern MacBooks have no Ethernet port. If you do not have adapters, the build still works with the switch, the router, and two wired machines while the rest connect over the router's Wi-Fi, but check this before class rather than discovering it at 0:40.
- A power strip for the switch and the router.
- Masking tape and a marker for labeling cables and ports.
- Index cards for the unplugged activity: about 20 blank ones for packets, plus a card per student with a node name (A through H or similar). String or yarn is optional and makes the links visible.
- Whiteboard with the theme question, plus a large clear area for the network diagram, which must survive to Week 21.
- Projector for the terminal demonstrations and the router's admin page.
- Printed acronym card, one per student, described in Section 5.
- Printed Week 19 homework handout, one per student.

## 5. Pre-class prep checklist

- **Build the whole network once, alone, before class.** Every problem you will hit in front of students is findable in twenty minutes of prep: a dead cable, a router whose admin password you do not have, a laptop with no adapter, a switch port that does not light. Build it, confirm every machine gets an address, then take it apart and coil the cables. (30 min the first time)
- **Know the router's admin address and password.** It is usually printed on a label on the underside, and the address is commonly something like `192.168.0.1` or `192.168.1.1`. Log in during prep and find the DHCP client list page, because you will project it in Segment 3 and hunting for it live is tedious. If you cannot log in, factory reset the router during prep, not during class. (15 min)
- **Decide the safety rule about the house network and write it on the board.** The router's WAN port connects to the house internet; the router's LAN ports connect to the switch and the classroom machines. Never plug a LAN port of the classroom router into the house network, because two DHCP servers on one network hands out conflicting addresses and takes down the house. State this to students too; it is a real lesson, not just housekeeping. (5 min)
- **Check that `traceroute` and `dig` exist on your machines.** Both are present by default on macOS. On WSL Ubuntu they often are not, and installing them needs `sudo apt install traceroute dnsutils` with a working internet connection, which must happen during prep. (15 min)
- **Know the WSL address gotcha before a student finds it.** WSL2 runs behind its own virtual NAT, so `ip addr` inside Ubuntu shows a private address that is not the machine's address on the classroom network. For this week, Windows students run the networking commands in PowerShell or Windows Terminal's PowerShell profile, not in Ubuntu. Write the PowerShell equivalents on the acronym card. This is genuinely confusing and worth pre-empting; it is also a perfect real-world example of NAT, and Segment 5 uses it as one. (10 min)
- **Write and print the acronym card.** One page. Left column: MAC, IP, DHCP, DNS, NAT, router, switch, packet, gateway, each with a one-line plain-English definition. Right column: the commands, in two rows, macOS and Windows PowerShell. This card is the single most useful thing you hand out this week. (20 min)
- Choose an outside host for `traceroute` and test it during prep so you know how many hops it takes and where it stalls. Something geographically distant makes a better demonstration. Verify it still responds on the day; hosts change their ICMP policies. (10 min)
- Print homework handouts and acronym cards. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up and homework check (0:00 to 0:10)

- **You do:** Ask two students to run their `find_lines.py` from the terminal on the projector. Thirty seconds each. This is the Week 18 assessment check and it takes almost no time.
- **You do:** Pose the theme question concretely. Put a laptop on the projector, open a page, and ask: there are billions of computers. How did that request find the one machine that has this page, and how did the answer find its way back to this specific laptop, in this room, rather than to any of the others? Take answers for two minutes without correcting anything.
- **You do:** Say what the day looks like: forty minutes with no computers at all, then the room becomes a network, then the commands.

### Segment 2: Packet Routing, unplugged (0:10 to 0:40), Systems strand

Run this entirely from the steps below. The canonical source is in Section 13 for prep, but nothing here requires it.

1. **Build the network out of students.** Spread the class around the room and give each student a card with a single letter on it, A through however many you have. Assign each student two or three neighbors they are connected to, and have them either hold a piece of string to each neighbor or simply remember and announce them. Draw the same graph on the whiteboard as you go, labeled with the same letters. Make sure the graph is not a straight line: there must be at least two different routes between the two most distant nodes. That redundancy is the entire point of step 7.
2. **State the one rule that makes this teach networking.** Each node may only pass a card to a node it is directly connected to. Nobody may walk across the room. Nobody has a map. Say it twice, because the temptation to just hand it to the destination is enormous.
3. **Send one message.** Write a short message on an index card and put the destination letter in the corner: "TO: H". Hand it to student A. Each student who receives it looks at the destination, picks a neighbor they think is closer, and passes it. Let it arrive, or let it wander; both outcomes are useful. Ask the class to trace the path it actually took on the whiteboard graph.
4. **Ask the important question.** Did anybody in this room know the whole route? No. Each person made one local decision. Say the sentence: that is routing, and there is no machine on the internet that knows the whole path either. Every router knows only its neighbors and a rough sense of which direction is better.
5. **Now break the message up.** Write a sentence of about eight words. Put each word on its own index card, and number them 1 of 8, 2 of 8, and so on, all addressed to the same destination. Hand them to A a couple of seconds apart. Tell the intermediate nodes they may choose different neighbors for different cards if they like, and encourage a couple of them to do so.
6. **Read the result at the destination.** The cards arrive out of order, and probably by different routes. Have the destination student read them in the order received, which is gibberish, then reassemble them by number and read the real sentence. Name all three ideas at once: those cards are packets, splitting the message is why one large file cannot block the whole network, and putting them back in order is a job for something at the far end. Say that the something has a name, TCP, and that it is next week's topic.
7. **Kill a node, which is the AP moment.** Start another eight-card message, and after the third card, tap a busy intermediate node and have them sit down and fold their arms. Do not announce a fix. The remaining nodes have to find another way, and they will. Ask what would have happened if there had been only one path. Then say the design principle plainly: the network was built during the Cold War with the assumption that parts of it would be destroyed, so it was designed with many possible paths and no central controller. That is fault tolerance and redundancy, and it is exam topic 4.2.
8. **Add congestion in one minute, if the group is enjoying it.** Tell one node they may only hold three cards at a time and must refuse the fourth. Watch senders have to try again. Name it: that is congestion, and the network's answer is to slow down and retry rather than to make the pipe bigger.
9. **Close with the honest scale comparison.** Roughly a dozen nodes here. The real internet is hundreds of thousands of independent networks, run by thousands of separate organizations that agree on nothing except how to pass packets. Nobody is in charge of it. That is the most surprising true fact about the internet and it is worth ten seconds of silence.

**Purpose:** Packets, routing, redundancy, fault tolerance, reassembly, and congestion all arrive physically, with a story attached to each, before a single acronym is spoken.

### Segment 3: Build the physical network (0:40 to 1:05), Systems strand

Students do the plugging. You narrate. Keep the whiteboard diagram from Segment 2 visible and draw the real network next to it.

1. **Lay out the parts on a table and name each one as a job, not a product.** The router is the gateway between this room and everything else. The switch is the thing that connects machines inside this room to each other. The cables are the wires. Say the distinction you want them to keep: a switch moves traffic within one network, a router moves traffic between networks.
2. **Power the switch and plug one cable from a router LAN port into any switch port.** Point at the link light that comes on. Say what it means: there is a working electrical connection and both ends agree on a speed. On a gigabit switch the light or its color often indicates the negotiated speed; a cheap or damaged cable can silently negotiate down, which is a real-world troubleshooting fact worth mentioning once.
3. **Say the safety rule out loud and write it on the board.** The router's WAN port goes to the house internet and nowhere else. No cable from the classroom router's LAN side ever goes into a house network jack. Explain why in one sentence: two devices both handing out addresses on one network is a genuine outage, and it is one of the most common self-inflicted network failures there is.
4. **Have each student plug their own laptop into a switch port,** with a USB-C Ethernet adapter where needed. Label each cable at the switch end with a piece of tape and the student's name; it makes Segment 5 much easier. Watch the link lights appear one at a time.
5. **Watch the addresses arrive.** Have every student run the address command for their platform:

   ```bash
   ipconfig getifaddr en0
   ```
   On a Mac with a USB Ethernet adapter, `en0` may be the wrong interface. The reliable version, which works regardless:

   ```bash
   ifconfig | grep "inet "
   ```
   On Windows, in PowerShell:

   ```powershell
   ipconfig
   ```
   Have each student call out their address. Write them all on the board in a column.
6. **Ask the question the board answers for you.** What is the same about all of these addresses, and what is different? They share the first three groups and differ in the last. Name it: the shared part identifies this network, the different part identifies the machine on it. That is the whole idea of an IP address in one sentence.
7. **Ask who gave them those addresses.** Nobody typed one in. Name DHCP: the router runs a service that hands out an address to any machine that asks, along with the address of the gateway and of a DNS server. It is a lease, not a gift; it expires and gets renewed. Then project the router's admin page and show the DHCP client list, with the same names and addresses that are on the board. Students find this genuinely satisfying.
8. **Show the MAC address and draw the distinction hard.**

   ```bash
   networksetup -listallhardwareports
   ```
   on macOS, or `ipconfig /all` in PowerShell on Windows, or `ip link` in Linux. The MAC is burned into the network hardware at the factory and does not change when you move. The IP is assigned by whichever network you are on and changes every time you move. Ask what their laptop's IP was at home yesterday; nobody knows, and that is the point. Then say where each is used: the MAC gets a frame across one physical hop, and the IP gets a packet across the whole world. Say that most phones and laptops now randomize their MAC on Wi-Fi for privacy reasons, so "burned in at the factory" is true of the hardware and no longer true of what the network sees; verify the current behavior on your own devices before stating it as fact.
9. **Find the gateway, and name it.**

   ```bash
   netstat -rn | grep default
   ```
   on macOS, or `route print` or `ipconfig` in PowerShell. That address is the router. Say what "default" means: if I do not know where this packet goes, I hand it to the gateway and it becomes their problem. Every machine in the room has the same default gateway, and that is the door out of this network.
10. **Connect the router's WAN port to the house internet.** Then have everyone reload a web page. It works. Point out that nothing about their machine changed; a door opened one level up.

### Segment 4: Stretch (1:05 to 1:10)

A short break. Leave the address column on the board and the network built; hand out the acronym cards as students sit back down, ready for Segment 5.

### Segment 5: Names, addresses, and the trip out (1:10 to 1:35), Systems strand

Hand out the acronym cards at the start of this segment.

1. **Ping the machine next to you.** Pick two students whose addresses are on the board:

   ```bash
   ping -c 4 192.168.1.42
   ```
   Read the output as a class: bytes, the address that answered, and the round-trip time. Point at the time and say what it measures: there and back, in milliseconds. On this switch it will be well under a millisecond. Say what `ping` actually does in one sentence: it sends a tiny "are you there" message that the other machine's OS answers automatically, without any application being involved.
2. **Ping something far away** and compare the times:

   ```bash
   ping -c 4 1.1.1.1
   ```
   Ten to a hundred times slower. Ask why, and give the answer in two parts, in this order, because students get it backwards otherwise. First, distance. Signals travel fast but not instantly: light in glass fibre moves at roughly two thirds of its speed in a vacuum, about 200,000 kilometres per second, which works out at about 10 milliseconds of round trip for every 1,000 kilometres of cable. Do the arithmetic on the board for somewhere they know. That number is a floor. No amount of money, better hardware, or clever software gets a packet there faster than the distance allows. Second, everything else adds on top of the floor: each router along the way has to receive the packet, look up where to send it, and put it back on a wire, and if a link is busy the packet waits in a queue first. On a healthy uncongested path those additions are small next to the distance. On a congested one they can dominate, which is exactly what a network engineer is looking for when the ping time is far above the floor the map says it should be.
3. **Show `arp` and connect it to Segment 2.**

   ```bash
   arp -a
   ```
   This is the table mapping IP addresses in this room to MAC addresses. Say what it is for: to actually put a packet on the wire, the machine needs the neighbor's hardware address, so it shouts "who has 192.168.1.42?" on the local network and remembers the answer. This is the local half of routing, and it only works within one network, which is exactly what a switch bounds.
4. **Now names.** Ask what is wrong with `1.1.1.1` as something to remember. Then:

   ```bash
   dig example.com +short
   ```
   or, if `dig` is unavailable, `nslookup example.com`. Name DNS: a global, distributed directory that turns names into addresses. Say the four-step shape without belaboring it: your machine asks a resolver, usually the one DHCP told it about; the resolver asks a root server which servers know about `.com`; those point at whoever is authoritative for `example.com`; that server gives the address. Then say the practical fact: almost none of that happens most of the time, because every layer caches the answer, which is why the second lookup is instant.
5. **Show the cache and the failure mode in one move.** Run `dig example.com` twice and compare the query times. Then say the sentence that makes DNS memorable: when people say "the internet is down," it is very often DNS that is down, because a name that will not resolve is indistinguishable from a site that does not exist.
6. **NAT, with the classroom as the example.** Ask every student to visit a "what is my IP" page or just tell them the router's public address. Every machine in the room reports the same public address. Ask how that is possible when they all have different addresses on the board. Name NAT: the router rewrites the source address of every outgoing packet to its own public one, keeps a table of who asked for what, and rewrites the replies on the way back. Say why it exists: IPv4 has about four billion addresses and the world needed more, so NAT lets an entire building share one. Then use the Windows machines as the second example: WSL2 sits behind another NAT of its own, which is why the address inside Ubuntu is not the address on the board. Two layers of NAT in one room.
7. **IPv6 in ninety seconds.** Show one:

   ```bash
   ifconfig | grep inet6
   ```
   Say the three things worth knowing. It is much longer, written in hexadecimal with colons instead of decimal with dots. There are enough addresses that every device on earth can have a globally unique one, which removes the reason NAT was invented. And the transition has been under way for decades and is still not finished, because changing something this large while it stays running is genuinely hard. Do not teach IPv6 notation rules; recognition is the objective.
8. **`traceroute`, as the finale.**

   ```bash
   traceroute example.com
   ```
   Project it and narrate as the lines appear. Each line is one router along the path, with three timing samples. Point out three things: the first hop is the classroom router they just plugged in, the addresses become recognizable network operators as they get further out, and some hops show `* * *` because plenty of routers are configured not to answer, which does not mean the path is broken. Then connect it back to Segment 2 explicitly: every one of those lines is one student passing an index card, and not one of them knew the whole route. On Windows the command is `tracert`.

### Segment 6: Addresses in Python (1:35 to 1:55), Coding strand

- **You do:** Make the point first. Everything they did in the last twenty-five minutes, a program can do, because these are just services the operating system offers.
- **You do:** Build this at the projector:

  ```python
  import socket

  print(socket.gethostname())
  print(socket.gethostbyname("example.com"))
  ```
  Say what happened: the second line is DNS, done from Python, using the same resolver the whole machine uses. Nine characters of code for a global distributed lookup, which is abstraction doing its job again.
- **You do:** Add the subnet question, which is where the concept lands:

  ```python
  import ipaddress

  network = ipaddress.ip_network("192.168.1.0/24")
  print(network.num_addresses)

  a = ipaddress.ip_address("192.168.1.42")
  b = ipaddress.ip_address("192.168.1.99")
  c = ipaddress.ip_address("8.8.8.8")

  print(a in network, b in network, c in network)
  ```
  Explain `/24` in one sentence: the first 24 bits identify the network and the rest identify the machine, which is exactly the "same first three groups" observation from the board in Segment 3. Then say why this matters: this is the actual decision every machine makes for every packet. If the destination is in my network, send it directly to that machine. If it is not, send it to the gateway. Two lines of logic, running billions of times a second across the world.
- **Students do:** Write a program that takes a list of five or six site names, looks up each one, and prints the name and address side by side. A list and a `for` loop is all this needs; it is Week 6 and Week 7 material pointed at a new problem. If a name does not resolve, the program stops with a `socket.gaierror` and prints nothing after that point. Treat that as a result rather than a bug: have them read the error, check the spelling of the name, and drop or correct it. Python does have a way to catch an error and carry on, and we meet it later in the course; today the useful lesson is that a failed lookup is a real thing that happens and the error message says which name caused it.
- **Students do, if time allows:** Have them look up the same name twice and time both with `time.time()`. The second is dramatically faster. Ask why, and get "caching" back from them rather than saying it.
- **Purpose:** DNS and subnetting stop being diagram words and become two things a program does in a handful of lines. This also sets up Week 20, where `requests` will do the same lookup silently as step one of every call.

### Segment 7: Wrap and homework (1:55 to 2:00)

- **You do:** Point at the network diagram on the board and say it stays up until Week 21, because the mid-year assessment walks straight through it.
- **You do:** Hand out homework, noting the Extra Credit AP Track section and telling AP-track students that after two off-topic weeks, today was squarely on the exam.
- **You do:** Exit question at the door: what is the difference between a MAC address and an IP address? One sentence each.

## 7. Key scripts and analogies

- **A packet:** "You cannot mail a sofa. You can mail it in forty numbered boxes and let the person at the other end put it back together. That is a packet, and the numbering is the important part."
- **Routing:** "Nobody in that game had a map, and nobody on the internet has one either. Every router knows its neighbors and a rough sense of which way is better. Billions of local decisions, no plan."
- **Fault tolerance:** "It was built assuming pieces of it would be destroyed. So there is no center to attack, and no single failure that matters. When you sat down mid-message, the network routed around you and did not even complain."
- **Switch versus router:** "A switch is the hallway inside one building. A router is the front door to the street. Different jobs, and the switch has no idea the street exists."
- **MAC versus IP:** "Your MAC is like your name; it comes with you and it does not change. Your IP is like your seat number in this room; it is about where you currently are, and you get a different one tomorrow."
- **DHCP:** "You walked into the room and something handed you a seat number, a map to the door, and the phone number of the directory. Nobody typed anything."
- **DNS:** "The phone book of the internet, except the phone book is spread across thousands of machines and there is no complete copy of it anywhere."
- **Why DNS breaks everything:** "A name that will not resolve looks exactly like a site that does not exist. That is why 'the internet is down' is so often just DNS."
- **NAT:** "One street address for the whole building, and a receptionist keeping a list of who is expecting a delivery. That list is the whole trick."
- **Why far away is slow:** "Distance sets a floor you cannot argue with. Light in a fibre covers about 200 kilometres every millisecond, so a server 1,000 kilometres away costs you about 10 milliseconds there and back before anybody has done any work. Every router along the way then adds a little on top, looking up where to send it and sometimes making it wait in a queue. The distance is the floor; the routers are the extra."
- **The default gateway:** "If I do not know where this goes, I hand it to the router and it is their problem now. Every machine in this room says that about almost every packet it sends."
- **Scale:** "Hundreds of thousands of separate networks run by organizations that agree on almost nothing, except how to pass a packet. Nobody is in charge of the internet. That still sounds wrong and it is still true."

## 8. Differentiation

- **Younger or newer students:** This is the acronym spike the readiness guide warns about, so pre-load it if you can: assign one of the short internet films from Section 13 the week before, so the vocabulary is not brand new today. In class, give them a physically central node in the unplugged activity so they handle many cards. During the build, have them do the plugging, which is concrete and memorable. On the commands, three are enough: `ipconfig getifaddr en0` or `ipconfig`, `ping`, and `traceroute`. Skip `arp` and `dig` for them. In Segment 6, running the two-line DNS lookup is a complete result; skip the `ipaddress` work.
- **Extensions for advanced or AP-track students:** Have them run `traceroute` to a server on another continent and count the hops, then to something local, and explain the difference. Have them work out from the board how many machines could fit on the classroom network and confirm it with the `ipaddress` code. Have them find the manufacturer of their own network card by looking up the first three bytes of their MAC address, which is a real, assigned identifier. Have them explain, precisely, why the address shown inside WSL Ubuntu differs from the one on the board. The strongest can look up what `ping` actually sends (ICMP echo request) and why some servers never answer it.

## 9. Common pitfalls

- **No Ethernet adapters for the MacBooks.** The single most likely way this session fails. Check in prep.
- **Two DHCP servers.** If the classroom router's LAN side reaches the house network, addresses conflict and things break in confusing ways. Enforce the rule in Segment 3 step 3, and keep the WAN cable in your pocket until step 10.
- **WSL showing the wrong address.** Windows students running `ip addr` inside Ubuntu see a NAT address and conclude the build failed. Tell them before it happens and run PowerShell for this week's commands.
- **`traceroute` or `dig` missing on Ubuntu.** Install during prep. Installing packages mid-class costs ten minutes and needs internet, which may be the thing you unplugged.
- **`en0` is not the Ethernet interface.** With a USB adapter it usually is not. Use `ifconfig | grep "inet "` and read the private address from the list rather than teaching interface names.
- **`* * *` hops read as failure.** Say in advance that many routers are configured not to reply and that the trace continues past them.
- **Acronym overload.** Eight abbreviations is genuinely a lot. The acronym card is the mitigation, and so is refusing to introduce any acronym that is not on it. Resist adding VLANs, subnetting math, or the OSI model. The seven-layer model in particular is a tempting detour that adds nothing here and confuses everyone; if a student raises it, say it exists, that it is a teaching model rather than what the software actually implements, and move on.
- **The unplugged activity overrunning.** It is fun and expands to fill any time. Hard stop at 0:40. The node-drops-out step is the one that must happen; if you are short, cut the congestion step instead.
- **Students handing cards across the room.** Restate rule 2 every time it happens. The whole activity collapses without it.
- **Cables left in a heap.** Assign two students to coil and count them at the end. You need the same count next week.

## 10. Homework

Full details in `handouts/week-19-homework.md`. In summary: run five network commands on their home network and record the output; a traceroute to a site of their choice with three questions about the output; compare their home IP address to the one they had in class and explain why it differs; extend the Python DNS lookup program; a short written explanation of routing and fault tolerance in their own words; the optional Crash Course episode on computer networks. The handout closes with an Extra Credit AP Track section carrying a real AP unit for the first time in three weeks.

## 11. Assessment

Observational plus homework. During Segment 2, the thing to watch for is whether students keep the local-decision rule or start walking cards across the room; the ones who break it are the ones who have not yet got the idea, and a quiet word is more effective than a correction to the group.

The exit question (MAC versus IP) is the quick check. In the homework, the two items that matter are the explanation of why the home IP address differs from the classroom one, which tests whether DHCP and NAT landed, and the routing paragraph, which is a rehearsal for the Week 21 milestone. Score against the weekly-labs rubric.

Keep the acronym recall informal this week. Recognition is the target now; recall is checked on the Unit 4 concept check in Week 21, and students should be told that so they know the card is a study aid and not a crutch forever.

## 12. AP alignment

This session directly covers **AP CSP topic 4.1 The Internet** and **topic 4.2 Fault Tolerance**, and it is the strongest AP session of Unit 4. Big Idea 4 is 11 to 15 percent of the multiple-choice exam, and most of that weight sits on exactly today's material: packets, routing, redundancy, protocols as agreements, and the idea that the internet is a network of networks with no central authority.

Specific things the exam expects, all of which happened today: a packet contains data plus metadata used for routing and reassembly, packets may arrive out of order and by different paths, routing is done by independent devices making local decisions, and redundancy in the network's structure is what makes it fault tolerant. The node that sat down in Segment 2 is topic 4.2 in physical form; refer back to that moment when it comes up again.

One clarification worth making so nobody over-claims: **topic 4.3, Parallel and Distributed Computing, is not this week.** It is covered in Week 29 alongside cloud and distributed systems. Distributing a computation across machines is a different idea from routing a packet between them, and conflating them causes real confusion on the exam.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, which is where the internet and cybersecurity material lives. Work only the internet lessons: how the internet is structured, protocols, addressing, and routing. Stop before the cybersecurity material; that belongs with our Week 28. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`. This unit is a direct match, and the early lessons on addressing, packets, routing, and redundancy cover today almost exactly. Do those and stop; the protocol and HTTP lessons later in the unit are next week.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Packet Routing unplugged: Segment 2 is complete on its own. The canonical versions are CS Unplugged's Routing and Deadlock and Network Protocols activities, from the activities index at `https://classic.csunplugged.org/activities/`. Review during prep only if you want additional variants of the congestion round. The activity description and its place in the course are in `teaching-activities/Unplugged-Logic-Activities.md`.
- The physical network build and the command work: Segments 3 and 5 are complete on their own. The one thing to look up in advance is your specific router's admin address and DHCP client list page, which is model-specific and usually printed on the device.
- CodeAI internet film series, "How the Internet Works," short films of a few minutes each. Worth assigning the week before to any student flagged on the readiness diagnostic, per Section 4 of `student-prep/Younger-Student-Readiness-and-Prep.md`. Find the current series from `https://code.org`; the hosting of these films has moved more than once, so verify the link before assigning it.
- Crash Course Computer Science, Episode 28 ("Computer Networks"), optional homework viewing and a close match for this session. Episode 29 ("The Internet") is Week 20's assignment and Episode 30 ("The World Wide Web") is Week 21's; do not assign them early, or students will meet them twice and read the second showing as new work. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- Python `socket` and `ipaddress` documentation, for your reference: `https://docs.python.org/3/library/socket.html` and `https://docs.python.org/3/library/ipaddress.html`
- CodeAI CSP Unit 2, The Internet (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/2`
- AP topics 4.1 and 4.2 and where the course covers them: `ap-track/AP-CSP-Topic-Coverage.md`.
- Lab equipment list, including the switch, router, and cables used today: Section 7 of `curriculum/CS-Curriculum-and-Setup.md`.
