# Proof of Life Probe Advisor - Output Templates

Six schemas that make one probe auditable: the assumption record, the kill
criterion, the candidate comparison, the probe definition, the run plan, and the
result record - so a later reader can tell real learning from mere activity.

## Template stability contract

These schemas are contracts, not styling. Probes get audited, re-run, and pasted
into decision logs, so a renamed section breaks somebody's trail. Change a section
only as a **labelled new version** (`v2`) with a migration note saying what moved
and why - never silently. Two contracts outrank convenience:

1. **The kill criterion appears above the probe method** in every artifact. Order
   on the page enforces order in time.
2. **The result record keeps the pre-registered threshold beside the observed
   number** - both columns, always, so nobody can quietly move the goalposts.

**Evidence labels:** **[Fact]** sourced, **[Inference]** evidence-based reading,
**[Assumption]** working guess. One assumption per artifact; a second one belongs
in Assumptions to Validate.

## 1. Assumption record

```markdown
## Assumption Under Test

- **Assumption**: <one statement, phrased so it could be false>
- **Source**: <Lean UX Canvas Box 7 / OST leaf / interview / stakeholder claim>
- **Risk type**: value / usability / feasibility / viability
- **If false, we waste**: <the build, the quarter, the headcount - be specific>
- **Decision this feeds**: <the build / no-build call it informs>
- **Decision date**: <YYYY-MM-DD>  **Decision owner**: <named human, not a team>
- **Current evidence**: <what is known now> [Fact / Inference / Assumption]
```

## 2. Kill criterion - written before any probe is named

```markdown
## Kill Criterion (pre-registered <YYYY-MM-DD> by <names>)

- **Signal**: <the one observable thing measured>
- **Baseline**: <our own current number, and where it came from> [Fact / Assumption]
- **Threshold**: <the number or comparison separating go from stop>
- **Why this threshold**: <the business fact making this the line, not a benchmark>
- **Sample floor**: <n below which the run is inconclusive>
- **Timebox**: <days or weeks, and the stop date>
- **Alternative if killed**: <what the team does instead>

> If <signal> is <worse than threshold> over <floor> observations in <timebox>,
> we do not build <thing>; we do <alternative> instead.
```

## 3. Candidate comparison

```markdown
## Candidate Probes

| # | Probe | What it could prove | Evidence rung | Cost | Time | Signature false positive | Blast radius |
|---|---|---|---|---|---|---|---|
| 1 | <type> | <the kill signal it can return> | money / behaviour in context / behaviour in a lab / stated intent | <low / med / high, plus the real unit> | <days or weeks> | <the one that would fool us> | <who sees it> |
| 2 | <type> | | | | | | |
| 3 | <type> | | | | | | |

**Disqualified**: candidate <n> - <the reason it cannot return the kill signal>.
**Recommendation**: candidate <n> - cheapest probe that could still fail.

> Which probe do you want to run - 1, 2, 3, or a combination?
```

## 4. Probe definition

```markdown
## Probe: <name>

- **Type**: fake door / painted door / landing page / concierge / Wizard of Oz /
  prototype test / interview / data archaeology / pre-sale or LOI
- **Kill criterion**: <restated verbatim from section 2 - never re-derived>
- **Evidence rung**: <ladder position, plus a reason if below behaviour in context>
- **Timebox**: <start date to stop date>
- **Cost**: <money, people-days, and engineering days - all three>
- **Engineering budget**: <none / minimal, and what exactly gets built>

### What each result means, agreed in advance

| Result | Observed condition | What we do |
|---|---|---|
| Pass | <at or better than threshold, n at or above floor> | <next action> |
| Kill | <worse than threshold, n at or above floor> | <the alternative> |
| Inconclusive | <n below floor, or the run broke> | <extend / redesign / drop> |

### Signature false positive
- **The trap**: <the way this probe type flatters itself>
- **The guard**: <the design choice that blunts it>

### Blast radius
- **Who sees it**: <cohort, and whether they are in a vulnerable moment>
- **Real path out**: <the existing channel that stays visible throughout>
- **What is fabricated**: <mechanism only - never a state, decision, or commitment>
- **Regulatory exposure**: <rule, reviewer, date - or OPEN, which blocks the run>
```

Inconclusive is a first-class outcome. A run below the sample floor is not a pass.

## 5. Run plan

```markdown
## Run Plan

- **Window**: <YYYY-MM-DD> to <YYYY-MM-DD>, readout <YYYY-MM-DD>
- **Owner / who makes the call**: <named human> / <named human>
- **Cohort and selection**: <who, how many, method, holdout if any>
- **Instrumentation**: <the event or count, and where it is read from>
- **Stop-early conditions**: <complaint volume, regulatory flag, obvious harm>
- **What we are NOT measuring**: <so nobody mines the run for a second answer>
```

## 6. Result record - stays empty until the probe has run

```markdown
## Result Record

**Status**: NOT YET RUN / RUNNING / COMPLETE (as of <YYYY-MM-DD>)

| Field | Pre-registered | Observed |
|---|---|---|
| Signal | <signal> | <value, or blank> |
| Threshold | <threshold> | - |
| Sample | floor <n> | <actual n, or blank> |
| Window | <timebox> | <actual dates, or blank> |

- **Verdict**: pass / kill / inconclusive
- **Decision taken**: <what the humans decided, and who>
- **False positive check**: <was the signature trap plausibly in play?>
- **What this probe still cannot prove**: <carried into Assumptions to Validate>
```

An artifact carrying invented results looks like evidence. It is not.

## 7. Assumptions to Validate

```markdown
## Assumptions to Validate

- <Runner-up assumption from Box 7 or the OST leaf> - <who probes it, when>
- <Something the chosen probe explicitly cannot prove> - <how it gets covered>
- <Any input labelled Assumption above> - <who confirms it>
```

---

## Provenance

Original work, MIT, copyright Bruno Lima Soares. The **Proof of Life probe**
framing is Dean Peters'; these schemas are an independent implementation of that
idea, not adapted from any file in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts).
Methods credited to their sources: Eric Ries, *The Lean Startup* (concierge,
Wizard of Oz, smoke test); Teresa Torres, *Continuous Discovery Habits*
(assumption tests); Google Ventures, *Sprint*; fake-door and painted-door patterns.
