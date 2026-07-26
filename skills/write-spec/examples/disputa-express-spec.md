# Write Spec - Worked Example

Spec for Aurora Bank's *Disputa Express* v1. Fictional.

The useful parts: the **P0 challenge demoting two requirements**, and a
**non-goal that removed two-thirds of the estimate**.

---

## Collapse, then one question

**Agent:**

> Four upstream artifacts exist, so most of this spec is already decided.
>
> **Found** - problem statement with evidence and a quote; persona; Lean UX canvas
> with Box 2 metrics (contact rate 0.14 to 0.10, repeat calls 3.1 to 1.5, approval
> rate as guardrail); story map with four release slices.
> **Inferred** - Goals come straight from Box 2; User Stories from slice 1;
> Assumptions from Box 7.
> **Still missing** - baselines. The canvas has targets, but I only have a current
> value for contact rate. Repeat calls per dispute at 3.1 came from the support
> deck; I cannot find a measurement method for it.
>
> One question: **is repeat calls per dispute actually instrumented, or was 3.1 an
> estimate in the deck?**

**User:** Good catch. It was an estimate from a sample of 40 tickets.

**Agent:** Then it goes in as a leading metric with the measurement method
*needs instrumentation*, and the baseline is flagged rather than treated as known.
That also becomes a data open question.

---

## The P0 challenge

The team arrived with six P0s.

```markdown
### P0 Challenge

| Requirement | Breaks if omitted? | Core journey possible without it? | Regulatory or hard dependency? | Verdict |
|---|---|---|---|---|
| Open a dispute from a transaction row | Journey cannot start | No | No | P0 |
| Show current state in plain language | The problem is unsolved | No - this IS the product | No | P0 |
| State liability for the disputed amount | Named in the problem statement | Journey works, problem does not | Consumer-protection wording | P0 |
| Warn when scheme window has closed | Customer opens an unwinnable dispute | Yes - it is worse, not broken | Scheme rules on eligibility | P0 - kept on the dependency, not the pain |
| Push notification on state change | Worse, not broken | Yes - she can open the app | No | demoted to P1 |
| Filter dispute history by date | Nothing | Yes | No | demoted to P2 |

**Demoted**: push notification (P1), history filter (P2)
**All survived**: no - two demoted, which is the expected outcome of a real
challenge
```

The interesting one is the scheme-window warning. It failed question 2 — the
journey works without it — but passed question 3, because accepting an ineligible
dispute is a scheme-rules problem, not a CX problem. Question 3 exists precisely
for this case.

---

## Output (excerpt)

```markdown
# Disputa Express v1 - Spec

- **Author**: PM, Cards squad
- **Date**: 2026-07-24
- **Status**: in review
- **Upstream artifacts**: PROBLEM_STATEMENT.md, PROTO_PERSONA.md,
  LEAN_UX_CANVAS.md, USER_STORY_MAP.md

## 1. Problem Statement

**The problem**: A cardholder who reports a fraudulent charge cannot find out
whether she is still liable for it without calling and re-explaining her case.

**Who has it**: First-time disputers, mobile-only. 4,200 disputes a month; the
majority are first-timers (assumption, one query away).

**Impact**: 31% of all call minutes; 11-day median acknowledgement; 3.1 estimated
calls per dispute.

**Evidence**:
- "Robbed twice. Once by whoever took the money, once by the wait."
  (support transcript, 2026-06-09)
- Q2 support deck, dispute volume and call-minute breakdown

## 3. Non-Goals

1. **No evidence upload in v1** - 78% of first-timer disputes need no document
   (support sample, Q2), and photo upload was roughly two-thirds of the estimate.
   It also creates an LGPD retention duty we have not designed for.
   Reconsider if: dispute approval rate falls below the current baseline, or if
   ops report evidence requests on more than 30% of app-opened disputes.
2. **No merchant disputes, only fraud** - different journey, different persona,
   different scheme rules. Reconsider if: merchant disputes exceed 25% of volume.
3. **No in-app chat with an agent** - would replace one silent channel with an
   expensive one and does not address the root cause. Reconsider if: the Box 7
   experiment shows customers want a human rather than a status.
4. **No dispute history filtering** - demoted from P0 during the challenge; no
   evidence anyone asked for it. Reconsider if: support sees repeat disputers
   struggling to find prior cases.

## 6. Success Metrics

**Leading**

| Metric | Current | Target | How measured |
|---|---|---|---|
| Repeat calls per dispute | 3.1 (ESTIMATE, n=40 tickets) | 1.5 | NEEDS INSTRUMENTATION - see open question 3 |
| App-opened disputes as share of total | 0% | 60% | Existing dispute-source field |
| Status views per open dispute | n/a | 2+ | New event, ships with the feature |

**Lagging**

| Metric | Current | Target | How measured |
|---|---|---|---|
| Contact rate per active card | 0.14 | 0.10 | Existing telephony dashboard |

**Guardrail**

| Metric | Current | Must stay | How measured |
|---|---|---|---|
| Dispute approval rate | 71% | within 3pts | Existing ops report |

## 7. Open Questions

| # | Question | Owner | Blocking? |
|---|---|---|---|
| 1 | Does the regulated acknowledgement clock start at customer submission or bank acknowledgement? | legal | **yes - blocks scope lock** |
| 2 | Can the Genesys webhook fire on back-office state change? | eng | **yes - blocks P0-2** |
| 3 | Can repeat calls per dispute be instrumented before launch, for a real baseline? | data | no - but the target is unfalsifiable without it |
| 4 | Exact liability wording shown to the customer | legal | no - copy can land late |

## Assumptions to Validate

- That first-timers are the majority of disputers - one query, blocks nothing but
  invalidates the persona if wrong.
- That 3.1 repeat calls is roughly right - it is a 40-ticket estimate being used as
  a baseline for a headline target.
- That visible status deflects calls rather than adding a checkpoint - Lean UX
  Box 7, two-week IVR experiment, running now.
```

---

## What this example is meant to teach

1. **A real P0 challenge always demotes something.** Six P0s became four. If all
   six had survived, the right response is suspicion, not satisfaction.
2. **Question 3 exists for the unglamorous case.** The scheme-window warning was
   not painful and not journey-breaking, but shipping without it means accepting
   disputes you cannot win. Regulatory and dependency P0s do not have to hurt to
   be real.
3. **A flagged baseline is worth more than a clean one.** 3.1 was a 40-ticket
   estimate about to become a headline target. Marking it ESTIMATE and opening a
   data question kept a soft number from hardening into an OKR.
4. **Reconsider-if turns non-goals into decisions instead of arguments.** Every
   non-goal names the condition that would reopen it, so the next stakeholder who
   asks for evidence upload gets a threshold rather than a debate.
5. **The spec cites discovery, it does not rewrite it.** The Problem section is
   four lines and a quote, because `PROBLEM_STATEMENT.md` already did that work.

---

## Provenance

Example for the `write-spec` skill, adapted from Anthropic's `product-management`
example plugin (MIT), following the conventions in CONVENTIONS.md adapted from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Aurora Bank is fictional; all figures invented.
