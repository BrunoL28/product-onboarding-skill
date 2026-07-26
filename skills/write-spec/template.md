# Write Spec - Output Template

Section order is a stability contract. Reviewers learn where to look; do not
reorder without a version label.

---

```markdown
# <Feature Name> - Spec

- **Author**: <name>
- **Date**: <YYYY-MM-DD>
- **Status**: draft / in review / agreed
- **Upstream artifacts**: <PROBLEM_STATEMENT.md, LEAN_UX_CANVAS.md, ...>

## 1. Problem Statement

**The problem**: <what the user cannot do today>

**Who has it**: <persona, and how many of them>

**Impact**: <the cost of the problem, with a number where one exists>

**Evidence**:
- <quote, data point, or ticket volume - cite the source>

## 2. Goals

**User goals**
1. <measurable outcome for the user>
2. <measurable outcome>

**Business goals**
1. <measurable outcome for the business>
2. <measurable outcome>

## 3. Non-Goals

Each with a rationale and a reconsider-if condition.

1. **<Thing we are not doing>** - <why> - Reconsider if: <condition>
2. **<Thing we are not doing>** - <why> - Reconsider if: <condition>
3. **<Thing we are not doing>** - <why> - Reconsider if: <condition>

## 4. User Stories

**<Persona>**
- As a <persona>, I want to <action>, so that <outcome>
- As a <persona>, I want to <action>, so that <outcome>

**Edge cases**
- As a <persona> in <edge condition>, I want to <action>, so that <outcome>

## 5. Requirements

### P0 - Must have

| # | Requirement | Acceptance criteria | Survived P0 challenge? |
|---|---|---|---|
| P0-1 | <requirement> | <Given/When/Then or checklist> | yes - <which of the three questions> |

### P1 - Nice to have

| # | Requirement | Acceptance criteria |
|---|---|---|
| P1-1 | <requirement> | <criteria> |

### P2 - Future

| # | Requirement | Why later |
|---|---|---|
| P2-1 | <requirement> | <reason> |

## 6. Success Metrics

**Leading** (tells us in time to change course)

| Metric | Current | Target | How measured |
|---|---|---|---|
| <metric> | <baseline or NEEDS DATA> | <target> | <instrumentation, query, or survey> |

**Lagging** (tells us whether it worked)

| Metric | Current | Target | How measured |
|---|---|---|---|
| <metric> | <baseline or NEEDS DATA> | <target> | <method> |

**Guardrail** (must not degrade)

| Metric | Current | Must stay | How measured |
|---|---|---|---|
| <metric> | <baseline> | <threshold> | <method> |

## 7. Open Questions

| # | Question | Owner | Blocking? |
|---|---|---|---|
| 1 | <question> | eng / design / legal / data | yes / no |

## 8. Timeline Considerations

- **Hard deadlines**: <date and what makes it hard, or none>
- **Dependencies**: <team or system, and whether they have been asked>
- **Phasing**: <what ships first, and the gate before the next phase>

## Assumptions to Validate

- <Assumption 1> - <how to settle it>
- <Assumption 2> - <how to settle it>
```

---

## P0 challenge record

Run before the spec ships. Include the table so reviewers can see the reasoning.

```markdown
### P0 Challenge

| Requirement | Breaks if omitted? | Core journey possible without it? | Regulatory or hard dependency? | Verdict |
|---|---|---|---|---|
| <req> | <answer> | <answer> | <answer> | P0 / demoted to P1 |

**Demoted**: <list, or none>
**All survived**: <if so, the defence for that>
```

---

## Provenance

Adapted from the `write-spec` skill in Anthropic's `product-management` example
plugin (MIT). Conventions from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0.
