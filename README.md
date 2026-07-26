# product-onboarding

An installable Claude plugin that takes a product from a raw idea to a
board-ready backlog, by orchestrating eleven product-management skills across
five phases.

The plugin **bundles every skill it needs**. Install once and you have the
orchestrator plus all sub-skills — no "assumes you already have these."

---

## What is in the box

```
.claude-plugin/
  plugin.json           # plugin manifest
  marketplace.json      # lets this repo be added as a marketplace
CONVENTIONS.md          # the skill authoring contract (read before editing)
ATTRIBUTION.md          # licensing: what is MIT, what is CC BY-NC-SA 4.0
skills/
  product-onboarding/   # the orchestrator - start here
  company-research/           pestel-analysis/
  proto-persona/              problem-statement/
  lean-ux-canvas/             user-story/
  write-spec/                 prd-development/
  epic-breakdown-advisor/     roadmap-planning/
  product-strategy-session/
```

Every skill directory has the same three parts:

```
skills/<name>/
  SKILL.md      # how the model behaves
  template.md   # the stable output schema it must emit
  examples/     # a worked example: the conversation AND the artifact
```

That structure is the main change in `0.2.0`. Previously the skills carried the
method but no output contract and no examples, which meant the same skill could
produce a different shape every run — fine for a chat, useless for anything you
export into Jira.

---

## The five phases

| Phase | Goal | Skills chained | Artifacts |
|---|---|---|---|
| 1 - Discovery | Understand market, user, problem | `company-research`, `pestel-analysis`, `proto-persona`, `problem-statement` | `COMPANY_RESEARCH.md`, `PESTEL.md`, `PROTO_PERSONA.md`, `PROBLEM_STATEMENT.md` |
| 2 - Requirements and Scope | Frame what to build | `lean-ux-canvas`, `user-story`, `write-spec` | `LEAN_UX_CANVAS.md`, `USER_STORY_MAP.md`, `SPEC.md` |
| 3 - PRD | Consolidate into one document | `prd-development` | `PRD.md` |
| 4 - Delivery Planning | Make it buildable | `epic-breakdown-advisor`, `roadmap-planning` | `EPIC_BREAKDOWN.md`, `board_import.csv`, `ROADMAP.md` |
| 5 - Strategy Session | Stress-test the whole thing | `product-strategy-session` | `STRATEGY_SESSION.md` |

Each phase consumes the previous phase's artifact and ends at a confirmation
gate, so discovery cannot be skipped on the way to a PRD.

---

## Install

**As a plugin (recommended).** Add this repo as a marketplace, then install:

```
/plugin marketplace add BrunoL28/product-onboarding-skill
/plugin install product-onboarding
```

**Manually.** Copy the directories under `skills/` into your skills directory —
`~/.claude/skills/` for personal use, or `<repo>/.claude/skills/` for a single
project. The orchestrator is `skills/product-onboarding/`.

Then trigger it in plain language:

- "onboard a new product"
- "run discovery for this idea and turn it into a PRD and backlog"
- "bootstrap this product from scratch"

Or call a single skill directly: "write a PESTEL for this," "split this epic,"
"draft the problem statement."

---

## The running example

Every skill's `examples/` directory works the same fictional product, so you can
read the whole chain and watch one idea turn into a backlog:

> **Aurora Bank** is a mid-size digital bank. Card fraud disputes are handled by
> phone, take 11 days to acknowledge, and drive the highest call volume of any
> journey. The proposed product, **Disputa Express**, lets a cardholder open and
> track a dispute in-app. The protagonist persona is **Cardholder Camila**.

Start at [`skills/product-onboarding/examples/aurora-bank-walkthrough.md`](skills/product-onboarding/examples/aurora-bank-walkthrough.md)
for the orchestrated version, then read any individual skill's example for the
detail of that step.

The example is deliberately fictional. Every number in it is invented and
labelled as such — which is also the behaviour the skills demand of themselves.

---

## How the skills are written

All twelve skills follow one architecture, documented in
[CONVENTIONS.md](CONVENTIONS.md):

- **Five blocks** — Context, Instruction, Parameter, Output, Validation.
- **One declared interaction mode** — facilitation, checkpointed
  co-construction, or autonomous investigation. The mode decides who asks, who
  waits, and what happens when nobody answers.
- **Generative Guidance v2** for facilitation skills — budgeted questions, one
  at a time, three context-aware options plus Other, and two standing bypasses
  ("take your best guess" and bulk drop) that are always honoured.
- **Required Context Keys and a Missing Context Rule** — at most three targeted
  questions, then proceed with labelled assumptions. Never stall, never invent.
- **Template stability** — output schemas are contracts. Change one only as a
  labelled new version with a migration note.
- **Evidence honesty** — Fact / Inference / Assumption labels, a domain-specific
  do-not-invent list, and an "Assumptions to Validate" section closing every
  artifact.
- **A Final Step block** — exactly four next options, recommended first.

If you are editing a skill, the authoring checklist at the end of
`CONVENTIONS.md` is the thing to run through before committing.

---

## Attribution and licence

This plugin is a mix of original and adapted work under two licences. The short
version:

- The orchestrator, the plugin scaffolding, and this README are **MIT**.
- The sub-skills adapted from
  [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
  by Dean Peters, and `CONVENTIONS.md`, are **CC BY-NC-SA 4.0** — attribution,
  share-alike, non-commercial.

> Adapted from [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
> by Dean Peters, CC BY-NC-SA 4.0.

Read [ATTRIBUTION.md](ATTRIBUTION.md) for the full breakdown, the ShareAlike and
non-commercial implications, and credit for the underlying frameworks.
