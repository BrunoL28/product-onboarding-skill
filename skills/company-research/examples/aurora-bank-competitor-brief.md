# Company Research - Worked Example

Researching a competitor ahead of scoping Aurora Bank's *Disputa Express*.
All content is fictional, including the sources.

---

## Intake

**User:** Research Nimbo, the digital bank. We're scoping in-app card disputes
and want to know how they think about it.

**Agent:**

> Purpose read as competitive analysis, window last 24 months. Two things I could
> ask about, but I will default and you can correct me: entity is Nimbo
> Servicos Financeiros S.A. (the licensed bank, not the payments subsidiary), and
> the questions are the seven framework sections with extra depth on their
> disputes journey.
>
> **Search plan**
> - Looking for: exec commentary on service and disputes 2024-2026, help-centre
>   documentation of their dispute flow, PM job postings, any published SLA.
> - Source classes: earnings transcripts, help centre, product blog, job
>   postings, Brazilian fintech trade press.
> - Fact vs read: quotes and published SLAs marked Fact with URLs; anything about
>   their intent marked Inference.
>
> Continuing unless you want to change that.

**User:** Go.

---

## Output (excerpt)

```markdown
## Executive Insights Company Profile: Nimbo

- **Research purpose**: competitive analysis - in-app card disputes
- **Recency window**: Aug 2024 - Jul 2026
- **Date of research**: 2026-07-26
- **Source classes used**: earnings transcripts, help centre, product blog, job postings, trade press

### Company Overview

**Basic Information:**
* **Name:** Nimbo Servicos Financeiros S.A.
* **Headquarters:** Sao Paulo, BR
* **Industry:** Digital banking, card issuing
* **Founded / size:** 2016, ~2,400 employees [Fact - nimbo.example/investors]

**Brief History:**
* Launched as a prepaid card, took a full banking licence in 2021, which is when
  disputes became their own regulatory problem rather than the processor's.
  [Fact - nimbo.example/investors/2021-annual]

### Executive Quotes on Strategic Vision

**Quote from the CEO:**
* "Every call we receive is a product failure we have not fixed yet."
  - Ana Ribeiro, CEO, Q1 2026 earnings call, 2026-02-11. [Fact - URL]
  - Context: answering an analyst question about rising support costs.

**Quote from the COO:**
* No public commentary found from this role in the window.

**Quote from the VP of Product Management:**
* "We measure a dispute by how long the customer spends not knowing."
  - Caio Menezes, VP Product, Fintech Brasil conference talk, 2025-11-04.
    [Fact - URL]

### Detailed Product Insights

**Product Strategy Overview:**
* Deflect contact volume by making state visible rather than by making support
  cheaper. Both exec quotes point the same direction. [Inference - basis: CEO and
  VP Product quotes above]

**Recent Product Launches and Innovations:**
* In-app dispute tracking with a published 72-hour acknowledgement SLA, shipped
  Mar 2025. [Fact - nimbo.example/help/disputas]

### Organizational Impact of Product Management

**Role of Product Management in Strategic Decisions:**
* Their PM job posting for the Cards squad lists "reduce contact rate per active
  card" as a primary success measure. PM owns a support metric, which suggests
  service cost sits with product and not with operations. [Inference - basis:
  job posting, URL]

### Future Product Roadmap and Challenges

**Anticipated Market Challenges:**
* Named rising fraud volume as a margin pressure in Q1 2026 remarks. [Fact - URL]

**Competitive Threats:**
* Their 72-hour SLA is published, which makes it a promise competitors can be
  measured against - including Aurora. [Inference]

### Key Takeaways for Our Product

* **Strategic principle worth borrowing:** publish the SLA. It converts an
  internal target into a customer-facing commitment.
* **PM lesson:** they gave PM the contact-rate metric. Ownership followed the
  metric.
* **Where they are exposed:** the 72-hour clock is acknowledgement, not
  resolution. Their help centre is quiet about resolution time. [Inference]

### Evidence and Assumptions

**Evidence Used:**
* Q1 2026 earnings transcript - URL - 2026-02-11
* Help centre disputes page - URL - retrieved 2026-07-26
* Cards squad PM job posting - URL - retrieved 2026-07-26

**Thin Sections:**
* Transformation strategies - no engineering blog and no conference material on
  their platform work. Would need a practitioner conversation to fill.
* COO commentary - nothing public in the window.

**Assumptions to Validate:**
* That the 72-hour SLA is met in practice, not just published.
* That contact-rate ownership sits with PM rather than being one line in one
  posting.
* That their dispute flow covers fraud and merchant disputes in one journey.
```

---

## What this example is meant to teach

1. **The empty section is a finding.** "No public commentary found from this
   role" told the team something real: Nimbo's COO does not talk about service.
   A manufactured quote would have destroyed that signal.
2. **Job postings are strategy documents.** The single most useful line in the
   brief came from a job ad, not an earnings call.
3. **Fact and Inference do different work.** The 72-hour SLA is a Fact you can
   hold them to. "They deflect volume by making state visible" is an Inference —
   useful, but it is your read, and labelling it says so.
4. **Look for what the competitor is quiet about.** The gap between published
   acknowledgement time and unpublished resolution time is the opening.

---

## Provenance

Example adapted to the schema in
`prompts/company-profile-executive-insights-research.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Nimbo and all quotes are fictional.
