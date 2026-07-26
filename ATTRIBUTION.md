# Attribution and Licensing

This plugin is a mix of original work and adapted work. The two carry different
licences, and this file records which is which.

---

## Original work — MIT

MIT licensed, copyright Bruno Lima Soares:

- The `product-onboarding` orchestrator skill (its five-phase sequencing, phase
  gates, artifact index contract, and handoff rules).
- The plugin scaffolding: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`.
- `README.md`.
- The `write-spec` skill, adapted from Anthropic's `product-management` example
  plugin.

---

## Adapted work — CC BY-NC-SA 4.0

The following sub-skills are **adaptations** of prompts from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, licensed
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/):

| Skill | Upstream source |
|---|---|
| `company-research` | `prompts/company-profile-executive-insights-research.md` |
| `pestel-analysis` | `prompts/pestel-analysis-prompt-template.md` |
| `proto-persona` | `prompts/proto-persona-profile.md` |
| `problem-statement` | `prompts/framing-the-problem-statement.md` |
| `lean-ux-canvas` | `prompts/lean-ux-canvas-prompt-template.md`, `workshops/lean-ux-canvas-workshop.md` |
| `user-story` | `prompts/user-story-prompt-template.md`, `prompts/user-story-mapping.md` |
| `prd-development` | `prompts/prd-prompt-template.md`, `workshops/prd-workshop.md` |
| `epic-breakdown-advisor` | `prompts/user-story-splitting-prompt-template.md`, `prompts/backlog-epic-hypothesis.md` |
| `roadmap-planning` | `prompts/backlog-epic-hypothesis.md` and the repo's roadmap conventions |
| `product-strategy-session` | `prompts/strategic-scrum-team-session-kickoff.md` and the workshop set |

`CONVENTIONS.md` is likewise adapted from that repository's
`prompting-style-guide.md`, `generative-guidance-pattern.md`,
`interaction-modes.md`, and `SUBMISSIONS-GUIDE.md`.

> Adapted from [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
> by Dean Peters, CC BY-NC-SA 4.0.

### What ShareAlike means here

CC BY-NC-SA 4.0 carries a **ShareAlike** term: anything built from that material
and then shared must carry the same licence. The adapted sub-skills and
`CONVENTIONS.md` therefore ship as CC BY-NC-SA 4.0, not MIT.

Earlier versions of this repository described the whole plugin as MIT. That was
incorrect for the adapted skills, and this file supersedes it.

### Non-commercial term

CC BY-NC-SA 4.0 is **non-commercial**. Per the upstream
[LICENSING.md](https://github.com/deanpeters/product-manager-prompts/blob/main/LICENSING.md),
expressed written permission from Dean Peters is required to, among other
things, bundle the material into a paid product or service, use it as material
for paid training or consulting deliverables, or put it behind a paywall.

Using these skills for your own product practice, adapting them for your team,
and sharing them onward under the same licence are all explicitly encouraged.

*This is a plain-language summary written by the repository maintainer, not legal
advice. If your use might be commercial, read the upstream LICENSE and ask Dean.*

---

## Framework sources

The skills stand on published methodology. Credit where it is due:

- **INVEST** — Bill Wake
- **User stories** — Mike Cohn, *User Stories Applied*
- **Story splitting** — Richard Lawrence and Peter Green, *The Humanizing Work
  Guide to Splitting User Stories*
- **User story mapping** — Jeff Patton, *User Story Mapping*
- **Lean UX Canvas v2** — Jeff Gothelf, *Lean UX*
- **Continuous discovery, opportunity solution trees** — Teresa Torres,
  *Continuous Discovery Habits*
- **Product discovery and PRD practice** — Marty Cagan, *Inspired*;
  Martin Eriksson, "How to Write a Good PRD"
- **Roadmaps** — Bruce McCarthy and C. Todd Lombardo, *Product Roadmaps Relaunched*
- **RICE** — Intercom
- **PESTEL** — extends Francis Aguilar's 1967 PEST framework
- **Proto-personas** — Productside Product Manager's Playbook
- **Working Backwards** — Amazon
- **Gherkin** — Cucumber project
