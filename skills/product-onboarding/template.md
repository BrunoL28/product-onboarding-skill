# Product Onboarding - Output Templates

The orchestrator emits six things of its own: the `INDEX.md` state file, the
`MEASUREMENT.md` thread, a phase-gate summary, a phase handoff block, a
gate-failure record, and the closing readout. Sub-skill artifacts use their own
`template.md`.

**Template stability.** These are contracts. Improve the facilitation freely;
change a section name only as a labelled new version with a migration note.

---

## 1. INDEX.md - the state file

Written at kickoff, updated at the end of every phase. This is the resume point.

```markdown
# <Product Name> - Product Onboarding Index

- **Product**: <one line>
- **Company / client**: <name>
- **Primary stakeholder**: <name, role>
- **Protagonist persona**: <persona name>
- **Started**: <YYYY-MM-DD>
- **Last updated**: <YYYY-MM-DD>
- **Depth**: standard | express
- **Facilitation**: solo | room
- **Board target**: none | nextcloud-deck | jira | linear
- **Working language**: <language>

## Artifacts

| # | Phase | Artifact | Status | Updated | Notes |
|---|---|---|---|---|---|
| 1 | 0 Framing | POSITIONING.md | pending / in-progress / done | | |
| 2 | 0 Framing | JTBD.md | pending | | |
| 3 | 1 Discovery | COMPANY_RESEARCH.md | pending | | |
| 4 | 1 Discovery | PESTEL.md | pending | | |
| 5 | 1 Discovery | MARKET_SIZING.md | pending | | |
| 6 | 1 Discovery | PROTO_PERSONA.md | pending | | |
| 7 | 1 Discovery | PROBLEM_STATEMENT.md | pending | | |
| 8 | 2 Requirements | LEAN_UX_CANVAS.md | pending | | |
| 9 | 2 Requirements | OPPORTUNITY_TREE.md | pending | | |
| 10 | 2 Requirements | POL_PROBES.md | pending | | |
| 11 | 2 Requirements | USER_STORY_MAP.md | pending | | |
| 12 | 2 Requirements | SPEC.md | pending | | |
| 13 | 3 PRD | PRD.md | pending | | |
| 14 | 4 Delivery | EPIC_HYPOTHESES.md | pending | | |
| 15 | 4 Delivery | PRIORITIZATION.md | pending | | |
| 16 | 4 Delivery | EPIC_BREAKDOWN.md | pending | | |
| 17 | 4 Delivery | board_import.csv | pending | | |
| 18 | 4 Delivery | ROADMAP.md | pending | | |
| 19 | 5 Strategy | STRATEGY_SESSION.md | pending | | |
| 20 | 0-4 | MEASUREMENT.md | pending | | thread, not a phase |

## Gates passed

Append a row per attempt. Never overwrite a failed attempt.

| Phase | Gate question | Result | Date | Confirmed by | Reason if failed |
|---|---|---|---|---|---|
| 0 | Can we name the customer and the job without naming the product? | | | | |
| 1 | Does the problem statement resonate with someone who lives it? | | | | |
| 2 | Is scope agreed, and does the riskiest assumption have an owned probe? | | | | |
| 3 | Is the PRD reviewed, with open decisions still open? | | | | |
| 4 | Is the sequence credible to engineering? | | | | |

## Open decisions

| # | Decision | Owner | Needed by | Blocking? |
|---|---|---|---|---|
| 1 | | | | |

## Assumptions to Validate

- <assumption carried forward, with the artifact it came from>
```

---

## 2. MEASUREMENT.md - the thread

Filled across phases, not at the end. Each row advances one column per phase, so
an empty cell is a visible gap rather than a silent one.

```markdown
# <Product Name> - Measurement Thread

A metric is not real until it has all five columns. Baseline comes from Phase 1,
target and guardrail from Phase 2, instrument from Phase 3, read-out from
Phase 4.

## Primary metrics

| Metric | Baseline (+ source) | Target | Instrument | Read-out date | Owner |
|---|---|---|---|---|---|
| <name> | <value> - <source, or [ASSUMPTION]> | <value by when> | <event, query, dashboard> | <YYYY-MM-DD> | <name> |

## Guardrail metrics

Things that must not move the wrong way while the primary metric improves.

| Guardrail | Baseline (+ source) | Must stay | Instrument | Owner |
|---|---|---|---|---|

## Not measured, and why

- <thing everyone will ask about> - <why it is not instrumented in v1>

## Assumptions to Validate

- <every baseline tagged [ASSUMPTION] belongs here>
```

---

## 3. Phase handoff block

Opens each phase. It makes the chain auditable: if a phase cannot cite the one
before it, the chain is broken.

```markdown
### Starting Phase <N>: <phase name>

**Carrying forward**
- From <ARTIFACT.md>: <the specific line or finding this phase depends on>

**Sub-skills in this phase**
- <skill-name> -> <artifact it will produce>

**Measurement thread advances to**
- <baseline | target and guardrail | instrument | read-out date>

**Not yet resolved, and this phase will not resolve it**
- <item> - stays open
```

---

## 4. Phase-gate summary block

Emitted at the end of every phase. Sticky-Note Rule applies: 4-8 words a bullet,
ASCII only.

```markdown
### Phase <N> complete: <phase name>

**Produced**
- <ARTIFACT.md> - <what it establishes>

**What we now know (Fact)**
- <finding, with source>

**What we are reading into it (Inference)**
- <inference>

**What we guessed (Assumption)**
- <assumption, and how to kill it cheaply>

**Still open**
- <open question> - suggested owner: <role>

**Gate:** <the phase's gate question>

1. Continue to Phase <N+1>: <name> (Recommended)
2. Refine <weakest artifact> before moving on
3. Go get evidence for <riskiest assumption> first
4. Stop here and hand off what exists

Reply with `1`, `2`, `3`, `4`, or your own path.
```

---

## 5. Gate-failure record

Written when a gate does not pass. Appended to `INDEX.md`, never overwritten.

```markdown
### Phase <N> gate NOT passed - <YYYY-MM-DD>

**Gate question**: <the question>
**Answer**: no
**Stated reason**: <in the reviewer's words, not paraphrased>

**Smallest thing that would change the answer**
- <one specific missing piece of evidence or one decision>

**Paths**
1. Fix <the specific gap> and re-gate (Recommended)
2. Proceed with the gap recorded as a labelled risk, carried into
   STRATEGY_SESSION.md
3. Stop here and hand off what exists

**If path 2 is taken**: this is a decision. Record it below.

| Decision | Owner | Date | Risk carried |
|---|---|---|---|
```

---

## 6. Closing readout

```markdown
# <Product Name> - Onboarding Readout

## The problem
<Two sentences, in the persona's language.>

## Who it is for, and the job it does
<One sentence each, from POSITIONING.md and JTBD.md.>

## The scoped v1
<What is in, in one paragraph. Then the three loudest non-goals.>

## How it gets built
<Walking skeleton first, then the release sequence in one line each.>

## How we will know it worked
<The primary metric with its baseline, target, instrument, and read-out date.>

## Riskiest assumption
<The one that would invalidate the most work, its probe, and the probe's status.>

## Decisions needing an owner
| Decision | Owner | Needed by | Blocking? |
|---|---|---|---|

## Gates not passed
| Phase | Reason | Risk carried |
|---|---|---|

## Artifact set
<Table from INDEX.md.>

## Assumptions to Validate
- <rolled up across all phases>
```

---

## Provenance

Original work, MIT, Bruno Lima Soares. Conventions (sticky-note rule, evidence
labels, Assumptions to Validate, Final Step) adapted from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0.
