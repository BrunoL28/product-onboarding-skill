---
name: epic-breakdown-advisor
description: Break down epics into user stories with Humanizing Work split patterns. Use when a backlog item is too large to estimate, sequence, or deliver safely.
---

## Purpose
Break epics into user stories using Richard Lawrence's Humanizing Work methodology—a systematic, flowchart-driven approach applying 9 splitting patterns sequentially. Split while preserving user value (vertical slices delivering end-to-end value), not horizontal slices (technical layers).

## Three-step process
1. **Pre-split validation (INVEST, except Small):** Independent, Negotiable, Valuable, Estimable, Testable. If it fails "Valuable," stop—it's a technical task; reframe.
2. **Apply splitting patterns in order** until one fits:
   1. Workflow Steps (thin end-to-end slices, not step-by-step)
   2. Operations (CRUD)
   3. Business Rule Variations
   4. Data Variations
   5. Data Entry Methods (simple UI first)
   6. Major Effort (implement one + add remaining)
   7. Simple/Complex (core simplest version first)
   8. Defer Performance (make it work before fast)
   9. Break Out a Spike (time-boxed investigation for uncertainty)
3. **Evaluate splits:** prefer splits that reveal low-value work to deprioritize, or that produce roughly equal-sized stories.

**Meta-pattern:** identify core complexity → list variations → reduce to one complete vertical slice → make other variations separate stories.

## Output
Per story: summary, use case (As a/I want/so that), acceptance criteria (Given/When/Then), why-first, estimate. Plus a split evaluation and INVEST check. A board-ready flat export (one row per story: ID, Epic, Type, Summary, User Story, Acceptance Criteria, Priority, Release, Estimate, Dependencies, Labels) is ideal for importing to a dev board.

## Common Pitfalls
1. Skipping INVEST validation.
2. Step-by-step workflow splitting (should be thin end-to-end).
3. Horizontal slicing (build API / build UI) — keep vertical.
4. Forcing a pattern that doesn't fit.
5. Not re-splitting stories still >5 days.
6. Ignoring split evaluation.

### References
Richard Lawrence & Peter Green, *The Humanizing Work Guide to Splitting User Stories*; Bill Wake, INVEST. When run interactively, an optional `workshop-facilitation` skill provides the session protocol; the domain logic here is self-contained.
