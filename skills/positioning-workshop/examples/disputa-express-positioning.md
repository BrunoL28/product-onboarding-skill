# Positioning Workshop - Worked Example

Positioning Aurora Bank's *Disputa Express* before the launch brief. Fictional,
competitor and figures included. The useful parts: the **primary alternative being
Aurora's own call centre**, and the **swap test failing** on the first draft.

---

## Collapse, then two decisions

**Agent:**

> `PROBLEM_STATEMENT.md`, `PROTO_PERSONA.md`, and the Nimbo brief are upstream, so
> I am not interviewing you about the customer.
>
> **Found** - first-time disputers, mobile-only, 4,200 disputes a month; a charge
> she did not make, then silence. **Inferred** - the unmet need is liability
> certainty, not refund speed. **Still missing** - what those documents cannot
> decide: **category frame** and **differentiation angle**.
>
> **Question 1 of 4: alternatives.** If Disputa Express vanished tomorrow, what
> would Camila actually do?
>
> 1. **Call the Aurora support line** - 4,200 disputes a month arrive this way.
> 2. **Switch the charge to Nimbo's app** - their help centre documents this.
> 3. **Do nothing and absorb the R$ 480** - the silent option nobody logs.
> 4. Other.

**User:** Mostly 1. Some of 3, honestly - small charges people give up on.

**Agent:** Then the primary alternative is your own call centre, not Nimbo. A
competitor is a more comfortable opponent than a process you already own.

---

## The category decision

**Agent:**

> **Question 3 of 4: category frame.** It sets the comparison set before anyone
> reads a feature.
>
> 1. **In-app card dispute resolution** - whole dispute in the app; rules out the
>    broader fraud story; compares us to Nimbo.
> 2. **Fraud protection suite** - Aurora protects you; rules out nothing.
> 3. **Self-service banking tool** - saves the bank money; rules out the stake.
>
> Recommending 1. Two flatters and commits to nothing; three is the internal frame.

**User:** 1, but "resolution" has to include the money. Not just tracking.

**Agent:** Then the benefit slot carries liability, not status - the correction
the DE-EPIC-2 hypothesis already made.

---

## The swap test, first attempt

**Agent:** First assembly, unpolished: *"...unlike calling the support line,
Disputa Express makes disputes faster and simpler."*

> Now the swap: *"Calling the support line makes disputes faster and simpler."* A
> call-centre manager would say that with a straight face, so it is a **FAIL**.
> Faster and simpler are adjectives. Rewriting the slot around what only we can do:
> real internal state plus the liability answer, on the card screen.

**User:** And Nimbo can't say that? They show a status too.

**Agent:** Their help centre documents a status list [Fact - nimbo.example/help,
2026-07-22]; no source shows a liability statement. Not a claim that they lack it
- an Inference that we have not found it, with the check in Assumptions.

---

## Output

```markdown
## Positioning Worksheet: Disputa Express

- **Date**: 2026-07-25
- **Participants**: PM, CX lead, brand lead
- **Segment covered**: first-time card disputers, mobile-only
- **One plain sentence**: open a card dispute in-app and see where it stands

### 1. Competitive alternatives

| Alternative | What they actually do | Who picks it | Evidence |
|---|---|---|---|
| Aurora call centre (status quo) | Call, wait, call again | Everyone today | Q2 support deck [Fact] |
| Do nothing, absorb charge | Give up on small charges | Low-value charges | CX lead read [Inference] |
| Nimbo in-app disputes | File and track in app | Dual-banked customers | Nimbo help centre [Fact] |

- **Status quo verdict**: primary alternative - it holds 100% of volume today

### 2. Unique attributes

| Attribute | Which alternatives lack it | Evidence |
|---|---|---|
| Liability answer while open | Call centre, Nimbo | No source found [Inference] |
| Real queue state, plain words | Call centre | Back-office read model [Fact] |
| No re-explaining on return | Call centre | Transcripts, n=3 [Fact] |

### 3. Value and proof

| Attribute | What it lets a customer achieve | Proof today | Label |
|---|---|---|---|
| Liability answer | Stops wondering if she owes it | 3 transcripts lead with it | Fact |
| Real queue state | Stops calling to ask | Holdout test not yet run | Assumption |

### 4. Target market

- **Segment**: first-time disputers, mobile-only, one open dispute
- **Why they care more**: no vocabulary, highest fear
- **Find five tomorrow**: support panel, disputes flagged this week

### 5. Market category

| Candidate frame | Makes obvious | Rules out | Comparison set |
|---|---|---|---|
| In-app dispute resolution | Whole dispute in app | Broader fraud story | Nimbo, neobanks |
| Fraud protection suite | Aurora protects you | Nothing, which is the flaw | Card networks |
| Self-service banking tool | Saves the bank money | Emotional stake | IVR, chatbots |

- **Chosen**: in-app card dispute resolution - by the PM, as the only legible frame
- **What we accept losing**: the prevention story, and the internal cost story

### 6. Trends - none claimed; no customer named one first
```

```markdown
## Positioning Statement: Disputa Express

- **For** Aurora cardholders facing a charge they did not make, first dispute
- **who** need to know they are no longer liable, not merely that a form arrived
- **Disputa Express** is an **in-app card dispute resolution service**
- **that** tells them where the dispute stands and whether they still owe the
  money, in their own language, without a phone call
- **unlike** calling the Aurora support line, where the only way to learn anything
  is to call again and re-explain the story
- **Disputa Express** exposes the dispute's real internal state and the liability
  answer on the card screen, continuously, from the moment it is opened

**Assembled**: For Aurora cardholders facing a charge they did not make, who need
to know they are no longer liable rather than that a form arrived, Disputa Express
is an in-app card dispute resolution service showing where the dispute stands and
whether they still owe the money - unlike calling support and re-explaining.

### Swap test

- **Swapped in**: calling the Aurora support line
- **Resulting sentence**: "Calling the support line exposes the real state and the
  liability answer on the card screen."
- **Still reads true?**: no - pass
- **What we changed**: the draft said "faster and simpler", which the support line
  could claim too. Liability plus continuous visibility, it cannot.

### Proof points

| Claim in the statement | Proof | Source | Label |
|---|---|---|---|
| Calling is the real alternative | 4,200 disputes/month by phone | Q2 support deck | Fact |
| Alternatives omit liability | No liability line found | Nimbo help centre | Inference |
| Visible state deflects calls | Holdout test pending | DE-EPIC-2 hypothesis | Assumption |

### Variants

- **Executive**: In-app card dispute resolution, competing with our own phone
  queue and its 4,200 disputes a month. We defend liability certainty.
- **Customer-facing**: See exactly where your dispute stands - and whether you
  still owe the money - without calling anyone.

### Assumptions to Validate

- That neither the support line nor Nimbo answers the liability question. Riskiest
  entry, an Inference from an absent source. Check: mystery shop one Nimbo dispute
  and listen to five Aurora calls for the liability answer.
- That "in-app card dispute resolution" is legible to a cardholder. Read it to
  five panel members and ask what they expect it to do.
```

---

## What this example is meant to teach

1. **The primary alternative was the bank's own call centre**, not the competitor.
2. **The swap test kills adjectives** - "faster and simpler" survived the swap.
3. **The flattering frame was the broad one**; "fraud protection suite" ruled
   nothing out, which is why it sharpened nothing.
4. **Absence of evidence got a label, not a claim.** "No liability line found" is
   an Inference with a mystery shop attached.

---

## Provenance

Example built on the schema in `prompts/positioning-statement.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: April Dunford, *Obviously Awesome*.
Statement: Geoffrey Moore, *Crossing the Chasm*. Aurora Bank and Nimbo are
fictional; every figure is invented.
