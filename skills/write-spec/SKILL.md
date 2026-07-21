---
name: write-spec
description: Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a feature with goals and non-goals, defining success metrics and acceptance criteria, or breaking a big ask into a phased spec.
---

# Write Spec

Write a feature specification or product requirements document.

## Workflow

### 1. Understand the feature
Accept a feature name, a problem statement, a user request, or a vague idea.

### 2. Gather context (conversationally, most important first)
User problem & who has it; target users; success metrics; constraints (technical, timeline, regulatory, dependencies); prior art.

### 3. Pull context from connected tools
If a project tracker / knowledge base / design tool is connected, search for related tickets, docs, research, and mockups. Otherwise work from what the user provides.

### 4. Generate the spec
Sections: **Problem Statement** (user problem, who, impact); **Goals** (3–5 measurable outcomes, user vs business); **Non-Goals** (3–5 out-of-scope items with rationale); **User Stories** (As a/I want/so that, grouped by persona, incl. edge cases); **Requirements** categorized **Must-Have (P0) / Nice-to-Have (P1) / Future (P2)** each with acceptance criteria; **Success Metrics** (leading + lagging with targets and measurement method); **Open Questions** (tagged with owner: eng/design/legal/data; blocking vs non-blocking); **Timeline Considerations** (hard deadlines, dependencies, phasing).

### 5. Review and iterate
Ask what needs adjustment; offer follow-ups (design brief, ticket breakdown, stakeholder pitch).

## Key guidance
- Be opinionated about scope; a tight spec beats an expansive vague one.
- Be ruthless about P0s — if everything is P0, nothing is.
- Non-goals are as important as goals; they prevent scope creep.
- Success metrics must be specific and measurable.
- Acceptance criteria in Given/When/Then or checklist; cover happy path, errors, edge cases; include negative cases.
- Keep the document scannable — headers and bold carry the gist.

### Provenance
From the product-management plugin's `write-spec` skill. Bundled here in the product-onboarding plugin for self-containment.
