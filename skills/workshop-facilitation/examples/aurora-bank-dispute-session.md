# Workshop Facilitation - Worked Example

A 60-minute, four-person session at Aurora Bank on *Disputa Express*. Aurora Bank
is fictional and **every figure below is invented**.

The point is the ending. The fraud ops lead and the engineering lead do not agree,
the session does not resolve it, and the record says so - by name, with the
evidence that would settle it and the date it arrives. A record that smoothed this
into "the team aligned on auto-acknowledge" would be tidier and worthless.

---

## The plan, shown at the open

```markdown
## Session Plan: Disputa Express slice 1 - acknowledgement model
- **Deliverable**: a decision on how a dispute is acknowledged, plus the top 3
  items for slice 1
- **Host skill**: prioritization-advisor (owns the scoring; this skill owns the room)
- **Timebox**: 60 minutes
- **Decision owner**: Rafael Nunes, PM
- **Decision rule**: dot vote to shortlist, Rafael decides

### Participants
| Name | Role | Brings | Speaks |
|---|---|---|---|
| Marcos Pinho | Designer | What Camila does when the screen says nothing | 1st |
| Tereza Villar | Fraud ops lead | Abuse patterns, the manual queue | 2nd |
| Beatriz Amaral | Engineering lead | What the back office can and cannot emit | 3rd |
| Rafael Nunes | PM, decision owner | The commitment to the exec review | last |
```

**Facilitator:** Three questions, one at a time, 60 minutes. At any point you can
say "take your best guess" or drop your notes in. Speaking order is Marcos, Tereza,
Beatriz, Rafael - Rafael last, because he decides and his first sentence would
otherwise become everyone else's frame.

---

## Minute 4: the anchor attempt

**Beatriz:** This is all downstream of whether the back office can emit an event on
state change. If it cannot, none of the rest matters.

**Facilitator:** Hold that - it is a real constraint and it goes on the wall in two
minutes. First, everyone writes their own answer to *what does acknowledgement have
to do for Camila*. Three minutes, silent. Then we read out in order.

**Marcos (1st):** She needs to know within a minute that something is happening.
Eleven days of nothing is why she calls twice.

**Tereza (2nd):** Ops needs to know the dispute is real before we tell her it is
accepted. Acknowledged and accepted are different words to a customer.

**Beatriz (3rd):** Acknowledgement in-app is cheap. State updates are expensive.

**Rafael (last):** I promised the exec review a number in hours, not days.

---

## Minutes 12-30: diverge, then converge

**Facilitator:** Divergence now - no evaluation. If you think an option will not
work, park the objection and I will bring it back in the converge phase.

Six options went up. Tereza's *"that just moves the queue"* was parked at minute 19
and returned to at minute 31 - it turned out to be the whole disagreement.

**Dot vote**, two dots each, cast simultaneously on paper:

| Option | Dots |
|---|---|
| Auto-acknowledge in app, immediately | 4 (Marcos 2, Beatriz 2) |
| Manual fraud-ops review before acknowledgement | 2 (Tereza 2) |
| Auto-acknowledge with a per-card rate limit | 2 (Rafael 2) |
| The other three options | 0 |

**Facilitator:** A heat map, not a decision - and one of four people, two in the
same function. Rafael still decides.

---

## Minute 33: triaging the disagreement

**Tereza:** Auto-acknowledge invites dispute farming. We will see abuse triple.

**Beatriz:** A manual gate rebuilds the eleven-day queue we are here to remove.

**Facilitator:** Two different kinds of claim. Tereza, "abuse will triple" is a
**prediction** - nothing said in this room settles it. Beatriz, "a manual gate
rebuilds the queue" is checkable: what is ops' current review turnaround?

**Tereza:** Median 4 days for the manual check. It is not a queue-killer if we
staff it.

**Facilitator:** Fact settled: a gate adds a median 4 days unless staffing changes.
What is left is the prediction. What number, threshold, and date would prove you
right?

**Tereza:** Disputes later withdrawn or found invalid - about 6% now. Past 12% in
the first eight weeks and I was right.

---

## Minute 41: the decision nobody agreed with

**Rafael:** We ship auto-acknowledge with a rate limit of three open disputes per
card and watch Tereza's number weekly for eight weeks. I am choosing the customer's
first minute over the abuse risk, and that is a judgement, not a finding.

**Facilitator:** Tereza, I am recording you as dissenting. Correct this: *"Acknowledging
before any human review teaches customers that disputes are free. Ops carries the
cost, not the app team."* Is that your position, in your words?

**Tereza:** Yes. Add that I will run the weekly number myself.

**Facilitator:** And do you commit to the decision while we watch it?

**Tereza:** Yes - and I want it on the record that I did not agree with it.

**Facilitator:** That is exactly what the record is for.

At minute 48 we were behind, so we cut scope - three items ranked instead of seven
- and cut neither the dissent nor the read-back. That trade goes one way only.

---

## The record, read back at minute 55

```markdown
## Session Record: Disputa Express slice 1 - acknowledgement model
- **Date**: 2026-07-14  **Duration**: 58 min (planned 60)
- **Present**: Rafael Nunes, Tereza Villar, Beatriz Amaral, Marcos Pinho
- **Absent but affected**: Carla Reis (Compliance) - follow-up note sent
- **Decision owner**: Rafael Nunes

## Decisions
| # | Decision | Made by | Basis | Date |
|---|---|---|---|---|
| D1 | Auto-acknowledge in app on submission, no human gate | Rafael Nunes | judgement, against one dissent | 2026-07-14 |
| D2 | Rate limit: max 3 open disputes per card | Rafael Nunes | mitigation for D1 | 2026-07-14 |
| D3 | Slice 1 = open in app, status on demand, acknowledge | Rafael Nunes | dot vote + RICE from prioritization-advisor | 2026-07-14 |

## Dissent
| # | Who | Position | Grounds | What would change their mind | Review | Commits? |
|---|---|---|---|---|---|---|
| X1 | Tereza Villar | "Acknowledging before any human review teaches customers that disputes are free. Ops carries the cost, not the app team." | prediction | Invalid-or-withdrawn rate above 12% in 8 weeks (baseline 6%) | 2026-09-08 | Yes |

## Parking Lot
| # | Item | Raised by | Owner | Next step |
|---|---|---|---|---|
| P1 | Can the back office emit on state change? | Beatriz Amaral | Beatriz | 2-day spike, feeds slice 2 |
| P2 | Wording of "acknowledged" vs "accepted" in PT-BR | Marcos Pinho | Marcos | Draft for legal review |
| P3 | Ops staffing if D1 is reversed at review | Tereza Villar | Tereza | Dropped for now, agreed |

## Actions
| # | Action | Owner | Due | Depends on |
|---|---|---|---|---|
| A1 | Instrument invalid-or-withdrawn rate, weekly | Tereza Villar | 2026-07-21 | X1 |
| A2 | Run the emit spike | Beatriz Amaral | 2026-07-18 | P1 |
| A3 | Book the 8-week review | Rafael Nunes | 2026-07-15 | X1 |

## Assumptions to Validate
- The 6% invalid-or-withdrawn baseline is a Q2 figure from one ops report.
- D2's limit of 3 open disputes per card is a guess; nobody has a distribution.
- D1 assumes rate limiting is a meaningful abuse control. Untested here.
- X1 is open until 2026-09-08.
```

**Marcos:** One correction - "acknowledged and accepted are different words" was
Tereza's line, not mine. I said she needs to see something within a minute.

**Facilitator:** Fixed. That is the whole reason we read it back in the room.

---

## What this example is meant to teach

1. **Speaking order is a design decision.** Rafael last, Beatriz third: her framing
   at minute four was accurate and would still have hijacked the session.
2. **Silent writing buys four independent answers** instead of one answer and three
   reactions to it.
3. **Triage the disagreement before resolving it.** One half was a fact that took
   30 seconds to settle; the other a prediction only a metric and a date can.
4. **A dot vote is a heat map.** Four dots from two people in one function is not a
   mandate, and saying so aloud protects the decision owner.
5. **Record the dissent by name, in their words, with a falsifier.** X1 is the
   most useful row in the document, and on 2026-09-08 it is the only one anyone
   will reread.
6. **Read it back while everyone is present.** Marcos' correction took eight
   seconds; found a week later in a wiki it is a fabricated attribution.

---

## Provenance

Adapted from `generative-guidance-pattern.md` and `interaction-modes.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, **CC BY-NC-SA 4.0**. Aurora Bank, Disputa Express, Cardholder
Camila, and all four participants are fictional; every figure was invented.
