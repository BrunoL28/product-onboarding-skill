---
name: prd-development
description: Build a structured PRD that connects problem, users, solution, and success criteria. Use when turning discovery notes into an engineering-ready document for a major initiative.
---

## Purpose
Guide PMs through structured PRD creation by orchestrating problem framing, user research synthesis, solution definition, and success criteria into a cohesive document that aligns stakeholders and provides engineering context—avoiding ambiguity, scope creep, and the "build what's in my head" trap.

This is not a waterfall spec—it's a living document that evolves through delivery.

## Standard PRD structure
1. Executive Summary (problem + solution + impact)
2. Problem Statement (who, what, why painful, evidence)
3. Target Users & Personas (primary/secondary, JTBD)
4. Strategic Context (business goals/OKRs, market, competition, why now)
5. Solution Overview (high-level, flows/wireframes, key features)
6. Success Metrics (primary, secondary, guardrail; current → target)
7. User Stories & Requirements (epic hypothesis, stories with acceptance criteria, edge cases)
8. Out of Scope (and why)
9. Dependencies & Risks (technical/external; risks + mitigations)
10. Open Questions

For product-onboarding, also include **Non-Functional Requirements** and a **Technical Architecture** section that explicitly names the system of record / primary datastore, plus **ADRs** and **Appendices** where math or protocols must be verified.

### Anti-Patterns
Not a detailed pixel spec; not a frozen contract; not a substitute for collaboration.

## Application (phased)
1. Executive summary (write first for clarity, refine last).
2. Problem statement — use the `problem-statement` skill; ground in evidence (quotes, analytics, tickets).
3. Personas — use `proto-persona`.
4. Strategic context — OKRs, optional market sizing, competition, why now.
5. Solution overview — high-level; let design own UI details.
6. Success metrics — primary, secondary, guardrail.
7. User stories & requirements — use `epic-hypothesis`, `epic-breakdown-advisor`, `user-story`.
8. Out of scope & dependencies — explicit non-goals, dependencies, risks, open questions.

## Common Pitfalls
1. PRD written in isolation → collaborate on stories.
2. No evidence in problem statement → cite data/quotes.
3. Solution too prescriptive → keep high-level.
4. No success metrics → always define a primary metric.
5. Out of scope not documented → prevents scope creep.

### References
Martin Eriksson, "How to Write a Good PRD"; Marty Cagan, *Inspired*; Amazon Working Backwards. Orchestrates `problem-statement`, `proto-persona`, `epic-hypothesis`, `epic-breakdown-advisor`, `user-story`. When run as a guided conversation, an optional `workshop-facilitation` skill supplies the interaction protocol.
