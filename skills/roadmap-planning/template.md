# Roadmap - Output Template

One artifact in seven parts: header and confidence-decay key, strategic
narrative, horizon tables, dependency map, walking skeleton, capacity gate, and
assumptions.

Two things here are **stability contracts** and must not be quietly changed: the
initiative row columns (teams build board views against them) and the presence of
the confidence-decay key inside the artifact.

---

## 1. Header and confidence-decay key

```markdown
# <Product> Roadmap - <horizon label, e.g. next two quarters>

- **Audience**: <who reads this and what they decide with it>
- **Format**: Now / Next / Later | Theme-based | Timeline
- **Format rejected**: <the one you did not pick, and why>
- **Prioritization input**: <framework, date, artifact link>
- **Teams**: <squads this plan allocates>
- **Last updated**: <date> by <name>

## How to read this roadmap

| Horizon | Status | What it means | What changes it |
|---|---|---|---|
| Now | Committed | Scoped, sized, in flight | An incident, or an explicit descope |
| Next | Directional | Intent is real, shape is not | Discovery, spike outcomes, capacity |
| Later | Hypothesis | A bet we have not tested | Almost anything, including deletion |

This is a plan, not a contract. Nothing here is a delivery date. Dates in this
document, if any, belong to the external party named beside them.
```

---

## 2. Strategic narrative

```markdown
## Why this order

<Two or three sentences. What outcome this sequence is chasing, what it does
first and why, and what it is consciously not doing yet.>
```

Prose, before the tables. If it cannot be written, the roadmap is a feature list.

---

## 3. Horizon tables

Column order is the stability contract. One table per horizon.

```markdown
### Now - committed

| Initiative | Outcome (measure, baseline, direction) | Stories | Size | Dependencies | Confidence |
|---|---|---|---|---|---|
| <name> | <measure> from <baseline> to <target> | <IDs> | <T-shirt, from engineering> | <IDs or external> | Committed |

### Next - directional

| Initiative | Outcome (measure, baseline, direction) | Stories | Size | Dependencies | Confidence |
|---|---|---|---|---|---|
| <name> | <measure> from <baseline> to <target> | <IDs> | <or blank> | <what gates it> | Directional |

### Later - hypothesis

| Initiative | Outcome (measure, baseline, direction) | Condition that moves it | Confidence |
|---|---|---|---|
| <name> | <the outcome we believe it moves> | <what has to become true> | Hypothesis |
```

Rules:

- **The outcome cell is mandatory.** A measure, a baseline and a direction - or a
  visible blank with an owner named beneath the table. Never a phrase like
  "better experience".
- **Size comes from engineering.** Blank is a legitimate value; a guess is not.
- **Later rows carry a condition**, not a date. A Later item with no condition
  that would move it is a deletion nobody had to defend.
- Tag any number that is not sourced as **Assumption**.

---

## 4. Dependency map

ASCII, so it survives every tool the roadmap gets pasted into.

```markdown
## Dependencies

<ID> <initiative>
  +--> <ID> <initiative>        [hard]
  |      +--> <ID> SPIKE: <question>
  |             +--(yes)--> <ID> <what becomes possible>   Next
  |             +--(no)---> <ID> <the degraded shape>      Later
  +--> <ID> <initiative>        [soft - cheaper after, not blocked]

[external] <team or decision outside this plan>
  +--> <ID> <initiative>        [hard, not ours to schedule]

Hard = cannot start before. Soft = cheaper after.
```

---

## 5. Walking skeleton

```markdown
## First slice - walking skeleton

- **Stories**: <IDs>
- **What it proves**: <the whole path, in one sentence>
- **Deliberately omits**: <the branches left thin>
- **Demonstrable to a real user?**: yes / no
- **If no**: this is a foundation, not a skeleton. Say what would make it one.
```

---

## 6. Capacity gate

```markdown
## Capacity gate

- **Asked of**: <engineering lead, date>
- **Scope presented**: <slices>
- **Engineering response**: fits / does not fit / not yet sized
- **Sizes given**: <as given, verbatim>
- **Sizes still open**: <slices with no size, and the gate stays open>
- **Status**: OPEN / CLOSED

No slice moves from Next to Now while this gate is OPEN. The roadmap author does
not estimate on engineering's behalf.
```

---

## 7. Assumptions to Validate

```markdown
## Assumptions to Validate

- <every blank capacity cell, with who must fill it>
- <every suspected dependency nobody has confirmed with the other team>
- <every outcome baseline tagged Assumption, with the query that settles it>
- <every open spike, with the branch each answer sends the plan down>
```

---

## Provenance

Adapted from the roadmap conventions in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Structure follows Bruce McCarthy and C. Todd
Lombardo, *Product Roadmaps Relaunched*; walking skeleton, Alistair Cockburn.
