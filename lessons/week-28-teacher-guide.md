# Week 28 Teacher Guide

## 1. Header

- **Week:** 28 of 32
- **Unit:** 6, The Future of Computing
- **Theme question:** Who is trying to get in, and what is actually stopping them?
- **Session length:** 2 hours

## 2. Learning objectives

By the end of the session, each student can:

- Encrypt and decrypt a message with a Caesar cipher using a wheel, crack an intercepted one, and say why the cipher is weak.
- Explain, using the paint demonstration, how two people can agree on a shared secret while an eavesdropper watches everything they send.
- Distinguish a hash from encryption, and explain why a website should store hashes of passwords rather than the passwords.
- Explain what multi-factor authentication adds, in terms of "something you know, have, or are."
- Explain what a certificate proves when the browser shows a padlock, and what it does not prove.
- Detect a single flipped bit in a parity grid and explain how the same idea underlies checksums and error detection.
- Trace the classroom's own defenses from the internet down to the user, name what each layer stops and what it misses, and explain defense in depth.
- Recognize phishing tells, and describe SQL injection and cross-site scripting at a concept level as the same underlying mistake.

## 3. Where this sits

This is the week where the course's own infrastructure becomes the lab. Every layer traced in Segment 7 is a layer the instructor actually built: the router from Week 19, the DNS filtering from the laptop configuration checklist, the OS permissions from Week 17, the HTTPS and TLS from Week 20. Nothing here is hypothetical, which is what makes the trace land.

Cryptography arrives unplugged first, per the physical-first pattern, and the three activities are sequenced deliberately: Caesar establishes the idea of a key and shows that a small key space fails, paint mixing shows how to agree on a key in the open, and parity shows the separate idea of detecting change. The Python hashing demo sits between the second and third because a hash is the bridge from secrecy to integrity.

Week 27 unlocked AI as a coding tool. Week 28 quietly earns some of that back by showing students the difference between something that ran and something that is correct, in a domain where the difference is expensive.

## 4. Materials and setup

- Printed cipher wheels, two paper circles per student (one about 10 cm across, one about 8 cm) with the alphabet already printed evenly around each edge, plus one brad pin per student. Printing these beats drawing them; hand-marking 26 even divisions eats fifteen minutes of class.
- Printed intercepted-message cards for the cracking round, one per pair, all encrypted with the same unknown shift. Include an English letter-frequency strip on the card.
- Paint or colored materials for the key exchange. Cheapest reliable version: three colors of translucent plastic chips or three colors of water in clear cups with food coloring. Colored paper squares that can be stacked also work.
- Two manila folders as privacy screens for the key exchange.
- Two-color cards for parity: 40 or so cards, black on one side and white on the other. Playing cards face up and face down work perfectly and cost nothing.
- Each student's laptop with VS Code and Python; projector.
- The classroom network hardware powered on and reachable: router, switch, class server.
- Instructor access to the router admin page and the NextDNS dashboard, already logged in on the demo machine before class.
- Whiteboard with the theme question written large, and space for the defense-in-depth stack, which stays up all session.
- Printed Week 28 homework handout, one per student.

## 5. Pre-class prep checklist

- Print and assemble one cipher wheel yourself, so you know how long it takes and can demonstrate with a finished one. Print the class set and count out brad pins. (20 min)
- Write your intercepted message, encrypt it by hand at a shift you choose, and print the cards. Make the message at least four sentences; short messages are hard to crack by frequency and the point of the round is that it can be done. (15 min)
- Rehearse the paint-mixing exchange once with the actual materials. Confirm that Alice's and Bob's final mixtures visibly match. If they do not, your color choices are wrong; yellow public with red and blue secrets is reliable. (15 min)
- **Rehearse Parity Magic at least twice, alone, until you can find the flipped card in under ten seconds.** This is a performance and it fails if you are visibly counting. Practice adding the parity row and column quickly too. (15 min)
- Set up the network trace: log in to the router admin page and the NextDNS dashboard on the demo machine, and pick a test domain that your filter definitively blocks so the `nslookup` demonstration works on the first try. Check it works today, not last month. (20 min)
- **Decide now how you will show the NextDNS query log, and set it up before class rather than in front of the room.** Either filter the dashboard view to the instructor's own device and leave it filtered, or take a sanitised screenshot during prep and show that instead. A room-wide log is other people's real browsing and it does not go on the projector. Segment 7, step 3 has the wording for the rule you state before the dashboard opens. (10 min)
- Run the hashing script from Segment 4 once. (5 min)
- Print homework handouts, cipher wheels, and intercepted-message cards. (10 min)

## 6. Minute-by-minute class flow

### Segment 1: Warm-up (0:00 to 0:08)

- **You do:** Collect the project proposals from last week. Do not let this slide; they are the input to Week 31.
- **You do:** Pose the theme question. Ask the class to name everything between a hostile stranger on the internet and the file on their laptop. Write the list on the board in whatever order it comes out. You will reorder it into the real stack in Segment 7.

### Segment 2: Caesar cipher, unplugged (0:08 to 0:30)

Run entirely from these steps; the canonical source is in Section 13 for prep.

1. **Assemble the wheels.** Hand out the two printed circles and a brad pin per student. Push the pin through both centers, small circle on top, and open the tabs. The inner circle must spin freely.
2. **Define the key.** Rotate the inner wheel so its A sits under the outer D. Say plainly: that is a shift of 3, and 3 is the key. Write on the board: outer ring is plaintext, inner ring is ciphertext.
3. **Encrypt together, one word.** Take the word `HELLO`. Find H on the outer ring, read the letter under it on the inner ring, write it down. Do all five letters as a class so everyone's wheel is oriented the same way. Check that the whole room got the same answer before moving on; a student whose rings are reversed will get the wrong answer all segment.
4. **Decrypt.** Give the class a short encrypted word at shift 3 and have them reverse the lookup: find it on the inner ring, read the outer.
5. **Pairs exchange.** Each pair agrees on a shift between 1 and 25, writes a one-sentence message, encrypts it, and hands the ciphertext to another pair along with the key. That pair decrypts it. Two minutes each way.
6. **Now take the key away.** Hand each pair an intercepted-message card, all encrypted with the same shift, which you do not tell them. Give them five minutes to read it.
7. **Let them find the two attacks themselves.** Some pairs will brute force: try shift 1, then 2, and so on. Ask how many they would have to try at worst. The answer is 25, which is nothing. Other pairs will use the frequency strip: the most common ciphertext letter is probably E, and the shift falls out of that in one step.
8. **Land three ideas.** First, the key space is the whole security here, and a key space of 25 is not security. Second, frequency analysis works because the cipher does not hide the structure of the language. Third, and most important, state Kerckhoffs's principle: a good system stays secure even when the enemy knows exactly how it works, because only the key is secret. Ask what that means for keeping an encryption algorithm secret. It means it is a bad plan, and it is why real algorithms are published.

### Segment 3: Paint-mixing key exchange, unplugged (0:30 to 0:45)

The counterintuitive one. Run it as a demonstration with two volunteers and the class as the eavesdropper.

1. **Set the stage.** Alice at one side of the room, Bob at the other, and every other student is Eve, who can see and hear everything that crosses the room but cannot see inside the folders. Say the goal out loud before starting: Alice and Bob will end up holding the same secret color, and Eve will not be able to make it, even though Eve watched the entire thing.
2. **Agree on a public color, in the open.** Announce it to the room: yellow. Give Alice and Bob each a cup of yellow. Eve gets a cup of yellow too, because it is public.
3. **Each picks a private color, behind a folder.** Alice takes red, Bob takes blue, neither announces it, and neither shows the other. Emphasize that these never leave the folder for the rest of the demonstration.
4. **Each mixes public plus private, behind the folder.** Alice makes yellow plus red, which is orange. Bob makes yellow plus blue, which is green.
5. **They swap the mixtures in the open.** Alice walks her orange across the room to Bob; Bob walks his green to Alice. Hold both up so the whole room clearly sees them. Eve now knows yellow, orange, and green.
6. **Each adds their own private color to what they received, behind the folder.** Alice adds red to the green she received. Bob adds blue to the orange he received. Both now have yellow plus red plus blue.
7. **Hold both final cups up side by side.** They match. Alice and Bob now share a color neither of them sent across the room.
8. **Now put Eve to work.** Ask the class to make the same final color from what they saw: yellow, orange, green. They will try mixing orange and green, which gives the wrong result because it contains two doses of yellow. To do it properly Eve would have to separate the red back out of the orange, and unmixing paint is the hard part.
9. **Name it and generalize.** This is the Diffie-Hellman key exchange. The real version uses modular arithmetic instead of paint, where the easy direction is raising a number to a power and taking a remainder, and the hard direction, recovering the exponent, has no fast method known. Say the general principle: all of public-key cryptography rests on operations that are easy one way and impractically hard to reverse.
10. **Draw the distinction students will otherwise blur.** Key exchange agrees on a shared secret. A public and private key pair is a related but different tool: anyone can encrypt with your public key, only you can decrypt with your private key, and you can sign with your private key so anyone can verify it was you. Write both on the board.
11. **Finish with certificates, ninety seconds.** A certificate is a signed statement from an authority the browser already trusts, saying "this public key belongs to this domain name." That is what the padlock checks. Then say what it does not prove: not that the site is honest, not that the company is real, only that you are talking to whoever controls that domain and that nobody is reading it in transit. Phishing sites have valid certificates all the time.

### Segment 4: Hashing and passwords (0:45 to 1:05), Coding strand

1. **Ask the question first.** When you type your password into a website, what should the website store? Take answers. Most students say it stores the password. Ask what happens when that database leaks.
2. **Live-code it.** Students type this into `hashing.py`:

   ```python
   import hashlib

   def sha256(text):
       return hashlib.sha256(text.encode()).hexdigest()

   print(sha256("password"))
   print(sha256("Password"))
   print(sha256("password "))
   ```

3. **Read the output.** Three hashes, all 64 hex characters, all completely different despite the inputs differing by one character. Name that: the avalanche effect. Then note the fixed length no matter the input, and have a student hash a whole paragraph to prove it.
4. **State the three properties on the board.** Same input always gives the same output. You cannot work backwards from the output to the input. It is impractical to find two inputs with the same output.
5. **Make the distinction explicit.** Encryption is reversible with a key; that is the whole point of it. Hashing is not reversible at all, and that is the whole point of it. Students conflate these constantly.
6. **Now show why hashing alone is not enough.** Students add this:

   ```python
   common = ["123456", "password", "qwerty", "letmein", "dragon"]
   stolen = sha256("letmein")

   for guess in common:
       if sha256(guess) == stolen:
           print("cracked:", guess)
   ```

   It cracks instantly. Ask why, given that hashes cannot be reversed. The answer is that the attacker never reversed anything; they hashed guesses until one matched. Scale that to a list of ten million common passwords and it still takes seconds.
7. **Introduce salt as the fix.** The site stores a random value per user and hashes the password with it, so identical passwords produce different hashes and one precomputed table cannot crack the whole database at once. Have them add a salt to the script and watch the crack fail.

   ```python
   salt = "x7Qp2"
   stolen = sha256(salt + "letmein")
   ```

8. **Close with the practical layer, five minutes.** Password length beats password complexity, because attack cost grows with length far faster than with adding a punctuation mark. Reusing a password means one breached site breaks every other account. A password manager exists precisely so that unique long passwords are possible for a human, and Bitwarden is on their laptops already. Then MFA in one framing: something you know, something you have, something you are. MFA means a stolen password alone is not enough. Note that SMS codes are the weakest common second factor because phone numbers can be taken over, and an app or a hardware key is stronger.

### Segment 5: Stretch (1:05 to 1:10)

### Segment 6: Parity Magic, unplugged (1:10 to 1:24)

This is a performance. It only lands if you can find the flipped card fast, so rehearse it during prep.

1. **Lay a 5 by 5 grid** of two-color cards on a table where the class can gather, mixed randomly between the two colors. Do not explain anything yet.
2. **Say you are going to make it magic,** then add a sixth column. For each row, add one card so that the number of black cards **in that row** is even. Do it row by row, out loud but quickly, without labeling what you are doing as a rule.
3. **Add a sixth row.** For each column, add one card so that the number of black cards **in that column** is even. Work left to right.
4. **The corner card.** The last card, at the intersection of the new row and the new column, has to make both its row and its column even. It always can. That is not luck and it is worth mentioning once at the end; the total number of black cards in the original grid is either even or odd, and both the new row and the new column are correcting for the same total.
5. **Turn your back.** Ask one student to flip exactly one card, anywhere in the whole 6 by 6 grid, quietly.
6. **Turn around and find it.** Scan the rows for the one row with an odd number of black cards, then the columns for the one column with an odd number. The flipped card is at their intersection. Point at it. Do not explain yet.
7. **Do it again,** with a different student flipping. The room will start staring at the extra row and column, which is where you want them.
8. **Now hand it over.** Ask a student to be the magician while you flip a card. Then get every pair building their own 4 by 4 grid with parity row and column, and taking turns.
9. **Explain and name it.** The extra row and column are parity bits. Any single change breaks exactly one row rule and exactly one column rule, and two broken lines pin down one square. Write the general statement: adding redundant information lets you detect, and sometimes locate, a change you did not see happen.
10. **Push on the limits, which is the real lesson.** Ask what happens if two cards flip. Sometimes you detect it, sometimes the two errors cancel in a way that leaves both rules satisfied, and you cannot locate two errors even when you detect them. Then say where this actually lives: checksums on downloaded files, error-correcting codes in RAM and on disks, CRCs in every network packet from Week 20, and the redundancy that lets a scratched QR code still scan.
11. **Connect it back to hashing in one line.** A hash is the industrial-strength version of the same instinct: a short value derived from data that changes if the data changes. Parity detects accidents. A cryptographic hash detects deliberate tampering.

### Segment 7: The classroom network trace, defense in depth (1:24 to 1:47), Systems strand

The lab. Everything here is the actual classroom, which is the point.

1. **Build the stack on the board, top to bottom,** taking the list from Segment 1 and putting it in order. Leave room to write beside each box.

   ```text
   The internet
   ISP modem
   Router: NAT and firewall
   NextDNS filter
   Switch
   Laptop OS: firewall, standard account, Gatekeeper, FileVault
   Browser: HTTPS, sandbox, SafeSearch
   The user
   ```

2. **Walk it downward, asking three questions at every box** and writing the answers next to it: what does this layer stop, what does it not stop, and what happens if it fails silently?
3. **Demonstrate the DNS filter, and state the query-log rule before the dashboard is open, not after.** On the demo machine, run `nslookup` against a site you know your filter blocks, and then against one it allows. Show the two different answers. Then stop, before you open anything else, and say the rule out loud: the query log records what every person in this room actually looked at, so the class sees only the instructor's own device, or a screenshot you sanitised during prep. Nobody else's browsing goes on the wall and no student gets named. Only then open the dashboard, with the device filter already set to your own machine, or show the prepared screenshot instead. One device is enough for the lesson to land, because the point is not what anyone looked at, it is that the log exists, that it is far more detailed than students expect, and that a person can sit down and read it. Close by asking who else keeps a log like this one. That question, not the raw list, is the moment of the session.
4. **Demonstrate the router.** Open the router admin page and show the firewall settings and the NAT table. Point out that inbound connections have nowhere to go by default because the devices behind NAT have no public address, and connect it straight back to Week 19.
5. **Demonstrate the OS layer.** Show the macOS firewall in System Settings. Then try to install something from the standard student account and let the admin prompt appear. Ask what that prompt is actually protecting against, and get to the answer: it is not protecting from them, it is protecting from software that arrives without them intending it.
6. **Demonstrate the browser layer.** Click the padlock on any HTTPS site and open the certificate. Walk the chain from the site up to the root authority. Connect back to Segment 3: this is the signed statement, and this is the authority the browser trusts.
7. **Run the kill-a-layer exercise.** Assign each pair one box in the stack. Their job, in three minutes: describe one specific bad thing that now gets through because their layer is gone, and one bad thing that still does not get through because the other layers held. Take answers going down the stack.
8. **Land defense in depth in one sentence,** ideally taken from something a student said: no layer is sufficient, every layer will eventually fail, and the design assumes that.
9. **Then name the layer with no technical control.** Point at the bottom box, the user. Ask which layer all the others depend on, and let them get there.

### Segment 8: Attacks on people and on programs (1:47 to 1:57)

1. **Phishing, with real examples.** Show two or three real phishing emails, ideally from your own spam folder with identifying details removed. Have the class find the tells rather than telling them: the sender's actual domain rather than the display name, the urgency, the link text that does not match the link target (hover to show it), the slightly wrong logo, the request that bypasses a normal process. Say the honest thing: good phishing has none of these, and the reliable defense is the habit of never acting on a link in a message, but navigating to the site yourself.
2. **Malware in three categories, thirty seconds each.** Ransomware encrypts your files and sells you the key, which is a chilling use of everything from Segment 3. Spyware and keyloggers watch. Worms spread on their own. Then the honest note on how it usually gets in: the user runs it, which is why Gatekeeper and the admin prompt are in the stack.
3. **SQL injection, conceptually, at the board.** Write a login query built by gluing strings together:

   ```text
   SELECT * FROM users WHERE name = '<what the user typed>'
   ```

   Then show what happens when the user types `' OR '1'='1`. Read the resulting line out loud and let the class see that the user's text became part of the command. Name the underlying mistake: data was handed to a system that treats it as instructions.
4. **Cross-site scripting, as the same mistake in a different place.** A user types `<script>...</script>` into a comment box, the site stores it, and every later visitor's browser executes it because the browser cannot tell the difference between the site's code and the attacker's text.
5. **Give the one-sentence unifying idea, which is worth more than the details.** Both attacks are the same failure: mixing untrusted input with trusted instructions. The fix in both cases is to keep them separate, by using parameterized queries and by escaping output, rather than by trying to guess which inputs are bad.

### Segment 9: Wrap (1:57 to 2:00)

- **You do:** Point at the stack on the board and note that they built or configured or traced almost every box of it during this course. Hand out homework, noting the Extra Credit AP Track section. Exit question at the door: what does the padlock prove, and what does it not prove?

## 7. Key scripts and analogies

- **Kerckhoffs's principle:** "A good lock is still a good lock when the burglar has the blueprints. If your security depends on nobody knowing how it works, you do not have security, you have a secret that will eventually get out."
- **Key space:** "Twenty-five possible keys is not a lock, it is a suggestion. Modern keys have more possibilities than there are atoms in what you can see."
- **Key exchange:** "They both end up holding the same paint. Everything that crossed the room was seen by everyone, and nobody watching can mix it. Mixing is easy, unmixing is not, and that gap is the whole of cryptography."
- **Hashing versus encryption:** "Encryption is a locked box; the point is getting the thing back out. A hash is a blender; the point is that you cannot."
- **Why hashes still get cracked:** "Nobody reverses the hash. They guess a password, blend it, and see if the smoothie matches. Computers guess very fast."
- **Password length:** "Every character you add multiplies the attacker's work. Swapping an o for a zero does not; that trick is in every cracking list already."
- **MFA:** "Something you know, something you have, something you are. Two of the three means a stolen password on its own is a dead end."
- **What the padlock means:** "It says nobody is listening on the way, and you reached the domain in the address bar. It says nothing at all about whether the people who own that domain are honest."
- **Parity:** "Add one card that is not information, only a rule. Now any single change breaks the rule, and you can see something happened without having watched it happen."
- **Defense in depth:** "No single wall. A dozen thin walls, each of which will eventually fail, arranged so that the ones still standing cover for the one that fell."
- **SQL injection and XSS:** "You handed someone a form to fill in and they wrote instructions in it, and your program did as it was told. The bug is not the attacker's creativity, it is that you let data and commands share a sentence."

## 8. Differentiation

- **Younger or newer students:** Section 11 notes that the encryption content is already conceptual and needs no alternate. Keep it that way: no modular arithmetic on the board. In the cipher-cracking round, hand them the letter-frequency strip and point at the first step. In the hashing segment, running the supplied script and describing what changed is a full outcome; the salting extension is optional. In parity, they should be the magician at least once; being able to perform it is the understanding.
- **Extensions for advanced or AP-track students:** Have them work the actual Diffie-Hellman arithmetic with small numbers, using a public base and modulus and their own secret exponents, and confirm both sides land on the same value. Have them implement a Caesar cipher and a brute-force cracker in Python. Point them at the picoCTF beginner challenges from the Section 9 cybersecurity extra-credit track, noting that picoCTF now sits under CyLab Security Academy. Have them add a per-user random salt properly, using `secrets.token_hex`, and explain why `random` would be the wrong module.

## 9. Common pitfalls

- **Cipher wheels eat the clock.** Print them with the letters already on. Hand-drawing 26 even divisions is a fifteen-minute detour into geometry.
- **Reversed cipher wheels.** Half the room encrypts with the inner ring as plaintext and gets consistent, wrong answers. Check the whole room after step 3 of Segment 2, not at the end.
- **The paint exchange fails visibly.** If Alice's and Bob's finals do not obviously match, the demonstration teaches the opposite of the intended lesson. Rehearse with the real materials and use yellow public with red and blue secrets.
- **Students conclude paint mixing is how HTTPS works.** It is an analogy for one step. Say so, and be clear that the real thing is arithmetic and that certificates solve a different problem, namely who you are talking to.
- **Parity performed badly.** If you count slowly and squint, it is a math exercise instead of a trick, and the room disengages. Rehearse it.
- **The parity corner card confuses someone.** It always works. If a student challenges it, that is a good student; give them the even-or-odd argument in step 4 and move on rather than proving it at the board.
- **The DNS block demonstration does not block.** Filter lists change and caches lie. Verify your test domain the morning of class, and have a second one ready.
- **Showing the NextDNS query log gets personal.** It logs real student browsing. The constraint is in Segment 7, step 3 and in the prep checklist because it has to be set before the dashboard opens, not remembered afterwards: instructor device only, or a sanitised screenshot, and the rule said out loud first. The transparency is valuable; the ambush is not, and an unfiltered log on a projector is an ambush even when nothing embarrassing turns up.
- **Live phishing links.** Never click one in class, even to demonstrate. Hover to show the target, and take a screenshot beforehand if you want the destination visible.
- **SQL injection turns into a how-to.** Keep it at the board, on a fictional query, and pivot immediately to the fix. If a student asks whether they can try it on a real site, the answer is no, and it is a good moment to say plainly that unauthorized access is a crime regardless of intent or of how easy it was.

## 10. Homework

Full details in `handouts/week-28-homework.md`. In summary: crack a second intercepted message and explain the method; a written walk of the defense-in-depth stack for their own home network; a short hashing exercise in Python; an audit of their own password habits with a parent; and continued final-project work. The handout closes with an Extra Credit AP Track section carrying this week's AP slice and the Create Task reminder.

## 11. Assessment

Observational across the four activities, plus the written homework trace.

The three checks worth making by walking the room: can the student decrypt without being told the method again, can they state what the padlock does not prove, and can they find the flipped parity card themselves. Those three cover the substance of the day.

The homework's home-network trace is the graded artifact. Score it against the weekly-labs rubric. What you are looking for is not completeness of the list but whether the student can say what a layer misses, because "this layer stops everything" is the misconception that makes the whole framing useless.

Also note who is now behind on the final project. Week 28 is the last comfortable week to correct scope.

## 12. AP alignment

This session directly covers AP CSP topic **5.6 Safe Computing**, which is the cleanest single-topic match in Unit 6. It also reinforces **4.1 The Internet**, since certificates, DNS, and NAT are all revisits of Week 19 through Week 21 from the security angle, and it touches **5.5 Legal and Ethical Concerns** through the privacy side of filtering and logging.

For the exam specifically, 5.6 expects students to know: what personally identifiable information is and why it is worth protecting, that encryption can be symmetric or public-key, that a certificate authority issues digital certificates, what multi-factor authentication is, and what phishing, keylogging, rogue access points, and malware are. Every one of those was covered today; say so, because it is unusual for a single session to map this cleanly.

**AP-track self-study for this week, and only this week's slice.** One matching slice below, not the whole course, and extra credit rather than required work:

- **Project STEM (the AP spine):** Unit 6, Innovative Technologies, and specifically its cybersecurity and safe-computing lessons. Work only that portion; the impact and ethics material in the same unit belongs with Week 30. Verify this unit numbering against the live course when you enroll; see the provider unit reference in the README.
- **CodeAI, formerly Code.org (verified free alternative):** Unit 8, Cybersecurity and Global Impacts, at `https://studio.code.org/courses/csp-2025/units/8`. Do the cybersecurity lessons and stop there. The global-impacts half of the same unit is Week 30's slice, so students should not burn it now.

Nothing here is required of non-AP students.

## 13. Resources used this week

- Caesar cipher and the paint-mixing key exchange: Segments 2 and 3 are complete on their own. The canonical activities are CS Unplugged's Cryptographic Protocols and Public Key Encryption, from the activities index at `https://classic.csunplugged.org/activities/`. For your own prep on the real mathematics of key exchange, Computerphile's Diffie-Hellman explainer is the clearest short treatment; search for it on YouTube.
- Parity Magic: Segment 6 is complete, but **rehearse it from the canonical source if you have never performed it**, because the patter matters more than the rule. CS Unplugged Error Detection, `https://classic.csunplugged.org/activities/error-detection/` and `https://www.csunplugged.org/en/topics/error-detection-and-correction/`. The site has a demonstration video.
- Full activity descriptions and the canonical link list: `teaching-activities/Unplugged-Logic-Activities.md`.
- Python `hashlib`, for your reference: `https://docs.python.org/3/library/hashlib.html`. Note for the extension: use `secrets` rather than `random` for anything security-related, at `https://docs.python.org/3/library/secrets.html`.
- The classroom stack being traced in Segment 7 is documented in Section 8 of `curriculum/CS-Curriculum-and-Setup.md`, including the NextDNS configuration and the standard-versus-admin account design. Section 8 also contains the "teaching tie-in" note that this segment fulfills.
- NextDNS dashboard and your router's admin page: your own credentials. Log in before class rather than in front of the room.
- picoCTF, for the cybersecurity extra-credit track: `https://picoctf.org`. It has joined Carnegie Mellon's CyLab Security Academy at `https://cylabacademy.org`; existing accounts carry over. Verify the current state of that transition before pointing students at it.
- Crash Course Computer Science, Episodes 31 ("Cybersecurity"), 32 ("Hackers and Cyber Attacks"), and 33 ("Cryptography"), optional homework viewing. Episode 33 is the one that matches Segments 2 through 4 directly, and these three are this course's only assignment of them. Series playlist: `https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo`
- CodeAI CSP Unit 8, Cybersecurity and Global Impacts (AP-track reinforcement): `https://studio.code.org/courses/csp-2025/units/8`
