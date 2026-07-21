# product-onboarding

A Claude skill that onboards a brand-new product **end to end** — from a raw
idea to a board-ready backlog — by orchestrating the product-management skill
suite in five phases.

It doesn't reinvent the individual skills; it **sequences** them and carries
context forward, writing a versioned markdown artifact at each step so any
later session can pick up where the last one ended.

## The five phases

| Phase | Goal | Skills chained | Artifacts |
|---|---|---|---|
| 1 · Discovery | Understand market, user, problem | `company-research`, `pestel-analysis`, `proto-persona`, `problem-statement` | `COMPANY_RESEARCH.md`, `PESTEL.md`, `PROTO_PERSONA.md`, `PROBLEM_STATEMENT.md` |
| 2 · Requirements & Scope | Frame what to build | `lean-ux-canvas`, `user-story`, `product-management:write-spec` | `LEAN_UX_CANVAS.md`, `USER_STORY_MAP.md`, `SPEC.md` |
| 3 · PRD | Consolidate into a formal doc | `prd-development` | `PRD.md` |
| 4 · Delivery Planning | Make it buildable | `epic-breakdown-advisor`, `roadmap-planning` | `EPIC_BREAKDOWN.md`, `board_import.csv`, `ROADMAP.md` |
| 5 · Strategy Session | Tie it all together | `product-strategy-session` | `STRATEGY_SESSION.md` |

## Principles

- One phase at a time, in order — each consumes the previous phase's output.
- Ask before assuming; research before writing; never fabricate personas or market data.
- Everything is a versioned markdown artifact.
- Confirm at phase gates before spending effort on the next phase.

## Install

Copy the `product-onboarding/` folder (containing `SKILL.md`) into your skills
directory:

```
~/.claude/skills/product-onboarding/SKILL.md
```

Then trigger it with things like *"onboard a new product"*, *"run discovery for
this idea and turn it into a PRD and backlog"*, or *"bootstrap this product from
scratch"*.

## License

MIT
