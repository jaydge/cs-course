# High School Computer Science: Course Plan, Lab, and Setup

A 32-week course built around one question: **how does a button press become something useful?** Students leave with a systems-level mental model from transistors to cloud AI, plus real, sustained programming practice.

This document contains:

1. Design principles and what changed from the draft
2. Credit and standards alignment (AP CS Principles)
3. Assessment and grading
4. The weekly two-strand structure
5. Full 32-week curriculum
6. Recommended backbone resources and tools
7. Lab equipment list
8. Student laptop configuration checklist (Windows golden image)
9. Extra credit project tracks
10. Course policy on AI use
11. Adjustments for younger students (8th to 11th grade)
12. Software platforms and accounts

---

## 1. Design principles

- **Coding never stops.** Every week has a Coding strand running parallel to the Systems strand. Programming is the through-line, not a phase.
- **Depth over coverage.** A small number of core skills taught deeply; everything else is a single "guided tour" lesson that builds a mental model, not mastery.
- **Build the stack.** The course repeatedly produces tangible artifacts, each becoming input to the next, ending with a full button-press-to-pixels trace and a final project.
- **Open the black boxes.** Every student should leave able to say "I know what is inside the computer, the OS, the internet, the app, and the model."

**Class-time target:** 60% hands-on building and programming, 15% demos and labs, 15% discussion and diagrams, 10% quizzes, review, and presentations.

### What changed from the draft

| Area | Draft | This version |
|---|---|---|
| Credit defensibility | Not addressed | Mapped to AP CSP Big Ideas; grading and checkpoints added |
| Coding cadence | Front-loaded, then thins out | Continuous Coding strand every week |
| Hardware-to-language arc | Improvise it | nand2tetris and Turing Complete |
| Beginner IDE | VS Code from day one | Thonny first, VS Code from Unit 5 |
| Programming emphasis | Breadth and depth balanced | Depth prioritized; systems breadth trimmed |
| AP backbone | Aligned in spirit only | Code.org CSP supplies concepts, pseudocode, and Create Task scaffolds |
| Teacher workload | 32 weeks from scratch | Code.org CSP and Crash Course CS as free backbones |
| Scope creep | Many one-off topics | Rust/Haskell/Lisp/C++ as mentions; blockchain and distributed merged; GraphQL, WebSockets, Paxos cut |

---

## 2. Credit and standards alignment

Anchor the course to **AP Computer Science Principles (AP CSP)**. You do not have to administer the exam to benefit; the framework gives the credit a recognized backbone for transcripts and college admissions and maps cleanly onto the units. If students do sit the exam, the course is already most of the way there.

| AP CSP Big Idea | Covered in |
|---|---|
| Creative Development | Units 1, 5 (programming, software engineering, projects) |
| Data | Units 1, 3, 6 (binary, compression, data structures, embeddings, databases) |
| Algorithms and Programming | Units 1, 3 (the programming core) |
| Computing Systems and Networks | Units 2, 4 (hardware, OS, networking) |
| Impact of Computing | Unit 6 and the recurring ethics and "how it works" threads |

### What is left to fully align with the exam

The exam has two scored parts: a fully digital end-of-course exam (Bluebook app: multiple choice plus two written responses) and the through-course Create Performance Task. Your content covers the Big Ideas, so the specific gaps to close are:

1. **The Create Performance Task (required, 30% of the AP score).** Students build a program of their choice, record a video of it running, and write a Personalized Project Reference (screen captures of one list and one procedure), submitted via the AP Digital Portfolio by the late-April deadline. They get 9 hours of in-class time. It is language-agnostic, so students do it in Python. Treat the final project as this task; start it in February and protect the 9 hours.
2. **AP pseudocode fluency.** The multiple-choice section uses College Board pseudocode, not a real language. Add a few sessions reading and tracing it. It is a thin layer over Python (same concepts, different syntax). Code.org's lessons drill this directly.
3. **Explicit data topics.** Data representation is roughly 17 to 22% of multiple-choice questions and leans on compression (lossy vs lossless), metadata, and extracting information from data. Compression is now back in Unit 1, Week 2; use Code.org's Data unit here.

### Homeschool exam logistics

- Homeschoolers can take any AP exam without enrolling in an official AP course.
- You cannot register directly with College Board. Use the AP Course Ledger to find a local public or private school that administers AP, then call and ask the AP coordinator if they accept outside homeschool testers this year.
- For AP CSP specifically, the coordinator must create an "exam only" section and give your students a join code so they can submit the performance task through the AP Digital Portfolio.
- School ordering deadline is mid-November. Homeschoolers can be added later (through mid-March) without a late fee at the coordinator's request, but call in September or October because individual schools set earlier internal cutoffs.
- Fee is roughly $98 to $101 per exam. Use homeschool code 970000 on exam day. Verify current fees and dates before each cycle.

### College credit reality

Passing the exam and earning college credit are separate. College Board scores 1 to 5; each college decides independently whether and how a score counts. Some grant credit at 3, others require 4 or 5, and many give only elective credit. Selective schools often grant little or none. Check the specific AP-credit policy of the colleges your students target. AP CSP generally earns less credit than AP CSA (the Java-based Computer Science A exam), which colleges credit more reliably toward a CS major. Given the programming-depth priority, CSA is a sensible year-two target for an ambitious student, while CSP remains the right first exam here.

### Audited AP option

If you want an audited "AP Computer Science Principles" transcript available to students, adopt Project STEM's endorsed syllabus for the AP Course Audit and run it as an opt-in layer underneath this course. Your course still drives; Project STEM is the adopted resource and the document the audit sees. The AP track is per-student and exam-free for anyone not pursuing it, so younger students are never under exam pressure. See the companion AP Layer: Project STEM Overlay guide for the audit steps and the unit mapping.

### Seat-time note

2 hours x 32 weeks is 64 class hours, realistically 50 to 55 instructional. A traditional full credit assumes roughly 120 hours. For SC homeschool, credit is generally competency-based and awarded by the teaching parent, so this is defensible. To make a full credit clean:

- Count lab time, required homework, and project hours toward the total (this clears 120 easily with the capstone and projects).
- Keep a portfolio of student work (GitHub repos, lab artifacts, the final project or Create Task) as mastery evidence.

---

## 3. Assessment and grading

Project-and-portfolio based, not exam-heavy. Suggested weighting (tune to taste):

| Component | Weight | Notes |
|---|---|---|
| Weekly labs and in-class builds | 40% | Completion plus a simple "works / partly / not yet" rubric |
| Unit checkpoints | 20% | Short concept quiz plus one build per unit (6 total) |
| Two milestone assessments | 15% | Mid-year "trace the button press" (oral or written) and an end-of-Unit-4 systems concept check |
| Final project / AP Create Task | 20% | Student-chosen program; for AP-track students this doubles as the Create Performance Task, done in Python |
| Participation and discussion | 5% | Wow-day engagement, code reviews, helping peers |

Extra credit tracks add on top and never penalize students who do not pursue them.

**Rubric shorthand for labs** (keeps grading fast):

- 4 = works and student can explain why
- 3 = works
- 2 = partly works or works with help
- 1 = attempted
- 0 = not submitted

**Two anchor assessments worth building carefully:**

- **Mid-year (end of Unit 4): "Trace the button press."** Student walks the full path: input device, USB, OS, application, language, machine code, CPU, memory, network card, TCP/IP, internet, server, database, response, browser, GPU, display, pixels, eyes. This is the single best measure of whether the systems model landed.
- **Final project demo.** Proposal, working artifact, five-minute demo, and a one-page writeup explaining the layers it touches.

---

## 4. Weekly two-strand structure

Each 2-hour week runs two strands so coding never pauses:

- **Systems strand (about 60 to 75 min):** the narrative topic for that week (hardware, OS, networking, etc.), heavy on demos, the lab hardware, and diagrams.
- **Coding strand (about 45 to 60 min):** continuous Python skill-building that progresses independently of the systems topic, plus the week's small build.

Every 2 to 3 weeks, spend 15 minutes of the Systems strand on a **"Mystery Day"** wow question.

Also run an **unplugged activity** at the launch of each major concept (roughly one every 2 to 3 weeks, 20 to 45 minutes): an offline, physical logic game done before the on-screen version. These need no computer fluency, so they work from Day 1 while students are still learning the laptop, and they level naturally across the age range. See the companion Unplugged Logic Activities guide, which maps each activity to the week it reinforces.

---

## 5. Full 32-week curriculum

**Programming-depth rebalance.** This version favors programming depth over systems breadth. The Coding strand gets the majority of every week; the Unit 3 programming core is the center of gravity; and the Unit 6 breadth topics (cloud, distributed systems, blockchain) are compressed into single guided tours to free time for sustained coding and the Create Task. If you want even more depth, pull another week from Unit 6 into Unit 3.

**No required pre-course prep.** There is no mandatory pre-course computer class. Week 1 opens with a brief computer-fluency intro of 2 to 4 hours (see the companion "Course Intro: Computer Basics" guide), and the rest of the fluency is taught just in time, at the moment the course first needs it: folders and saving when students save their first Python file, paths right before the terminal unit, and so on. Families who want a head start can use the optional take-home videos in that guide, but nothing is required. The intro is part of the 50 to 55 instructional hours, not on top of them; it consumes roughly the first one to two sessions, and the compressed Unit 6 leaves room to absorb it.

Notation per week: **Theme question** / Systems strand / Coding strand / Lab or build / Resource.

### Unit 1: Thinking Like a Computer Scientist (Weeks 1 to 5)
Goal: students learn how programmers think and start writing code immediately.

- **W1: "What is a computer?"** Open with the brief computer-fluency intro (Course Intro guide) since there is no pre-course prep; run the readiness diagnostic here. Then: history and computational thinking; boot the Apple IIe and type `10 PRINT "HELLO" / 20 GOTO 10 / RUN`. Coding: Thonny setup, variables, print, input. Build: a name-and-greeting program. Resource: Crash Course CS Ep. 1. (If the intro runs long, the Python ramp slides into W2; that is fine.)
- **W2: "Why only 1s and 0s?"** Binary, number systems, character encoding (ASCII, Unicode), compression (lossy vs lossless: ZIP, JPEG, MP3). Coding: integers, strings, arithmetic, type conversion. Build: a decimal-to-binary converter. Resource: Crash Course CS Ep. 4 to 5, plus Code.org Data unit (AP-tested material).
- **W3: "How do we tell a computer what to do?"** Algorithms and problem decomposition. Coding: conditionals and boolean logic. Build: a number-guessing game. 
- **W4:** Coding: loops (for, while); introduce the idea of a library by importing `random` (AP 3.14 Libraries). Build: a calculator and Rock Paper Scissors. Mystery Day: "Why do programming languages exist?"
- **W5:** Coding: functions and basic debugging. Build: Hangman. **Unit 1 checkpoint** (binary, basic Python).

### Unit 2: Inside the Computer (Weeks 6 to 10)
Goal: remove the mystery of hardware. Tier 2 guided tours; coding keeps progressing.

- **W6: "What is a transistor really?"** Electricity, transistors, logic gates, boolean algebra. Lab: build AND/OR/NOT gates on a breadboard with switches and LEDs. Coding: lists and indexing.
- **W7:** Flip-flops, registers, the ALU, building up to a CPU. Lab: Turing Complete or nandgame.com (build gates to adder in-game). Coding: list methods, iterating over lists.
- **W8:** CPU, clock speed, pipelines, cache, RAM, storage (SSD vs HDD), GPU. Lab: disassemble the old desktop PC; locate components on a dead motherboard. Coding: strings as sequences; simple text processing.
- **W9:** Motherboards, BIOS/UEFI, buses. "Which part actually thinks?" Lab: Raspberry Pi tour ("a whole computer on one board"). Coding: nested loops; a multiplication table and ASCII art.
- **W10: "What happens when you press a key?"** Follow the signal from key to screen. Show Python bytecode with the `dis` module to connect code to machine instructions. **Unit 2 checkpoint.**

### Unit 3: Programming Like a Professional (Weeks 11 to 16)
Goal: real programming muscle now that students know what the machine is. This is a Tier 1 core block; give it room.

- **W11:** Dictionaries; modeling real data. Build: a contact manager.
- **W12:** Objects and classes. Build: a simple inventory or pet/RPG class.
- **W13:** Data structures by hand (array, stack, queue, linked list conceptually). Build: a to-do stack and a print queue.
- **W14:** Searching and sorting; Big-O conceptually (why some programs are fast and others slow); a brief note that some problems cannot be solved by any algorithm (the halting problem, AP 3.18 Undecidable Problems). Lab: race linear vs binary search; visualize bubble vs built-in sort. 
- **W15:** Debugging and testing; reading tracebacks; writing simple tests. Build: Tic-Tac-Toe with a few tests.
- **W16:** Build week: a text adventure that uses dictionaries, functions, and a class. Short simulation exercise: model dice rolls or a random walk and count the outcomes (AP 3.16 Simulations, building on random values). **Unit 3 checkpoint.** Mystery Day: "Why does a computer get slower over time?"

### Unit 4: Operating Systems and the Internet (Weeks 17 to 21)
Goal: the course starts feeling "real." Transition students from Thonny to the terminal. Macs help here: macOS is Unix underneath, so the terminal (zsh), SSH, and standard Unix commands are already present with nothing to install. Windows students reach the same place through WSL2/Ubuntu.

- **W17:** Operating systems: processes, threads, memory, files, permissions. Lab: macOS Terminal and WSL/Ubuntu side by side; navigate the filesystem. Compare Finder to File Explorer to the same paths seen from the shell. Good moment for "Why are macOS, Windows, and Linux different?" (shared Unix ancestry vs Windows NT).
- **W18:** The shell. Lab: terminal-only challenges (create, move, search files; pipes; write a tiny shell script). Coding: run Python from the command line; file read/write.
- **W19:** Networking foundations: IP (v4/v6), MAC, DNS, DHCP, routers, switches, NAT. Lab: build the physical network with your switch and router; `ping`, `traceroute`.
- **W20:** TCP/UDP, HTTP/HTTPS, TLS. Lab: capture packets with Wireshark; watch a page load. Coding: serve a folder with Python `http.server`; write a minimal request with `requests`.
- **W21: "What happens when you open google.com?"** Trace it end to end. Lab: SSH into the MacBook class server; `git clone` from it. **Unit 4 checkpoint and mid-year "trace the button press" milestone.**

### Unit 5: Building Modern Software (Weeks 22 to 26)
Goal: connect everything into a working web app. Move to VS Code.

- **W22:** Software engineering, SDLC, Agile basics, technical debt. Coding: VS Code setup; Python project structure.
- **W23:** Git and version control. Lab: a collaborative Git project against the class server; branches, commits, code review.
- **W24:** Web fundamentals: HTML, CSS, JavaScript, the DOM, the rendering pipeline. Build: a personal page from scratch.
- **W25:** APIs and JSON. Build: a small Flask app that consumes a public API (weather or similar). Data lab: load a small dataset (CSV), extract information from it (filter, count, find a pattern, read its metadata), and show a simple summary or chart. This covers AP Data topics 2.3 (Extracting Information from Data) and 2.4 (Using Programs with Data).
- **W26:** **How mobile apps work** (high level, both platforms): native (Android/Kotlin, iOS/Swift), cross-platform (Flutter, React Native, .NET MAUI), and PWAs; app stores, permissions, sensors, GPS, push, offline storage, cloud sync. Discuss why companies pick each approach. Lab: convert their Flask/web app into a Progressive Web App. **Unit 5 checkpoint.**

### Unit 6: The Future of Computing (Weeks 27 to 32)
Goal: tour modern computing, then spend real time finishing a substantial program. Breadth is compressed here so depth lands in the project. AP-track students run the Create Performance Task across this window (started in February, submitted by the late-April deadline).

- **W27:** AI and ML tour: history, search, neural networks, embeddings, transformers (conceptual), LLMs, inference vs training, hallucinations. Lab: build a tiny perceptron in Python, or call an LLM API. Begin or continue Create Task work. This unit also includes the "using AI as a coding tool" session that unlocks AI-assisted work for non-exam projects (see Section 10).
- **W28:** Cybersecurity: passwords, hashing, MFA, encryption, public/private keys, certificates, phishing, malware, common web vulnerabilities (SQL injection, XSS) at a concept level. Lab: "How is our classroom network protected?" Trace internet to DNS filter to firewall to OS to browser to user; defense in depth.
- **W29:** Single combined tour: cloud and infrastructure (servers, data centers, virtualization, containers and Docker overview, serverless, object storage, CDNs) plus blockchain, consensus, and distributed systems (CAP theorem, replication, eventual consistency). One lesson, mental model only.
- **W30:** Ethics and society (AP Impact of Computing): privacy, surveillance, bias in AI, deepfakes, copyright and licensing, open source, the digital divide, crowdsourcing (AP 5.4), automation, responsible AI. Dedicated Create Task work time.
- **W31 to W32:** **Final project / Create Performance Task** build, demo, video, and writeup. Submit to the AP Digital Portfolio if testing. Mystery Day options: "How does Face ID work?", "How does Netflix stream 4K?", "How do multiplayer games stay in sync?"

### Recurring "Mystery Day" bank
Why restarting fixes things; how Wi-Fi and Bluetooth work; why a partly-covered QR code still scans; how Google Maps reroutes so fast; why deleted files can be recovered; how password managers work; how GPS works; why floating point gives 0.1 + 0.2 not equal to 0.3.

---

## 6. Recommended backbone resources and tools

Use these to cut prep time and raise quality.

| Resource | Use | Cost |
|---|---|---|
| [Code.org CS Principles](https://code.org/en-US/curriculum/computer-science-principles) | AP-aligned lessons, assessments, standards spine | Free |
| [AP CSP Exam Reference Sheet (College Board)](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf) | Official, authoritative pseudocode spec used on exam day; also discussed below | Free |
| [Crash Course Computer Science (40 eps)](https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo) | Tier 2 guided-tour video for hardware/OS/networking | Free |
| [Turing Complete (Steam)](https://store.steampowered.com/app/1444480/Turing_Complete/) | In-class NAND-to-CPU building, very engaging | Paid, low cost (about $20) |
| [nand2tetris.org](https://www.nand2tetris.org) and "The Elements of Computing Systems" | Ambitious students: full build-the-stack | Free course |
| [Harvard CS50](https://cs50.harvard.edu/x) and [CS50 AP](https://cs50.harvard.edu/ap) | Stretch material and problem sets | Free |
| [picoCTF](https://picoctf.org) | Cybersecurity capture-the-flag track | Free |
| [Wireshark](https://www.wireshark.org) | Networking labs | Free |

Two naming notes, verified August 2026 but worth re-checking before relying on them: Code.org now operates as CodeAI, and older `code.org/educate/csp` links redirect to the curriculum page linked above. picoCTF has joined Carnegie Mellon's CyLab Security Academy (`https://cylabacademy.org`); `picoctf.org` currently explains the transition, and existing picoCTF accounts carry over.

**On Code.org and Python.** Code.org CSP is AP-endorsed and supplies the conceptual lessons (Data, Internet, Impact of Computing), AP pseudocode practice, an assessment bank, and Create Task scaffolds. Its built-in programming uses App Lab (JavaScript-flavored), not Python. Because AP CSP is language-agnostic, use Code.org for concepts and AP prep while keeping Python (Thonny, then VS Code) as the language where programming depth is built. Students complete the Create Task in Python.

**Software stack for every machine (Mac or Windows):** Thonny (beginner Python IDE), VS Code (from Unit 5), Python, Git, GitHub Desktop, Node.js (later), the terminal (zsh on Mac, Windows Terminal on PC), a browser (Chrome and Firefox), Wireshark, Bitwarden. Verify current versions and pricing for paid items before purchase.

**Office and documents.** Mac students use Pages and Numbers (free, preinstalled, and every save is a Finder lesson). Google Docs and Drive serve as the shared, cross-platform layer for collaboration and submissions, introduced after file-system fundamentals are solid (see Section 12). Teach real files first, cloud second, or students never learn where a file actually lives. A useful moment later: a Google Doc is not a file on disk at all until it is exported as .docx or .pdf.

**Official AP CSP reference sheet:** `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`. This is the authoritative pseudocode spec students get on exam day. Do not recreate it. If AP-track students need help moving between Python and this pseudocode, build a short Python-to-pseudocode "bridge" sheet plus trace problems (the off-by-one risk: AP lists are 1-indexed, Python lists are 0-indexed).

---

## 7. Lab equipment list

The classroom is **Mac-primary with some Windows**. That mix is an asset, not a compromise: students see two real operating systems side by side all year, which makes the "why are these different?" lesson concrete rather than theoretical. Macs also give you a Unix terminal for free. The one thing Macs do not give you is hands-on hardware exposure (opening the case, swapping RAM, BIOS), and the disassembled PC lab covers that.

### Already on hand
- Instructor MacBook Pro (teaching machine)
- Spare MacBooks: one as the always-on class server, the others for student use
- Raspberry Pi (CanaKit, ~2023): IoT/embedded station
- Apple IIe with dot matrix printer and floppies: the "computing museum" and Day 1 demo
- Networking kit: gigabit switch, old Wi-Fi router, ethernet cables
- An old desktop PC to disassemble (easy to source cheaply)

### To acquire

| Item | Purpose | Approx. budget |
|---|---|---|
| Additional student laptops as needed | Prefer used MacBooks for consistency with the primary fleet; refurbished Windows 11 Pro (8 to 16 GB RAM, SSD, WSL2-capable) is the cheaper path and keeps the two-OS comparison alive | Mac used: varies; Windows refurb: $150 to $300 each |
| Dead/spare motherboard | "Show and tell": locate CPU socket, RAM slots, PCIe, SATA, M.2, BIOS chip, CMOS, VRMs | Free to low |
| Breadboard + logic kit (transistors, LEDs, resistors, switches, jumper wires) | Build real AND/OR/NOT gates in W6 | $20 to $40 |
| Multimeter (basic) | Demonstrate voltage/signal in the electricity lesson | $15 to $30 |
| USB-to-SATA adapter | Storage labs; read a bare drive | $10 to $20 |
| Antistatic wrist strap | Safe PC teardown | Under $10 |
| Recovery USB drives (one per laptop) | Imaging and recovery | $5 to $10 each |
| Optional: Arduino starter kit | Hardware extra-credit track | $25 to $40 |
| NextDNS subscription | DNS filtering across all devices | Low annual cost |

Verify current laptop pricing and NextDNS plan details at purchase time; these ranges are approximate.

### Station layout (the classroom as a small tech company)
- MacBook server: the "company server"
- Switch: the "office network"
- Router: the "internet gateway"
- Raspberry Pi: the "IoT device"
- Apple IIe: the "computing museum"
- Disassembled PC and motherboard: the "hardware lab"

---

## 8. Student laptop configuration checklist

The fleet is **Mac-primary with some Windows**. Build one machine of each type perfectly, then replicate. For 4 to 12 machines, scripted provisioning (below) beats disk imaging and doubles as a teaching artifact for the software-engineering unit.

The goal on both platforms is the same: a **standard, non-admin student account** with an **admin account only you hold**, security on, DNS filtering that follows the laptop home, and enough freedom left that students can still learn how a computer works.

### macOS setup (primary fleet)

**Core OS and accounts**
- [ ] macOS updated to a currently supported version; automatic updates on
- [ ] **Standard (non-admin)** student account for daily use
- [ ] Separate **administrator** account, password known only to you
- [ ] FileVault disk encryption on (optional, recommended)
- [ ] Firewall on (System Settings, Network, Firewall)
- [ ] Gatekeeper left at default (App Store and identified developers)
- [ ] Find My enabled for a school-owned device
- [ ] Consistent device name (e.g., CS-MAC-01) and a physical asset tag

**Developer environment**
- [ ] Xcode Command Line Tools (`xcode-select --install`), which provides git and the compiler toolchain
- [ ] Homebrew (the package manager; installs as admin, and this is a nice teaching moment about package managers)
- [ ] Thonny (beginner Python IDE)
- [ ] Python (latest stable via Homebrew, not the system Python)
- [ ] VS Code (from Unit 5)
- [ ] GitHub Desktop
- [ ] Node.js (can defer to Unit 5)
- [ ] Wireshark
- [ ] Terminal is already present; zsh is the default shell, nothing to install

**Productivity and security**
- [ ] Chrome and Firefox (Safari already present)
- [ ] Bitwarden (password manager)
- [ ] Pages and Numbers (already installed) for documents and spreadsheets
- [ ] Preview already handles PDFs
- [ ] NextDNS client installed and configured; lock so the standard account cannot change it
- [ ] Force SafeSearch and YouTube Restricted Mode via NextDNS

**Lockdown (focused, not draconian)**
- [ ] Standard account cannot install software, change DNS, or disable security
- [ ] Screen Time configured for content restrictions and (optionally) app limits; this is Apple's built-in parental-controls layer and covers a lot without third-party software
- [ ] Restrict VPN profile installation
- [ ] Document the admin password and store it securely (offline)

**Sample Homebrew provisioning script** (run in Terminal on the golden Mac, as the admin user)

```bash
# Install Homebrew first if not present:
#   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install python git node
brew install --cask thonny
brew install --cask visual-studio-code
brew install --cask github
brew install --cask wireshark
brew install --cask bitwarden
brew install --cask google-chrome
brew install --cask firefox
```

Verify each formula and cask name with `brew search <name>` before a wide rollout, since names change.

### Windows setup (secondary fleet)

Same philosophy, different mechanics. Everything taught in the course works on both.

- [ ] Windows 11 **Pro** (Pro is required for BitLocker, Hyper-V/WSL2, local accounts, and policy controls; Home is limiting)
- [ ] **Standard (non-admin)** student account; separate **administrator** account held by you
- [ ] Automatic Windows Updates; Microsoft Defender and Firewall enabled; SmartScreen on
- [ ] Optional BitLocker disk encryption
- [ ] WSL2 enabled with Ubuntu installed (this is how Windows students reach the same Unix shell the Macs have natively)
- [ ] Same app stack: Thonny, Python, VS Code, Git, GitHub Desktop, Node.js, Windows Terminal, Wireshark, Chrome, Firefox, Bitwarden, a PDF reader
- [ ] An office suite for local documents (LibreOffice is free; Microsoft 365 if you have it)
- [ ] NextDNS client installed and locked; force SafeSearch and YouTube Restricted Mode
- [ ] Standard account cannot install software, change DNS, disable security, or create admin accounts; restrict VPN clients and browser proxy settings
- [ ] Recovery USB prepared and stored by you
- [ ] Consistent device name (e.g., CS-PC-01) and asset tag

**Sample winget provisioning script** (run in an elevated PowerShell on the golden Windows machine)

```powershell
winget install --id Python.Python.3.12 -e
winget install --id Microsoft.VisualStudioCode -e
winget install --id Git.Git -e
winget install --id GitHub.GitHubDesktop -e
winget install --id OpenJS.NodeJS.LTS -e
winget install --id Microsoft.WindowsTerminal -e
winget install --id WiresharkFoundation.Wireshark -e
winget install --id Bitwarden.Bitwarden -e
winget install --id Google.Chrome -e
winget install --id Mozilla.Firefox -e
winget install --id TheDocumentFoundation.LibreOffice -e
winget install --id AivarAnnamaa.Thonny -e

# Enable WSL2 + Ubuntu (reboot when prompted)
wsl --install -d Ubuntu
```

Verify each package ID with `winget search <name>` before a wide rollout, since IDs and versions change.

### Parent monitoring layer (transparent, parent-owned, both platforms)
- [ ] Parents install and own a parental-control tool of their choice (Mobicip, Bark, or Net Nanny) on their student's device. On Macs, built-in Screen Time may be all a family needs
- [ ] Full disclosure to parents and students in the enrollment agreement; nothing covert
- [ ] Collect the minimum needed; the instructor does not become custodian of browsing histories

### A teaching tie-in
In the cybersecurity unit, explain the very stack on these laptops: how DNS filtering works, what endpoint software can and cannot see, why acceptable-use policies exist, and the privacy-vs-security tradeoff. The safety measures stop feeling mysterious and become part of opening the black boxes.

---

## 9. Extra credit project tracks

Optional, ungraded-against-the-grade, available to interested students with extra time. Each project deepens a topic covered at high level. Difficulty: **Starter**, **Intermediate**, **Ambitious**.

### Game development (ties to Units 1, 3)
- Pong in pygame (Starter)
- Snake (Intermediate)
- Tetris (Intermediate)
- A simple 3D scene or a small platformer (Ambitious)

### Web development (Units 5)
- Personal portfolio site (Starter)
- Interactive page with JavaScript (Starter)
- Weather app consuming a public API (Intermediate)
- Small CRUD app with a database (Ambitious)

### Mobile apps (Unit 5)
- Convert their web app to a polished PWA (Starter)
- Flutter "hello world" and one screen (Intermediate)
- A basic SwiftUI or Kotlin screen on a Mac (Ambitious)

### AI and machine learning (Unit 6)
- Call an LLM API and build a simple chatbot (Starter)
- Train a tiny classifier with scikit-learn (Intermediate)
- A perceptron or small neural net from scratch in NumPy (Intermediate)
- A retrieval-augmented "study assistant" over their own notes (Ambitious)

### Cybersecurity (Unit 6)
- picoCTF beginner challenges (Starter; picoCTF is now part of CyLab Security Academy, see Section 6)
- Audit weak passwords and explain hashing (Intermediate)
- Find and fix a vulnerability in a deliberately vulnerable app (Ambitious)
- Analyze real phishing emails and document the tells (Intermediate)

### Hardware and embedded (Unit 2)
- Raspberry Pi: blink an LED, read a button (Starter)
- Read a temperature sensor and log it (Intermediate)
- Tiny web server on the Pi serving live sensor data (Ambitious)
- Arduino project or simple home automation (Intermediate to Ambitious)

### Cloud and systems (Units 4, 6)
- Deploy a project to a free cloud tier (Intermediate)
- Stand up an API plus database on the class server (Intermediate)
- Monitor application logs and build a small dashboard (Ambitious)
- Build the privacy-conscious classroom logging agent (Ambitious; reports only high-level events to a parent-visible dashboard, modeling minimal-collection design)

### Build the Stack (the capstone track, Units 1, 2, 7-style depth)
The most ambitious and most memorable path, end to end:
- nandgame.com: gates to adder (Starter)
- Turing Complete: gates to a working CPU (Intermediate)
- nand2tetris projects 1 to 6: logic, ALU, CPU, assembler (Ambitious)
- Build a tiny language in Python: tokenizer, parser, evaluator for something like `ADD 2 3 / PRINT 5` (Ambitious)

By year's end, a student who completes this track has traced computing from transistors to a programming language they built themselves, on top of the systems model the whole class shares.

---

## 10. Course policy on AI use

The course runs in two deliberate phases. The goal is that every line of code a student submits early on was written and understood by that student, not generated by a tool they cannot explain.

### Phase 1: no AI assistance (Week 1 through the AI unit)

From the start of the course until the AI unit in Unit 6, students may not use AI tools to do their coursework.

- **Not allowed:** using ChatGPT, Claude, GitHub Copilot, or any AI to generate code, debug code, or write explanations the student turns in as their own.
- **Allowed:** official documentation, the textbook and Code.org lessons, class notes, and asking the instructor or peers. (You set the line on general web search. A reasonable rule: reading documentation and concept articles is fine; pasting an AI-generated answer is not.)

Rationale: you cannot learn fundamentals if a tool writes them for you. This mirrors teaching arithmetic before handing students a calculator. The skill being built is the ability to reason about code, and that only forms through doing it unaided.

**Enforcement that actually works:** the work surfaces understanding. Use short "explain your code" checks, oral or written. If a student cannot explain a line, it does not count, regardless of where it came from. The in-class builds, the handwritten pseudocode traces, and the mid-year "trace the button press" oral already do this. Keep major graded coding done in class where practical.

### Phase 2: AI taught, then permitted as a tool (from the AI unit onward)

The AI unit explicitly teaches responsible AI-assisted coding: effective prompting, always verifying output, never shipping code you do not understand, spotting hallucinated APIs and subtle bugs, and the over-reliance trap. Introduce Claude Code as an agentic example. After this unit, AI-assisted work is permitted on non-exam projects.

**Important caveat for AP-track students.** The AP Create Performance Task has its own College Board originality and AI rules and must be the student's own work. "AI is now unlocked" must not bleed into the Create Task. Keep the Create Task AI-restricted per College Board even after the AI unit. College Board publishes guidance on plagiarism and AI for the task; review it with any student who tests.

---

## 11. Adjustments for younger students (8th to 11th grade)

Default stance: 8th graders do the same work as 11th graders. Alternates are offered only in the specific spots where the barrier is math maturity, and only for a student who needs one. Differentiation runs both ways here: the tiered extra-credit tracks raise the ceiling for older and ambitious students, while the alternates below lower the floor where needed.

| Topic (week) | Default (all students) | Optional alternate for younger students | Notes |
|---|---|---|---|
| Binary and hex arithmetic (W2) | Convert by hand using place values | Provide a place-value conversion table; focus on reading binary and checking with a converter rather than multi-step mental arithmetic | Concept retained, mechanics scaffolded |
| Big-O and time complexity (W14) | Informal Big-O notation: O(n), O(log n), O(n squared), and growth rates | Drop the log and exponent notation; teach via the timing "race" lab and qualitative language (scales well vs poorly) | Same intuition, no logarithms |
| Neural network (W27) | Build a tiny perceptron in Python with weighted sums | Use a visual tool (TensorFlow Playground or Teachable Machine) or the "call an LLM API" lab to build intuition | Avoids linear algebra |
| Encryption math (W28) | Conceptual public and private keys, hashing, MOD as remainder | None needed; already conceptual | MOD is just remainder, which 8th graders know |
| Floating-point Mystery Day | Conceptual (why 0.1 + 0.2 is not 0.3) | None needed | Conceptual only |

General supports for the mixed age range: pair an older student with a younger one for selected labs; allow extra homework time; keep core coding assessments in class where you can scaffold; let the extra-credit tracks absorb older students' extra capacity. Two companion documents support this: the Course Intro guide (the brief in-course computer-fluency orientation, since there is no pre-course class), and the Younger-Student Readiness and Prep guide (the readiness diagnostic, optional supplemental videos, and recommended books).

---

## 12. Software platforms and accounts

Get written parental consent before creating any account for a minor. Each student needs an email address to register for the core platforms; plan ahead for students who do not have one. Services set their own minimum-age and terms-of-service rules; verify current terms before enrolling students.

| Platform | Account per student? | Purpose | Notes |
|---|---|---|---|
| Email address | Yes (prerequisite) | Needed to register for GitHub, Code.org, and Google | Set up or use a parent-supervised address for students who lack one |
| Google account (Docs and Drive) | Yes | The shared, cross-platform document layer: collaboration, submissions, and handouts | Introduce after file-system fundamentals are solid, not before. Standard Google accounts have a minimum age (13 in the US); for younger students use a parent-managed account via Family Link. Verify current age terms |
| GitHub (plus GitHub Classroom for you) | Yes | Version control, collaboration, the Git unit, and final project repos | GitHub requires users to be at least 13; get parental consent. GitHub Classroom lets you distribute assignments and collect student repos |
| Code.org | Yes | AP-aligned concept lessons, pseudocode practice, assessments | You create a class section and students join; designed for school use including middle grades |
| LLM API access (Anthropic or OpenAI) | No (instructor-owned) | The AI unit and in-class AI demos | API keys cost money and provider terms generally restrict minors; you own the key and mediate access |
| College Board / My AP | Only for exam-takers | AP CSP registration and Digital Portfolio | Defer until a student commits to the exam |
| Cloud free-tier (a PaaS host) | Optional, extra-credit only | The cloud deployment track | Often needs a payment method; keep parent-managed |
| Turing Complete (Steam) | No per-student account | In-class CPU building | One purchase on a lab machine |

No-account tools (free, installed locally or run in a browser): Thonny, VS Code, Python, Git, Node.js, Wireshark, browsers, Pages and Numbers (Mac), LibreOffice (Windows), nandgame.com, TensorFlow Playground.

**A note on the 8th graders.** Several account minimums sit at 13, which some of your youngest students may not have reached. Where that is the case, use a parent-managed account (Google Family Link) or have the student work under a parent's account with the parent's knowledge. Check each student's age against each platform before the course starts rather than discovering it in Week 23 when Git accounts are needed.
