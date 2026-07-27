# Epic Hypothesis - Worked Example

Framing DE-EPIC-2 from Aurora Bank's *Disputa Express* as a bet the team could
lose. Fictional; figures invented. The useful part is the **falsifier gate firing
twice**: on a threshold no result could reach, then on a decision nobody could make.

---

## Collapse, not interview

**Agent:**

> `PROBLEM_STATEMENT.md`, `PROTO_PERSONA.md` and the Lean UX Canvas are upstream,
> so I am not interviewing you about the persona or the outcome.
>
> **Found** - first-time disputers, mobile-only; contact rate per active card,
> 0.14 today; the guardrail the team already named (approval rate flat); and the
> epic itself from the breakdown session, DE-EPIC-2.
> **Inferred** - what she wants is liability certainty, not speed, read from
> "robbed twice" rather than any stated finding.
> **Still missing** - the two things no upstream artifact can decide. Questions 3
> and 4 only. **What result would make you stop building this?**

**User:** If contact rate doesn't come down at all, I guess.

**Agent:** Hold that; I test it in a minute. Draft first.

---

## Both grammars, and the gap between them

**Agent:** Same claim, two shapes.

> - **If/Then**: If we show first-time disputers the real state of their dispute
>   and whether they are still liable, then they will stop calling to ask.
> - **Gothelf**: We believe an in-app dispute status view for first-time disputers
>   will achieve a fall in contact rate per active card, and we will know we are
>   right when it reaches 0.115 or below over six weeks.
>
> These do not say the same thing. The If/Then says *liability certainty*; the
> Gothelf version says *a status view*. If the timeline ships and she still cannot
> tell whether she owes the money, the first is false and the second is true.

**User:** Then it's liability. The screen has to answer the money question.

**Agent:** Recorded - and that also changes DE-4's acceptance criteria, a cheaper
place to catch it than a usability test.

---

## The falsifier gate, and what is not a signal

**Agent:**

> Your kill threshold was "if contact rate doesn't come down at all." Contact rate
> is 0.14, and card growth alone moves it a point either way over six weeks. That
> threshold sits inside the noise you already have: you would see 0.138, call it
> directional, and ship. Where is the line at which you would actually stop?

**User:** ...if it's still above 0.135 after six weeks, this didn't work.

**Agent:** That bites, and leaves a real band from 0.115 to 0.135. What happens in
the band?

**User:** Extend once. Three more weeks.

**Agent:** Once, then it is a fail. Unlimited extension is how a bet turns back
into a belief.

**User:** Can we also track timeline views per dispute? That would show it working.

**Agent:** That measures shipping - views rise because the screen exists, and the
number cannot come back low unless the feature is broken. The behavioural version:
**of five disputers interviewed, how many say they did not call because the app
answered them?** That can come back 1 of 5.

**User:** Fine. Four of five to confirm; two or fewer falsifies.

---

## The window, and the cheapest test

**Agent:** Six weeks is two dispute lifecycles, not a sprint multiple. Median
open-to-outcome is 21 days [Inference from the 11-day acknowledgement plus scheme
timelines]; a 14-day window would sample mostly unresolved disputes.

> Climbing the ladder: an **existing data query** has no behaviour to read, since
> nobody can see status today. The **IVR question** from the canvas measures intent,
> not the avoided call. **Five interviews** give the qualitative signal only. The
> first rung producing both is an **instrumented thin slice** - DE-4 alone, behind
> a randomised 20% holdout. The cheapest honest test is a slice of the epic itself,
> and it re-sequences you: DE-4 ships with the holdout, DE-8's push pipeline waits.

**User:** Who signs off on killing it? Probably the Cards tribe lead - but I
haven't asked her.

**Agent:** Then the card ships provisional, and getting her to accept the 0.135
branch goes into Assumptions to Validate. I do not write a name against a decision
its owner has not agreed to.

---

## Output

```markdown
> **PROVISIONAL.** The falsifying signal has no named decision owner. Until one
> is named, this is a forecast, not a bet. See Assumptions to Validate.

## Epic Hypothesis: DE-EPIC-2 Liability certainty without a phone call

- **Date**: 2026-07-24
- **Team**: PM, tech lead, CX lead
- **Upstream**: PROBLEM_STATEMENT.md, PROTO_PERSONA.md, Lean UX Canvas v2
- **Status**: provisional

### Epic as a user story

- **As a** first-time disputer with an open dispute
- **I want to** see what is happening with my dispute without calling
- **so that** I know whether I am still liable

### The claim, in both grammars

- **If/Then**: If we show first-time disputers the real state of their dispute
  and whether they still owe the money, then they will stop calling to ask.
- **Gothelf**: We believe that a liability-answering dispute view for first-time
  mobile-only disputers will achieve a fall in contact rate per active card. We
  will know we are right when contact rate reaches 0.115 or below over six weeks.
- **Difference between the two**: the draft said "status view" where the claim
  needs "liability answer". Resolved toward liability; DE-4 criteria updated.

### Signals

| Signal | Measure | Baseline | Source | Confirm | Falsify | Window |
|---|---|---|---|---|---|---|
| Quantitative | Contact rate per active card, disputers only | 0.14 [Fact - Q2 support deck] | Genesys weekly extract | <= 0.115 | >= 0.135 | 6 weeks |
| Qualitative | Disputers who say the app answered them instead of a call | none [Assumption - never asked] | 5 interviews, holdout excluded | 4 of 5 | 2 or fewer of 5 | 6 weeks |
| Guardrail | Dispute approval rate | 62% [Assumption - not yet queried] | Back-office monthly | stays within 2 points | falls below 60% | 6 weeks |

- **Window derived from**: two dispute lifecycles; median open-to-outcome 21 days
  [Inference from 11-day acknowledgement plus scheme timelines].
- **Inconclusive band**: 0.116 to 0.134 - extend once by 3 weeks, then fail.
- **Behaviour, not adoption**: timeline views were rejected; views rise because
  the screen exists. The avoided call is the behaviour.
- **Non-obviousness**: the CX lead predicts the opposite - "under review" prompts
  a call rather than preventing one. Both views are held in the room.

### Decision rule

Pre-committed 2026-07-24, before any data.

- **If the confirming signal fires**: build DE-8 push, extend to DE-10, slice 2.
- **If the falsifying signal fires**: stop the status investment at DE-4, re-test
  with immediate provisional credit as the lead solution.
- **If we land in the band**: extend once by 3 weeks, then treat as a fail.
- **Who can act on the falsifying branch**: OPEN - proposed Cards tribe lead.

### Validation method

- **Rung on the ladder**: instrumented thin slice - DE-4 only, three common
  states, liability line, randomised 20% holdout.
- **Cheaper rungs ruled out**: data query has no behaviour to read; the IVR
  question measures intent; five interviews give only the qualitative signal.
- **What it costs**: one story (M) plus holdout config, against a four-story epic.
- **Instrumentation required**: dispute-view event with holdout arm, plus contact
  attribution to dispute ID. Neither exists; both are part of DE-4.
- **Read-out date**: 2026-09-11.

### Assumptions to Validate

- Approval-rate baseline of 62% is an Assumption; one query against the
  back-office outcomes table settles it before the window opens.
- The kill decision has no owner. Ask the Cards tribe lead to accept the 0.135
  branch in writing; until then this card is provisional.
- Contact attribution to dispute ID does not exist. Without it the quantitative
  signal is unreadable, so it gates the window start, not the epic.
```

---

## What this example is meant to teach

1. **"No improvement at all" is not a falsifier.** It sits inside the noise.
2. **The two grammars caught a real error** - status view versus liability answer
   is one word on the card and one acceptance criterion in DE-4.
3. **Adoption metrics feel like evidence.** A number that can only move one way is
   not a measurement.
4. **The window belongs to the dispute, not the sprint**, with the derivation
   written down so the next reader argues with reasoning, not with a number.
5. **Provisional beats a borrowed name** - a name against a threshold its owner
   never agreed to makes a card that looks complete and kills nothing.

---

## Provenance

Example built on the card in `prompts/backlog-epic-hypothesis.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Hypothesis format: Jeff Gothelf, *Lean UX*.
Aurora Bank is fictional; every figure is invented.
