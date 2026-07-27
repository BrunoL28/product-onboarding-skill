# Opportunity Solution Tree - Output Templates

Two artifacts: **the tree** and **the decision summary**. The tree is rendered as
ASCII so it survives a paste into a ticket, a wiki, or a Slack message. Node
labels are a stability contract - `OPP-n` and `SOL-na` identifiers get referenced
from stories, tests, and prioritisation scores. Never renumber a shipped tree.

**Sticky-Note Rule:** every node 4-8 words, ASCII only, no emoji. Hypothesis and
pass-signal lines are the only exceptions.

---

## 1. The ASCII tree

Four levels. Assumption tests hang only under the target opportunity's solutions.

```
OUTCOME: <metric> from <baseline> to <target>
   |
   +-- OPP-1 <"I cannot ..." in the customer's voice>          [evidence tag]
   |     |
   |     +-- SOL-1a <candidate solution, 4-8 words>
   |     +-- SOL-1b <candidate solution>
   |     +-- SOL-1c <candidate solution>
   |
   +-- OPP-2 <"I struggle to ..."> **TARGET**                  [evidence tag]
   |     |
   |     +-- SOL-2a <candidate solution>
   |     |     |
   |     |     +-- TEST-2a1 <assumption under test>
   |     |     +-- TEST-2a2 <assumption under test>
   |     |
   |     +-- SOL-2b <candidate solution>
   |
   +-- OPP-3 <"I worry that ...">                              [evidence tag]
         |
         +-- SOL-3a <candidate solution>
         +-- SOL-3b <candidate solution>

PARKED: <opportunity that is real but does not ladder to this root>
```

Evidence tags: `[Fact: n interviews]`, `[Inference]`, `[Assumption]`.

---

## 2. The written tree

```markdown
## Opportunity Solution Tree: <initiative>

- **Incoming request**: <verbatim, in the requester's words>
- **Where it landed in the tree**: <SOL-na>
- **Date**: <YYYY-MM-DD>

### Desired Outcome (root)
- <metric> from <baseline> to <target>, by <horizon>
- **Type**: product outcome / business outcome
- **Why this root**: <one sentence>

### Opportunities

| ID | Opportunity (customer's voice) | Evidence | Sized? |
|---|---|---|---|
| OPP-1 | I cannot ... | <source> | <n per month / unsized> |
| OPP-2 | I struggle to ... | <source> | <...> |
| OPP-3 | I worry that ... | <source> | <...> |

### Target opportunity: OPP-<n>

| Factor | OPP-1 | OPP-2 | OPP-3 |
|---|---|---|---|
| Opportunity sizing | | | |
| Market factors | | | |
| Company factors | | | |
| Customer factors | | | |

**Chosen**: OPP-<n> - <one sentence, comparing it to its siblings only>

### Solutions under the target

| ID | Solution | Serves | Note |
|---|---|---|---|
| SOL-na | <4-8 words> | OPP-n | |
| SOL-nb | <4-8 words> | OPP-n | |
```

---

## 3. Assumption map and test card

```markdown
### Assumptions behind SOL-<na>

| # | Assumption | Category | Importance | Evidence | Test? |
|---|---|---|---|---|---|
| 1 | <must be true> | desirability | high / low | strong / weak | yes / no |
| 2 | <must be true> | viability | | | |
| 3 | <must be true> | feasibility | | | |
| 4 | <must be true> | usability / ethical | | | |

Test the assumptions that are **high importance and weak evidence**. Nothing else.

### TEST-<na1>: <the assumption in one line>

- **Hypothesis**: If <simulation>, then <observable behaviour>.
- **Method**: <story-based interview / one-question survey / prototype / painted door>
- **Sample**: <who, how many>
- **Pass signal**: <fixed before running, e.g. 6 of 8 within 20 seconds>
- **Fail signal**: <what would make us drop or rework SOL-na>
- **Timebox**: <days>
- **What we do with each answer**: if pass, <X>; if fail, <Y>
```

---

## 4. Decision summary

```markdown
## Decisions Made
- **Incoming request**: <verbatim>
- **Outcome selected as root**: <metric movement> - <why>
- **Evidence base**: <n interviews / tickets / assumption-first>
- **Target opportunity**: OPP-<n> - <why, versus its siblings>
- **First test**: TEST-<na1>, <timebox>
- **Experiment appetite**: <what the team can actually run>

## Assumptions to Validate
- <unevidenced opportunity> - test: <cheapest thing that settles it>
- <unsized branch> - test: <the one query that sizes it>
- <untested assumption behind the target solution> - test: <...>
```

---

## Field rules

- **One root.** Two roots is two trees. Split the artifact rather than the metric.
- **Opportunities never contain a UI noun.** No button, tab, screen, dashboard,
  filter, or report appears at the opportunity level. If one does, it is a
  solution and belongs a level down.
- **Opportunities cannot be done.** They are addressed, reduced, or served. A node
  that could be ticked off is a solution.
- **The incoming request must appear.** Delete it and the requester will conclude
  they were ignored. Place it as a leaf, with its ID, and point at it.
- **Only one TARGET marker.** Two targets is a roadmap with a new name.
- **Pass signals are set before running.** A test whose threshold is decided after
  the data arrives has validated nothing.
- **Parked opportunities stay visible**, in the PARKED line, not in the bin.
- **Assumptions to Validate is never empty.**

---

## Provenance

Adapted from `workshops/opportunity-solution-tree-workshop.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Framework: Teresa Torres, *Continuous Discovery
Habits* - opportunity solution trees, compare and contrast, assumption mapping
and assumption testing.
