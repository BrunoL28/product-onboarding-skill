# Positioning Workshop - Output Templates

Two schemas that ship together as one package. The **Dunford worksheet** is the
reasoning: the alternatives, attributes, value, segment, and category frame that
were considered and the ones that were rejected. The **Moore statement** is the
sentence that reasoning produced, plus its variants and its swap test.

Shipping the statement without the worksheet is the commonest way this artifact
rots. Six months later nobody remembers which alternatives were on the list, so
nobody notices when they change.

## Template stability

The six Moore slot names - **For / who / is a / that / unlike / [product]** - and
the Dunford component numbering (1 alternatives, 2 attributes, 3 value and proof,
4 target market, 5 category, 6 trends) are a stability contract. These get pasted
into launch briefs and sales enablement, and renaming a slot breaks someone's
copy deck mid-quarter.

Change a section only as a **labelled new version** (`Positioning package v2`)
with a migration note naming what moved where. Improve the intake and the
facilitation freely; leave the slots alone.

**Sticky-Note Rule** applies to every bullet in the worksheet tables: 4-8 words,
ASCII only, no emoji. Prose belongs in the proof lines, not the canvas.

---

## 1. Dunford build-order worksheet

Work bottom-up. Component 1 is the pivot; get it wrong and everything below
inherits the error.

```markdown
## Positioning Worksheet: <product or working label>

- **Date**: <YYYY-MM-DD>
- **Participants**: <who was in the room>
- **Segment covered**: <exactly one - a statement covering three covers none>
- **One plain sentence**: <what it does, no adjectives>

### 1. Competitive alternatives

| Alternative | What they actually do | Who picks it | Evidence |
|---|---|---|---|
| <status quo - required row> | <4-8 words> | <4-8 words> | <source> [label] |
| <alternative 2> | <4-8 words> | <4-8 words> | <source> [label] |
| <alternative 3> | <4-8 words> | <4-8 words> | <source> [label] |

- **Status quo verdict**: used as primary alternative / ruled out because <reason>

### 2. Unique attributes

| Attribute | Which alternatives lack it | Evidence |
|---|---|---|
| <capability, not adjective> | <named> | <source> [label] |

### 3. Value and proof

| Attribute | What it lets a customer achieve | Proof today | Label |
|---|---|---|---|
| <attribute> | <outcome they would notice> | <what we can stand behind now> | Fact / Inference / Assumption |

### 4. Target market

- **Segment**: <specific enough to recruit five, or list accounts for>
- **Why they care more than others**: <4-8 words>
- **How we would find five tomorrow**: <channel or list>

### 5. Market category

| Candidate frame | Makes obvious | Rules out | Comparison set |
|---|---|---|---|
| <frame A> | <4-8 words> | <4-8 words> | <who we get compared to> |
| <frame B> | <4-8 words> | <4-8 words> | <who we get compared to> |
| <frame C> | <4-8 words> | <4-8 words> | <who we get compared to> |

- **Chosen**: <frame> - chosen by <human name or role>
- **Why**: <one sentence>
- **What we accept losing**: <what the rejected frames would have made obvious>

### 6. Trends (optional - off unless a customer named it first)

- <trend, and the customer who named it, or "none claimed">
```

---

## 2. Positioning statement package

```markdown
## Positioning Statement: <product>

- **For** <target customer, the segment from component 4>
- **who** <unmet need, in the painful moment>
- **<product>** is a **<market category, from component 5>**
- **that** <key benefit - an outcome the customer would notice>
- **unlike** <primary alternative - usually the status quo>
- **<product>** <differentiation, with proof standing behind it>

**Assembled**: <the six slots read aloud as one paragraph>

### Swap test

- **Swapped in**: <primary alternative's name in place of the product's>
- **Resulting sentence**: <the swapped sentence, written out>
- **Still reads true?**: yes = FAIL, rewrite the differentiation slot / no = pass
- **What we changed to make it false**: <the edit, or "passed first time">

### Proof points

| Claim in the statement | Proof | Source | Label |
|---|---|---|---|
| <claim> | <evidence> | <where it came from> | Fact / Inference / Assumption |

### Variants

- **Executive**: <two sentences, frame plus the one number that matters>
- **Customer-facing**: <one sentence in the customer's words, no category jargon>
- **Sales one-liner (optional)**: <a third variant, never a replacement>

### Assumptions to Validate

- <riskiest alternatives-list entry - most inference, most consequence if wrong>
- <proof point tagged Assumption, and what would turn it into a Fact>
- <segment claim not yet tested outside the room>
- <category frame nobody outside the team has heard read aloud>
```

---

## Provenance

Adapted from `prompts/positioning-statement.md` and
`prompt-generators/positioning-statement-prompt-generator.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: April Dunford, *Obviously Awesome*.
Statement template: Geoffrey Moore, *Crossing the Chasm*. Runs in Phase 0
alongside `jobs-to-be-done`; feeds `product-strategy-session`.
