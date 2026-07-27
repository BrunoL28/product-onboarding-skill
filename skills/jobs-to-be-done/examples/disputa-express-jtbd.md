# Jobs to be Done - Worked Example

The JTBD canvas behind Aurora Bank's *Disputa Express*, run in Phase 0 before
anyone had drawn a screen. Aurora Bank, Camila, and **every figure below are
invented**. The part worth studying is **Question 3**, where three transcripts
filled push, pull, and habit and left the anxiety column empty.

---

## Facilitation

**Agent:**

> Four questions, one at a time, then I build the canvas. Pick an option, type
> your own, say "take your best guess," or drop in notes to skip ahead. You can
> also skip, go back, or say "that's enough, build it."
>
> **Question 1 of 4: the situation.** A job lives in a circumstance, not in a
> person. Which circumstance is this canvas scoped to?
>
> 1. **The moment she spots the charge** - R$ 480 she does not recognise, no
>    vocabulary for what just happened.
> 2. **The eleven days after she reports it** - your median time to acknowledge,
>    and where the repeat calls sit.
> 3. **The moment the outcome lands** - smallest volume, worst public reviews.
> 4. Other - type your own, or combine numbers with commentary.

**User:** 2. That's where the call volume is. But she gets there through 1.

**Agent:** So it scopes to the waiting period, triggered by the discovery moment.

> **Question 2 of 4: the decision.** What changes depending on what this canvas
> says? It decides how hard I push on measurability. (Options: go/no-go on
> Disputa Express; v1 scope given build is approved; the argument to fraud and
> ops. Other.)

**User:** 2, mostly. Build is approved. Take your best guess on the rest.

**Agent:** Taking the guess: the canvas informs v1 scope, and the ops-side
eleven-day cycle is out of scope here. Both labelled as assumptions.

> **Question 3 of 4: evidence.** What do you have that I can read rather than
> infer?

**User:** *(pastes three support call transcripts flagged by the CX lead)*

**Agent:** *(reads them)*

> **Found** - three verbatim quotes, all mobile-only, all calling within 24 hours
> of the push alert; "robbed twice"; one caller asking whether she owes the bill
> while the bank investigates.
>
> **Inferred** - the functional job is not "get a refund" but "get the charge
> reversed and my name cleared": two of three were asked to confirm they had not
> shared their card.
>
> **Still missing** - the right-hand side of the forces model. Three transcripts
> say why she wants change; nothing says what makes her hesitate, and an empty
> anxiety column cannot explain non-adoption.
>
> **Question 4 of 4: anxiety.** When you have described a self-service dispute
> flow to customers, what have they worried about out loud?
>
> 1. **"If I do it in the app, does a human still look at it?"** - fits
>    transcript 3; self-service reads as lower priority.
> 2. **"If I get it wrong, do I lose the right to dispute?"** - first-timers with
>    no vocabulary, filling a form with nobody checking.
> 3. **"Will the app say anything the phone would not?"** - habit rather than
>    anxiety, same effect on adoption.
> 4. Other.

**User:** 1 and 2 both came up in the design review. Nobody said 3.

**Agent:** So anxiety is being downgraded plus self-inflicted error - both
cheaper to answer with copy than with features.

> **Known**: situation, functional job, quotes, pains, both anxieties.
> **Assumed**: emotional job wording, every rating, ops cycle time out of scope.
> **Open**: whether liability certainty outranks refund speed. Build it?

**User:** Build it.

---

## Output

```markdown
## Jobs to be Done: Cardholder Camila, first-time disputer

- **Situation in scope**: waiting after reporting an unrecognised charge
- **Decision this informs**: what Disputa Express v1 does first
- **Evidence base**: 3 support transcripts, 1 design review, team knowledge
- **Date**: 2026-07-24

### 0. Job Statement

- **Main job**: Clear an unrecognised charge off my card and off my name
- **Job story**: When I see a charge I did not make and report it, I want to know
  where it stands and whether I still owe it, so I can stop worrying and get on
  with my week.
- **Solution-swap check**: phone the call centre, chargeback via the card
  network, complain publicly, or give up and pay it
- **Stability check**: yes - true before any app existed, true after

### 1. Customer Jobs

#### Functional Jobs
- Get the charge reversed (Fact)
- Learn whether the bill is due meanwhile (Fact)

#### Emotional Jobs
- Stop feeling robbed twice (Fact)
- Stop feeling like a suspect (Inference)

#### Social Jobs
- Not look careless to her family (Assumption)

### 2. Forces of Progress

#### Push of the Situation (toward change)
- R$ 480 gone, unexplained (Fact)

#### Pull of the New Solution (toward change)
- Check status without calling (Inference)

#### Habit of the Present (against change)
- Calling works, eventually (Fact)

#### Anxiety of the New (against change)
- Does a human still review it? (Fact, design review)
- Can I forfeit by filing wrong? (Fact, design review)

### 3. Pains

#### Challenges
- No vocabulary to search help (Fact)

#### Costliness
- Three calls per dispute, average (Fact)

#### Common Mistakes

#### Unresolved Problems
- Never told if she owes it (Fact)

### 4. Gains

#### Expectations
- Told plainly who pays meanwhile (Fact)

#### Savings
- Zero calls per dispute (Inference)

#### Adoption Factors
- Says a human reviews it (Fact)

#### Life Improvement
- Stops checking her balance nightly (Assumption)

### 5. Desired Outcome Statements

| # | Outcome statement | Importance | Satisfaction | Source |
|---|---|---|---|---|
| 1 | Minimize the time it takes to find out whether I am liable for a disputed charge | 9 | 2 | assumed |
| 2 | Minimize the number of times I must re-explain the same dispute | 8 | 2 | assumed |
| 3 | Minimize the time it takes to confirm my report was received | 8 | 3 | assumed |

**Unmet needs** (high importance, low satisfaction): 1, 2, 3

### 6. Assumptions to Validate
- Liability certainty outranks refund speed - ask five disputers to rank them.
- The social job exists at all - nobody voiced it; probe in five interviews.
- Ops cycle time is out of scope - confirm with the fraud lead before scope locks.
```

---

## What this example is meant to teach

1. **The empty column was the finding.** Blank anxiety meant unexamined, not
   absent. Question 4 existed only to fill it, and produced the cheapest item on
   the canvas: "a human still reviews it".
2. **Anxiety is answered with sentences; pull is answered with roadmap.** The
   adoption factor is copy on a confirmation screen; every entry in the pull
   column is a build. Skipping the right-hand side spends the budget on the
   expensive side of the model.
3. **The main job survives the product.** "Clear an unrecognised charge off my
   card and off my name" was true when the only option was a phone call, and will
   be true after Disputa Express is replaced - the stability check passing.
4. **Unevidenced entries are labelled, not omitted.** Ratings read `assumed`, and
   the social job carries `(Assumption)` plus an instruction to delete it if the
   next five interviews do not raise it.

---

## Provenance

Example built on the canvas in `prompts/jobs-to-be-done.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: Clayton Christensen, Bob Moesta, Tony
Ulwick. Aurora Bank, Camila, the transcripts, and all figures are fictional.
