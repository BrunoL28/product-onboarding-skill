# Epic Breakdown - Output Templates

Three schemas: the story card, the split evaluation report, and the flat board CSV.

The **CSV column order is a hard stability contract** — teams build tracker import
mappings against it. Do not reorder or rename without a version label.

---

## 1. INVEST pre-split record

```markdown
### INVEST Check: <EPIC-ID> <epic summary>

| Letter | Check | Result | Note |
|---|---|---|---|
| Independent | Buildable without another story first? | pass / fail | |
| Negotiable | What is fixed, how is open? | pass / fail | |
| Valuable | Would a user or the business notice? | pass / fail | |
| Estimable | Does the team know enough to size it? | pass / fail | |
| Testable | Is there a stateable pass condition? | pass / fail | |

**Verdict**: proceed to split / **STOP - fails Valuable, reframe first**
**Reframed as**: <if it failed Valuable, the value-bearing story it becomes>
```

---

## 2. Split evaluation report

```markdown
## Original Epic
- <EPIC-ID> <epic in canonical user-story form>
- **Too large because**: uncertainty / breadth / many variations

## Suggested Splits

1. **Split 1 using <pattern name>**
   - <smaller story in canonical user-story form>
   - <smaller story in canonical user-story form>

2. **Split 2 using <pattern name>**
   - <smaller story>
   - <smaller story>

3. **Split 3 using <pattern name>**
   - <smaller story>
   - <smaller story>

## Evaluation

| Split | Reveals droppable work? | Roughly equal sizes? | Front-loads learning? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Recommended**: Split <n> - <why, in one sentence>

## Risks and Tradeoffs
- <tradeoff 1>
- <tradeoff 2>

## Assumptions to Validate
- <assumption 1>
- <assumption 2>
```

---

## 3. Story card

```markdown
### <ID>: <summary>

- **Epic**: <EPIC-ID>
- **Type**: story / spike / enabler
- **Priority**: P0 / P1 / P2
- **Release**: <slice name>
- **Estimate**: <relative or T-shirt only>
- **Dependencies**: <IDs, or none>
- **Labels**: <comma separated>

#### Use Case
- **As a** <persona>
- **I want to** <action>
- **so that** <outcome>

#### Acceptance Criteria
- **Given** <precondition>
- **When** <one trigger>
- **Then** <one outcome>

#### Why this one first
- <the user-visible outcome this slice delivers end to end>

#### Vertical check
- <what a user could do after this ships that they could not before>
```

**Spike variant:**

```markdown
### <ID>: SPIKE - <the question>

- **Type**: spike
- **Timebox**: <e.g. 2 days>
- **Question to answer**: <one specific, answerable question>
- **What we do with each answer**: <if yes, X; if no, Y>
- **Blocks**: <story IDs>

<A spike with no stated question is a research habit, not a story.>
```

---

## 4. Board import CSV

Column order is a hard contract.

```csv
ID,Epic,Type,Summary,User Story,Acceptance Criteria,Priority,Release,Estimate,Dependencies,Labels
```

Rules:

- One row per story. Never one row per epic.
- `User Story` holds the full As a / I want to / so that on one line.
- `Acceptance Criteria` holds Given / When / Then on one line, separated by ` | `.
- Quote any field containing a comma.
- `Estimate` may be empty. An empty estimate is honest; a guessed one is not.
- `Dependencies` holds IDs, semicolon-separated.

Example row:

```csv
DE-4,DE-EPIC-2,story,"Camila sees dispute state and liability","As a first-time disputer I want to find out where my dispute stands and whether I owe the amount so that I stop wondering if I am liable","Given an open dispute | When she opens it from her card screen | Then she sees the state in plain language with liability stated",P0,Slice 1,M,DE-3,"disputes;mobile"
```

---

## Provenance

Adapted from `prompts/user-story-splitting-prompt-template.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: Richard Lawrence and Peter Green, *The
Humanizing Work Guide to Splitting User Stories*.
