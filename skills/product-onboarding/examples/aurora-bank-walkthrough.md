# Product Onboarding - Worked Example: Aurora Bank "Disputa Express"

A condensed six-phase run; every figure is invented. Aurora Bank is a fictional
mid-size digital bank whose card fraud disputes are handled by phone, take 11 days
to acknowledge, and drive its highest call volume; *Disputa Express* lets a
cardholder open and track one in-app. **Cast:** Rafael Nunes (PM, decision owner),
Beatriz Amaral (engineering), Tereza Villar (fraud ops), Marcos Pinho (design),
Helena Braga (Head of Cards, sponsor). Handoff blocks name every sub-skill a phase
runs; only notable runs are narrated, elided as `[runs <skill> -> ARTIFACT.md]`.
Detail lives in those skills' own examples -
[problem-statement](../../problem-statement/examples/disputa-express-problem-statement.md),
[pol-probe-advisor](../../pol-probe-advisor/examples/disputa-express-status-probe.md),
[roadmap-planning](../../roadmap-planning/examples/disputa-express-roadmap.md).

## Step 1 - Artifact-First Context Intake

**User:** I need to onboard a new product. We want cardholders to open fraud
disputes in the app instead of calling. Attaching the support team's Q2 deck.

**Agent:**

> Reading the deck before I ask anything. No `INDEX.md` in this session or the
> working folder, so this is a fresh run and not a resume.
> **Found** - 4,200 disputes/month; 11-day median acknowledgement; 31% of call
> minutes; Genesys plus a manual back-office queue. Product and company given.
> **Inferred** - a retail cardholder, not a business customer (the deck breaks out
> consumer cards only); the "regulatory pressure" slide means Bacen timelines.
> **Still missing** - stakeholder (key 2), the cardholder v1 is for (key 3),
> competitors (4), constraints (5), board destination (6).
>
> Three questions maximum, one at a time. Say "take your best guess" at any point,
> or drop more notes and I re-read rather than ask.

## Kickoff intake - three questions, then labelled defaults

> **Question 1 of 3: the protagonist.** The deck splits consumer from business
> cards but not by behaviour. Who is v1 for - (1) the blindsided first-timer, never
> disputed, wants reassurance, (2) the repeat disputer, knows the process, wants
> speed, (3) the high-balance saver, low volume and high churn cost, or (4) yours?

**User:** 1. Most callers have never done it before and just want to know they are
not on the hook for the money.

**Agent:** Then reassurance is a requirement, not a nice-to-have. *(Question 2: the
stakeholder - Helena Braga, sponsor; Rafael Nunes, PM. Question 3 spent the budget
on the constraint no search settles - do Bacen timelines bind acknowledgement,
resolution, or both? Both, probably, and nobody owns the reading.)*

> Budget spent; the rest are labelled defaults, not questions.
> **[ASSUMPTION] Board target: none** - I show the cards at Phase 4 and stop.
> **[ASSUMPTION] No hard deadline**; **competitors** derived by search in Phase 1;
> **[OPEN] Bacen clock** carried to Phase 3 unowned rather than resolved.

**Step 2.** Working folder `./product-onboarding/disputa-express/`; `INDEX.md`
written with 20 rows, all `pending`; `MEASUREMENT.md` opened empty. Depth
`standard`, facilitation `room`.

## Phase 0 - Framing

```markdown
### Starting Phase 0: Framing
**Carrying forward**: the first-time disputer; a sponsor who can move scope
**Sub-skills**: positioning-workshop -> POSITIONING.md; jobs-to-be-done -> JTBD.md
**Measurement thread advances to**: nothing - Phase 0 has no number to capture
**Not yet resolved, and not resolved here**: Bacen clock start point
```

`[runs positioning-workshop -> POSITIONING.md]` "Faster and simpler" failed the swap test.
`[runs jobs-to-be-done -> JTBD.md]` Main job: *clear an unrecognised charge off my card and off my name.*

**Gate:** name the customer and the job in one sentence each, without naming the
product. Passed (Rafael Nunes), and it retargets Phase 1 at the wait, not the form.

## Phase 1 - Discovery

```markdown
### Starting Phase 1: Discovery
**Carrying forward**: JTBD.md - the job is liability removal, not form submission;
POSITIONING.md - the alternative is the support line, not a competitor
**Sub-skills**: company-research -> COMPANY_RESEARCH.md; pestel-analysis -> PESTEL.md;
tam-sam-som-calculator -> MARKET_SIZING.md; proto-persona -> PROTO_PERSONA.md;
problem-statement -> PROBLEM_STATEMENT.md
**Measurement thread advances to**: baseline, with a source against every number
**Not yet resolved, and not resolved here**: Bacen clock start point
```

`[runs pestel-analysis -> PESTEL.md]` One Legal entry changes scope: Bacen makes
acknowledgement a compliance surface. Two competitors publish a 72-hour SLA
[company-research, Fact with URLs]; sizing ran in value-pool mode.
`[runs proto-persona -> PROTO_PERSONA.md]` **Cardholder Camila**, 34, Recife,
mobile-only; household income shipped as `[PLACEHOLDER - NEEDS RESEARCH]`.
`[runs problem-statement -> PROBLEM_STATEMENT.md]` She needs to know she is no
longer liable for the R$ 480, because her dispute sits in a queue built for ops.

**Measurement thread, baseline captured:**

```markdown
| Metric | Baseline (+ source) | Target | Instrument | Read-out | Owner |
|---|---|---|---|---|---|
| Contact rate per active card | 0.14 - telephony dashboard [Fact] | | | | |
| Repeat contacts per dispute | 3.1 - 40-ticket sample [ASSUMPTION] | | | | |
| Median acknowledgement | 11 days - Q2 support deck [Fact] | | | | |
```

Four columns empty on purpose. **Gate:** read back to two panel cardholders;
"unprotected" was too soft, her word was *robbed twice*. Passed.

## Phase 2 - Requirements and Validation

```markdown
### Starting Phase 2: Requirements and Validation
**Carrying forward**: PROBLEM_STATEMENT.md - "robbed twice", so certainty not
speed; MEASUREMENT.md - contact rate 0.14, repeat contacts 3.1 [ASSUMPTION]
**Sub-skills**: lean-ux-canvas -> LEAN_UX_CANVAS.md; opportunity-solution-tree -> OPPORTUNITY_TREE.md;
pol-probe-advisor -> POL_PROBES.md; user-story -> USER_STORY_MAP.md; write-spec -> SPEC.md
**Measurement thread advances to**: target, plus the guardrail
**Not yet resolved, and not resolved here**: Bacen clock; repeat-contacts instrument
```

`[runs lean-ux-canvas -> LEAN_UX_CANVAS.md]` Box 7's first answer was findability;
the real one: **does visible status deflect calls, or add a channel people check
before calling anyway?** The tree set the root outcome, repeat contacts 3.1 -> 1.5.
`[runs pol-probe-advisor -> POL_PROBES.md]` Kill criterion before method: *above
2.2 inbound contacts in the 14 days after submission, over at least 120 treated
disputes, we do not build the status read model.* `DEFINED - NOT YET RUN`, unowned.
`[runs write-spec -> SPEC.md]` Loudest non-goal: **no evidence upload in v1.**
Target against the Phase 1 baseline - contact rate 0.14 -> 0.10; guardrail, dispute
approval rate within 3 points of 71%.

### The gate does not pass

```markdown
### Phase 2 gate NOT passed - 2026-07-24

**Gate question**: Is scope agreed, and does the riskiest assumption have an owned
probe?
**Answer**: no
**Stated reason**: Rafael Nunes - "Scope is fine. The probe is written down and
nobody has said they will run it. Ops is the only team that can reach 120 people."

**Smallest thing that would change the answer**
- Tereza Villar reads POL_PROBES.md, accepts the probe with a start date or says
  why not. Half an hour, not a rewrite.

**Paths**
1. Fix the ownership gap and re-gate (Recommended)
2. Proceed with the gap recorded as a labelled risk, carried into
   STRATEGY_SESSION.md
3. Stop here and hand off what exists
```

**User:** 2. Tereza is on leave until the 29th and Helena wants the PRD at
Thursday's steering group.

**Agent:** Then it is a decision, not a detail, and it is logged as one.

| Decision | Owner | Date | Risk carried |
|---|---|---|---|
| PRD written before the riskiest assumption has an owned probe | Rafael Nunes | 2026-07-24 | v1 may be scoped on an untested deflection belief |

The row is appended to `INDEX.md`, never overwritten; `POL_PROBES.md` keeps
`DEFINED - NOT YET RUN, UNOWNED`, and Phases 3, 4 and 5 all have to carry it.

## Phase 3 - PRD

```markdown
### Starting Phase 3: PRD
**Carrying forward**: SPEC.md - P0 set, non-goals, the 0.14 -> 0.10 target; the
2026-07-24 gate record - a probe that is unowned and unrun
**Sub-skills**: prd-development -> PRD.md
**Measurement thread advances to**: instrument - what actually produces each number
**Not yet resolved, and not resolved here**: Bacen clock start point, ADR Proposed
```

`[runs prd-development -> PRD.md]` Technical Architecture names the system of
record - **the queue stays authoritative; the app is a read model** - and Bacen
ships as an **ADR marked Proposed, not Accepted**, owned by Compliance. The failed
gate shows here too: Success Metrics opens by saying the deflection assumption
behind the target has a probe that is defined, unrun and unowned. Instruments -
telephony dashboard for contact rate, back-office acknowledgement timestamp for the
11 days, and for repeat contacts **nothing exists**, so a new `dispute_status_view`
event joined to tickets becomes DE-8 work.

**Gate:** PRD reviewed by Beatriz Amaral and Marcos Pinho, open ADR left open. Passed.

## Phase 4 - Delivery Planning

```markdown
### Starting Phase 4: Delivery Planning
**Carrying forward**: PRD.md - a read model over the queue, DE-8 owning the missing
instrument; MEASUREMENT.md - instruments named, read-out still blank
**Sub-skills**: epic-hypothesis -> EPIC_HYPOTHESES.md; prioritization-advisor -> PRIORITIZATION.md;
epic-breakdown-advisor -> EPIC_BREAKDOWN.md + board_import.csv; roadmap-planning -> ROADMAP.md
**Measurement thread advances to**: read-out date and owner; MEASUREMENT.md closes
**Not yet resolved, and not resolved here**: Bacen clock start point
```

`[runs epic-hypothesis -> EPIC_HYPOTHESES.md]` DE-EPIC-2: confirm at contact rate 0.115 over six weeks, falsify above 0.135.
`[runs epic-breakdown-advisor -> EPIC_BREAKDOWN.md + board_import.csv]` One epic
failed INVEST on *Valuable*; the Genesys webhook unknown became spike DE-7.
`[runs roadmap-planning -> ROADMAP.md]` Now / Next / Later, skeleton first,
capacity gate **OPEN** because nobody sized the thin skeleton.

**The Phase 2 gate is re-run here.** Tereza came back on the 29th, read
`POL_PROBES.md` and took the probe with a start date. A second row is appended.

| Phase | Gate question | Result | Date | Confirmed by | Reason if failed |
|---|---|---|---|---|---|
| 2 | Scope agreed, riskiest assumption owned? | failed | 2026-07-24 | Rafael Nunes | Probe defined, unowned |
| 2 | Scope agreed, riskiest assumption owned? | passed | 2026-07-29 | Tereza Villar | - |

Path 2 was legitimate and not free: the PRD keeps its caveat. The board default was reversed here, so the agent showed all 28 cards and waited.

**Measurement thread, closed:**

```markdown
| Metric | Baseline (+ source) | Target | Instrument | Read-out | Owner |
|---|---|---|---|---|---|
| Contact rate per active card | 0.14 - telephony dashboard [Fact] | 0.10 | Telephony dashboard, weekly, dispute reason codes | 2026-11-30 | Rafael Nunes |
| Repeat contacts per dispute | 3.1 - 40-ticket sample [ASSUMPTION] | 1.5 | New `dispute_status_view` event joined to tickets, built in DE-8 | 2026-12-15 | Tereza Villar |
| Median acknowledgement | 11 days - Q2 support deck [Fact] | 3 days | Back-office acknowledgement timestamp | 2026-11-30 | Beatriz Amaral |

## Guardrail metrics
| Guardrail | Baseline (+ source) | Must stay | Instrument | Owner |
|---|---|---|---|---|
| Dispute approval rate | 71% - ops report [Fact] | within 3 pts | Ops report | Tereza Villar |
```

**Gate:** credible to engineering? Beatriz said yes for the skeleton, no for DE-8 until DE-7 lands. Passed, capacity gate OPEN.

## Phase 5 - Strategy

```markdown
### Starting Phase 5: Strategy
**Carrying forward**: the whole artifact set, one failed gate, one open ADR
**Sub-skills**: product-strategy-session (closing-session) -> STRATEGY_SESSION.md
**Measurement thread advances to**: nothing - it closed in Phase 4; this phase argues with it
**Not yet resolved, and not resolved here**: Bacen clock leaves owned and dated, not answered
```

`[runs product-strategy-session -> STRATEGY_SESSION.md]` The coherence check found
the thing that mattered: the roadmap optimises for **submission speed**, the problem
statement is about **liability anxiety**. A fast form that says nothing for eleven
days solves the wrong half, so status visibility moved ahead of submission polish.
The premortem's top risk is what Phase 2's failure predicted - *she read the status
and called anyway* - now owned, probed and dated.

## Closing readout (excerpt)

```markdown
## How we will know it worked
Contact rate per active card, 0.14 today [telephony dashboard, Jun 2026], target
0.10, read out 2026-11-30 by Rafael Nunes. Guardrail: approval rate within 3 pts.

## Riskiest assumption
That visible status reduces calls rather than adding a channel people check first.
Probe: 120 treated disputes, kill above 2.2 contacts in 14 days.
Status: OWNED (Tereza Villar), NOT YET RUN.

## Gates not passed
| Phase | Reason | Risk carried |
|---|---|---|
| 2 | Riskiest assumption had a probe but no owner | PRD written and reviewed on an untested belief; the caveat stands in Success Metrics |
```

## What this example is meant to teach

1. **A gate that fails is the gate working.** Phase 2 caught an unowned probe that
   no structural check would have; the failure is recorded, the retry appended.
2. **A failed gate has a price, and the price stays visible.** The PRD carries a
   caveat, the roadmap a risk, the premortem the same assumption. Not free.
3. **The thread fills one column per phase** - baseline in 1, target and guardrail
   in 2, instrument in 3, date and owner in 4; Phase 3 found one metric with none.
   And placeholders beat plausible inventions: Camila's income stayed empty, the
   3.1 baseline stayed `[ASSUMPTION]`, the Bacen ADR shipped as Proposed.

## Provenance

Original example, MIT, Bruno Lima Soares. Aurora Bank, Disputa Express, and
Cardholder Camila are fictional; all figures are invented.
