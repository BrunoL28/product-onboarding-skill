# Proof of Life Probe - Worked Example

Probe selection for Aurora Bank's *Disputa Express*, picking up **Box 7** of the
Lean UX Canvas run the week before. Aurora Bank is fictional and every figure here
is invented. Study the order of operations - threshold before instrument - and the
moment a comfortable probe gets disqualified out loud.

## Intake

**User:** We ran the canvas. Box 7 says the riskiest assumption is whether visible
status actually deflects calls or just adds a channel people check before calling
anyway. Box 8 says add an IVR question and do five interviews. What probe?

**Agent:**

> I have the canvas, so I will not re-interview you on it. Box 7 gives me a value
> assumption and a stated waste - submission flow, status read model, push
> pipeline, the whole v1. I am holding Box 8's method: start from a method and you
> end up with a threshold it can pass.
>
> **[Question 1 of 3]** What would you have to see to **not** build this?

**User:** If most people had already checked the app and called anyway. Then status
alone isn't worth a quarter and we'd lead with provisional credit instead.

**Agent:** A kill criterion in prose. We will put a number on it before we pick.

> **[Question 2 of 3]** Which disputers can you reach this week without asking
> anyone's permission - and what is the decision date?

**User:** All of them. About 4,200 disputes a month, all through the phone queue.
Ops can message any customer. Scope lock 2026-09-15, me and the CX lead decide.

**Agent:** Behaviour in context is affordable, so stated intent is not good enough.

## Kill criterion before method

**Agent:**

> Box 2 targets contact rate per active card from 0.14 to 0.10, a 29% cut, and in
> v1 status visibility is the only lever on it. So the line sits near a 30% drop
> against your own baseline of 3.1 repeat calls [Fact - contact centre logs].
>
> Proposed: **if treated disputes average above 2.2 inbound contacts in the 14 days
> after submission, over at least 120 treated disputes, we do not build the status
> read model; we scope immediate provisional credit instead.**
>
> Two things I will not do: quote an industry deflection benchmark, or call
> anything significant at this sample size. Does 2.2 hold?

**User:** It holds. But if it lands between 2.2 and 2.6 we'd argue forever, so call
that inconclusive rather than a pass.

## Candidates and the gate

**Agent:**

> | # | Probe | Could prove | Rung | Cost | Time | Signature false positive | Blast radius |
> |---|---|---|---|---|---|---|---|
> | 1 | IVR intercept + 5 interviews | Whether callers say status would have stopped them | Stated intent | Low | 1 wk | People predict themselves badly, and are polite | None new |
> | 2 | Concierge status service | Whether knowing the state changes calling behaviour | Behaviour in context | Med | 4 wks | The human, not the status, carries the value | Real disputers, distressed |
> | 3 | Painted door "Acompanhar disputa" tile | That people look for status in-app | Behaviour in context | Med | 2 wks | Shown to the most engaged cohort | Fraud victims tap a dead end |
>
> **Disqualified: candidate 3.** It measures seeking, not deflection - someone can
> tap the tile and still call. And a fraud victim tapping "coming soon" in a
> distressed moment has been failed twice. We do not fake-door this journey.
>
> Candidate 1 is Box 8's own method. Cheap, and it cannot return the kill signal:
> it collects what people say about a behaviour the product never afforded.
>
> **Recommendation: candidate 2.** Which do you want - 1, 2, 3, or a combination?

**User:** 2. Can we keep the IVR question running alongside?

**Agent:** Yes, as instrumentation to interpret the result - not as a second probe.
It gets no threshold of its own, because two thresholds means whichever one passes
becomes the headline.

## Output

```markdown
## Assumption Under Test

- **Assumption**: Making dispute status visible reduces inbound calls per dispute
- **Source**: Lean UX Canvas Box 7, 2026-07-21
- **Risk type**: value
- **If false, we waste**: submission flow, status read model, push pipeline - v1
- **Decision this feeds**: build status read model, or scope provisional credit
- **Decision date**: 2026-09-15  **Decision owner**: PM, cards squad
- **Current evidence**: 31% of call minutes touch disputes [Fact - call logs]

## Kill Criterion (pre-registered 2026-07-27 by PM and CX lead)

- **Signal**: inbound contacts per dispute, first 14 days, treated vs holdout
- **Baseline**: 3.1 repeat calls per dispute [Fact - contact centre logs, Q2]
- **Threshold**: treated cohort at or below 2.2 contacts per dispute
- **Why this threshold**: Box 2 needs a 29% contact-rate cut and status is the
  only v1 lever; below 30% deflection the build cannot reach the outcome
- **Sample floor**: 120 treated disputes and 120 holdout disputes
- **Timebox**: 4 weeks, stop 2026-08-28 - at the ceiling because each dispute
  needs a 14-day observation window and enrolment runs 14 days
- **Alternative if killed**: scope immediate provisional credit as the lead
  solution and re-probe liability certainty rather than status visibility

> If contacts per dispute stay above 2.2 over 120 treated disputes in 4 weeks,
> we do not build the status read model; we scope provisional credit instead.

## Probe: Concierge status service

- **Type**: concierge
- **Kill criterion**: as pre-registered above, verbatim
- **Evidence rung**: behaviour in context
- **Timebox**: 2026-07-31 to 2026-08-28, readout 2026-09-01
- **Cost**: ~R$ 150 messaging, 40 ops person-hours, 0 engineering days
- **Engineering budget**: none - ops sends from the existing template console

### What each result means, agreed in advance

| Result | Observed condition | What we do |
|---|---|---|
| Pass | 2.2 or fewer contacts per dispute, n >= 120 | Build the status read model |
| Kill | Above 2.6 contacts per dispute, n >= 120 | Scope provisional credit first |
| Inconclusive | 2.2 to 2.6, or n < 120 | Extend enrolment 2 weeks, then decide |

### Signature false positive
- **The trap**: concierge value comes from the operator, not the status content
- **The guard**: fixed template text, send-only number, no agent judgement, no
  commitments. Replies route to the normal queue and **count as contacts**, so
  channel-shifting cannot read as deflection

### Blast radius
- **Who sees it**: 120 real disputers in a distressed moment; holdout gets
  today's experience unchanged, so nobody is made worse off
- **Real path out**: the dispute phone number appears in every message
- **What is fabricated**: nothing - every message states a true state read from
  the live queue. No invented decision, no invented liability outcome
- **Regulatory exposure**: message wording needs compliance sign-off - **OPEN**,
  requested 2026-07-27. The run does not start until cleared

## Run Plan

- **Window**: 2026-07-31 to 2026-08-28, readout 2026-09-01
- **Owner / who makes the call**: CX lead / PM with CX lead
- **Cohort and selection**: every third new dispute treated, remainder holdout,
  allocated by submission order, no cherry-picking
- **Instrumentation**: contacts joined to dispute ID in the contact centre log;
  the IVR intercept runs on all callers as interpretation only
- **Stop-early conditions**: any complaint about the messages, any compliance
  flag, any message sent carrying a wrong state
- **What we are NOT measuring**: message open rates, CSAT, approval rates

## Result Record

**Status**: NOT YET RUN (as of 2026-07-27)

| Field | Pre-registered | Observed |
|---|---|---|
| Signal | Contacts per dispute, 14 days | |
| Threshold | 2.2 | - |
| Sample | floor 120 treated, 120 holdout | |
| Window | 2026-07-31 to 2026-08-28 | |

- **Verdict**: pending
- **Decision taken**: pending
- **False positive check**: pending
- **What this probe still cannot prove**: that a pull-based in-app timeline
  performs like a proactive message; that push is the right channel

## Assumptions to Validate

- Liability certainty outranks refund speed - canvas runner-up, n = 3
  [Assumption]. Research owns it, probed after this one resolves
- Push reaches Camila despite zero email engagement [Assumption]. This probe
  uses WhatsApp and cannot answer it - needs a channel test before v1
- A self-serve timeline deflects like a proactive message [Assumption]. The
  probe pushes, v1 pulls. Not proven here
- The 3.1 baseline is stable month to month [Assumption] - contact centre
  analyst confirms before the readout
- Compliance clearance of message wording - **OPEN, blocks the run**
```

## What this example is meant to teach

1. **The threshold was written before the method.** 2.2 came from Box 2's own
   target, not from a deflection benchmark somebody half-remembered.
2. **The user invented the inconclusive band.** Naming the range where the team
   would argue forever is what stops a weak result reading as a pass.
3. **The comfortable probe was Box 8's own.** An IVR question is stated intent
   about a behaviour the product never afforded - so it became instrumentation.
4. **A probe was disqualified on blast radius, not cost.** The painted door was
   cheap and fast. Fake-dooring fraud victims is not a budgeting question.
5. **The result record is empty and says so.** Anything else would look like
   evidence four weeks before the evidence exists.

## Provenance

Original work, MIT, copyright Bruno Lima Soares. The **Proof of Life probe**
framing is Dean Peters'. Methods credited to their sources: Eric Ries, *The Lean
Startup* (concierge); Teresa Torres, *Continuous Discovery Habits* (assumption
tests). Aurora Bank is fictional; all figures, logs, and dates are invented.
