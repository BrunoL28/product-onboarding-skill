# Changelog

All notable changes to this plugin are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.3.0] - 2026-07-27

Unreleased. Twelve skills became twenty. The chain now starts a phase
earlier, at who the product is for, and probes the riskiest assumption
before the spec gets written rather than after.

### Added

- `positioning-workshop` - builds a positioning statement: target
  segment, market category, key benefit, differentiation, proof. Added
  because every downstream artifact was quietly assuming a segment and
  a category that nobody had ever written down.
- `jobs-to-be-done` - surfaces the functional, emotional, and social
  job the product is hired to do, with pains and gains. Added so the
  persona and problem statement start from a job rather than a
  demographic.
- `tam-sam-som-calculator` - top-down and bottom-up market sizing with
  the arithmetic shown and every input labelled. Added because
  discovery could describe a problem in detail and still not say
  whether it was worth solving.
- `opportunity-solution-tree` - maps a desired outcome to
  opportunities, solutions, and the tests that would settle them.
  Added to stop the jump from canvas straight to backlog.
- `pol-probe-advisor` - designs a Proof of Life probe for the riskiest
  assumption: concierge, Wizard of Oz, smoke test, fake door,
  prototype test. Added because Phase 2 could produce a confident spec
  built on an untested belief.
- `epic-hypothesis` - frames an epic as a testable hypothesis with a
  target user, an expected outcome, and how the team would know it
  worked. Added as the entry point to delivery planning, ahead of
  breakdown.
- `prioritization-advisor` - picks a scoring framework to fit the
  decision (RICE, ICE, Kano, MoSCoW, WSJF, Opportunity Scoring),
  applies it, and shows the sensitivity of the ranking. Added because
  sequencing was happening in the roadmap skill with no stated method.
- `workshop-facilitation` - the session protocol other skills borrow
  when they run live with a room: silent writing, divergence before
  convergence, dot voting, disagree-and-commit, a `SESSION_RECORD.md`.
  Added so eight skills stopped each describing their own facilitation
  rules slightly differently.
- `scripts/validate_skills.py` - checks every skill against the
  mechanical subset of the CONVENTIONS.md section 10 checklist:
  frontmatter, hidden-curriculum comment, one declared interaction
  mode, the Five Blocks in order, required subheadings, the Final Step
  contract, template.md presence, and at least one example. Exit code
  0 when everything passes.
- `LICENSE` (MIT) and `LICENSE-CC-BY-NC-SA` (CC BY-NC-SA 4.0). The
  repository always had two licences and until now had neither file.
- `CHANGELOG.md`, this file.
- A measurement thread running across phases 1 to 4 into
  `MEASUREMENT.md`: the baseline is captured in Discovery, the target
  is set in Requirements and Validation, the instrumentation is named
  in the PRD, and the read-out is scheduled in Delivery Planning. It
  is one document handed forward, not four disconnected metrics
  sections.

### Changed

- **Phase numbering shifted.** Phase 0 - Framing is new and sits ahead
  of Discovery. Discovery, Requirements, PRD, Delivery Planning, and
  Strategy Session keep their numbers, but "the first phase" is no
  longer Discovery. Anything that referred to phases by number -- your
  own notes, a fork's orchestrator, a script keyed on phase index --
  needs re-reading. There is no automatic migration; the phase names
  are stable and are the safer thing to key on.
- Phase 2 renamed from "Requirements and Scope" to "Requirements and
  Validation", and now carries `opportunity-solution-tree` and
  `pol-probe-advisor` alongside the canvas, stories, and spec. The
  rename is not cosmetic: the phase gate now asks whether the riskiest
  assumption has been probed, not only whether the scope is written
  down.
- Phase 1 - Discovery gained `tam-sam-som-calculator` and its
  `MARKET_SIZING.md` artifact.
- Phase 4 - Delivery Planning gained `epic-hypothesis` and
  `prioritization-advisor`, ahead of `epic-breakdown-advisor` and
  `roadmap-planning`.
- `roadmap-planning` rebuilt from a 30-line stub onto the Five-Block
  architecture, with a `template.md`, a worked example, an explicit
  interaction mode, and a do-not-invent list. It now consumes
  `PRIORITIZATION.md` rather than re-deriving an order of its own.
- `product-strategy-session` rebuilt from a 30-line stub the same way.
  It now stress-tests the Phase 0 positioning and JTBD alongside the
  PRD and roadmap, so the session has something to argue against.
- `product-onboarding` orchestrator updated for the new phase map, the
  eight new skills, the measurement thread, and the new phase gates.
- The Aurora Bank running example extended to all twenty skills. One
  fictional product, one persona, one chain you can read end to end.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
  updated for twenty skills; keywords extended.
- `README.md` rewritten for the new shape, plus a section on the
  validation script.
- `CONVENTIONS.md` gained a section on the validation script, and the
  section 10 authoring checklist now points at it.
- `ATTRIBUTION.md` extended to cover all twenty skills and the new
  repository files.

---

## [0.2.0] - 2026-07-17

The release that made the output predictable.

### Added

- A `template.md` in every skill directory: the stable output schema
  the skill must emit, with one home rather than being inlined and
  drifting.
- A worked example in every skill's `examples/` directory, showing the
  conversation and the resulting artifact, not just the artifact.
- The Aurora Bank running example. Every skill's example works the
  same fictional product -- a mid-size digital bank, an in-app card
  dispute flow, and Cardholder Camila -- so the whole chain reads as
  one story.
- `CONVENTIONS.md`, the skill authoring contract: the Five-Block
  structure, the three interaction modes and the burden-shifting test,
  Generative Guidance v2, context intake rules, output rules, the
  Final Step contract, and the authoring checklist.
- `ATTRIBUTION.md`, recording which parts are MIT and which are
  CC BY-NC-SA 4.0.

### Changed

- Every skill rebuilt onto the Five-Block architecture: Context,
  Instruction, Parameter, Output, Validation, each with a
  hidden-curriculum comment above the body.
- Each skill declares exactly one interaction mode.
- Evidence labelling (Fact / Inference / Assumption), a
  domain-specific do-not-invent list, and a closing "Assumptions to
  Validate" section became mandatory in every artifact.

### Fixed

- Earlier versions described the whole plugin as MIT. That was wrong
  for the skills adapted from Dean Peters' product-manager-prompts,
  which carry CC BY-NC-SA 4.0 and its ShareAlike term. `ATTRIBUTION.md`
  corrects and supersedes it.

Before this, the skills carried the method but no output contract and
no examples, so the same skill could produce a different shape every
run. Fine for a chat, useless for anything you export into Jira.

---

## [0.1.0] - 2026-03-19

Initial release.

### Added

- The `product-onboarding` orchestrator: five phases, phase gates, an
  artifact index, and handoff rules between steps.
- Eleven bundled sub-skills: `company-research`, `pestel-analysis`,
  `proto-persona`, `problem-statement`, `lean-ux-canvas`,
  `user-story`, `write-spec`, `prd-development`,
  `epic-breakdown-advisor`, `roadmap-planning`,
  `product-strategy-session`.
- Plugin scaffolding: `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, so the repository can be added as
  a marketplace and installed in one step.
