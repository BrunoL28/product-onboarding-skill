# PRD - Worked Example

PRD for Aurora Bank's *Disputa Express* v1. Fictional.

The useful parts: the **system-of-record sentence** that ended a recurring
argument, and an **ADR that stayed Proposed** rather than being quietly resolved.

---

## Artifact precondition and the one question worth asking

**Agent:**

> Five upstream artifacts present, so the precondition is met and Sections 2, 3, 6,
> 7, and 11 are largely derivable.
>
> The gap is Section 9. Discovery artifacts never contain technical context, and I
> will not guess an architecture. One question:
>
> **What exists today?** Specifically: where does a dispute physically live, what
> state does it already have, and what can emit an event when that state changes?

**User:** It's a table in the back-office system, Genesys handles the calls, and ops
work it through a queue UI. There's a status column with about a dozen internal
codes. I don't know if anything can emit on change.

**Agent:** That last part is the spike, then — and it is an ADR, because the answer
decides whether v1 is event-driven or polled. Drafting Section 9 now.

---

## Output (excerpts)

```markdown
# Disputa Express PRD

- **Author**: PM, Cards squad
- **Version**: 0.3
- **Date**: 2026-07-25
- **Status**: in review
- **Upstream artifacts**: PROBLEM_STATEMENT.md, PROTO_PERSONA.md, PESTEL.md,
  LEAN_UX_CANVAS.md, USER_STORY_MAP.md, SPEC.md

## 1. Executive Summary

First-time cardholders who report a fraudulent charge cannot find out whether they
are still liable for it without calling and re-explaining their case. Disputes live
in a back-office queue built for ops, not customers, so 31% of call minutes are
people asking what is happening. Disputa Express v1 puts a read-only, plain-language
view of an existing dispute in the app, states liability explicitly, and warns when
a scheme deadline has passed. Target: contact rate per active card from 0.14 to
0.10 without degrading the 71% dispute approval rate.

## 9. Technical Architecture

### System of record

The back-office dispute table remains authoritative for dispute state. The app is
a read model over it and never writes state directly.

### Primary datastore

No new datastore for v1. The app reads a projection of the existing dispute table.
Rationale: a second source of dispute truth in a regulated journey is a
reconciliation liability, and nothing in v1 requires state the back office does not
already hold.

### Integrations

| System | Direction | Purpose | Confirmed? |
|---|---|---|---|
| Back-office dispute table | read | dispute state, amounts, timestamps | yes |
| Genesys | read | link phone-opened disputes to the app view | partially - see ADR-2 |
| Push service | write | notify on state change (P1, slice 2) | yes |
| Internal code mapping service | read | internal code to customer-facing state | does not exist - to build |

### Data flow

Ops change state in the queue UI. The projection surfaces the mapped
customer-facing state. Whether that projection is event-driven or polled is ADR-2.

## 10. Architectural Decision Records

### ADR-1: The app is a read model, not a second source of truth

- **Status**: Accepted
- **Context**: Two candidate designs - mirror dispute state into a
  customer-facing store, or project from the back-office table on read. The journey
  is regulated and the back office is where ops already work.
- **Decision**: The back-office table is authoritative. The app never writes state.
- **Consequences**: Makes reconciliation a non-issue and keeps ops workflow
  unchanged. Makes the app's latency and availability dependent on the back office,
  and makes offline state display impossible.
- **Alternatives considered**: A dedicated dispute service owning customer-facing
  state. Rejected for v1 - it is the right long-term shape but requires a migration
  and a dual-write period that v1 does not justify.

### ADR-2: State propagation - event-driven or polled

- **Status**: **Proposed**
- **Owner**: Platform tech lead
- **Needed by**: end of week 2, before slice 1 build starts
- **Context**: The customer-facing state must reflect back-office changes. We do
  not currently know whether the back office or Genesys can emit an event on state
  change. If neither can, the options are polling on a schedule or polling on app
  open.
- **Decision**: Not yet made. A two-day spike will establish whether an event hook
  exists.
- **Consequences**: Event-driven enables push notifications in slice 2 at low extra
  cost. Polling on app open makes slice 2's push story significantly more
  expensive and possibly not worth building.
- **Alternatives considered**: Recorded, but pending the spike result.

### ADR-3: Regulated acknowledgement clock start point

- **Status**: **Proposed**
- **Owner**: Legal
- **Needed by**: before v1 scope lock
- **Context**: Regulated acknowledgement timelines apply. Whether the clock starts
  at customer submission or at bank acknowledgement changes whether app submission
  starts a compliance obligation the back office is not staffed to meet.
- **Decision**: Not made. This is a legal reading, not a product decision.
- **Consequences**: If the clock starts at submission, opening disputes in-app
  increases regulated volume with no ops change, which is a compliance risk rather
  than a CX win. That would make status-only v1 the safer scope.

## Assumptions to Validate

- That visible status deflects calls rather than adding a checkpoint - Box 7
  experiment, result due week 2.
- That the dozen internal codes map cleanly onto a small set of customer-facing
  states - needs an ops review; if they do not, the mapping service is larger than
  estimated.
- That 3.1 repeat calls per dispute is roughly right - it is a 40-ticket estimate
  being used as a baseline.
```

---

## Closing self-critique

```markdown
### Self-Critique

- **Strongest section**: 9 and 10. The system-of-record sentence and ADR-1 settle
  the question that would otherwise be re-litigated in every design review.
- **Weakest section**: 8, Non-Functional Requirements. Availability and latency
  targets are inherited from the back office and nobody has agreed to a number.
  Every row is a proposal with no agreed-by. Fixing it needs thirty minutes with
  the platform lead, not more writing.
- **Top assumptions to validate**: the Box 7 deflection assumption; the internal
  code mapping being small; the repeat-calls baseline.
- **Recommended next step**: run the ADR-2 spike now. It gates slice 1 and it is
  two days.
```

---

## What this example is meant to teach

1. **One sentence ended a recurring argument.** *The back-office dispute table
   remains authoritative; the app is a read model.* Teams re-litigate this for
   weeks when it is not written down.
2. **Two ADRs stayed Proposed, with owners and dates.** ADR-2 and ADR-3 were not
   promoted to Accepted to make the PRD look finished. Each has a named owner and a
   needed-by, which is what makes an open decision actionable rather than merely
   honest.
3. **ADR-3 could invalidate the scope, and the PRD says so.** If the regulated
   clock starts at submission, in-app submission raises regulated volume without an
   ops change. The PRD states that consequence plainly instead of hiding it.
4. **The weakest section was named honestly and cheaply.** Section 8 has no agreed
   numbers. Saying so, and saying it costs thirty minutes to fix, is more useful
   than inventing an SLO.
5. **The PRD cites discovery rather than rewriting it.** Section 1 is one
   paragraph; the evidence lives upstream and is referenced.

---

## Provenance

Example built on the schema in `prompts/prd-prompt-template.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Aurora Bank is fictional; all figures, systems,
and decisions are invented.
