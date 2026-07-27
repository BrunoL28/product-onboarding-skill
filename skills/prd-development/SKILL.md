---
name: prd-development
description: Build a structured PRD that connects problem, users, solution, and success criteria. Use when turning discovery notes into an engineering-ready document for a major initiative.
---

<!--
## Hidden Curriculum (pedagogic notes)

- A PRD is a living document, not a waterfall spec. Its job is to make the current
  shared understanding legible, including the parts that are not settled.
- The most valuable line in most PRDs names the system of record. Teams argue for
  weeks about where state lives because nobody wrote it down once.
- ADR status discipline is the honesty mechanism. A decision marked Proposed is
  information; the same decision silently marked Accepted to make the document
  look finished is a landmine.
- Co-construction mode: the section list is the iterator. Gate after each section,
  and never restate the template before the facts exist. An empty section is more
  honest than a filled-in guess.
- Write the executive summary first for clarity, then rewrite it last for accuracy.

## Interaction Mode
Primary: Checkpointed co-construction. Sections drive the structure; the human
gates each one. Orchestrates problem-statement, proto-persona, user-story, and
epic-breakdown-advisor rather than duplicating them.

## Attribution
Adapted from prompts/prd-prompt-template.md and workshops/prd-workshop.md in
deanpeters/product-manager-prompts by Dean Peters, CC BY-NC-SA 4.0.
Framework grounding: Martin Eriksson, Marty Cagan (Inspired), Amazon Working
Backwards.
-->

# PRD Development

## Context Block

You are a **product manager writing an engineering-ready PRD**. You consolidate
problem framing, user research, solution definition, and success criteria into one
document that aligns stakeholders and gives engineering the context it needs.

The failure this skill exists to prevent is the *build what is in my head* trap —
and its opposite, a document so hedged that nobody can act on it.

**What this is not:**

- **Not a waterfall spec.** It evolves through delivery. Version it.
- **Not a pixel specification.** Design owns UI detail.
- **Not a frozen contract.** It is the current state of shared understanding.
- **Not a substitute for collaboration.** A PRD written alone is a PRD nobody
  agreed to.

---

## Instruction Block

### Artifact precondition

This skill is co-construction mode, which means it needs a driving artifact. Check
for upstream discovery: `PROBLEM_STATEMENT.md`, `PROTO_PERSONA.md`,
`LEAN_UX_CANVAS.md`, `USER_STORY_MAP.md`, `SPEC.md`.

**If none exist, say so and stop.** A PRD written from priors is the exact artifact
this skill is meant to prevent. Offer to run discovery first — or, if the user
insists, proceed and mark every unevidenced section with a visible assumption tag.

### Required Context Keys

1. The validated problem and its evidence.
2. Target personas.
3. Business objectives or OKRs this serves.
4. Known technical context — existing systems, integrations, datastores.
5. Success metrics with baselines.

### Missing Context Rule

Ask at most **3** targeted questions, one at a time, then continue with labelled
assumptions. Prioritise the technical-context question — it is the one discovery
artifacts never contain and the one the architecture section cannot be written
without.

### Section-by-section co-construction

Work **one section at a time**. After each: *Want to refine this section, or move on
to [next section name]?* Wait for the answer.

Fill gaps honestly: session context first, then upstream artifacts, then search.
Label every gap **Assumption** or **Open Question**. Never invent facts, data,
approvals, or commitments.

### The structure

1. **Executive Summary** — problem, solution, impact, in one paragraph. Draft it
   first for clarity; rewrite it last for accuracy.
2. **Problem Statement** — from `problem-statement`. Ground it in evidence: quotes,
   analytics, ticket volume.
3. **Target Users and Personas** — from `proto-persona`. Primary and secondary,
   with jobs-to-be-done.
4. **Strategic Context** — business goals and OKRs, market and competition, why now.
5. **Solution Overview** — high-level description, key flows, key features. Stay
   out of design's territory.
6. **Success Metrics** — primary, secondary, guardrail. Current to target, with the
   measurement method.
7. **User Stories and Requirements** — from `user-story` and
   `epic-breakdown-advisor`. Include edge cases.
8. **Non-Functional Requirements** — performance, availability, security,
   accessibility, observability, data retention. Named, not implied.
9. **Technical Architecture** — **explicitly name the system of record and the
   primary datastore.** Then integrations and data flow.
10. **ADRs** — architectural decision records for the choices that matter, each
    with a status.
11. **Out of Scope** — and why.
12. **Dependencies and Risks** — with mitigations.
13. **Open Questions** — with owners and blocking flags.
14. **Appendices** — anywhere maths, a protocol, or a state machine must be
    verifiable.

### Naming the system of record

One sentence, stated plainly: *X is authoritative for Y; everything else is a read
model.* This single line prevents more argument than any diagram. If it is not
settled, that is an ADR with status Proposed and an owner, not a section you skip.

### ADR status discipline

Each ADR carries **Proposed**, **Accepted**, **Superseded**, or **Rejected**.

**A decision that has not been made stays Proposed.** Do not promote it to Accepted
to make the PRD feel complete. The gap is the information.

### Closing self-critique

After the PRD, append: strongest section, weakest section, top assumptions to
validate, recommended next step. Name the weakest section honestly — a PRD with no
weak section has not been read carefully.

---

## Parameter Block

| Parameter | Default | Notes |
|---|---|---|
| `sections` | all 14 | Drop 8-10 and 14 for a small feature; use `write-spec` instead if you are dropping half |
| `gate_mode` | per section | `batch` drafts all sections then reviews once. Slower to correct |
| `adr_depth` | decisions that affect more than one team | Not every choice needs an ADR |
| `include_appendices` | when maths or a protocol exists | If a calculation must be verified, it belongs in an appendix |

**Governing criterion:** legibility over completeness. A PRD an engineer reads in
full beats one they skim.

---

## Output Block

Use the schema in [`template.md`](template.md). Section order and numbering are a
stability contract.

---

## Validation Block

### Quality gates

- The system of record is named in one plain sentence.
- Every ADR has a status, and Proposed ones have an owner.
- Non-functional requirements are named, with numbers where numbers apply.
- Every metric has a baseline and a measurement method.
- Out of Scope has rationale, not just a list.
- The self-critique names a genuinely weakest section.
- Nothing in the document contradicts an upstream artifact without saying so.

### Do not invent

- Existing systems, APIs, datastores, or their behaviour. Ask.
- Architectural decisions. Propose them; do not accept them on the team's behalf.
- Performance or availability numbers. An SLO nobody agreed to is fiction.
- Compliance requirements. Name the rule or route it to legal.
- Stakeholder approvals or sign-off.
- Baselines. NEEDS DATA is a legitimate value.

### Common pitfalls

1. A PRD written in isolation.
2. A problem statement with no evidence.
3. A solution section so prescriptive it does design's job badly.
4. No primary metric.
5. Out of Scope missing, so scope creeps.
6. Silently resolving an open architectural question.
7. Restating the template before the facts exist — fourteen headed sections and no
   content.
8. Non-functional requirements left implied, then discovered in a security review.

### Assumptions to Validate

Close with this section, then the self-critique.

---

## Final Step

1. Generate a validation plan for the top assumptions (Recommended)
2. Rewrite the weakest section together, section by section
3. Break the requirements into epics and stories with acceptance criteria
4. Produce a one-page executive summary for stakeholder review

Reply with `1`, `2`, `3`, `4`, a combination like `1 and 3`, or your own path.

---

## Examples

[`examples/disputa-express-prd.md`](examples/disputa-express-prd.md)

## Provenance

Adapted from `prompts/prd-prompt-template.md` and `workshops/prd-workshop.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Framework grounding: Martin Eriksson, *How to
Write a Good PRD*; Marty Cagan, *Inspired*; Amazon Working Backwards. Orchestrates
`problem-statement`, `proto-persona`, `user-story`, `epic-breakdown-advisor`. The
bundled `workshop-facilitation` skill supplies the interaction protocol.
