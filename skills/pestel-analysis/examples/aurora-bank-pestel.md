# PESTEL Analysis - Worked Example

PESTEL for Aurora Bank's *Disputa Express*. Fictional product, invented figures
and sources — the point is the shape and the honesty discipline.

---

## Intake

**User:** Do a PESTEL for our in-app card dispute product.

**Agent:**

> One question, because it changes half the analysis.
>
> **Geographic scope.** Legal and Political depend almost entirely on
> jurisdiction, and card disputes are one of the most heavily rule-bound journeys
> in banking. I will not guess this one.
>
> 1. **Brazil only** - one regulator, one card-scheme relationship, tightest
>    analysis.
> 2. **Brazil now, LatAm within the horizon** - I would flag where Mexican and
>    Colombian rules diverge, so v1 does not hard-code Brazilian assumptions.
> 3. **Brazil plus a card-scheme lens** - domestic rules alongside Visa and
>    Mastercard global dispute rules, which bind regardless of country.
> 4. Other.
>
> Horizon defaults to 18 months and purpose to strategic planning unless you say
> otherwise.

**User:** 3.

**Agent:**

> Brazil plus scheme rules. That means the Legal section carries the most weight,
> and scheme timelines may bind harder than local ones.
>
> **Search plan**
> - Looking for: Bacen dispute-handling and consumer-protection rules, scheme
>   chargeback timeframes, Brazilian card fraud volume data, digital banking
>   adoption and trust surveys.
> - Source classes: Bacen publications, scheme rulebooks and public summaries,
>   Febraban and industry reports, IBGE, credible fintech press.
> - Fact vs read: rules and published data marked Fact with URL; product
>   implications marked Inference; anything regulatory I am unsure of goes to
>   legal as an open question rather than being asserted.
>
> Continuing.

---

## Output (excerpt)

```markdown
# PESTEL Analysis: Disputa Express

## Overview

- **Project/Product Name**: Disputa Express - in-app card fraud dispute flow
- **Analysis Purpose**: Strategic planning
- **Geographic Scope**: Brazil, plus Visa and Mastercard scheme rules
- **Time Horizon**: 18 months
- **Analyst**: Product, Cards squad
- **Date**: 2026-07-26

## 2. Economic Factors

- **Consumer Spending**: Card spend growing, disputes track volume [Fact - source]
  - Impact: dispute volume grows with card growth, so a manual queue gets worse
    on its own even with no change in fraud rate.
  - Threat: cost per dispute is the constraint, not fraud rate. Implication:
    measure success in contact rate per active card, not disputes closed.
- **Cost of Capital**: Higher rates tighten provisioning [Fact - source]
  - Impact: money held during a dispute has a real carrying cost.
  - Opportunity: faster provisional credit is now a finance argument, not only a
    CX one. Implication: bring finance into the v1 conversation.

## 3. Social Factors

- **Consumer Attitudes**: Trust collapses after unresolved fraud [Fact - survey]
  - Impact: the dispute journey is a retention surface, not a support cost centre.
  - Threat: a fast form with a silent aftermath makes it worse, because it raises
    an expectation it then fails to meet. Implication: status visibility must
    ship with submission, not after it.

## 6. Legal Factors

- **Compliance Requirements**: Regulated acknowledgement timelines apply
    [Fact - Bacen resolution, URL]
  - Impact: acknowledgement speed is a compliance surface, not a service target.
  - Threat: the clock's start point (customer submission or bank
    acknowledgement) materially changes the build. Implication: this is an open
    legal question and a scope blocker, not a product decision.
- **Scheme Rules**: Chargeback windows bind independently [Fact - scheme summary]
  - Impact: a dispute opened too late is unrecoverable regardless of our SLA.
  - Threat: the app could let a customer open a dispute already out of window.
    Implication: the flow must surface the deadline before submission.
- **Data Protection**: LGPD governs evidence handling [Fact - LGPD]
  - Impact: any future evidence upload adds a retention and minimisation duty.
  - Opportunity: reinforces the v1 non-goal of no evidence upload.

## 7. Strategic Synthesis

- **Top 3 Opportunities**:
  1. Publish an acknowledgement SLA - Action: match or beat the 72-hour
     benchmark and say so in-app.
  2. Reframe disputes as retention - Action: take the case to finance using
     carrying cost, not CSAT.
  3. Surface scheme deadlines pre-submission - Action: turn a compliance
     constraint into a visibly helpful warning.
- **Top 3 Threats**:
  1. Regulated clock start ambiguous - Mitigation: legal ruling before scope lock.
  2. Volume grows regardless of fraud rate - Mitigation: instrument contact rate
     per active card from day one.
  3. Out-of-window disputes accepted in-app - Mitigation: block or warn at entry.
- **Roadmap Guardrails**:
  1. No v1 scope lock before the legal ruling on clock start.
  2. Status visibility ships in the same release as submission.
  3. No evidence upload until an LGPD retention design exists.

## Low-Impact Factors (stated honestly)

- **Environmental**: No material bearing on a software dispute flow. Aurora's
  reporting duties exist but do not touch this product.
- **Political**: Stable within the horizon, no trade or taxation exposure for a
  domestic digital journey.
- **Technological / Automation**: Relevant later for triage automation, not for
  v1, which is a read model over an existing queue.

## Assumptions to Validate

- That regulated acknowledgement timelines start at customer submission -
  **Legal must confirm. This blocks scope.**
- That scheme chargeback windows are the binding constraint rather than the
  domestic rule - Legal and the scheme relationship owner.
- That the trust survey generalises to Aurora's segment rather than the national
  average - Research.
```

---

## What this example is meant to teach

1. **Ask about geography; default the rest.** One question protected the half of
   the analysis that would otherwise have been wrong.
2. **Naming low impact is the discipline.** Three factors were closed in one line
   each. That is what makes the other three credible.
3. **A macro factor changed the roadmap.** "Status ships with submission" came
   out of the Social section, not from a design opinion.
4. **Regulatory readings go to legal, not into the artifact as fact.** The clock
   question is flagged as a scope blocker with an owner. A PESTEL that quietly
   picked an answer would have shipped a compliance risk as a requirement.

---

## Provenance

Example built on the schema in `prompts/pestel-analysis-prompt-template.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Aurora Bank is fictional; all figures and
sources are invented.
