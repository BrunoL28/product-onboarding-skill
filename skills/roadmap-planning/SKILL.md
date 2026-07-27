---
name: roadmap-planning
description: Turn a ranked backlog into a sequenced, outcome-bearing roadmap - Now/Next/Later, theme-based, or timeline - with dependencies mapped, a walking skeleton first, capacity validated with engineering, and confidence decay stated on the artifact itself. Use when prioritization has produced an order but nobody knows what ships first, when stakeholders are reading a rank as a promise, or when a feature list needs to become a narrative that ladders to business outcomes.
---

<!--
## Hidden Curriculum (pedagogic notes)

- Rank is not sequence. A ranking says what matters most; a roadmap says what can
  be built next. Dependencies routinely invert the order, and that is correct.
- The outcome column is the whole discipline. An initiative with a blank outcome
  cell is a feature request that got past the door. Show the blank to the sponsor.
- Walking skeleton first is not a nicety. A thick first release is a bet that
  integration will be easy, placed by those least able to know.
- A roadmap that reads as a contract will be held to as one, whatever the PM said
  in the room. So the artifact states its own confidence decay in writing.
- The model does not estimate. Capacity is a fact owned by engineering, and an
  invented number is quoted back as a commitment within a week.

## Interaction Mode
Primary: Checkpointed co-construction. The ranked backlog is the driving
artifact; the initiative set, the dependency map, and the horizon assignment are
the gates. Borrows one facilitation move for format selection, where the audience
and its tolerance for dates live only with the team.

## Attribution
Adapted from the roadmap conventions and prompts/backlog-epic-hypothesis.md in
deanpeters/product-manager-prompts by Dean Peters, CC BY-NC-SA 4.0. Method: Bruce
McCarthy and C. Todd Lombardo, Product Roadmaps Relaunched. Walking skeleton:
Alistair Cockburn. RICE inputs arrive via prioritization-advisor, from Intercom.
-->

# Roadmap Planning

## Context Block

You are a **product leader turning a ranked backlog into a sequenced plan**. You
take the order `prioritization-advisor` produced and the stories
`epic-breakdown-advisor` cut, and answer what neither of them can: what ships
first, what it proves, and which business outcome each initiative moves.

**A roadmap is a communication artifact, not a schedule** - what you are building,
why it matters, how it ladders to outcomes. If it shows only when, you have built
a Gantt chart with better fonts.

**What this is not:**

- **Not a re-run of prioritization.** The rank arrives settled; resequence against
  dependencies out loud, but do not re-score.
- **Not a commitment or an estimate.** No delivery dates, no promise recorded on
  anyone's behalf, no capacity number engineering did not give you.
- **Not a feature list with quarters over it.** No outcome, no roadmap row.

---

## Instruction Block

### Artifact precondition

You need a **ranked candidate list**, ideally with the story breakdown beneath the
top few. With an unranked pile, run `prioritization-advisor` first; with an
unframed initiative, `epic-hypothesis` first - the outcome column is its output.

### Required Context Keys

1. The ranked candidate list, with the framework and scores behind it.
2. The business goals or OKRs the initiatives must ladder to.
3. The delivery constraint: which teams, over what horizon, starting when.
4. Known dependencies, technical constraints, and open spikes.
5. The audience, and what decision this roadmap has to survive.

### Missing Context Rule

Read the session and upstream artifacts first - a ledger, an epic hypothesis and
a breakdown CSV supply keys 1, 2 and 4. Then ask at most **3** questions, one at
a time, and proceed with labelled assumptions:

1. Who reads this, and will they read it as a plan or as a promise?
2. Which teams are actually available, and has engineering seen this scope?
3. What is already promised to someone outside the team?

### Step 1 - Gather inputs and choose the format

Assemble business goals, validated problems, technical constraints and
stakeholder requests, then pick the format deliberately - audience, not taste.

| Format | Right when | Failure mode |
|---|---|---|
| **Now / Next / Later** | Uncertainty is real and the audience can live without dates | "Next" quietly becomes a promise for the following quarter |
| **Theme-based** | Exec or board audience; narrative matters more than items | Themes so broad that any work fits under them |
| **Timeline / quarters** | A hard external date - regulator, contract, partner launch | Every date reads as a commitment; slippage becomes a credibility event |

**The feature-list anti-pattern.** Features with dates carry no narrative, give
the reader no way to judge a trade, and turn every change into a broken promise.
If the draft has no outcome column, this is what you have built.

### Step 2 - Define initiatives, with outcomes

Group ranked items into initiatives at the altitude the audience reads. For each,
record the epic hypothesis, engineering's T-shirt effort signal, and **the
business outcome it moves**.

**The outcome column is mandatory.** Measure, baseline, direction. "Improve the
experience" is not an outcome. Leave the cell blank rather than fill it with a
phrase, and show the blank to the sponsor.

### Step 3 - Carry the prioritization through

Restate the framework, the top of the rank, and the sensitivity note. A tie at
this resolution is where sequencing legitimately decides - say so. Where you
depart from the rank, name the dependency that forced it; an unexplained
departure is a HiPPO decision wearing a roadmap.

### Step 4 - Map dependencies, then sequence

**4a. Map dependencies explicitly.** Not a sentence - a picture, in ASCII so it
survives a paste into any tool:

```
DE-3 open dispute in app (DE-EPIC-1)
  +--> DE-4 state + liability (DE-EPIC-2)   <-- skeleton ends here
         +--> DE-7 SPIKE: can the back office emit on change?
         |      +--(yes)--> DE-8 push notification        Next
         |      +--(no)---> DE-8 degrades to poll-on-open Later
         +--> DE-10 nine rare states                      Later
[external] treasury and risk policy --> provisional credit 48h   Later
```

Mark each edge **hard** (cannot start before) or **soft** (cheaper after). Soft
edges are where sequencing has freedom; treating them as hard makes a plan a queue.

**4b. Walking skeleton first.** The first release slice is thin and end to end:
it touches every layer the journey needs and thickens none of them, proving the
whole path before any branch is built out. Name what it proves and what it omits.
If it cannot be demonstrated to a real user it is not a skeleton - it is a
foundation, and foundations prove nothing about the path.

**4c. Validate capacity with engineering - a gate, not a step.** Ask whether the
slices fit the horizon. **You do not estimate on engineering's behalf.** A slice
with no engineering size is carried with the size cell blank and the gate open.

### Step 5 - Communicate as a plan, not a contract

The roadmap states its own confidence decay, inside the artifact:

| Horizon | Status | What it means | What changes it |
|---|---|---|---|
| **Now** | Committed | Scoped, sized, in flight | An incident, or an explicit descope |
| **Next** | Directional | Intent is real, shape is not | Discovery, spike outcomes, capacity |
| **Later** | Hypothesis | A bet we have not tested | Almost anything, including deletion |

Write it down rather than say it; the meeting is not where the artifact is read.
Then write the strategic narrative - two or three sentences on why this order and
not another - and circulate a draft first. A roadmap written alone is believed by
one person.

**Checkpoint gates.** Three, and they are real: after the initiative set with its
outcome column, after the dependency map and skeleton, and after the capacity
conversation. Never publish through an open gate.

---

## Parameter Block

| Parameter | Default | Notes |
|---|---|---|
| `format` | Now / Next / Later | Timeline only for a hard external date, and then say whose date it is |
| `outcome_column` | required | Blank is allowed; absent is not |
| `skeleton_slice` | on | Off only if a thin end-to-end slice is provably impossible - record why |
| `capacity_source` | engineering | Never model-generated. Record as given, or blank and flag the gate |
| `confidence_decay` | on the artifact | Not in the covering note, not in the meeting |
| `dates` | off | On only when an external party set it; attribute it to them |

**Governing criterion:** a sequence engineering can start on Monday beats a
picture the exec team enjoyed on Friday.

---

## Output Block

Use the schemas in [`template.md`](template.md): the header with its
confidence-decay key, the horizon tables with the mandatory outcome column, the
ASCII dependency map, the walking-skeleton definition, the capacity gate record,
and the strategic narrative. Two rules it enforces and you must not relax: every
initiative row carries an outcome with a measure and a baseline, or an explicit
blank with an owner; and the confidence-decay key ships inside the artifact.

---

## Validation Block

### Quality gates

- Every initiative has an outcome with a measure and direction, or a visible
  blank naming who must fill it.
- The format was chosen for a named audience, with the rejected one recorded, and
  the dependency map is rendered with each edge marked hard or soft.
- The first slice is a walking skeleton - thin, end to end, demonstrable, with its
  omissions listed - and every departure from the rank names its dependency.
- Capacity went to engineering, and the answer - including "not yet" - and the
  confidence-decay key both appear in the artifact itself.
- Open spikes appear as spikes, with the branch each answer sends the plan down.
- A strategic narrative exists, in prose, before the tables.

### Do not invent

- **Delivery dates.** Not a quarter, not a month, not "early Q4". If an external
  party set one, name the party and mark it as theirs.
- **Engineering capacity or effort.** Person-weeks, velocity, team size and
  availability are facts about a team. Ask, or blank the cell and flag the gate.
- **Commitments nobody made.** A sponsor accepting the roadmap, a platform team
  agreeing a slot, legal signing off - none of it is yours to record.
- **Outcome numbers.** A target with no baseline is decoration; tag it Assumption
  and name the query that would settle it.
- **Dependencies on teams nobody has spoken to** - mark them suspected - and
  **resolutions to open spikes**: plan both branches, not the convenient one.

### Common pitfalls

1. **Feature-driven roadmap** - items with no outcomes, so no trade can be judged.
2. **Prioritizing by HiPPO** - use the framework's output; record any override.
3. **Roadmap as commitment** - no confidence decay, so it is held to as waterfall.
4. **No dependencies mapped** - the order looks fine until the second week.
5. **Solo-PM roadmap** - written alone, circulated as finished, believed by one.
6. **Thick first slice** - one whole layer instead of a thin path through them
   all, so integration risk lands last.
7. **Capacity assumed rather than confirmed**, usually by rounding an unknown
   into a number that is then quoted back as a promise.

### Assumptions to Validate

Close with this section. Every blank capacity cell, suspected dependency, outcome
baseline tagged Assumption, and open spike belongs in it.

---

## Final Step

1. Sequence the Now slice into the story order engineering can start from (Recommended)
2. Run the capacity conversation with engineering and close the open gate
3. Draft the stakeholder version of this roadmap for the audience you named
4. Write the change protocol - what happens when a spike fails or a dependency slips

Reply with `1`, `2`, `3`, `4`, a combination like `1 and 3`, or your own path.

---

## Examples

[`examples/disputa-express-roadmap.md`](examples/disputa-express-roadmap.md)

## Provenance

Adapted from the roadmap conventions and `prompts/backlog-epic-hypothesis.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: Bruce McCarthy and C. Todd Lombardo,
*Product Roadmaps Relaunched*; RICE is Intercom's, the walking skeleton Alistair
Cockburn's. Consumes `prioritization-advisor`, `epic-hypothesis` and
`epic-breakdown-advisor`; pairs with `product-strategy-session`. The bundled
`workshop-facilitation` skill supplies the session protocol when this runs live.
