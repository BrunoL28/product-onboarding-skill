# TAM SAM SOM - Worked Example

> **READ THIS FIRST. EVERY NUMBER IN THIS FILE IS INVENTED.**
> Aurora Bank is a fictional company. There is no Bacen table behind `U_cards`,
> no survey behind `r_dispute`, and no contact-centre study behind
> `p_cost_contact`. Every source cell below says `[ILLUSTRATIVE]` because no
> source exists. Nothing here may be quoted, pasted into a deck, or cited as a
> market figure. What is real is the **shape**: named variables, two independent
> passes, a printed reconciliation ratio, a swing variable, and a band.

Sizing for Aurora Bank's *Disputa Express*. The interesting moves: refusing to
size revenue for something nobody buys, and finding that a R$ 330-600M "market" is
worth about R$ 1M a year to Aurora.

## Intake

**User:** How big is the market for Disputa Express?

**Agent:**

> Before the boundary question, one correction to the frame. Disputa Express is an
> in-app dispute journey for existing cardholders - nobody buys it separately, so
> a revenue TAM would be fiction. I am switching to **`value_pool_mode`**: I will
> size the money currently spent handling card disputes, and the title will say so.
>
> **[Question 1 of 3]** Boundary. This sets the universe count, which drives
> everything downstream, so I will not default it.
>
> 1. **Brazil, all card issuers** - widest defensible pool, what an exec asks for.
> 2. **Brazil, all issuers, Aurora's own pool broken out** - same TAM, plus the
>    only number that is actually yours to capture.
> 3. **Brazil, digital-first issuers only** - narrower, smaller headline.
> 4. Other.
>
> Defaults for the rest unless you say otherwise: SOM horizon **3 years**,
> currency **BRL** with no conversion, pricing anchor **benchmarked**.

**User:** 2.

**Agent:**

> ```
> Search plan:
> - Looking for: active card count Brazil, disputes per card per year, loaded
>   cost per contact, back-office cost per case, issuers publishing deflection
> - Source classes: central bank and regulator statistics, issuer filings,
>   card-scheme summaries, trade bodies
> - Fact vs read: published counts Fact with URL and date; derived rates
>   Inference; unsourceable inputs [ASSUMPTION] with a method and a wide range
> ```
>
> Continuing unless you revise it.

**User:** Go.

**Agent:** Two things came back badly, and they change the grade.

> `r_dispute` - disputes per active card per year - is not published anywhere I
> could open. Tagged `[ASSUMPTION]` with a 4x range; it ends up as the swing
> variable, so it is what your next research should attack.
>
> And no issuer could be named that has published a dispute-deflection result. SOM
> therefore carries the widest band, and I am not inventing a comparable.

## Output

```markdown
# Value Pool Sizing: Disputa Express - Brazil, annual
# [ILLUSTRATIVE MODEL - EVERY FIGURE INVENTED - DO NOT CITE]

## 0. Headline

- **TAM (value pool)**: R$ 330M to R$ 600M per year - grade **C**
- **SAM (digital-first issuers)**: R$ 100M to R$ 180M per year
- **SOM (3-year, Aurora only)**: R$ 0.8M to R$ 1.7M per year
- **Reconciliation**: bottom-up : top-down = 1.8x
- **Swing variable**: `r_dispute`
- **Rounding**: 2 significant figures, set by `r_dispute` [ASSUMPTION]

## 1. Boundary

| Field | Value |
|---|---|
| Product sized | In-app card dispute journey - NOT sold separately |
| Buyer | Card issuers bearing the handling cost; Aurora broken out |
| Geography | Brazil |
| Period | Annual |
| Currency | BRL, no conversion performed (any FX needs rate + date) |
| Mode | `value_pool_mode` - cost avoided, not revenue |

- **Pool definition**: contact-centre cost plus back-office case handling
- **Whose money**: the issuer's operating budget
- **Not revenue**: this pool is cost avoided; it never becomes income

## 2. Variable register

| Name | Meaning | Value | Unit | Low | High | Source or [ASSUMPTION] | Label |
|---|---|---|---|---|---|---|---|
| `U_cards` | Active cards, Brazil | 200M | cards | 150M | 250M | [ILLUSTRATIVE] - stands in for a regulator table | [Fact] |
| `r_dispute` | Disputes per card per year | 0.020 | rate | 0.010 | 0.040 | [ASSUMPTION] - unpublished; ranged 4x | [Assumption] |
| `f_contacts` | Contacts per dispute | 3.1 | count | 2.0 | 4.5 | [ILLUSTRATIVE] - stands in for Aurora call logs | [Fact] |
| `p_cost_contact` | Fully loaded cost per contact | 14 | BRL | 9 | 22 | [ILLUSTRATIVE] - stands in for a cost study | [Inference] |
| `p_case_handling` | Back-office cost per dispute | 40 | BRL | 25 | 70 | [ASSUMPTION] - from headcount over volume | [Assumption] |
| `r_cards_share` | Card queries share of servicing opex | 0.25 | rate | 0.15 | 0.35 | [ASSUMPTION] - stated method: queue mix | [Assumption] |
| `r_dispute_share` | Dispute share of card contact | 0.20 | rate | 0.10 | 0.30 | [ASSUMPTION] - softest link in the chain | [Assumption] |
| `r_digital` | Digital-first issuer share of pool | 0.30 | rate | 0.20 | 0.40 | [ASSUMPTION] - by card base | [Assumption] |
| `U_aurora_disputes` | Aurora disputes per year | 50,400 | count | 45,000 | 56,000 | [ILLUSTRATIVE] - 4,200/month | [Fact] |
| `c_som_yr3` | Deflection Aurora could hold by yr 3 | 0.30 | rate | 0.20 | 0.40 | [ASSUMPTION] - no comparable nameable | [Assumption] |

Every [ASSUMPTION] row carries a wide range, and that width propagates.

## 3. Top-down pass

| Step | Variable | Operation | Running total |
|---|---|---|---|
| Retail servicing opex, Brazil banks | published total | - | R$ 12bn |
| Filter 1 | `r_cards_share` | x 0.25 | R$ 3.0bn |
| Filter 2 | `r_dispute_share` | x 0.20 | R$ 600M |

- **Top-down result**: R$ 600M (R$ 180M to R$ 1.3bn)
- **Weakest link**: `r_dispute_share` - an [ASSUMPTION] applied to an
  [ILLUSTRATIVE] published total, so the chain is only as good as its softest link

## 4. Bottom-up pass

- **Arithmetic**: `U_cards x r_dispute x ((f_contacts x p_cost_contact) +
  p_case_handling)` = 200M x 0.020 x ((3.1 x 14) + 40) = 4.0M disputes x R$ 83
- **Bottom-up result**: R$ 330M (R$ 65M to R$ 1.7bn)
- **Prices reused from another segment**: none

## 5. Reconciliation

- **Ratio**: bottom-up : top-down = 330 : 600 = **1.8x**
- **Read**: 1.5x to 3x - one input is soft
- **Soft input named**: `r_dispute_share`
- **Action taken**: report a band spanning both models, R$ 330M to R$ 600M.
  The two were **not averaged**; the gap is the finding

## 6. SOM against named comparables

| Comparable | What they captured | Over | Source | Read-across |
|---|---|---|---|---|
| none nameable | - | - | - | no issuer found publishing a deflection result |

- **No comparable could be named**, so SOM carries the widest band in the model
- **Second bound, and the important one**: SOM is capped by Aurora's own pool,
  not by market share. `U_aurora_disputes x R$ 83 x c_som_yr3` = 50,400 x 83 x
  (0.20 to 0.40) = **R$ 0.8M to R$ 1.7M per year**
- A 0.3% share of a R$ 600M pool is not the prize here. The prize is R$ 1M of
  avoided cost, and the retention effect this model does not size at all

## 7. Sensitivity and grade

| Case | Assumptions used | TAM |
|---|---|---|
| Worst | all variables at low | R$ 65M |
| Base | central values | R$ 330M |
| Best | all variables at high | R$ 1.7bn |

- **Swing variable**: `r_dispute` - its 4x range moves the total more than any
  other input, twice as much as `p_cost_contact`
- **Grade**: **C** - models within 3x, but key inputs are [ASSUMPTION]

## 8. Assumptions to Validate

- **SWING: `r_dispute`** - buy or request the regulator's dispute volume series,
  or derive it from three issuers' annual reports - owner: strategy analyst
- `r_dispute_share` [ASSUMPTION] - the softest link in the top-down chain; a
  queue-mix sample from Aurora's own contact centre would replace it - owner: CX
- `p_case_handling` [ASSUMPTION] - finance can source this exactly for Aurora,
  which also tightens the SOM - owner: finance business partner
- No comparable deflection result exists publicly - if none can be found, SOM
  stays a range and should never be quoted as a point - owner: PM
- Double-count risk: Aurora's own disputes sit inside the SAM figure as well as
  in the SOM bound. Do not add them - owner: PM
```

## What this example is meant to teach

1. **The frame got corrected before the arithmetic.** Nobody buys Disputa
   Express, so a revenue TAM would have been fiction with a currency symbol.
2. **One question, and it was the boundary.** Everything else was defaulted out
   loud - horizon, currency, pricing anchor - and the run continued unattended.
3. **The unsourceable input was labelled, not smoothed.** `r_dispute` became an
   [ASSUMPTION] with a 4x range, dropped the grade to C, and became the swing.
4. **1.8x was printed, not averaged.** Averaging to "R$ 465M" would have deleted
   the only genuinely informative result in the model.
5. **No comparable meant no comparable.** Inventing one issuer's deflection number
   would have tightened SOM and made the artifact worse.
6. **The big number was not the useful one.** R$ 330-600M is the pool, R$ 0.8-1.7M
   is Aurora's. Reporting only the first is how a sizing misleads.

## Provenance

Example built on the schema in `market-intelligence/tam-sam-som-analysis-prompt.md`
and `loops/market-sizing-loop.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Bottom-up discipline after Bill Aulet,
*Disciplined Entrepreneurship*. Aurora Bank is fictional and **every figure,
source, and citation in this file is invented and must not be quoted.**
