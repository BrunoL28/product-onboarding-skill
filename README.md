# product-onboarding (plugin)

An installable Claude plugin that onboards a brand-new product **end to end** —
from a raw idea to a board-ready backlog — by orchestrating a suite of
product-management skills in five phases.

The plugin **bundles all the skills it needs**, so a teammate installs once and
has the orchestrator plus every sub-skill available — no "assume you already
have them".

## What's inside

```
.claude-plugin/
  plugin.json         # plugin manifest
  marketplace.json    # lets the repo be added as a marketplace
skills/
  product-onboarding/ # the orchestrator (start here)
  company-research/    pestel-analysis/     proto-persona/     problem-statement/
  lean-ux-canvas/      user-story/          write-spec/
  prd-development/
  epic-breakdown-advisor/  roadmap-planning/
  product-strategy-session/
```

## The five phases

| Phase | Goal | Skills chained |
|---|---|---|
| 1 · Discovery | Understand market, user, problem | `company-research`, `pestel-analysis`, `proto-persona`, `problem-statement` |
| 2 · Requirements & Scope | Frame what to build | `lean-ux-canvas`, `user-story`, `write-spec` |
| 3 · PRD | Consolidate into a formal doc | `prd-development` |
| 4 · Delivery Planning | Make it buildable | `epic-breakdown-advisor`, `roadmap-planning` |
| 5 · Strategy Session | Tie it all together | `product-strategy-session` |

Each phase writes a versioned markdown artifact and feeds the next; confirmation
gates between phases prevent skipping discovery.

## Install

**As a plugin (recommended):** add this repo as a marketplace, then install:

```
/plugin marketplace add BrunoL28/product-onboarding-skill
/plugin install product-onboarding
```

**Manual:** copy the folders under `skills/` into your skills directory
(`~/.claude/skills/` for personal, or `<repo>/.claude/skills/` for a single
project). The orchestrator is `skills/product-onboarding/`.

Then trigger with *"onboard a new product"*, *"run discovery for this idea and
turn it into a PRD and backlog"*, or *"bootstrap this product from scratch"*.

## Notes & attribution

- The 11 bundled sub-skills are adapted from Anthropic's product-management
  example skills (several originate from the `deanpeters/product-manager-prompts`
  project, as noted in each skill's `Provenance`). They are bundled here only to
  make the orchestrator self-contained; upstream remains the source of truth.
- Only each sub-skill's `SKILL.md` is vendored. Their optional `template.md` /
  `examples/` companion files are **not** bundled (kept lean) — pull them from
  upstream if you want the fill-in templates.
- Four sub-skills (`lean-ux-canvas`, `prd-development`, `roadmap-planning`,
  `product-strategy-session`) and `epic-breakdown-advisor` reference an optional
  `workshop-facilitation` skill for their guided-conversation protocol. They
  work without it (their domain logic is self-contained); add
  `workshop-facilitation` separately if you want the facilitation layer.

## License

MIT (for the orchestrator and plugin scaffolding). Bundled sub-skills retain
their original licensing/attribution.
