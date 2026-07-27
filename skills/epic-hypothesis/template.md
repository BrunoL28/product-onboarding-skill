# Epic Hypothesis - Output Templates

Two schemas. The **Epic Hypothesis card** is the artifact a team pastes into an
epic description in Jira, ADO, or Linear before the epic is prioritised or split.
The **read-out** is what gets written against that card when the window closes,
so the bet and its result live in the same place. Both exist to make one thing
legible to someone who was not in the room: the result that would have made this
team stop.

## Template stability

These section names are a contract, not styling. Cards are pasted into trackers
and diffed at the end of the quarter against what actually happened, so a renamed
section silently breaks someone's saved filter and someone else's comparison.

The signal table's column order - **Measure, Baseline, Source, Confirm, Falsify,
Window** - is part of that contract. So is the presence of a Falsify column even
when the team has not filled it in; an empty cell is honest and a deleted column
hides the omission.

Change a section only as a **labelled new version** (`Epic Hypothesis card v2`)
carrying a migration note that says what moved where and what old readers should
do. Improve the facilitation freely. Never silently rename.

---

## 1. Epic Hypothesis card

Emit the banner only when the `provisional` parameter is on - that is, when the
kill threshold has no named owner.

```markdown
> **PROVISIONAL.** The falsifying signal has no named decision owner. Until one
> is named, this is a forecast, not a bet. See Assumptions to Validate.

## Epic Hypothesis: <EPIC-ID> <short name>

- **Date**: <YYYY-MM-DD>
- **Team**: <who was in the room>
- **Upstream**: <artifacts drawn from, or none>
- **Status**: committed / provisional

### Epic as a user story

- **As a** <persona - the same one the persona artifact names>
- **I want to** <action>
- **so that** <outcome the persona actually wants>

### The claim, in both grammars

- **If/Then**: If we <action> for <target user>, then they will <outcome>.
- **Gothelf**: We believe that <this capability> for <these people> will achieve
  <this outcome>. We will know we are right when we see <signal>.
- **Difference between the two**: <none, or the confusion the gap exposed>

### Signals

Column order is a hard contract. One quantitative and one qualitative by default;
the guardrail row is always present.

| Signal | Measure | Baseline | Source | Confirm | Falsify | Window |
|---|---|---|---|---|---|---|
| Quantitative | <behaviour, not adoption> | <value> [Fact/Inference/Assumption] | <query or report> | <threshold> | <threshold> | <n weeks> |
| Qualitative | <behaviour reported> | <value or none> [label] | <method, n> | <n of m> | <n of m> | <n weeks> |
| Guardrail | <what must not degrade> | <value> [label] | <source> | stays within <band> | breaches <band> | <n weeks> |

- **Window derived from**: <the journey step and its real duration - never the
  sprint calendar>
- **Inconclusive band**: <between X and Y> - <policy, per `inconclusive_policy`>
- **Behaviour, not adoption**: <what this measure would do if we shipped and
  nothing about the user's behaviour changed>
- **Non-obviousness**: <who would confidently have predicted the opposite, and why>

### Decision rule

Pre-committed <YYYY-MM-DD>, before any data.

- **If the confirming signal fires**: <expand / scale / next slice>
- **If the falsifying signal fires**: <stop / pivot / reduce to X>
- **If we land in the band**: <extend once by N, then treat as a fail>
- **Who can act on the falsifying branch**: <name and role, or OPEN - and OPEN
  means this card is provisional>

### Validation method

- **Rung on the ladder**: <existing data query | one question on an existing
  channel | five interviews | concierge | fake door | prototype test |
  instrumented thin slice>
- **Cheaper rungs ruled out**: <one line per rung skipped, saying which signal it
  could not produce>
- **What it costs**: <effort, in the same units used for the epic>
- **Instrumentation required**: <events that do not exist yet, or none - if any,
  that work is part of the epic>
- **Read-out date**: <YYYY-MM-DD>

### Assumptions to Validate

- <baseline tagged Assumption, and the exact query that would settle it>
- <kill-decision owner not yet named, and who would have to agree>
- <signal that needs instrumentation nobody emits today>
- <anything the team asserted that no source supports>
```

---

## 2. Window read-out

Written at the read-out date, appended to the same card. Never edit the original
thresholds; the diff is the point.

```markdown
## Read-out: <EPIC-ID> - <YYYY-MM-DD>

| Signal | Threshold set | Observed | Fired? |
|---|---|---|---|
| Quantitative | <confirm> / <falsify> | <value> | confirm / falsify / band |
| Qualitative | <confirm> / <falsify> | <value> | confirm / falsify / band |
| Guardrail | <band> | <value> | held / breached |

- **Rule applied**: <the pre-committed branch, quoted from the card>
- **Decision taken**: <what actually happened>
- **Decided by**: <name and role>
- **If the rule was not followed, why**: <the honest reason, or "n/a">
- **What we learned that was not on the card**: <one to three lines>
```

---

## Rules that travel with these schemas

- Every number carries **Fact**, **Inference**, or **Assumption**. A baseline with
  no label is a guess wearing a suit.
- Confirm and falsify thresholds must not touch. If they do, every result reads
  as a win and the card is decoration.
- Leave `Estimate`, dates, and owners blank rather than inventing them. A blank
  is a question; an invented value is a lie with a deadline.

---

## Provenance

Adapted from `prompts/backlog-epic-hypothesis.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Hypothesis format: Jeff Gothelf, *Lean UX*
(O'Reilly). Falsifiability framing after Karl Popper by way of lean startup
practice. Feeds `epic-breakdown-advisor` and `prioritization-advisor`.
