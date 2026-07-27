# Product Strategy Session - Worked Example

A `closing-session` run over Aurora Bank's *Disputa Express* artifact set, 100
minutes on 2026-07-30. Aurora Bank is fictional and **every figure below is
invented**. The artifact is shown in excerpt.

The point is what the session refuses to do. The coherence check finds a P0 in
the committed slice that the PRD scoped out; the room can argue it both ways in
four minutes and the facilitator will not let it close. It leaves as `SS-1`,
owned and dated. Cast carried from the `workshop-facilitation` example: Rafael
Nunes (PM), Beatriz Amaral (engineering), Tereza Villar (fraud ops), Marcos Pinho
(design), Carla Reis (compliance, not in the room).

---

## Precondition: who can actually decide

**Agent:** Who is the sponsor, and what can they approve?

**Rafael:** Helena Braga, Head of Cards. She has read the roadmap and the PRD
executive summary. Scope inside Cards and squad allocation, yes; headcount is the
October budget round.

**Agent:** Recorded - so any ask needing money leaves marked **pending**, not
agreed. Eight artifacts read, none summarised back to me: one stale (the epic
hypothesis guardrail was never queried), one gap (nothing says what an in-app
dispute does to the Bacen clock). The gap returns at S6.

## Step 2: the seam that did not hold

**Agent:** Seven seams walked. The one that matters, quoted in full:

> **S5 - backlog P0s vs PRD scope. Contradiction.** PRD Section 1: *"a
> **read-only**, plain-language view of an **existing dispute** in the app"*,
> ADR-1 **Accepted**: *"The app never writes state."* Roadmap **Now -
> committed**: *"Open a dispute in the app | Disputes opened without a call: 0%
> -> 60% of new disputes"*; breakdown DE-3, **P0, Slice 1**: *"a dispute is
> created with a reference."* Creating a dispute is a write.

**Beatriz:** Not real. The app calls the back-office API; the back office writes.

**Marcos:** Then why does the PRD only ever describe an existing dispute?

**Rafael:** It is a wording problem. I can amend the PRD line this afternoon.

**Agent:** Then answer what is underneath it. ADR-3 is **Proposed**, owner
**Legal**: *"If the clock starts at submission, opening disputes in-app increases
regulated volume with no ops change... That would make status-only v1 the safer
scope."* Carla is not in this room. Amend the line today and a committed slice
rests on a Proposed ADR resolving the way you prefer - seam **S6**, same finding.

**Rafael:** Fine. It stays open.

**Agent:** As `SS-1`, with an owner, a date and a default if the date passes.

Three shorter contradictions went into the table without being re-argued: two
contact-rate targets (PRD 0.10, hypothesis and roadmap 0.115) and two approval
baselines for one guardrail (71% and 62%); the only committed spike testing
slice-2 push rather than the assumption slice 1 rests on; and a scheme-window
warning that is v1 in the PRD and P0 in the spec but appears nowhere on the
roadmap.

## Steps 3 and 4: premortem, then the bet

Three minutes of silence, everyone writes, Helena reads last. Past tense: it is
July 2027 and this failed badly.

**Tereza (1st):** Abuse - but my number is already instrumented. Invalid-or-
withdrawn above 12%, reviewed 2026-09-08, from the July session.

**Agent:** Then it keeps that falsifier. We do not invent a second one.

**Marcos (2nd):** She opens the app, reads "in review", and calls anyway.

**Beatriz (3rd):** The twelve internal codes never mapped. Most disputes sit in
one opaque state for nine days of eleven.

**Rafael (last, self-inflicted):** We reported contact rate, it fell, phase 2 got
funded on it, and nobody measured whether she knew she was liable. Positioning
said we were giving up *"the internal cost story"*, then we shipped its metric as
the headline.

Everyone then named the biggest bet in silence: Rafael submission volume, Beatriz
the code mapping, Tereza abuse, Marcos legibility, Helena call deflection.

**Agent:** Five people, four bets, none matching the sponsor's - the spread is
the finding. The bet the artifacts rest on is that visible state answers the
liability question, and what kills it is not the screen but how often the state
changes.

## The artifact (excerpts)

```markdown
# Disputa Express Strategy Session
- **Mode**: closing-session (Phase 5 of product-onboarding)
- **Date**: 2026-07-30  **Timebox**: 100 min planned / 104 actual, inside a
  3-week engagement window from 2026-07-14
- **Sponsor**: Helena Braga, Head of Cards - decides scope inside Cards and squad
  allocation; cannot approve headcount before the October round
- **Sponsor has read**: the roadmap; the PRD executive summary only
- **Decision owner**: Rafael Nunes
- **Session record**: aurora-bank-dispute-session.md (2026-07-14)
- **Premortem horizon**: 12 months

### Participants
| Name | Role | Brings | Present for |
|---|---|---|---|
| Marcos Pinho | Design | What Camila does with an empty screen | all |
| Tereza Villar | Fraud ops | Abuse patterns, the manual queue | all |
| Beatriz Amaral | Engineering | What the back office can emit | all |
| Rafael Nunes | PM, decision owner | The steering-group commitment | all |
| Helena Braga | Head of Cards, sponsor | Scope, squad allocation | 0-30, 85-104 |
| Carla Reis | Compliance | The Bacen reading | absent - owns SS-2 |

## Artifact inventory (8 rows, version and date each - excerpted)
| Artifact | Version | Date | Status | Read? | Stale? |
|---|---|---|---|---|---|
| PRD.md | 0.3 | 2026-07-25 | in review | yes | no |
| EPIC_HYPOTHESES.md | 1.0 | 2026-07-21 | agreed | yes | yes - guardrail never queried |
| ROADMAP.md | 1.0 | 2026-07-28 | in review | yes | no |

- **Missing**: nothing states the ops consequence of in-app submission if the
  Bacen clock starts at submission. Feeds SS-1 and SS-2.
- **Stale**: EPIC_HYPOTHESIS guardrail baseline (62%) contradicts the PRD (71%).

## Coherence check
| # | Seam | Verdict | Finding |
|---|---|---|---|
| S1 | Positioning vs problem statement | holds | Both name first-time mobile-only disputers and liability certainty; segment size unvalidated, see S7 |
| S2 | Problem statement vs PRD scope | contradiction | C4 - scheme-window warning is v1/P0 in PRD and spec, absent from the roadmap |
| S3 | PRD metrics vs the stated outcome | contradiction | C2 - two contact-rate targets, two approval-rate baselines |
| S4 | Roadmap sequence vs riskiest assumption | contradiction | C3 - the only spike tests slice-2 push, not the assumption slice 1 rests on |
| S5 | Backlog P0s vs PRD scope and non-goals | contradiction | C1 - DE-3 is a committed P0 the PRD scoped out |
| S6 | Open decisions vs committed sequence | contradiction | C1 - a committed slice assumes ADR-3 resolves one way |
| S7 | Evidence base vs the weight on it | contradiction | Both Now initiatives rest on n = 3 transcripts; the 3.1 repeat-calls baseline is a 40-ticket estimate |

### C1: the committed slice creates a dispute; the accepted architecture says the app never writes
- **Side A** - PRD Section 1 / ADR-1 (Accepted): "a read-only, plain-language
  view of an existing dispute in the app" / "The app never writes state."
- **Side B** - Roadmap Now / BREAKDOWN DE-3 (P0, Slice 1): "Open a dispute in the
  app... 0% -> 60% of new disputes" / "a dispute is created."
- **Not a wording problem because**: ADR-3 is Proposed, owner Legal, and says
  status-only is the safer v1 if the clock starts at submission.
- **Confirmed real by**: Marcos Pinho. **Resolved here?**: no -> SS-1, SS-2

C2, C3 and C4 sit in the table rows above and carry to SS-3, SS-4 and SS-5. Only
C1 needed a full both-sides block.

## Premortem - 12 months
### Failure narrative (past tense)
Slice 1 shipped in September. Camila opened the app, read "in review" for nine of
eleven days, and called anyway. Contact rate fell four points on submission
deflection alone, phase 2 was funded on that number, and nobody measured the
liability question. In February compliance ruled the clock starts at submission,
in-app opening was switched off for six weeks, and the outcome was withdrawn.

### Causes, all five categories
- **Market and customer**: reads status, calls anyway | small charges abandoned
- **Product and solution**: twelve codes never mapped | one opaque state for days
- **Organizational and political**: clock ruled at submission | ops unstaffed
- **Execution and delivery**: skeleton never resized | spike answered too late
- **Self-inflicted**: shipped the metric positioning disowned | amended the PRD to
  make the set look finished

### Ranked top five, then converted to risks
| # | Assumed cause of death | Category | L x D | Risk, restated | Owner | Early-warning signal | Falsifier | Mitigation |
|---|---|---|---|---|---|---|---|---|
| R1 | She read the status and called anyway | market | H x H | Visible state does not answer liability | Marcos Pinho | calls within 24h of an in-app view | 20 panel disputers: 70%+ say they know whether they owe it, call-after-view under 15% | two questions on the existing panel, w/c 2026-08-10 |
| R2 | Twelve codes never mapped | product | H x M | Mapping larger than estimated; one opaque state for days | Beatriz Amaral | ops review needs more than 4 states | 10 of 12 codes map to 4 states or fewer, each with a liability line, by 2026-08-06 | half-day ops review before build |
| R3 | Clock ruled at submission | organizational | M x H | In-app opening raises regulated volume with no ops change | Carla Reis | legal reading trends to submission | reading lands on acknowledgement, by 2026-08-04 | SS-1 default is status-only |
| R4 | We reported contact rate and called it a win | self-inflicted | H x M | Phase 2 funded on a proxy positioning disowned | Rafael Nunes | steering deck leads with contact rate, no liability measure | paired liability measure in the same deck from 2026-08-12 | add it to the read-out |
| R5 | Slice 1 slipped, steering saw a date miss | execution | M x M | Skeleton unsized, capacity gate OPEN | Beatriz Amaral | gate still OPEN at 2026-08-05 | engineering sizes the thin skeleton | resize at Monday planning |

Abuse is carried, not reopened: dissent X1 already has a falsifier (above 12%,
reviewed 2026-09-08).

### Watchlist - unowned
| Cause | Why unowned | First decision |
|---|---|---|
| Back-office re-platform lands mid-year and breaks the read model | The re-platform has no named sponsor and no outcome | who owns this, by 2026-08-07 -> SS-7 |

## The biggest bet
- **Named in silence by**: Rafael: submission volume | Beatriz: code mapping |
  Tereza: abuse | Marcos: legibility | Helena: call deflection
- **The disagreement itself**: five people, four bets, none the sponsor's
- **The bet, as tested**: making the existing back-office state visible in plain
  language answers Camila's liability question well enough that she does not call

| # | What would have to be true | Label | If false |
|---|---|---|---|
| B1 | 4,200 disputes a month arrive by phone today | Fact (Q2 deck) | n/a |
| B2 | The twelve internal codes map onto a few customer-facing states | Assumption | kills the bet |
| B3 | State changes often enough to be worth opening the app for | Assumption | kills the bet |
| B4 | Liability certainty matters more than refund speed | Inference (n = 3) | survivable; changes the copy |

- **The killing condition**: B3 - the bet is state-change frequency, not the screen
- **Sequenced first?**: no - the only committed spike tests slice-2 push emission
- **Cheapest thing that would tell us**: 200 closed disputes, time-in-state per
  code, half a day of SQL - Tereza Villar, 2026-08-06

## Decision log
| ID | Decision or question | Status | Option chosen | Owner | Date | If the date passes |
|---|---|---|---|---|---|---|
| SS-1 | Does v1 include in-app dispute creation, or is it status-only over an existing dispute? | open | none - still open | Rafael Nunes | 2026-08-07 | Slice 1 defaults to status-only, the Now table is rewritten, Helena told the same day |
| SS-2 | Bacen clock start point (ADR-3): submission or acknowledgement? | open | none - still open | Carla Reis | 2026-08-04 | SS-1 cannot close; Rafael escalates to the legal director |
| SS-3 | Which contact-rate target is committed, 0.10 or 0.115 - and is contact rate the primary measure at all? | pending | none - Helena took it to the steering group | Helena Braga | 2026-08-12 | The hypothesis figure stands, the PRD is corrected, no steering commitment recorded |
| SS-4 | Dispute approval rate baseline: 62% or 71%? | open | one query against the ops report | Tereza Villar | 2026-07-31 | Slice 1 ships with an unusable guardrail |
| SS-5 | Is the scheme-window warning in v1, and where does it sit on the roadmap? | open | none - still open | Rafael Nunes | 2026-08-07 | Treated as a PRD error, struck from v1, PRD updated |
| SS-6 | Who accepts the 0.135 kill threshold for DE-EPIC-2? | pending | requested of Helena Braga in session | Helena Braga | 2026-08-12 | The hypothesis has no kill owner; Rafael escalates to the Cards tribe lead |
| SS-7 | Who owns the re-platform risk on the watchlist? | open | none - unowned, proposed to Beatriz Amaral | unidentified - the first decision is who | 2026-08-07 | Stays labelled unowned, re-read at the next session |

- **Read back in the room?**: yes (SS-4 owner was Beatriz, corrected to Tereza
  by Beatriz; SS-3 date moved to the steering date)
- **Carried from the session record**: X1 (review 2026-09-08), P1 (DE-7 spike)
- **Requested but not granted**: Helena said she would take SS-3 and SS-6 to the
  steering group on 2026-08-12. Nothing was approved; both rows are pending.

## Assumptions to Validate
- B2 and B3 are Assumptions and the bet dies on either: ops code review and the
  time-in-state query, both 2026-08-06.
- B4 rests on n = 3 transcripts and carries the liability framing. Ten disputers
  ranking liability against refund speed would settle it.
- S7: both Now initiatives rest on that same n = 3; the 3.1 repeat-calls baseline
  is a 40-ticket estimate used as a measure.
- The 60% in-app submission target is an Assumption, void if SS-1 lands on
  status-only.
- SS-1, SS-2, SS-4, SS-5 and SS-7 are open; SS-3 and SS-6 are pending on a
  steering group nobody in this room sits on.
```

---

## What this example is meant to teach

1. **The seam is the finding.** One amended PRD line would have made the set
   coherent in four minutes - and committed slice 1 to a legal reading nobody
   had done.
2. **A contradiction with an owner and a date beats agreement.** `SS-1` is the
   row anyone rereads on 2026-08-07.
3. **The best premortem cause was self-inflicted**, and came from the PM:
   shipping the metric the positioning had explicitly disowned.
4. **Do not invent a second falsifier.** Tereza's abuse prediction already had a
   number and a date; the premortem cited it and moved on.
5. **The bet was not the feature, and pending is not approved.** What kills it is
   how often state changes, which nothing tests first - and Helena agreeing to
   raise two rows at steering is recorded as pending, not as a decision.

---

## Provenance

Adapted from `prompts/strategic-scrum-team-session-kickoff.md` and
`prompts/premortem-prompt-template.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, **CC BY-NC-SA 4.0**. Premortem: Gary Klein, *Performing a Project
Premortem*, HBR 2007. Aurora Bank, Disputa Express, Cardholder Camila and every
participant are fictional; every figure here was invented for the example.
