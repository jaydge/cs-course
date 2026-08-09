# Week 19 Homework: Finding One Machine Out of Billions

This week the room became a network. You passed packets by hand, plugged the real thing together, and found out what all those acronyms actually name. Keep your acronym card next to you. Plan on about 45 minutes.

Everything below runs on your home network, which is a different network from the classroom one. That is the point of several of the questions.

## 1. Five commands on your own network

Run each of these and write down what it prints. Mac users use the first version, Windows users the second, in PowerShell (not Ubuntu, for the reason we talked about in class).

| What you want | Mac | Windows PowerShell |
|---|---|---|
| Your IP address | `ifconfig \| grep "inet "` | `ipconfig` |
| Your MAC address | `networksetup -listallhardwareports` | `ipconfig /all` |
| Your default gateway | `netstat -rn \| grep default` | `ipconfig` |
| Ping your own router | `ping -c 4 <gateway>` | `ping <gateway>` |
| Ping something far away | `ping -c 4 1.1.1.1` | `ping 1.1.1.1` |

Write down your IP address, your MAC address, your default gateway, and the two round-trip times. Which time is bigger, and roughly by how many times?

## 2. Trace a route

Pick a website you think is a long way away, and run `traceroute thesitename.com` (Windows: `tracert thesitename.com`). Copy down the first three lines and the last three, then answer:

1. How many hops did it take in total?
2. What was the very first hop, and what is that device in your house?
3. Some lines show `* * *` instead of a name and a time. Does that mean the connection is broken? Explain what it actually means.

## 3. Two addresses, two questions

1. Your IP address at home is different from the one you had in class. Your MAC address is the same. Explain why, in two or three sentences. Use the words DHCP and MAC.
2. Everyone in your house who is online right now shares one public address on the internet, even though each device has its own address inside the house. What is the name for the thing the router is doing, and roughly how does it keep the replies straight?

## 4. Extend the lookup program

Start from the program we wrote in class:

```python
import socket

print(socket.gethostbyname("example.com"))
```

Make a list of five websites you use, loop through the list, and print each name next to its IP address. Then look up the same name twice in a row, time both lookups with `time.time()`, and write one sentence saying which was faster and why.

If a name will not resolve, your program will stop with an error naming it. That is a real result, not a bug in your code: check the spelling, and drop the name if it is genuinely gone.

Save it into your CS Class folder as `lookup.py` and run it from the terminal with `python3 lookup.py`.

## 5. Explain it in your own words

Four or five sentences, no jargon you cannot explain.

You send a message across the internet. No single computer along the way knows the whole route to the destination. Explain how it gets there anyway, and explain why the message still arrives if one of the machines along the way stops working partway through.

## 6. Watch, if you want (optional)

Crash Course Computer Science, Episode 28, "Computer Networks," is about ten minutes and covers exactly this week. Episode 29 is next week's, so save it: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course, starting in Week 27. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.

One more thing, and it applies from here to the end of the unit: run these commands only on your own network, on your own machine. Poking at networks and machines that are not yours is a different thing entirely, and we will talk about exactly where that line is in Week 28.

---

## Extra Credit AP Track

Optional. This section is for students on the AP track and for anyone who finds this stuff interesting, whether for fun or for AP preparation. It is extra credit only: never required, and it is not part of your base grade. Skipping it costs you nothing.

**After two off-topic weeks, this one is squarely on the exam.** Today covered AP topic 4.1 The Internet and topic 4.2 Fault Tolerance. Big Idea 4 is 11 to 15 percent of the multiple choice, and most of that weight sits on what you did today.

Five things the exam expects you to be able to say, all of which you did in the index-card activity:

- A packet carries data plus metadata, and the metadata is what makes routing and reassembly possible.
- Packets from one message can travel different paths and arrive out of order.
- Routing is done by independent devices making local decisions. No device knows the whole path.
- Redundant paths are what make the internet fault tolerant. Remove one node and the traffic goes around it.
- A protocol is an agreed set of rules, and the internet works because independent organizations follow the same ones, not because anyone is in charge.

One thing to keep straight, because the exam does: topic 4.3, Parallel and Distributed Computing, is a different topic and it is not this week. That is about splitting a computation across several processors or machines, and our course covers it in Week 29.

**Your unit for this week.** Do only the slice below, not the whole course.

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, which is where the internet material lives. Work only the internet lessons: structure of the internet, protocols, addressing, and routing. Stop before the cybersecurity lessons; those belong with our Week 28. If the unit numbering on your account does not match, ask your instructor; the numbering is being confirmed.
- **CodeAI, formerly Code.org (free alternative):** Unit 2, The Internet, at `https://studio.code.org/courses/csp-2025/units/2`. This is a direct match. Do the lessons on addressing, packets, routing, and redundancy, then stop. The protocol and HTTP lessons later in that unit are next week's work.

**Extra practice if you want it.**

- Work out how many machines could fit on a network written as `192.168.1.0/24`, on paper, and then confirm it in Python with `ipaddress.ip_network("192.168.1.0/24").num_addresses`. Explain the `/24` in one sentence.
- The first three bytes of a MAC address identify the manufacturer of the network hardware. Look yours up in any public OUI lookup and see whose chip is in your laptop.
- Run `traceroute` to a site you know is on another continent and to a site hosted near you. Compare the hop counts and the times. Then estimate the floor: light in a fibre travels about 200 kilometres every millisecond, so work out roughly how long the round trip has to take for the distance alone, and compare that to what `traceroute` actually reported. Write two sentences on how much of the difference is distance and how much is everything the routers add on top.
