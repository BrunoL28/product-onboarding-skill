# PESTEL Analysis - Output Template

Canonical structure. Section names and numbering are a stability contract.

**Sticky-Note Rule (required):** each bullet 4-8 words, ASCII only, no emoji.
The detail lives in the impact and implication lines.

**Evidence labels:** **[Fact]** sourced, **[Inference]** evidence-based reading,
**[Assumption]** working guess.

---

```markdown
# PESTEL Analysis: <Product>

## Overview

- **Project/Product Name**: <name and one line on what it does>
- **Analysis Purpose**: <market entry / strategic planning / risk / pitch>
- **Geographic Scope**: <markets and jurisdictions>
- **Time Horizon**: <e.g. 18 months>
- **Analyst**: <person or team>
- **Date**: <YYYY-MM-DD>

## 1. Political Factors

- **Government Policies**: <what is true> [Fact - source]
  - Impact: <effect on this product>
  - Opportunity / Threat: <which, and the implication>
- **Political Stability**: <as above, or "Low impact - <one line why>">
- **Trade Regulations**: <as above>
- **Taxation Policy**: <as above>

## 2. Economic Factors

- **Economic Growth**: <what is true> [Fact - source]
  - Impact: <effect on this product>
  - Opportunity / Threat: <which, and the implication>
- **Inflation Rate**: <as above>
- **Exchange Rates**: <as above>
- **Consumer Spending**: <as above>

## 3. Social Factors

- **Demographics**: <as above>
- **Cultural Trends**: <as above>
- **Lifestyle Changes**: <as above>
- **Consumer Attitudes**: <as above>

## 4. Technological Factors

- **Technological Advancements**: <as above>
- **R&D Activity**: <as above>
- **Automation**: <as above>
- **Digital Transformation**: <as above>

## 5. Environmental Factors

- **Climate Change**: <as above>
- **Sustainability Practices**: <as above>
- **Resource Scarcity**: <as above>
- **Environmental Regulations**: <as above>

## 6. Legal Factors

- **Compliance Requirements**: <as above>
- **Intellectual Property Rights**: <as above>
- **Employment Laws**: <as above>
- **Health and Safety Regulations**: <as above>
- **Data Protection**: <as above>

## 7. Strategic Synthesis

- **Top 3 Opportunities**:
  1. <opportunity> - Action: <what to do>
  2. <opportunity> - Action: <what to do>
  3. <opportunity> - Action: <what to do>
- **Top 3 Threats**:
  1. <threat> - Mitigation: <how>
  2. <threat> - Mitigation: <how>
  3. <threat> - Mitigation: <how>
- **Roadmap Guardrails**:
  1. <constraint this analysis puts on the plan>
  2. <constraint>
  3. <constraint>

## Low-Impact Factors (stated honestly)

- <Factor>: <one line on why it does not bind here>

## Assumptions to Validate

- <Assumption 1 - who should confirm it>
- <Assumption 2>
- <Assumption 3>
```

---

## Scenario add-on (when `scenario_planning` is on)

```markdown
## Scenarios for <top threat>

| Scenario | Trigger | Effect on product | Response |
|---|---|---|---|
| Best | | | |
| Base | | | |
| Worst | | | |
```

---

## Delta output (repeat runs)

```markdown
# PESTEL Delta: <Product> since <date>

**Materially moved**
- <Factor> - <what changed> [Fact - source] - <new implication>

**New factor entered scope**
- <Factor> - <why it now binds>

**No material change**
- Sections <list> - see prior analysis.
```

---

## Provenance

Adapted from `prompts/pestel-analysis-prompt-template.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0.
