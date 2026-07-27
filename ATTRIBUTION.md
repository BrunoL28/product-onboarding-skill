# Attribution and Licensing

This plugin is a mix of original work and adapted work. The two carry different
licences, and this file records which is which, file by file.

The licence texts themselves are [LICENSE](LICENSE) (MIT) and
[LICENSE-CC-BY-NC-SA](LICENSE-CC-BY-NC-SA) (CC BY-NC-SA 4.0).

---

## Original work - MIT

MIT licensed, copyright 2026 Bruno Lima Soares:

| File or directory | What it is |
|---|---|
| `skills/product-onboarding/` | The orchestrator: phase sequencing, phase gates, the artifact index contract, the measurement thread, handoff rules |
| `skills/prioritization-advisor/` | Original skill. Framework selection and scoring across RICE, ICE, Kano, MoSCoW, WSJF, Opportunity Scoring |
| `skills/pol-probe-advisor/` | Original skill. Proof of Life probe design. The *Proof of Life probe* framing is Dean Peters', but this is an independent implementation, not an adaptation of any upstream file |
| `skills/write-spec/` | MIT, but from a different source - see the section below |
| `.claude-plugin/plugin.json` | Plugin manifest |
| `.claude-plugin/marketplace.json` | Marketplace manifest |
| `scripts/validate_skills.py` | The authoring-contract validator |
| `README.md` | |
| `CHANGELOG.md` | |
| `LICENSE`, `LICENSE-CC-BY-NC-SA`, `ATTRIBUTION.md` | |

Two caveats on the MIT skills. `prioritization-advisor` and `pol-probe-advisor`
are original in content, but their guided-session shape follows `CONVENTIONS.md`
sections 4 and 6, which are themselves adapted from Dean Peters. The prose in
those skills is MIT; the pattern they follow traces back to CC BY-NC-SA
material. If you lift the *structure* wholesale into something you publish,
treat it as you would `CONVENTIONS.md`.

### `write-spec` - MIT from a different source

`skills/write-spec/` is adapted from the `write-spec` skill in Anthropic's
`product-management` example plugin, which is MIT. It was then restructured to
the Five-Block architecture in `CONVENTIONS.md`. The content is MIT-derived; the
structure it was poured into is not. Same caveat as above.

---

## Adapted work - CC BY-NC-SA 4.0

The following sub-skills are **adaptations** of prompts from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, licensed
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Each
skill also names its upstream source in its own `## Provenance` section; if this
table and a skill's Provenance section ever disagree, the skill is the one that
was actually written from the source.

### Phase 0 - Framing

| Skill | Upstream source |
|---|---|
| `positioning-workshop` | `prompts/positioning-statement.md`, `prompt-generators/positioning-statement-prompt-generator.md` |
| `jobs-to-be-done` | `prompts/jobs-to-be-done.md` |

### Phase 1 - Discovery

| Skill | Upstream source |
|---|---|
| `company-research` | `prompts/company-profile-executive-insights-research.md` |
| `pestel-analysis` | `prompts/pestel-analysis-prompt-template.md` |
| `tam-sam-som-calculator` | `market-intelligence/tam-sam-som-analysis-prompt.md`, `loops/market-sizing-loop.md` |
| `proto-persona` | `prompts/proto-persona-profile.md` |
| `problem-statement` | `prompts/framing-the-problem-statement.md` |

### Phase 2 - Requirements and Validation

| Skill | Upstream source |
|---|---|
| `lean-ux-canvas` | `prompts/lean-ux-canvas-prompt-template.md`, `workshops/lean-ux-canvas-workshop.md` |
| `opportunity-solution-tree` | `workshops/opportunity-solution-tree-workshop.md` |
| `user-story` | `prompts/user-story-prompt-template.md`, `prompts/user-story-mapping.md` |

`pol-probe-advisor` and `write-spec` also sit in Phase 2 and are MIT - see above.

### Phase 3 - PRD

| Skill | Upstream source |
|---|---|
| `prd-development` | `prompts/prd-prompt-template.md`, `workshops/prd-workshop.md` |

### Phase 4 - Delivery Planning

| Skill | Upstream source |
|---|---|
| `epic-hypothesis` | `prompts/backlog-epic-hypothesis.md` |
| `epic-breakdown-advisor` | `prompts/user-story-splitting-prompt-template.md`, `prompts/backlog-epic-hypothesis.md` |
| `roadmap-planning` | `prompts/backlog-epic-hypothesis.md` and the upstream repository's roadmap conventions |

`prioritization-advisor` also sits in Phase 4 and is MIT - see above.

### Phase 5 - Strategy Session

| Skill | Upstream source |
|---|---|
| `product-strategy-session` | `prompts/strategic-scrum-team-session-kickoff.md`, `prompts/premortem-prompt-template.md` |

### Support

| Skill | Upstream source |
|---|---|
| `workshop-facilitation` | `generative-guidance-pattern.md`, `interaction-modes.md` - the same two files behind `CONVENTIONS.md` sections 4 and 5 |

### Repository files

`CONVENTIONS.md` is adapted from that repository's `prompting-style-guide.md`,
`generative-guidance-pattern.md`, `interaction-modes.md`, and
`SUBMISSIONS-GUIDE.md`, and is CC BY-NC-SA 4.0.

> Adapted from [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
> by Dean Peters, CC BY-NC-SA 4.0.

---

## What ShareAlike means here

CC BY-NC-SA 4.0 carries a **ShareAlike** term: anything built from that material
and then shared must carry the same licence. The adapted sub-skills and
`CONVENTIONS.md` therefore ship as CC BY-NC-SA 4.0, not MIT.

Practically, for a fork:

- Edit an adapted skill and publish the result, and your version of that skill
  is CC BY-NC-SA 4.0 too. You cannot relicense it MIT, Apache, or proprietary.
- Combining an adapted skill with new material of your own produces an
  adaptation. The adaptation carries the licence; the fact that you wrote half
  of it does not exempt it.
- You can keep MIT-licensed code in the same repository - that is exactly what
  this repository does - as long as the boundary is documented, which is what
  this file is for. Keep it accurate in your fork.
- Keep the `## Provenance` section in each skill and the framework attributions
  inside it. They are part of the attribution the licence requires, not
  decoration.
- Writing a *new* skill that merely follows the conventions is a grey area. A
  skill whose content is yours but whose scaffolding follows `CONVENTIONS.md`
  is how `prioritization-advisor` and `pol-probe-advisor` are treated here:
  MIT content, with the debt to the pattern stated openly. If you are unsure,
  the conservative move is to licence it CC BY-NC-SA 4.0 and lose nothing.

Earlier versions of this repository described the whole plugin as MIT. That was
incorrect for the adapted skills, and this file supersedes it.

## Non-commercial term

CC BY-NC-SA 4.0 is **non-commercial**. Per the upstream
[LICENSING.md](https://github.com/deanpeters/product-manager-prompts/blob/main/LICENSING.md),
expressed written permission from Dean Peters is required to, among other
things, sell this material or an adaptation of it, bundle it into a paid
product, app, or service, use it as material for paid training, courses,
workshops, or consulting deliverables, or put it behind a paywall, login, or
lead-capture wall.

The line that trips people up: using these skills to do product work inside a
company that makes money is fine - that is your own product practice. Charging
for the skills themselves, or for a workshop whose material is these skills, is
not. If you are close to the line, ask; per upstream, permission is available
and starts with a conversation, and when granted it is explicit and in writing.

Using these skills for your own product practice, adapting them for your team,
and sharing them onward under the same licence are all explicitly encouraged.

*This is a plain-language summary written by the repository maintainer, not legal
advice. If your use might be commercial, read the upstream LICENSE and ask Dean.*

---

## Framework sources

The skills stand on published methodology. Credit where it is due:

- **Positioning** - April Dunford, *Obviously Awesome*; statement template from
  Geoffrey Moore, *Crossing the Chasm*
- **Jobs to be Done** - Clayton Christensen, *Competing Against Luck*; Bob
  Moesta, *Demand-Side Sales 101*; Tony Ulwick, *Jobs to be Done: Theory to
  Practice*
- **Pains and gains** - Alexander Osterwalder, Value Proposition Canvas
- **Market sizing** - TAM/SAM/SOM as practised in venture and product strategy;
  bottom-up discipline after Bill Aulet, *Disciplined Entrepreneurship* (MIT)
- **INVEST** - Bill Wake
- **User stories** - Mike Cohn, *User Stories Applied*
- **Story splitting** - Richard Lawrence and Peter Green, *The Humanizing Work
  Guide to Splitting User Stories*
- **User story mapping** - Jeff Patton, *User Story Mapping*
- **Lean UX Canvas v2 and the hypothesis format** - Jeff Gothelf, *Lean UX*
- **Continuous discovery, opportunity solution trees, assumption tests** -
  Teresa Torres, *Continuous Discovery Habits*
- **Concierge, Wizard of Oz, smoke tests** - Eric Ries, *The Lean Startup*;
  fake-door and painted-door patterns as practised widely
- **Prototype tests** - Google Ventures, *Sprint*
- **Product discovery and PRD practice** - Marty Cagan, *Inspired*;
  Martin Eriksson, "How to Write a Good PRD"
- **Premortem** - Gary Klein, "Performing a Project Premortem", HBR 2007
- **Roadmaps** - Bruce McCarthy and C. Todd Lombardo, *Product Roadmaps Relaunched*
- **RICE** - Intercom. **ICE** - Sean Ellis. **Kano** - Noriaki Kano.
  **MoSCoW** - Dai Clegg, DSDM. **WSJF** - SAFe, after Don Reinertsen's cost of
  delay. **Opportunity Scoring** - Anthony Ulwick, *What Customers Want*
- **PESTEL** - extends Francis Aguilar's 1967 PEST framework
- **Proto-personas** - Productside Product Manager's Playbook
- **Working Backwards** - Amazon
- **Gherkin** - Cucumber project
