# Roadmap - Worked Example

Sequencing Q3 for Aurora Bank's *Disputa Express*, the in-app card dispute
journey. Aurora Bank is fictional and **every figure below is invented**.

This picks up exactly where two upstream artifacts stopped:

- `prioritization-advisor` produced a RICE ranking of seven candidates, a
  sensitivity note calling the top two a tie, and one row left unscored.
- `epic-breakdown-advisor` split `DE-EPIC-2` into stories DE-3, DE-4, DE-7
  (spike), DE-8 and DE-10, and deprioritised DE-10 out of the first slice.
- `epic-hypothesis` set the outcome: contact rate per active card, 0.14 today,
  confirm at 0.115 or below over six weeks, falsify above 0.135.

The useful parts: **an outcome cell left deliberately blank**, **a capacity
number the agent refused to produce**, and **an ID collision that only surfaced
when the two artifacts were laid side by side**.

---

## What arrived, and the format argument

**Agent:**

> I have the ranking, the breakdown and the hypothesis, so I am not interviewing
> you about scope. One question that no upstream artifact answers: **who reads
> this, and will they read it as a plan or as a promise?**

**User:** The quarterly steering group. They asked for it by quarter, with dates.

**Agent:**

> Then say whose dates. Is there a regulator deadline, a contract, or a partner
> launch behind Q3?

**User:** No. They just like seeing quarters.

**Agent:** Timeline format costs you the thing you most need this quarter, which
is the freedom to change DE-8 when the spike lands. Every date in a timeline
roadmap reads as a commitment, and the first slip becomes a credibility event
rather than a learning. I recommend **Now / Next / Later**, with the confidence
key printed on the artifact so the steering group can see what "Next" is worth.

**User:** They'll ask when.

**Agent:** They will, and the honest answer is in the capacity gate below, which
is currently open. Recording the rejection either way.

---

## The outcome column, and the blank

**Agent:** Six of the seven candidates have an outcome. DE-6, the guided
reason-selection wizard, does not. The prioritization run already scored it
Impact 1 and Confidence 50% on an analogy to a different product. What business
measure does it move?

**User:** It improves the quality of the dispute submission.

**Agent:** That is a description of the feature. Measured how, from what?

**User:** ...I'd have to ask ops whether rejected-for-detail is even tracked.

**Agent:** Then the cell stays blank and your name goes under the table as the
owner. I am not writing "better submission quality" into an outcome column - a
phrase in that cell is how a feature request gets onto a roadmap looking like a
bet. A blank argues for itself in the steering group.

---

## Rank, sequence, and the collision

**Agent:** The ranking put DE-2 (status in plain language) first and DE-1 (open a
dispute in app) second, and flagged them as a tie. Sequencing breaks the tie the
other way: DE-1 ships first, because DE-2 displays a dispute that DE-1 creates.
Recording that as a departure with its dependency, not as an override.

> One more thing, and it is not cosmetic. **DE-4 means two different items.** In
> the prioritization ledger it is "upload evidence in app". In the breakdown it is
> the story "Camila sees dispute state and liability". DE-7 collides too: a
> back-office re-platform candidate and a two-day spike. Both artifacts number
> from DE-1.

**User:** Nobody noticed that in either session.

**Agent:** Nobody had both open. I qualify every ID in this roadmap with its
source and log the renumbering as an action; silently picking one meaning is how
a board import puts the wrong story in the wrong slice.

---

## The capacity question

**User:** So how many weeks is the first slice? Ballpark is fine.

**Agent:** No. Engineering sized the *candidates* - DE-1 at 8 person-weeks and
DE-2 at 5 - and the walking skeleton is a thin subset of both, three common
states, one reason code, no notification. Nobody has resized it. A ballpark from
me becomes "13 weeks" in the steering deck by Thursday and a commitment by the
following Monday. The gate stays open with the question written down.

---

## The artifact

```markdown
# Disputa Express Roadmap - Q3 and beyond

- **Audience**: quarterly steering group (decides squad allocation)
- **Format**: Now / Next / Later
- **Format rejected**: Timeline - no external date exists; requested for habit
- **Prioritization input**: RICE, Q3 planning session, disputa-express-prioritization
- **Teams**: one squad (approx. 26 person-weeks per quarter) [Fact, ledger]
- **Last updated**: Q3 planning, by the PM

## How to read this roadmap

| Horizon | Status | What it means | What changes it |
|---|---|---|---|
| Now | Committed | Scoped, sized, in flight | An incident, or an explicit descope |
| Next | Directional | Intent is real, shape is not | DE-7 spike, discovery, capacity |
| Later | Hypothesis | A bet we have not tested | Almost anything, including deletion |

This is a plan, not a contract. There are no delivery dates in this document.

## Why this order

Camila cannot find out whether she still owes R$ 480 without calling, and that
call is the highest-volume contact in the journey. The first slice buys the
answer to that one question end to end and nothing else; notification, evidence
upload and provisional credit all wait behind what it teaches us.

### Now - committed

| Initiative | Outcome (measure, baseline, direction) | Stories | Size | Dependencies | Confidence |
|---|---|---|---|---|---|
| Open a dispute in the app | Disputes opened without a call: 0% -> 60% of new disputes [target = Assumption] | DE-3 (story) | 8 pw for the full candidate [Fact, eng] | none | Committed |
| See state and liability | Contact rate per active card 0.14 -> 0.115 over six weeks [Fact baseline; hypothesis target] | DE-4 (story) | 5 pw for the full candidate [Fact, eng] | DE-3 (hard) | Committed |
| Spike: back-office event emission | Decides whether push is small or absent | DE-7 (story spike, 2-day timebox) | S | none | Committed |

Guardrail for the Now slice: dispute approval rate must not move [from the epic
hypothesis].

### Next - directional

| Initiative | Outcome (measure, baseline, direction) | Stories | Size | Dependencies | Confidence |
|---|---|---|---|---|---|
| Tell her before she asks | Repeat status checks per dispute 3.1 -> 1.5 [baseline = Assumption, no instrumentation yet] | DE-8 (story) | (blank) | DE-7 spike answer (hard) | Directional |
| Evidence upload in app | Outbound document requests per dispute 0.41 -> 0.20 [Assumption, ops sample] | DE-4 (candidate) | 6 pw [Fact, eng] | DE-3 (soft) | Directional |
| Guided reason wizard | (blank - owner: PM, with ops, by end of month) | DE-6 (candidate) | 5 pw [Fact, eng] | none | Directional |

The wizard carries no outcome. It is on this roadmap provisionally and comes off
if the cell is still blank at the next review.

### Later - hypothesis

| Initiative | Outcome (measure, baseline, direction) | Condition that moves it | Confidence |
|---|---|---|---|
| Provisional credit within 48h | Complaint rate on open disputes, direction down | Treasury and risk agree the policy | Hypothesis |
| Nine rare dispute states | Blank-screen incidents, direction down (under 4% of disputes) | Slice 1 telemetry shows the generic message failing | Hypothesis |
| Back-office queue re-platform | (blank - no outcome stated by its sponsor) | Engineering produces a job size; then WSJF against DE-5 | Hypothesis |

## Dependencies

DE-3 open dispute in app (DE-EPIC-1)
  +--> DE-4 state + liability (DE-EPIC-2)   [hard]  <-- skeleton ends here
  |      +--> DE-7 SPIKE: can the back office emit on state change?
  |      |      +--(yes)--> DE-8 push notification            Next
  |      |      +--(no)---> DE-8 becomes poll-on-open, push   Later
  |      +--> DE-10 nine rare states        [soft]            Later
  +--> DE-4 (candidate) evidence upload     [soft - cheaper after, not blocked]

[external] treasury and risk policy decision
  +--> provisional credit within 48h        [hard, not ours to schedule]

## First slice - walking skeleton

- **Stories**: DE-3 + DE-4 (story)
- **What it proves**: a cardholder can open a dispute from a transaction row and
  read its state and her liability from the same screen - app, dispute service,
  back-office read and back, end to end.
- **Deliberately omits**: push notification, the nine rare states, evidence
  upload, provisional credit, all reason codes but one.
- **Demonstrable to a real user?**: yes - Camila can answer the liability
  question without calling.

## Capacity gate

- **Asked of**: engineering lead, Q3 planning session
- **Scope presented**: the skeleton (DE-3 + DE-4 thin), plus the DE-7 spike
- **Engineering response**: not yet sized
- **Sizes given**: DE-1 candidate 8 pw, DE-2 candidate 5 pw, DE-4 candidate 6 pw,
  DE-6 candidate 5 pw (all as given, for full candidates, not the thin slice)
- **Sizes still open**: the skeleton itself; DE-8, which depends on the spike
- **Status**: OPEN

## Assumptions to Validate

- Skeleton size unknown. Engineering resize needed before the Now slice is
  presented as committed. Gate OPEN.
- ID collision: DE-4 and DE-7 mean different things in the prioritization ledger
  and the breakdown. Renumber one space before any board import.
- Repeat-status-checks baseline of 3.1 is an Assumption; nothing measures it yet,
  and measuring it is part of DE-8.
- Guided reason wizard has no outcome and no measure identified.
- Treasury and risk have not been asked about provisional credit. Suspected
  dependency, not confirmed.
- DE-7 spike unresolved; both branches are planned, neither is assumed.
```

---

## What this example is meant to teach

1. **A blank outcome cell is a finding, not a gap.** The wizard survived a RICE
   score but could not name a measure, and the blank does the arguing at the
   review that the PM could not do in the room.
2. **Rank is not sequence, and the departure gets written down.** DE-2 ranked
   first and ships second because DE-1 creates the thing it displays.
3. **The skeleton is defined by what it omits.** Four omissions and one reason
   code are what make it thin enough to prove the path.
4. **The capacity gate stays open rather than getting a plausible number.** The
   ballpark that was refused is the one that would have been quoted back.
5. **Laying two artifacts side by side finds what neither session saw.** The DE-4
   collision was invisible until sequencing needed both IDs at once.

---

## Provenance

Adapted from the roadmap conventions in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: Bruce McCarthy and C. Todd Lombardo,
*Product Roadmaps Relaunched*; walking skeleton, Alistair Cockburn; RICE inputs
from Intercom's framework via `prioritization-advisor`. Aurora Bank and Disputa
Express are fictional; every number here was invented for the example.
