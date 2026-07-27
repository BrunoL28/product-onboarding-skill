# TAM SAM SOM Calculator - Output Template

One canonical schema for a two-method market sizing, plus two add-ons: the
per-segment format for `segments` above 1, and the `value_pool_mode` variant for
when the thing sized is not sold separately. It makes the model re-runnable by a
stranger - named variables, a source against each, both passes, the gap printed.

## Template stability contract

Section names and numbering are a contract, not styling. These models get re-run
and diffed quarter over quarter, so a renamed section silently breaks the diff.
Change one only as a **labelled new version** (`v2`) with a migration note saying
what moved, what it was called before, and why. Never reorder.

## The source rule

Every variable row carries **either a named source with a URL and a date, or the
literal tag `[ASSUMPTION]`** plus the estimation method behind it. There is no
third state; a blank source cell is a defect. No total appears without a band.

**Evidence labels:** **[Fact]** published and opened, **[Inference]** derived from
Facts by stated arithmetic, **[Assumption]** working guess with a method.

**Sticky-Note Rule:** summary bullets are 4-8 words, ASCII only, no emoji;
arithmetic lives in the model sections, never in the bullets.

---

## Main schema

```markdown
# Market Sizing: <product> - <geography>, <period>

## 0. Headline

- **TAM**: <low> to <high> <currency> per <period> - <grade A/B/C/D>
- **SAM**: <low> to <high> <currency> per <period>
- **SOM (<n>-year)**: <low> to <high> <currency> per <period>
- **Reconciliation**: bottom-up : top-down = <ratio>x
- **Swing variable**: <variable name>
- **Rounding**: <n> significant figures, set by <weakest input>

## 1. Boundary

| Field | Value |
|---|---|
| Product sized | <what, and whether it is sold separately> |
| Buyer | <who pays; secondary audience if one exists> |
| Geography | <market boundary> |
| Period | <annual / other> |
| Currency | <code; FX rate and date if any conversion was done> |
| Mode | revenue sizing / `value_pool_mode` |

## 2. Variable register

| Name | Meaning | Value | Unit | Low | High | Source (URL + date) or [ASSUMPTION] | Label |
|---|---|---|---|---|---|---|---|
| `U_<x>` | <universe count> | | | | | <URL, accessed YYYY-MM-DD> | [Fact] |
| `r_<x>` | <rate or share 0-1> | | | | | <derived from U_a / U_b> | [Inference] |
| `f_<x>` | <frequency per period> | | | | | [ASSUMPTION] - <method> | [Assumption] |
| `p_<x>` | <price or unit value> | | | | | <URL, accessed YYYY-MM-DD> | [Fact] |
| `c_<x>` | <capture rate> | | | | | [ASSUMPTION] - <method> | [Assumption] |

<Every [ASSUMPTION] row takes a deliberately wide range, which propagates.>

## 3. Top-down pass

Start from a published total for the boundary, then apply named filters.

| Step | Variable | Operation | Running total |
|---|---|---|---|
| Published total | `<name>` | - | <value> |
| Filter 1 | `r_<x>` | x <value> | <value> |
| Filter 2 | `r_<y>` | x <value> | <value> |

- **Top-down result**: <value> <currency> (<low> to <high>)
- **Weakest link in the chain**: <which filter, and why>

## 4. Bottom-up pass

- **Arithmetic**: `U_<x> x r_<x> x f_<x> x p_<x>` = <one line a reader can redo>
- **Bottom-up result**: <value> <currency> (<low> to <high>)
- **Prices and rates reused from another segment**: none / <named, with reason>

## 5. Reconciliation

- **Ratio**: bottom-up : top-down = <number>x
- **Read**: within 1.5x agree / 1.5-3x one input is soft / above 3x boundary
  mismatch, report divergence and no base case
- **Soft input named**: <variable>
- **Action taken**: <band spanning both models / widened / stopped>

<Never average the two models. The gap is the finding.>

## 6. SOM against named comparables

| Comparable | What they captured | Over | Source | Read-across |
|---|---|---|---|---|
| <named company> | <share or revenue> | <years> | <URL + date> | <why it applies> |

- **`c_som_yr<n>`**: <rate> (<low> to <high>)
- **SOM**: <low> to <high> <currency>
- **If no comparable could be named**: say so, and SOM carries the widest band.

## 7. Sensitivity and grade

| Case | Assumptions used | TAM |
|---|---|---|
| Worst | <all variables at low> | <value> |
| Base | <central values> | <value> |
| Best | <all variables at high> | <value> |

- **Swing variable**: <name> - moves the total by <x> across its range
- **Grade**: <A/B/C/D> - <the condition that produced it>

## 8. Assumptions to Validate

- **SWING: `<variable>`** - <research that would narrow it> - owner: <name>
- `<variable>` [ASSUMPTION] - <how to source it> - owner: <name>
- <boundary or double-counting risk> - owner: <name>
```

---

## Per-segment add-on (`segments` above 1)

Size one segment per turn, gate each, then roll up. Repeat sections 2 to 5 per
segment under `## Segment <n>: <name>`, then add:

```markdown
## Roll-up

| Segment | TAM low | TAM high | Ratio | Grade | Buyers shared with |
|---|---|---|---|---|---|
| <name> | | | | | <segments risking double-count> |

- **Overlap treatment**: <how shared buyers were removed, and from which segment>
- **Rolled band**: <sum of lows> to <sum of highs> - never a sum of point estimates
```

## `value_pool_mode` add-on

When the thing is not sold separately the title reads **Value Pool Sizing**,
section 1 says so, and revenue is replaced by money spent on the problem today:

```markdown
- **Pool definition**: <cost lines counted: labour, contact, write-off, penalty>
- **Whose money**: <the party currently bearing it>
- **Not revenue**: <one line stating this pool is cost avoided, not income>
```

---

## Provenance

Adapted from `market-intelligence/tam-sam-som-analysis-prompt.md` and
`loops/market-sizing-loop.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. TAM/SAM/SOM as practised in venture and product
strategy; bottom-up discipline after Bill Aulet, *Disciplined Entrepreneurship*.
