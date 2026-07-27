# Opportunity Solution Tree - Worked Example

A stakeholder request at Aurora Bank turned into a tree. Aurora Bank, Camila, and
**every figure below is invented**. The part worth studying is the **ladder-down
in Question 2**, where "add a filter button" stopped being the plan and became one
leaf of nine - and the compare-and-contrast in which the requester's branch lost.

---

## Facilitation

**Agent:**

> Four questions, one at a time, then I build the tree. Pick an option, type your
> own, say "take your best guess," or drop in notes to skip ahead. Skip, go back,
> and "that's enough, build it" all work at any turn.
>
> **Question 1 of 4: the incoming request.** In the requester's own words, what
> arrived?

**User:** *(pastes)* "Customers keep phoning to ask where their dispute is. Can we
add a filter button on the transaction list so they can filter to disputed
charges? Should be quick." - Head of Customer Service.

**Agent:** Treating that as a bulk drop.

> **Found** - the request (a filter button), the symptom (repeat phone calls), and
> an implied effort claim.
> **Inferred** - the requester's target is call volume, not filtering.
> **Still missing** - which number he would accept as proof.
>
> **Question 2 of 4: the outcome behind the request.** If the filter button
> shipped and worked perfectly, what would move? This becomes the root.
>
> 1. **Repeat contacts per dispute, 3.1 to 1.5** - a product outcome your team
>    can move directly, and the closest metric to "keep phoning".
> 2. **Contact rate per active card, 0.14 to 0.10** - the Lean UX canvas root;
>    broader, and disputes are only part of it.
> 3. **Cost to serve per dispute** - what his director cares about, but it moves
>    on agent handle time too, which you do not control.
> 4. Other - type your own, or combine numbers with commentary.

**User:** 1. That's the one we can actually be held to.

**Agent:** Root set: repeat contacts per dispute, 3.1 to 1.5.

> Before I go further - a filter button is a solution, not an opportunity. Ladder
> down with me: **if she had the filter, what would it let her do?**

**User:** Find the dispute she opened last week without scrolling.

**Agent:** That is the opportunity: **"I cannot find the dispute I opened last
week."** Search, a disputes tab, pinning open disputes to the top, and a push
notification all serve it. The filter button is now one candidate of four rather
than the plan - and it will appear in the tree by name, so he can find it.

> **Question 3 of 4: evidence.** What do I read rather than infer?
>
> 1. **The JTBD canvas plus the eight discovery interviews** - I lift the
>    opportunities straight out and label the sourcing.
> 2. **Support tickets and call reasons only** - gives me frequency, not language;
>    opportunities land in company voice and I have to translate.
> 3. **Nothing yet** - the tree ships hypothesis-first with every branch tagged
>    `(Assumption)`.
> 4. Other.

**User:** 1. Canvas plus the eight interviews.

**Agent:** Then every top-level branch can carry a count, which is what makes the
sibling comparison honest.

> **Question 4 of 4: experiment appetite.** When the tree points at a first test,
> what can you actually run?
>
> 1. **Prototype test with 8 panel disputers in two weeks** - the panel exists and
>    eight is enough for a 6-of-8 pass signal.
> 2. **Painted door in the live app** - larger sample, but you would ship UI to
>    learn something an interview answers.
> 3. **Concierge: agents read a scripted liability line for two weeks** - closest
>    to real, and it needs compliance sign-off first.
> 4. Other.

**User:** 1, and we can do 3 later if it passes.

**Agent:**

> **Known**: request, root outcome, three opportunities from 8 interviews, the
> appetite. **Assumed**: sizing for OPP-2, which nobody has counted. **Open**:
> whether legal permits stating liability before the case closes. Build it?

**User:** Build it.

---

## Output

```
OUTCOME: Repeat contacts per dispute, 3.1 to 1.5, by Q4
   |
   +-- OPP-1 I cannot tell if I still owe it   **TARGET**  [Fact: 6 of 8]
   |     |
   |     +-- SOL-1a Liability line on dispute card
   |     |     |
   |     |     +-- TEST-1a1 A written line satisfies her
   |     |     +-- TEST-1a2 Legal permits stating it early
   |     |
   |     +-- SOL-1b Provisional credit at open
   |     +-- SOL-1c Plain-language state, nothing due yet
   |
   +-- OPP-2 I cannot find last week's dispute            [Fact: 3 of 8]
   |     |
   |     +-- SOL-2a Filter button on transaction list  <-- the request
   |     +-- SOL-2b Dedicated disputes tab
   |     +-- SOL-2c Pin open disputes to top
   |
   +-- OPP-3 I retell my story every call                 [Fact: 5 of 8]
         |
         +-- SOL-3a Show her what she already told us
         +-- SOL-3b Same record on the agent screen

PARKED: I do not know if my card is safe - real, but ladders to the
        fraud-operations outcome, not to this root
```

```markdown
### Target opportunity: OPP-1

| Factor | OPP-1 | OPP-2 | OPP-3 |
|---|---|---|---|
| Opportunity sizing | 6 of 8, every dispute | 3 of 8, unsized | 5 of 8, 3.1 calls |
| Market factors | Regulator favours clarity | Table stakes elsewhere | Neutral |
| Company factors | Copy plus read model | Small UI change | Needs agent tooling |
| Customer factors | Importance 9, satisfaction 2 | Importance 6, satisfaction 3 | Importance 8, satisfaction 2 |

**Chosen**: OPP-1 - against its siblings it is the most important and least
satisfied, and it is the only one every disputer hits. OPP-3 is close and is the
next target. OPP-2, where the filter request lands, is real but is reached only
after she has already decided to look, so serving it alone moves the root least.

### TEST-1a1: a written liability line satisfies her without a human

- **Hypothesis**: If Camila sees "You owe nothing while we investigate" on the
  dispute card, then she can state her liability correctly and says she would not
  call.
- **Method**: prototype test, unmoderated, panel recruits
- **Sample**: 8 disputers from the last 60 days
- **Pass signal**: 6 of 8 answer "do you owe this now?" correctly within 20
  seconds, and 5 of 8 say they would not call
- **Fail signal**: fewer than 4 of 8 say they would not call - reassurance is not
  the lever and OPP-3 becomes the target
- **Timebox**: 2 weeks
- **What we do with each answer**: if pass, SOL-1a goes to v1 and the concierge
  test follows; if fail, retarget to OPP-3.

## Decisions Made
- **Incoming request**: filter button on the transaction list (Head of CX)
- **Outcome selected as root**: repeat contacts per dispute 3.1 to 1.5 - the team
  can move it directly; cost to serve is confounded by agent handle time
- **Evidence base**: JTBD canvas plus 8 discovery interviews
- **Target opportunity**: OPP-1, on sizing and customer factors versus siblings
- **First test**: TEST-1a1, 2 weeks
- **Experiment appetite**: prototype with 8 panel disputers; concierge later

## Assumptions to Validate
- OPP-2 is unsized - one query on how many disputers reopen the app within seven
  days would size it, and it may yet outrank OPP-3.
- Legal permits stating liability before the case closes - TEST-1a2, one hour
  with compliance, blocks SOL-1a entirely if it fails.
- Liability state is derivable from the back-office record without a schema
  change - spike, 2 days.
```

---

## What this example is meant to teach

1. **The ladder-down is the whole method.** One question - "if she had the filter,
   what would it let her do?" - converted a decided feature into a named customer
   problem with four candidate answers. Nobody had to argue with the requester.
2. **The request stays in the tree.** SOL-2a is labelled `<-- the request`. Deleting
   it would have read as being ignored; placing it as one leaf of nine made the
   point without a confrontation.
3. **The stakeholder's branch lost, and the tree said why.** OPP-2 was compared
   only against its siblings, on four factors, with the counts visible. That is a
   different conversation from "we decided not to do your thing."
4. **Parked is not deleted.** Card safety is a real need that ladders to a
   different root, so it sits on the PARKED line - seen, not missed.
5. **The pass signal was fixed before the test ran**, and the unsized branch was
   labelled rather than estimated. Set afterwards, any result would have read as
   encouraging; guessed, the OPP-2 count would have decided the target.

---

## Provenance

Example built on the schema in
`workshops/opportunity-solution-tree-workshop.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Framework: Teresa Torres, *Continuous Discovery
Habits*. Aurora Bank, Camila, the interviews, and all figures are fictional.
