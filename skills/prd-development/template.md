# PRD - Output Template

Section order and numbering are a stability contract. Sections 8-10 and 14 may be
dropped for a small feature; if you are dropping half, use `write-spec` instead.

---

```markdown
# <Feature/Product Name> PRD

- **Author**: <name>
- **Version**: <n.n>
- **Date**: <YYYY-MM-DD>
- **Status**: draft / in review / agreed / superseded
- **Upstream artifacts**: <list>

## 1. Executive Summary

<One paragraph: the problem, the solution, the expected impact. Drafted first for
clarity, rewritten last for accuracy.>

## 2. Problem Statement

- **Who has this problem**: <persona, and how many>
- **What the problem is, and why it is painful**: <plain language>
- **Evidence**: <quotes, analytics, ticket volume - cite each>

## 3. Target Users & Personas

- **Primary persona**: <name> - JTBD: <job>
- **Secondary persona**: <name> - JTBD: <job>
- **Explicitly not served in this version**: <who, and why>

## 4. Strategic Context

- **Business goals this serves**: <OKR or objective>
- **Market and competitive landscape**: <one paragraph, cited>
- **Why now**: <the trigger>

## 5. Solution Overview

- **High-level description**: <what it is>
- **Key user flows**: <flow, step by step at a high level>
- **Key features**: <list>
- **Design ownership note**: <what design decides, not this document>

## 6. Success Metrics

| Type | Metric | Current | Target | How measured |
|---|---|---|---|---|
| Primary | | | | |
| Secondary | | | | |
| Guardrail | | must stay | | |

- **Failure signals to watch**: <what would tell us to stop>

## 7. User Stories & Requirements

### Epic: <name>
- **<US-n>** As a <persona>, I want to <action>, so that <outcome>
  - **Given** <precondition> **When** <trigger> **Then** <outcome>

### Edge cases
- <case and expected behaviour>

## 8. Non-Functional Requirements

| Category | Requirement | Target | Agreed by |
|---|---|---|---|
| Performance | | | |
| Availability | | | |
| Security | | | |
| Accessibility | | | |
| Observability | | | |
| Data retention | | | |

<An NFR with no agreed-by is a proposal. Mark it as such.>

## 9. Technical Architecture

### System of record

<One plain sentence: X is authoritative for Y; everything else is a read model.>

### Primary datastore

<Named, with the reason.>

### Integrations

| System | Direction | Purpose | Confirmed? |
|---|---|---|---|

### Data flow

<How data moves, at a level an engineer can argue with.>

## 10. Architectural Decision Records

```
### ADR-<n>: <decision title>

- **Status**: Proposed / Accepted / Superseded / Rejected
- **Owner**: <who decides, required if Proposed>
- **Needed by**: <date or milestone, required if Proposed>
- **Context**: <what forces are at play>
- **Decision**: <what was decided, or what is proposed>
- **Consequences**: <what this makes easy, what it makes hard>
- **Alternatives considered**: <and why not>
```

<A decision that has not been made stays Proposed. Do not promote it to make the
document look finished.>

## 11. Out of Scope

| Not building | Why | Reconsider if |
|---|---|---|

## 12. Dependencies & Risks

**Dependencies**

| Dependency | Team or system | Asked? | Blocking? |
|---|---|---|---|

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|

## 13. Open Questions

| # | Question | Owner | Blocking? | Needed by |
|---|---|---|---|---|

## 14. Appendices

- **Appendix A**: <calculation, state machine, or protocol that must be verifiable>

## Assumptions to Validate

- <Assumption 1> - <how to settle it>
- <Assumption 2> - <how to settle it>
```

---

## Closing self-critique

Append after the PRD. Not optional — a PRD with no weakest section has not been
read carefully.

```markdown
### Self-Critique

- **Strongest section**: <which, and why>
- **Weakest section**: <which, and what would fix it>
- **Top assumptions to validate**: <the three that matter most>
- **Recommended next step**: <one action>
```

---

## Provenance

Adapted from `prompts/prd-prompt-template.md` and `workshops/prd-workshop.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0.
