# Problem Statement - Worked Example

Framing the problem behind Aurora Bank's *Disputa Express*, starting from the
Cardholder Camila proto-persona. Fictional throughout.

The useful part of this example is the **first draft failing four of five checks**,
and what fixing each one changed.

---

## Collapse, not interview

**Agent:**

> `PROTO_PERSONA.md` is upstream, so I am not going to interview you about Camila.
>
> **Found** - persona, four pains, three sourced quotes including "robbed twice,"
> and the behavioural detail that she sees charges via push alert.
> **Inferred** - the outcome she wants is liability removal rather than the refund
> itself; the transcripts consistently lead with "am I on the hook."
> **Still missing** - the root cause. The persona doc says she cannot see status.
> It does not say why status does not exist.
>
> One question, then.
>
> **Why can she not see the status of her own dispute?**

**User:** Because it's in the back-office queue and there's no customer-facing
state on it.

**Agent:** And why does the queue have no customer-facing state?

**User:** Honestly? It was built for the ops team to work through. Nobody designed
it expecting a customer to look at it.

**Agent:** That is the root cause — and it is a structural fact, not a missing
feature. Drafting.

---

## First draft, and why it failed

```markdown
**I am** a cardholder who wants to track my dispute.
**Trying to** see my dispute status in the app.
**But** there is no dispute tracking screen.
**Because** we have not built dispute tracking yet.
**Which makes me feel** frustrated.
```

Run the checks:

| Check | Result | Why |
|---|---|---|
| Solution smuggling | **fail** | "Track my dispute" and "dispute tracking screen" are the solution. The outcome she wants is not tracking; tracking is one way to get it. |
| Root cause | **fail** | "But" and "Because" are the same fact twice. "No tracking screen" / "have not built tracking" says nothing about cause. |
| Emotion provenance | **fail** | "Frustrated" appears in no transcript. Her word was "robbed twice." |
| User vs business | pass | |
| Specificity | **fail** | Any bank could paste this unchanged. |

Four of five failed, and the draft *reads* fine. That is the trap.

---

## Final output

```markdown
## Problem Framing Canvas

### Problem Framing Narrative

**I am**: a cardholder who has just seen a charge I did not make
- Never disputed anything before; do not know the vocabulary
- Bank only on my phone; found the charge in a push alert
- Called within a day, then heard nothing for eleven days

**Trying to**:
- Stop being liable for money I did not spend, and know that I am not

**But**:
- The only way in is a phone queue, and after the call nothing tells me anything
- Each time I call back I explain it again to someone new
- I do not know whether I still owe the amount while you look into it

**Because**:
- My dispute lives in an internal work queue that was built for the ops team to
  work through, not for a customer to look at. It has a state, but that state was
  never designed to be seen by me.

**Which makes me feel**:
- "Robbed twice. Once by whoever took the money, once by the wait."
  (support transcript 1, 2026-06-09)

### Context & Constraints
- Mobile-only; no email engagement; push is the only channel that reaches her
- Regulated acknowledgement timelines apply; clock start point is an open legal
  question
- Card-scheme chargeback windows bind independently of our own SLA
- The back-office queue stays the system of record; anything customer-facing is a
  read model over it

### Final Problem Statement
- A first-time disputer needs a way to know she is no longer liable for a
  fraudulent charge, because her dispute sits in an internal queue that was never
  designed to be visible to her, which currently leaves her feeling robbed twice -
  once by the fraud and once by the silence.

### Evidence Base
- Three support call transcripts, June 2026, flagged by the CX lead
- Q2 support deck: 4,200 disputes/month, 11-day median acknowledgement, 31% of
  call minutes
- n = 3 for qualitative. Thin. Named in Assumptions.

### Validation Record
- Read aloud to: two cardholders from the support panel, 2026-07-18
- Their words we adopted: "robbed twice" - our draft said "unprotected," and the
  first reader said that was too soft
- Where they disagreed: both said the repeat-explaining was worse than the wait
  itself. Promoted from a barrier bullet to a named pain

### Assumptions to Validate
- That liability certainty matters more than refund speed - ask ten recent
  disputers to rank them. Currently rests on n = 3.
- That first-timers are the majority of disputers - one query against the dispute
  table by customer history.
- That making the existing queue state visible is sufficient, rather than needing
  a new customer-facing state model - engineering spike.
```

---

## What this example is meant to teach

1. **A fluent draft can fail four of five checks.** The first version was
   grammatical, on-topic, and useless. Running the checks is not a formality.
2. **"But" and "Because" saying the same thing is the commonest failure.** "No
   tracking screen" / "we have not built tracking" is one fact twice. The real
   cause — a queue designed for ops, not customers — is a different kind of
   statement, and it is the one that shaped the architecture.
3. **Her word beat the PM's word.** "Unprotected" was the team's framing. "Robbed
   twice" was hers, and it is the line people repeated in every later meeting.
4. **The read-aloud gate changed the scope.** Both readers said repeat-explaining
   was worse than waiting. That promoted a barrier into a named pain and put
   "never re-explain" into the spec.
5. **Removing the solution from the framing widened it.** "See my dispute status"
   admits exactly one answer. "Know I am no longer liable" admits a push
   notification, a provisional credit, or a status screen — and the cheapest of
   those turned out to be worth testing first.

---

## Provenance

Example built on the canvas in `prompts/framing-the-problem-statement.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Aurora Bank and all transcripts are fictional.
