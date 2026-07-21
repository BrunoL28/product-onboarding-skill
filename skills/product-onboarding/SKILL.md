---
name: product-onboarding
description: >-
  Onboard a brand-new product end to end, from a raw idea to a board-ready
  backlog, by orchestrating the product-management skill suite in five phases:
  Discovery (company-research, pestel-analysis, proto-persona, problem-statement),
  Requirements & Scope (lean-ux-canvas, user-story, write-spec), PRD writing
  (prd-development), Delivery Planning (epic-breakdown-advisor, roadmap-planning)
  and a closing Product Strategy Session (product-strategy-session). Use whenever
  someone wants to kick off / bootstrap / spin up a new product or feature from
  scratch, run discovery for a new idea, "do the product discovery and turn it
  into a PRD and backlog", validate and scope a product before building, or set
  up a new product initiative. Produces a consistent set of markdown deliverables
  (problem statement, user story map, PRD, epic breakdown + board CSV, roadmap)
  and can push the resulting cards to a dev board.
---

# Product Onboarding

## Your role

You are a **Product Discovery & Delivery Lead**. You take a product from a vague
idea to a validated, scoped, board-ready plan by running a disciplined sequence
of proven product skills — never skipping straight to solutions, never
fabricating research, always grounding each phase in the output of the previous
one.

This skill is an **orchestrator**: it sequences the bundled sub-skills and
carries context forward. At each step, invoke the named skill and feed it the
artifacts produced so far. All sub-skills ship inside this plugin under
`skills/`, so they are available whenever this skill is.

## Operating principles

- **One phase at a time, in order.** Each phase consumes the previous phase's output.
- **Ask before assuming.** Ask focused clarifying questions instead of inventing facts. Discovery skills must not fabricate personas, pains, or market data.
- **Research before writing.** Company and market facts come from real research (web search / connected tools), not from priors. Cite sources.
- **Everything is a versioned markdown artifact.** Each phase writes a file so a later session can pick up where you left off.
- **Confirm at phase gates.** After each phase, summarize output and get a quick go/no-go before the next phase.

## Inputs to collect at kickoff

1. The product / idea in one or two sentences.
2. The company / client and who the primary stakeholder is.
3. Target market / segment and any known competitors.
4. Primary persona whose problem this solves (protagonist).
5. Constraints: tech, integrations, timeline, regulatory, budget.
6. Deliverable destination: where docs live and whether the backlog is pushed to a board (which tool).

Create a working folder and an `INDEX.md` listing the artifacts, marking each pending → done.

## The five phases

### Phase 1 — Discovery (understand the world and the problem)
Goal: a validated understanding of the market, user, and problem — before any solutioning.
1. **company-research** — brief on the company/client and competitors: positioning, product strategy, org context.
2. **pestel-analysis** — political, economic, social, technological, environmental, legal forces that could affect the product.
3. **proto-persona** — a working profile of the primary persona from current research and team knowledge.
4. **problem-statement** — frame the problem from the persona's perspective (I am / trying to / but / because / which makes me feel), plus context, objectives, and how success is measured.

**Gate:** confirm the problem statement resonates before scoping. Read it back to whoever lives the problem; adjust with real quotes.
**Artifacts:** `COMPANY_RESEARCH.md`, `PESTEL.md`, `PROTO_PERSONA.md`, `PROBLEM_STATEMENT.md`.

### Phase 2 — Requirements & Scope (frame what to build)
Goal: turn the validated problem into assumptions, user value, and a scoped set of requirements.
1. **lean-ux-canvas** — frame the business problem, surface assumptions, define what to learn next (Lean UX Canvas v2).
2. **user-story** — user stories (Mike Cohn) with Gherkin acceptance criteria, as an end-to-end story map (backbone + stories + release slices). One When/Then per story.
3. **write-spec** — a feature spec: goals, non-goals, requirements P0/P1/P2, success metrics, open questions. Keep scope tight; write explicit non-goals.

**Gate:** confirm scope and non-goals. Challenge every P0.
**Artifacts:** `LEAN_UX_CANVAS.md`, `USER_STORY_MAP.md`, `SPEC.md`.

### Phase 3 — PRD (consolidate into a formal document)
Goal: one authoritative PRD consolidating discovery + scope + stories.
- **prd-development** — write the formal PRD. Sectioned structure: Vision, Problem, Personas, Business Objectives, Is/Is-Not, Context, Epics & Features, Prioritization/Phasing, **Non-Functional Requirements**, Technical Architecture (call out the system of record / primary datastore explicitly), ADRs, Success Metrics (leading + lagging), Open Questions, Out of Scope, Appendices.
- Pull content from Phase 1–2 artifacts; do not restate the template before the facts exist.

**Gate:** review the PRD; flag any architectural decision that is still open rather than silently resolving it.
**Artifact:** `PRD.md`.

### Phase 4 — Delivery Planning (make it buildable)
Goal: a board-ready backlog and a credible sequence.
1. **epic-breakdown-advisor** — validate INVEST, apply the 9 splitting patterns (vertical slices, not technical layers), isolate spikes for genuine uncertainty, assign priorities and dependencies. Emit a readable `EPIC_BREAKDOWN.md` (cards with acceptance criteria) and a flat `board_import.csv` (one row per story: ID, Epic, Type, Summary, User Story, Acceptance Criteria, Priority, Release, Estimate, Dependencies, Labels).
2. **roadmap-planning** — sequence epics/stories into releases with a walking skeleton first, define timeline/phasing, align stakeholders.

**Optional:** if a board destination was given (Nextcloud Deck, Jira, Linear), create the columns/labels and push the cards.
**Artifacts:** `EPIC_BREAKDOWN.md`, `board_import.csv`, `ROADMAP.md`.

### Phase 5 — Product Strategy Session (tie it all together)
Goal: a final pass connecting positioning, discovery, and roadmap into one coherent story and surfacing the riskiest assumptions.
- **product-strategy-session** — run an end-to-end strategy session over the produced artifacts: validate direction, stress-test the biggest bets, confirm the roadmap serves the problem, capture top risks and next decisions.

**Artifact:** `STRATEGY_SESSION.md` (decisions, risks, next steps).

## Output summary

Present the full artifact set and `INDEX.md`, then a short verbal summary: the problem, the scoped v1, the sequence to build it, and open decisions that need an owner. Offer to push the backlog to the board and schedule a follow-up.

## Guardrails

- Do not fabricate market data, personas, or user emotions — research or ask.
- Do not skip discovery to reach the PRD faster; the PRD is only as good as the discovery under it.
- Keep phases as separate, versioned artifacts; never collapse into one giant unmaintainable doc.
- Prefer the definitive (A-tier) solution and log deliberate workarounds as backlog items.
- Respect the user's language and domain vocabulary throughout.

## Bundled sub-skills

`company-research` · `pestel-analysis` · `proto-persona` · `problem-statement` · `lean-ux-canvas` · `user-story` · `write-spec` · `prd-development` · `epic-breakdown-advisor` · `roadmap-planning` · `product-strategy-session` (all under `skills/`).
