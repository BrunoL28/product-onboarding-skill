# Company Research - Output Template

The canonical Executive Insights Company Profile. Section names are a stability
contract; change them only as a labelled new version.

Every bullet carries an evidence label: **[Fact]** (sourced), **[Inference]**
(evidence-based reading), **[Assumption]** (working guess).

---

```markdown
## Executive Insights Company Profile: <Company>

- **Research purpose**: <interview prep / competitive analysis / partnership / benchmarking / market entry>
- **Recency window**: <e.g. Jan 2025 - Jul 2026>
- **Date of research**: <YYYY-MM-DD>
- **Source classes used**: <e.g. earnings transcripts, product blog, job postings, trade press>

### Company Overview

**Basic Information:**
* **Name:** <official name>
* **Headquarters:** <location>
* **Industry:** <primary industries>
* **Founded / size:** <year, headcount range> [Fact - source]

**Brief History:**
* <milestone that explains today's market position> [Fact - source]

### Executive Quotes on Strategic Vision

**Quote from the CEO:**
* "<verbatim quote>"
  - <Name>, CEO, <venue>, <YYYY-MM-DD>. [Fact - URL]
  - Context: <why they were saying it, one line>

**Quote from the COO:**
* "<verbatim quote>" - <Name>, COO, <venue>, <date>. [Fact - URL]

**Quote from the VP of Product Management:**
* "<verbatim quote>" - <Name>, VP Product, <venue>, <date>. [Fact - URL]

**Quote from the Group Product Manager:**
* "<verbatim quote>" - <Name>, Group PM, <venue>, <date>. [Fact - URL]

> If no quote exists for a role in the window, write:
> "No public commentary found from this role in the window." Do not substitute a
> paraphrase or a quote from a different role.

### Detailed Product Insights

**Product Strategy Overview:**
* <how they connect market needs to technical capability> [Inference - basis]

**Recent Product Launches and Innovations:**
* <launch, date, and its effect on their position> [Fact - source]

### Transformation Strategies and Initiatives

**Digital Transformation:**
* <approach, and how it meets existing process> [Fact / Inference - source]

**AI Transformation:**
* <how AI enters core processes, products, positioning> [Fact / Inference - source]

**Agile Transformation:**
* <methodology adoption and stated results> [Fact / Inference - source]

### Organizational Impact of Product Management

**Role of Product Management in Strategic Decisions:**
* <what PM owns, and the evidence for it> [Inference - e.g. from PM job postings]

**Cross-Functional Collaboration:**
* <how PM works with design, eng, marketing, sales> [Inference - source]

### Future Product Roadmap and Challenges

**Upcoming Product Initiatives:**
* <publicly stated initiative and the goal it serves> [Fact - source]

**Anticipated Market Challenges:**
* <headwind they have named, plus their stated response> [Fact - source]

**Competitive Threats:**
* <threat, and who it comes from> [Inference - basis]

### Product-Led Growth Insights

**Implementation of PLG Strategies:**
* <self-serve motion, pricing model, activation path> [Fact - source]

**Data-Driven Product Decisions:**
* <what they have said about instrumentation and decision practice> [Fact / Inference]

### Key Takeaways for Our Product

* **Strategic principle worth borrowing:** <one>
* **PM lesson:** <one>
* **Where they are exposed:** <one, labelled Inference>

### Evidence and Assumptions

**Evidence Used:**
* <artifact or quote> - <URL> - <date>

**Thin Sections:**
* <section that lacked evidence> - <what would fill it>

**Assumptions to Validate:**
* <Assumption 1>
* <Assumption 2>
* <Assumption 3>
```

---

## Peer comparison add-on (when `peer_comparison` is on)

```markdown
### Side-by-Side: <Company> vs <Peer>

| Dimension | <Company> | <Peer> | Evidence quality |
|---|---|---|---|
| Stated strategy | | | Fact / Inference |
| Product velocity | | | |
| PLG motion | | | |
| Where PM sits | | | |
| Publicly stated weakness | | | |
```

---

## Delta output (repeat runs)

```markdown
## <Company> - Research Delta since <date of prior brief>

**Materially changed**
- <change> [Fact - source]

**New executive commentary**
- "<quote>" - <Name>, <role>, <date>. [Fact - URL]

**Unchanged**
- Sections <list> - see prior brief, no material movement.
```

---

## Provenance

Adapted from `prompts/company-profile-executive-insights-research.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0.
