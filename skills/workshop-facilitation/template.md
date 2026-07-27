# Workshop Facilitation - Output Templates

Two artifacts. The **session plan** is written before the session and shown to
the participants. The **session record** is written during it and read back out
loud before anyone leaves.

The record's four section names - **Decisions**, **Dissent**, **Parking Lot**,
**Actions** - are a stability contract. Teams paste them into wikis and diff them
across sessions. Never rename a section, and never delete an empty one: write
`none recorded` so the reader knows the question was asked.

---

## 1. Session plan

```markdown
## Session Plan: <session name>

- **Deliverable**: <what must exist when we finish>
- **Host skill**: <skill name, or "none - standalone facilitation">
- **Timebox**: <total>, starting <time>
- **Decision owner**: <name, role> - decides when the room does not agree
- **Decision rule**: owner decides / dot vote then owner confirms / escalate

### Participants
| Name | Role | Brings | Speaks |
|---|---|---|---|
| <name> | <role> | <the knowledge only they have> | <1st, 2nd, ...> |

Speaking order is reverse seniority. The decision owner speaks last.

### Arrival context
- **Already decided**: <what is not reopening today>
- **Prior artifacts**: <files, links, previous session records>
- **Questions this collapses**: <questions we no longer need to ask>

### Agenda
| Min | Segment | Mode | Output |
|---|---|---|---|
| 0-5 | Frame and contract | facilitator | budget and rules stated |
| 5-x | <segment> | silent write -> round robin | <output> |
| x-y | <segment> | diverge | <options on the wall> |
| y-z | <segment> | converge (dot vote) | <shortlist> |
| last 5 | Read back the record | facilitator | corrected record |

### Question budget
<N> questions, derived from the deliverable, stated at the open. Standing
bypasses announced once: "take your best guess" and bulk drop.
```

---

## 2. Session record

```markdown
## Session Record: <session name>
- **Date**: <date>  **Duration**: <actual, not planned>
- **Present**: <names, and anyone who left early with the minute they left>
- **Absent but affected**: <names - they get the follow-up note>
- **Decision owner**: <name>

## Decisions
| # | Decision | Made by | Basis | Date |
|---|---|---|---|---|
| D1 | <what was decided, in one sentence> | <name> | evidence / judgement / policy | <date> |

## Dissent
| # | Who | Position | Grounds | What would change their mind | Review | Commits? |
|---|---|---|---|---|---|---|
| X1 | <name> | <their position, their words, checked with them> | fact / prediction / value | <metric, threshold> | <date> | yes / no |

## Parking Lot
| # | Item | Raised by | Owner | Next step |
|---|---|---|---|---|
| P1 | <the question we did not answer> | <name> | <name> | <or "dropped, agreed"> |

## Actions
| # | Action | Owner | Due | Depends on |
|---|---|---|---|---|
| A1 | <one verb, one object> | <name, present and asked> | <date> | <D or X ref> |

## Assumptions to Validate
- <what the decision rests on that nobody has confirmed>
- <every open dissent, with the date its evidence arrives>
- <anything recorded as inferred rather than heard>
```

Rules the record enforces:

- A decision with no named owner is not a decision; record it as a parking lot item.
- Dissent is recorded **in the dissenter's words**, checked with them before the
  session closes. Never paraphrase into "had concerns".
- An empty Dissent table is written `none recorded` - never deleted. A reader
  should be able to tell the difference between a room that agreed and a room
  that was never asked.
- Actions name only people who were present and were asked.
- Anything the facilitator inferred rather than heard is labelled **Inference**.

---

## 3. Facilitator close (optional, 4 lines)

```markdown
- **Strongest moment**: <where the room did its best thinking>
- **Weakest**: <where we ran out of time, or one voice dominated>
- **Air time**: <roughly balanced / <name> held most of segment N>
- **For next time**: <one change to the plan>
```

---

## 4. Follow-up note (for people who were not in the room)

```markdown
<Session> on <date> decided <D1> and <D2>.

<Name> did not agree with <D1>, on the grounds that <grounds>. We are reviewing
that on <date> against <metric>. Meanwhile <name> is committed to the decision.

Open: <parking lot items with owners>. Actions: <A1>, <A2>.
```

Sending the dissent to people who were not in the room is the point of recording
it. A follow-up note that reports only the decision hides the most useful part.

---

## Artifact filenames

When this skill runs inside `product-onboarding`, or any time the session needs
to leave a file behind, use these names. The orchestrator's `INDEX.md` refers to
them, so they are part of the contract.

| Artifact | Filename | Written when |
|---|---|---|
| Session plan | `SESSION_PLAN.md` | Before the session |
| Session record | `SESSION_RECORD.md` | Within a day of the session, while memory is fresh |

If several sessions run across an engagement, suffix them --
`SESSION_RECORD_2026-07-24.md`. Never overwrite a prior record: a session record
is evidence of what a room decided on a date, and rewriting it destroys the one
thing it is for.

---

## Provenance

Adapted from `generative-guidance-pattern.md` and `interaction-modes.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, **CC BY-NC-SA 4.0** - also the source of `CONVENTIONS.md`
sections 4 and 5. Dissent register follows disagree-and-commit practice; the
divergence, convergence, and dot-voting moves are common facilitation practice.
