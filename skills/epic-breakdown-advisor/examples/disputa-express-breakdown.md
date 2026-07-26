# Epic Breakdown - Worked Example

Splitting an epic from Aurora Bank's *Disputa Express*. Fictional.

The useful parts: an epic that **fails INVEST on Valuable**, and a split evaluation
where the **winning split was the one that let the team drop work**.

---

## The epic that failed Valuable

Presented by the team:

> **DE-EPIC-2**: Build the dispute state projection and mapping service

**Agent:**

```markdown
### INVEST Check: DE-EPIC-2

| Letter | Check | Result | Note |
|---|---|---|---|
| Independent | Buildable without another story first? | pass | |
| Negotiable | What fixed, how open? | fail | The title names the implementation |
| Valuable | Would a user or the business notice? | **fail** | Nobody outside the team can tell whether a projection exists |
| Estimable | Enough known to size it? | fail | Depends on the unresolved event-hook question |
| Testable | Stateable pass condition? | pass | Technically yes, but only in engineering terms |

**Verdict**: **STOP - fails Valuable, reframe first**
```

> This is a technical task in a story's clothing. Splitting it produces smaller
> technical tasks, none of which anyone can demo.
>
> What can a customer do, once this exists, that they cannot do now?

**User:** She can see what's happening with her dispute without calling.

**Agent:** That is the epic. The projection is how, not what.

> **Reframed as DE-EPIC-2**: As a first-time disputer, I want to see what is
> happening with my dispute without calling, so that I know whether I am still
> liable.

Re-running INVEST: it now passes everything except Small, which is why we are
splitting it.

---

## Three candidate splits

```markdown
## Original Epic
- DE-EPIC-2: As a first-time disputer, I want to see what is happening with my
  dispute without calling, so that I know whether I am still liable.
- **Too large because**: breadth plus uncertainty (twelve internal state codes, and
  an unresolved event-propagation question)

## Suggested Splits

1. **Split 1 using Workflow Steps**
   - As a disputer, I want to open my dispute and see its current state, so that I
     know it exists in the system.
   - As a disputer, I want to see state changes as they happen, so that I do not
     have to keep checking.
   - As a disputer, I want to be told the final outcome, so that I know I am done.

2. **Split 2 using Data Variations (state codes)**
   - As a disputer, I want to see the three most common states in plain language,
     so that I understand the usual path.
   - As a disputer, I want to see the remaining nine states in plain language, so
     that unusual cases are not blank.

3. **Split 3 using Simple/Complex**
   - As a disputer, I want to see one state on demand when I open the app, so that
     I can check without calling.
   - As a disputer, I want to be notified when state changes, so that I do not have
     to open the app at all.

## Evaluation

| Split | Reveals droppable work? | Roughly equal sizes? | Front-loads learning? |
|---|---|---|---|
| 1 | no | roughly | partly - still needs propagation resolved in story 2 |
| 2 | **yes - strongly** | no, 3 states is far smaller than 9 | yes |
| 3 | partly | no | **yes - isolates the propagation unknown entirely** |

**Recommended**: Split 2 combined with Split 3 - Split 2 because the ops review
showed nine of the twelve internal codes account for under 4% of disputes, so the
second story is genuinely deprioritisable; Split 3 because pulling notification out
quarantines the unresolved event-hook question away from slice 1.
```

**Agent:** Which split do you want to take forward — 1, 2, 3, or a combination?

**User:** 2 and 3, as you suggested. And the nine rare states can wait.

---

## Resulting cards (excerpt)

```markdown
### DE-4: Camila sees dispute state and liability on demand

- **Epic**: DE-EPIC-2
- **Type**: story
- **Priority**: P0
- **Release**: Slice 1
- **Estimate**: M
- **Dependencies**: DE-3
- **Labels**: disputes, mobile

#### Use Case
- **As a** first-time disputer with an open dispute
- **I want to** see where it stands and whether I owe the amount
- **so that** I stop wondering whether I am still liable

#### Acceptance Criteria
- **Given** an open dispute in one of the three most common states
- **When** she opens it from her card screen
- **Then** she sees the state in plain language with liability stated explicitly

#### Why this one first
It is the thinnest slice that answers the question the problem statement is about,
and it needs no event propagation - it reads on app open.

#### Vertical check
After this ships, a customer can answer the liability question without calling.
Before it, she cannot.
```

```markdown
### DE-7: SPIKE - can the back office emit on state change?

- **Type**: spike
- **Timebox**: 2 days
- **Question to answer**: Can the back-office dispute table or Genesys emit an
  event when dispute state changes, without a schema change?
- **What we do with each answer**: If yes, DE-8 push notification is small and
  slice 2 proceeds as planned. If no, DE-8 becomes polling-on-open only, push moves
  to Later, and ADR-2 resolves to polled.
- **Blocks**: DE-8, DE-9
```

```markdown
### DE-10: The nine rare states in plain language

- **Priority**: P2
- **Release**: Later
- **Note**: Ops review found these nine codes cover under 4% of disputes. Slice 1
  shows a safe generic message for them. Deprioritised as a direct result of the
  Split 2 evaluation.
```

---

## Board CSV (excerpt)

```csv
ID,Epic,Type,Summary,User Story,Acceptance Criteria,Priority,Release,Estimate,Dependencies,Labels
DE-3,DE-EPIC-1,story,"Open a dispute from a transaction row","As a cardholder I want to start a dispute from the charge itself so that I do not have to find a form","Given a settled transaction | When she taps dispute on the row | Then a dispute is created with a reference",P0,Slice 1,M,,"disputes;mobile"
DE-4,DE-EPIC-2,story,"Camila sees dispute state and liability","As a first-time disputer I want to see where my dispute stands and whether I owe the amount so that I stop wondering if I am liable","Given an open dispute in a common state | When she opens it from her card screen | Then she sees the state in plain language with liability stated",P0,Slice 1,M,DE-3,"disputes;mobile"
DE-7,DE-EPIC-2,spike,"Can the back office emit on state change",,"Timebox 2 days | Answer decides ADR-2 | Blocks DE-8 DE-9",P0,Slice 1,S,,"spike;platform"
DE-10,DE-EPIC-2,story,"Nine rare states in plain language","As a disputer in an unusual state I want a meaningful message so that the screen is not blank","Given a dispute in one of nine rare states | When she opens it | Then she sees a specific message rather than a generic one",P2,Later,M,DE-4,"disputes"
```

Note `DE-7` has an empty `User Story` field — a spike has no user story, and
inventing one would be worse than leaving it blank.

---

## What this example is meant to teach

1. **Failing Valuable is the most useful INVEST outcome.** *Build the projection and
   mapping service* would have split into four smaller invisible tasks. Reframing it
   around what a customer can do produced an epic that could be sliced meaningfully.
2. **The best split was the one that let them drop work.** Split 2 surfaced that
   nine of twelve state codes cover under 4% of disputes. That is a P2 the team
   would otherwise have built in slice 1 without noticing.
3. **Combining two patterns beat picking one.** Split 2 handled breadth; Split 3
   quarantined the uncertainty. The flowchart says try patterns in order, not use
   exactly one.
4. **The spike names a question and both answers.** If yes X, if no Y is what
   separates a spike from an open-ended investigation, and here it pre-decides
   ADR-2.
5. **Every card carries a vertical check.** Writing down what a user can newly do is
   a mechanical test for horizontal slicing, and it catches it every time.

---

## Provenance

Example built on the schema in `prompts/user-story-splitting-prompt-template.md`
from [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: Richard Lawrence and Peter Green. Aurora
Bank is fictional; all figures invented.
