# Reply to Thread A's canonical handoff

In response to the handoff tagged **FORKTAG-CS-p4k9m2**. This is meant to be pasted
back into that thread, or into whatever thread picks up its context next, to close
out its open questions with what a direct repo inspection now confirms. Per that
handoff's own gap-check line, this repo's state wins over anything the handoff
says where the two conflict; several of its "no record" items are resolved below.

Written by the thread it calls Thread C, working directly against the repo. Date:
see the commits cited below for exact timestamps.

## Resolved

**Week 2 five-bit converter.** Demoted from a core Segment 6 deliverable to an
extension for students who finish early. `lessons/week-02-teacher-guide.md`,
commit `dd4a692`.

**Code.org versus CodeAI naming.** Checked all 32 teacher guides and all 32
homework handouts directly. Every mention uses the approved "CodeAI, formerly
Code.org" form. The batch-generation kickoff's naming fix held; this was never a
live problem in student-facing material.

**The at-a-glance visual's "may sit the AP CSP exam in May" line.** Verified
against the 2027 AP exam schedule: AP exams have been in May for decades, and the
line does not mention the Create Task deadline, which is the date that actually
moves year to year. JD's decision: leave it as written.

**Scope of commit `de17804`.** Read directly rather than inferred: `git show
de17804 --stat` and the full commit message. It is a correctness review, grouped
under Lab-breaking, Factual, Consistency, and Safety and policy, touching 41
files across Weeks 6 to 32. Session pacing and difficulty were not assessed; the
one difficulty-adjacent finding was prerequisite scaffolding, four untaught
constructs introduced explicitly. This matches JD's own prior read exactly.

**Classroom sync tooling.** `tools/` exists in the repo with all five files
(`classroom_auth.py`, `publish_handouts_to_docs.py`, `sync_classroom.py`,
`requirements.txt`, `README.md`) and has been run against live Google Classroom,
not just built. Per a separate thread's handoff pasted into this same
conversation: course ID `872157197298`, 8 topics, 33 coursework items (32
assignments plus 1 short-answer question), 2 Course Information materials
published, verified against the live Classroom UI rather than assumed.

**Concurrent sessions.** Checked `git log --format='%an <%ae>'` across the full
history and `git branch -a`. Every commit is authored by JD Smith
`<jaydge@gmail.com>`; one feature branch (`classroom-sync-tools`) is fully merged
into `main`; working tree is clean; history is linear. No evidence of a
conflicting concurrent session as of this reply. This cannot rule out a future
thread starting fresh without checking first, only report the state found now.

**README Conventions versus the no-sales-language rule.** It was previously a
one-time correction applied to a single file, not a standing rule. Now written
into `README.md`'s Conventions section. Commit `3dbf594`.

## Decided, not previously settled

**Whether the Unit 3 review-weighting instructions become standing conventions.**
They were originally given as scoped, one-off guidance for that single review
pass: coding exercises are exempt from "runnable from the guide alone" and should
prefer skeletons or fill-in-the-blank over verbatim solutions, and AP alignment
review is scoped to each week's Extra Credit AP Track section rather than every
AP mention in a guide. JD confirmed these should govern every future quality and
difficulty review pass, Unit 4 and Unit 6 included, not just Unit 3. Written into
`README.md`'s Conventions section, next to the two existing conventions they
qualify. Commit `c465c17`.

## Still open, not resolved by this reply

**Project STEM's real unit numbering.** Still unverified behind its teacher
login, as it has been throughout the project. JD's current position: not worth
chasing until an actual student commits to the AP track and wants to use it.
Deliberately deferred, not forgotten.

## Not addressed here

The handoff's attachment inventory, its terminology section, and its account of
Thread A's own design history are outside what a repo inspection can confirm or
deny, and are left as that document states them.
