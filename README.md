# product-onboarding

An installable Claude plugin that takes a product from a raw idea to a
board-ready backlog, by orchestrating nineteen bundled product-management skills
across six phases.

The plugin **bundles every skill it needs**. Install once and you have the
orchestrator plus all sub-skills - no "assumes you already have these."

---

## What is in the box

```
.claude-plugin/
  plugin.json           # plugin manifest
  marketplace.json      # lets this repo be added as a marketplace
CONVENTIONS.md          # the skill authoring contract (read before editing)
ATTRIBUTION.md          # licensing: what is MIT, what is CC BY-NC-SA 4.0
CHANGELOG.md            # what changed, and when
LICENSE                 # MIT, for the original parts
LICENSE-CC-BY-NC-SA     # CC BY-NC-SA 4.0, for the adapted parts
scripts/
  validate_skills.py    # checks skills against CONVENTIONS.md
skills/
  product-onboarding/         # the orchestrator - start here

  # phase 0 - framing
  positioning-workshop/       jobs-to-be-done/

  # phase 1 - discovery
  company-research/           pestel-analysis/
  tam-sam-som-calculator/     proto-persona/
  problem-statement/

  # phase 2 - requirements and validation
  lean-ux-canvas/             opportunity-solution-tree/
  pol-probe-advisor/          user-story/
  write-spec/

  # phase 3 - prd
  prd-development/

  # phase 4 - delivery planning
  epic-hypothesis/            prioritization-advisor/
  epic-breakdown-advisor/     roadmap-planning/

  # phase 5 - strategy session
  product-strategy-session/

  # support
  workshop-facilitation/
```

Every skill directory has the same three parts:

```
skills/<name>/
  SKILL.md      # how the model behaves
  template.md   # the stable output schema it must emit
  examples/     # a worked example: the conversation AND the artifact
```

That structure arrived in `0.2.0`. Previously the skills carried the method but
no output contract and no examples, which meant the same skill could produce a
different shape every run - fine for a chat, useless for anything you export
into Jira.

---

## The phases

| Phase | Goal | Skills chained | Artifacts |
|---|---|---|---|
| 0 - Framing | Know who it is for and what job it is hired to do | `positioning-workshop`, `jobs-to-be-done` | `POSITIONING.md`, `JTBD.md` |
| 1 - Discovery | Understand market, user, problem, and whether it is worth solving | `company-research`, `pestel-analysis`, `tam-sam-som-calculator`, `proto-persona`, `problem-statement` | `COMPANY_RESEARCH.md`, `PESTEL.md`, `MARKET_SIZING.md`, `PROTO_PERSONA.md`, `PROBLEM_STATEMENT.md` |
| 2 - Requirements and Validation | Frame what to build, and probe the riskiest assumption before writing it down | `lean-ux-canvas`, `opportunity-solution-tree`, `pol-probe-advisor`, `user-story`, `write-spec` | `LEAN_UX_CANVAS.md`, `OPPORTUNITY_TREE.md`, `POL_PROBES.md`, `USER_STORY_MAP.md`, `SPEC.md` |
| 3 - PRD | Consolidate into one document | `prd-development` | `PRD.md` |
| 4 - Delivery Planning | Make it buildable and sequenced | `epic-hypothesis`, `prioritization-advisor`, `epic-breakdown-advisor`, `roadmap-planning` | `EPIC_HYPOTHESES.md`, `PRIORITIZATION.md`, `EPIC_BREAKDOWN.md`, `board_import.csv`, `ROADMAP.md` |
| 5 - Strategy Session | Stress-test the whole thing | `product-strategy-session` | `STRATEGY_SESSION.md` |
| Support | Session protocol any skill can borrow | `workshop-facilitation` | `SESSION_RECORD.md` |

Each phase consumes the previous phase's artifact and ends at a confirmation
gate, so discovery cannot be skipped on the way to a PRD.

Phase 0 exists because everything downstream was quietly assuming a segment and
a category that nobody had written down. Phase 2 is called Requirements **and
Validation**, not Requirements and Scope, because its gate asks whether the
riskiest assumption has been probed - not only whether the scope is on paper.

### The measurement thread

One document, `MEASUREMENT.md`, runs across phases 1 to 4 rather than four
disconnected metrics sections:

- **Discovery** captures the baseline. What is the number today.
- **Requirements and Validation** sets the target. What would count as better,
  and by when.
- **PRD** names the instrumentation. Which event, which table, who owns it.
- **Delivery Planning** schedules the read-out. The date someone actually looks.

If you skip a phase, the thread has a hole in it, and the artifact says so
rather than quietly filling it in.

---

## Install

**As a plugin (recommended).** Add this repo as a marketplace, then install:

```
/plugin marketplace add BrunoL28/product-onboarding-skill
/plugin install product-onboarding
```

**Manually.** Copy the directories under `skills/` into your skills directory -
`~/.claude/skills/` for personal use, or `<repo>/.claude/skills/` for a single
project. The orchestrator is `skills/product-onboarding/`.

Then trigger it in plain language:

- "onboard a new product"
- "run discovery for this idea and turn it into a PRD and backlog"
- "bootstrap this product from scratch"

Or call a single skill directly: "write a PESTEL for this," "size this market,"
"split this epic," "draft the problem statement," "what should we test first."

---

## The running example

All twenty skills share one `examples/` story, so you can read the whole chain
and watch one idea turn into a backlog:

> **Aurora Bank** is a mid-size digital bank. Card fraud disputes are handled by
> phone, take 11 days to acknowledge, and drive the highest call volume of any
> journey. The proposed product, **Disputa Express**, lets a cardholder open and
> track a dispute in-app. The protagonist persona is **Cardholder Camila**.

Start at [`skills/product-onboarding/examples/aurora-bank-walkthrough.md`](skills/product-onboarding/examples/aurora-bank-walkthrough.md)
for the orchestrated version, then read any individual skill's example for the
detail of that step. The positioning statement in Phase 0, the market sizing in
Phase 1, the probe design in Phase 2, and the prioritized roadmap in Phase 4 are
all the same product, so the numbers and the persona line up across files.

The example is deliberately fictional. Every number in it is invented and
labelled as such - which is also the behaviour the skills demand of themselves.

---

## How the skills are written

All twenty skills follow one architecture, documented in
[CONVENTIONS.md](CONVENTIONS.md):

- **Five blocks** - Context, Instruction, Parameter, Output, Validation.
- **One declared interaction mode** - facilitation, checkpointed
  co-construction, or autonomous investigation. The mode decides who asks, who
  waits, and what happens when nobody answers.
- **Generative Guidance v2** for facilitation skills - budgeted questions, one
  at a time, three context-aware options plus Other, and two standing bypasses
  ("take your best guess" and bulk drop) that are always honoured.
- **Required Context Keys and a Missing Context Rule** - at most three targeted
  questions, then proceed with labelled assumptions. Never stall, never invent.
- **Template stability** - output schemas are contracts. Change one only as a
  labelled new version with a migration note.
- **Evidence honesty** - Fact / Inference / Assumption labels, a
  domain-specific do-not-invent list, and an "Assumptions to Validate" section
  closing every artifact.
- **A Final Step block** - exactly four next options, recommended first.

If you are editing a skill, the authoring checklist at the end of
`CONVENTIONS.md` is the thing to run through before committing.

---

## Validating a skill

`scripts/validate_skills.py` checks every skill against the mechanical subset of
that checklist. No dependencies, Python 3.9 or later.

```
python3 scripts/validate_skills.py             # everything
python3 scripts/validate_skills.py --quiet      # errors only, no warnings
python3 scripts/validate_skills.py user-story lean-ux-canvas
```

It exits 0 when every skill passes and 1 otherwise, so it drops into a
pre-commit hook or CI step unchanged.

What it checks: frontmatter `name` matches the directory and `description` is
present and a sane length; the hidden-curriculum comment exists and declares
exactly one interaction mode; the Five Blocks plus Final Step, Examples, and
Provenance are all present and in order; the required subheadings exist; the
Final Step has exactly four options with the first marked `(Recommended)` and
the standard reply line; the Output Block points at `template.md`; `template.md`
exists, is a real contract rather than a stub, and has a Provenance section;
`examples/` has at least one markdown file; and no emoji anywhere.

Example output:

```
  company-research            OK
  epic-breakdown-advisor      OK
  epic-hypothesis             OK
  jobs-to-be-done             OK
  lean-ux-canvas              FAIL
    - missing subheading '### Quality gates'
  opportunity-solution-tree   OK
  pestel-analysis             OK
  pol-probe-advisor           OK
  positioning-workshop        OK
  prd-development             OK
  prioritization-advisor      OK
  problem-statement           OK
  product-onboarding          OK
    ~ SKILL.md is 395 lines -- consider moving detail into template.md
  product-strategy-session    OK
  proto-persona               OK
  roadmap-planning            OK
  tam-sam-som-calculator      OK
  user-story                  OK
  workshop-facilitation       OK
  write-spec                  OK

  19 passed, 1 failed
```

Lines marked `-` are errors and fail the run. Lines marked `~` are warnings and
do not. What the script cannot check is whether the skill is any good: whether
the do-not-invent list is genuinely domain-specific, whether the facilitation
options sharpen from question to question, whether the example teaches anything.
Those are the parts that need a human, which is why the checklist is longer than
the script.

---

## Attribution and licence

This plugin is a mix of original and adapted work under two licences. The short
version:

- The orchestrator, `prioritization-advisor`, `pol-probe-advisor`, `write-spec`
  (adapted from Anthropic's MIT `product-management` example plugin), the plugin
  scaffolding, `scripts/validate_skills.py`, this README, and the CHANGELOG are
  **MIT** - see [LICENSE](LICENSE).
- The sub-skills adapted from
  [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
  by Dean Peters, and `CONVENTIONS.md`, are **CC BY-NC-SA 4.0** - attribution,
  share-alike, non-commercial. See [LICENSE-CC-BY-NC-SA](LICENSE-CC-BY-NC-SA).

> Adapted from [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
> by Dean Peters, CC BY-NC-SA 4.0.

Read [ATTRIBUTION.md](ATTRIBUTION.md) for the full file-by-file breakdown, the
ShareAlike and non-commercial implications for a fork, and credit for the
underlying frameworks.
