# User Story - Worked Example

Stories and the story map for Aurora Bank's *Disputa Express*. Fictional.

The useful parts: a story that **fails all three line tests**, a story that
**trips the split signal**, and a release slice that cuts across the backbone
instead of down it.

---

## A story that fails all three lines

First draft from the team's backlog:

```markdown
- **As a** user
- **I want to** click the dispute status button
- **so that** I can see the dispute status
```

| Line | Verdict | Why |
|---|---|---|
| As a | fail | User. Discovery produced Cardholder Camila, a first-time disputer, mobile-only. |
| I want to | fail | Names a button. The action is not clicking; it is finding out where things stand. |
| so that | fail | Restates the line above with the words reordered. |

**Agent:** Asking why three times on the so that line — why does she want to see
the status?

**User:** So she knows what's happening.

**Agent:** And why does she want to know what's happening?

**User:** So she knows whether she still has to pay the charge.

**Agent:** That is the motivation. It is a liability question, not a status
question — which also means a status chip reading *under review* would not satisfy
this story.

Rewritten:

```markdown
### User Story US-4

- **Summary**: Camila sees where her dispute stands without calling

#### Use Case:
- **As a** first-time disputer who has already reported a fraudulent charge
- **I want to** find out where my dispute stands and whether I owe the amount
- **so that** I stop wondering whether I am still liable for money I did not spend

#### Acceptance Criteria:
- **Scenario**: Camila opens the app during the wait
- **Given**: Camila has an open dispute
- **and Given**: she is signed in on her registered device
- **and Given**: the dispute has a state in the back-office queue
- **When**: she opens the dispute from her card screen
- **Then**: she sees the current state in plain language, with her liability for
  the disputed amount stated explicitly

#### Negative Case:
- **Given**: the back-office state is an internal code with no customer mapping
- **When**: she opens the dispute
- **Then**: the app must NOT display the raw internal code or an empty state

#### Notes
- **Open questions**: the exact liability wording needs legal sign-off. Not
  inventing the copy here.
- **Estimate**: blank - engineering owns this
```

---

## A story that trips the split signal

Proposed:

```markdown
- **When**: the back office changes the dispute state
- **Then**: Camila sees the new state in the app
- **When**: the dispute is resolved
- **Then**: Camila receives a push notification with the outcome
```

**Agent:**

> Split signal. Two Whens, two Thens — two triggers and two outcomes.
>
> **Proposed stories:**
> 1. **US-5** - Camila sees state changes reflected in the app. When the back
>    office changes state / Then the app shows the new state.
> 2. **US-6** - Camila is told the outcome without opening the app. When the
>    dispute resolves / Then she receives a push with the outcome.
>
> **Which ships first:** US-5. It completes a thinner end-to-end path — state
> exists and is visible — and US-6 depends on it. Push without a state model is a
> notification with nothing behind it.
>
> **Handoff:** `epic-breakdown-advisor` for the full pattern evaluation. This looks
> like Simple/Complex on the notification side.

---

## The story map

```markdown
## User Story Map: Disputa Express

### Who

#### Segment:
- Consumer cardholders, first dispute

#### Persona:
- Cardholder Camila - mobile-only, no dispute vocabulary

### Backbone

#### Narrative:
- Notice a charge she did not make, get liability removed, know that she has

#### Activities:
1. Notice the charge
2. Open a dispute
3. Wait and track
4. Receive the outcome

#### Steps:

For Notice the charge:
- Step 1: See push alert for charge
- Step 2: Recognise charge as not hers
- Step 3: Find the dispute entry point

For Open a dispute:
- Step 1: Confirm which transaction
- Step 2: State the reason
- Step 3: Submit and get confirmation

For Wait and track:
- Step 1: Check current state
- Step 2: Understand liability meanwhile
- Step 3: Get notified on change

For Receive the outcome:
- Step 1: See the decision
- Step 2: Understand what happens next

#### Stories:

Under Notice the charge, Step 3:
- US-1 Dispute entry from transaction row
- US-2 Scheme deadline warning before entry

Under Open a dispute, Step 3:
- US-3 Submit dispute and get a reference

Under Wait and track:
- US-4 See current state and liability
- US-5 State changes reflected in app
- US-6 Push on resolution

Under Receive the outcome:
- US-7 Plain-language decision with next steps

### Release Slices

#### Slice 1 - Walking Skeleton
- Camila opens a dispute, sees one state, learns the outcome. Thin at every step,
  complete end to end.
- Stories: US-1, US-3, US-4, US-7

#### Slice 2
- She stops having to check. Live state plus push.
- Stories: US-5, US-6

#### Slice 3
- Fewer disputes opened too late to win.
- Stories: US-2

### Out of the Map
- Evidence upload - 78% of first-timer disputes need no document, and it was
  two-thirds of the estimate. Explicit non-goal in SPEC.md.
- Merchant disputes as distinct from fraud - different journey, different persona.

### Assumptions to Validate
- That US-4 satisfies the liability question without a human, per the Lean UX
  Box 7 experiment.
- That push reaches her, given zero email engagement.
```

---

## What this example is meant to teach

1. **Why three times found the real story.** *See the status* became *know whether
   I am still liable*, and that reframing invalidated the obvious solution: a
   status chip reading under review answers the first and not the second.
2. **The split signal needs no seniority to spot.** Two Whens. Anyone on the team
   can catch that, which is precisely why the rule is worth enforcing mechanically.
3. **The negative case caught a real defect class.** Without *must not display the
   raw internal code*, the first build would have leaked ops codes to customers —
   the predictable failure when you put a read model over a system built for
   internal use.
4. **Slice 1 cuts across the backbone, not down it.** US-1, US-3, US-4, US-7 touch
   all four activities thinly. The tempting alternative — perfecting Notice and
   Open first — would have shipped a beautiful form leading to the same silence
   the problem statement was about.
5. **Open questions stay open in the story too.** The liability wording is a legal
   decision. Inventing the copy would have hidden a compliance dependency inside
   an acceptance criterion.

---

## Provenance

Example built on the schemas in `prompts/user-story-prompt-template.md` and
`prompts/user-story-mapping.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Aurora Bank is fictional; all figures invented.
