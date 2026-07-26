# Product Onboarding - Output Templates

The orchestrator emits four things of its own: the `INDEX.md` state file, a
phase-gate summary, a phase handoff block, and the closing readout. Sub-skill
artifacts use their own `template.md`.

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
- **Board target**: none | nextcloud-deck | jira | linear
- **Working language**: <language>

## Artifacts

| # | Phase | Artifact | Status | Updated | Notes |
|---|---|---|---|---|---|
| 1 | Discovery | COMPANY_RESEARCH.md | pending / in-progress / done | | |
| 2 | Discovery | PESTEL.md | pending | | |
| 3 | Discovery | PROTO_PERSONA.md | pending | | |
| 4 | Discovery | PROBLEM_STATEMENT.md | pending | | |
| 5 | Requirements | LEAN_UX_CANVAS.md | pending | | |
| 6 | Requirements | USER_STORY_MAP.md | pending | | |
| 7 | Requirements | SPEC.md | pending | | |
| 8 | PRD | PRD.md | pending | | |
| 9 | Delivery | EPIC_BREAKDOWN.md | pending | | |
| 10 | Delivery | board_import.csv | pending | | |
| 11 | Delivery | ROADMAP.md | pending | | |
| 12 | Strategy | STRATEGY_SESSION.md | pending | | |

## Gates passed

| Phase | Gate question | Passed on | Confirmed by |
|---|---|---|---|
| 1 | Does the problem statement resonate? | | |
| 2 | Is the scope and the non-goals list agreed? | | |
| 3 | Is the PRD reviewed, with open decisions still open? | | |
| 4 | Is the sequence credible to engineering? | | |

## Open decisions

| # | Decision | Owner | Needed by | Blocking? |
|---|---|---|---|---|
| 1 | | | | |

## Assumptions to Validate

- <assumption carried forward, with the artifact it came from>
```

---

## 2. Phase-gate summary block

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

## 3. Phase handoff block

Opens each phase. It makes the chain auditable: if a phase cannot cite the one
before it, the chain is broken.

```markdown
### Starting Phase <N>: <phase name>

**Carrying forward**
- From <ARTIFACT.md>: <the specific line or finding this phase depends on>

**Sub-skills in this phase**
- <skill-name> -> <artifact it will produce>

**Not yet resolved, and this phase will not resolve it**
- <item> - stays open
```

---

## 4. Closing readout

```markdown
# <Product Name> - Onboarding Readout

## The problem
<Two sentences, in the persona's language.>

## The scoped v1
<What is in, in one paragraph. Then the three loudest non-goals.>

## How it gets built
<Walking skeleton first, then the release sequence in one line each.>

## Riskiest assumption
<The one that would invalidate the most work, and the cheapest test for it.>

## Decisions needing an owner
| Decision | Owner | Needed by | Blocking? |
|---|---|---|---|

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
