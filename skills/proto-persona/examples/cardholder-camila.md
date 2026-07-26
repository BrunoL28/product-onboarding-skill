# Proto Persona - Worked Example

Building the protagonist for Aurora Bank's *Disputa Express*. Fictional — but the
placeholder discipline is the part to copy.

---

## Facilitation

**Agent:**

> Before I build the persona I need a few things. Three questions, one at a time.
> At any point you can pick an option, type your own, say "take your best guess,"
> or drop in your notes to skip ahead.
>
> **Question 1 of 3: the painful moment.** A persona is only as sharp as the
> moment you catch them in. Which moment is v1 designed for?
>
> 1. **The discovery moment** - they have just spotted the charge, adrenaline is
>    high, they want to know they are not liable. Highest emotional load.
> 2. **The waiting moment** - they have already reported it and heard nothing for
>    days. Lower adrenaline, higher resentment. This is where your call volume is.
> 3. **The resolution moment** - the outcome has landed and they do not
>    understand it. Smallest volume, worst reviews.
> 4. Other.

**User:** Honestly 1 and 2. They find it, they call, then they wait.

**Agent:** So the persona spans two moments with different emotional registers —
that matters, because the product has to do reassurance *and* patience.

> **Question 2 of 3: evidence.** You mentioned support handles this by phone. What
> do you actually have?
>
> 1. **Call transcripts or recordings** - best case, gives me real quotes.
> 2. **Support tickets and summaries** - gives me pains, but quotes will be
>    second-hand paraphrase.
> 3. **Only the team's impressions** - workable, but the Quotes section ships as
>    placeholders and I will say so.
> 4. Other.

**User:** We have transcripts from three calls the CX lead flagged, pasting them.

**Agent:** *(reads the transcripts)*

> **Found** - three verbatim quotes, the phrase "robbed twice" from one caller,
> all three are mobile-only customers, all three called within 24 hours of
> noticing.
> **Inferred** - the trigger is the push notification for the charge, not a
> statement review. All three mention seeing an alert.
> **Still missing** - decision authority is irrelevant here (consumer product),
> and I have nothing on income, which I will leave empty rather than guess.
>
> That covers question 3. Building the canvas.

---

## Output

```markdown
## Proto Persona Canvas

> **Status: PROTO.** Built from three support transcripts and team knowledge. Not
> validated research.

### Name
* Cardholder Camila

### Bio & Demographics
* Banks only on mobile, never opens bank email
* Sees charges via push alert, not statements (support transcripts, 2026-06)
* Has never disputed a charge before this one
* 34, Recife - included only because regional call-centre hours affect her

### Quotes
* "I don't even know what this is called. I just know it wasn't me."
  (support transcript 2, 2026-06-14)
* "I felt robbed twice. Once by whoever took the money, once by the wait."
  (support transcript 1, 2026-06-09)
* "Nobody told me if I have to pay the bill while you look into it."
  (support transcript 3, 2026-06-21)
* `[PLACEHOLDER - NEEDS RESEARCH]` - what she does in the gap between calling and
  hearing back. Would ask: "walk me through the days after your call."

### Pains
* Does not know the vocabulary, so cannot search help articles
* No way to check status without calling again
* Unclear whether she owes the disputed amount meanwhile
* Repeats her story to a new agent each call (support transcripts)

### What is this Person Trying to Accomplish
* Confirms the charge is not hers by checking her own memory first
* Calls within 24 hours of the push alert
* Calls back roughly every three days for status
* Wants liability removed - the refund is second to not being on the hook

### Goals
* **Short term:** hear that she is not liable, today
* **Long term:** keep trusting the bank enough to keep her salary there
* **Personal:** not feel foolish for having been targeted

### Attitudes & Influences
* **Decision Making Authority** - full, consumer product, not applicable
* **Decision Influencers** - family and a WhatsApp group; churn is socially
  contagious `[ASSUMPTION - VALIDATE]`
* **Beliefs & Attitudes** - believes the bank should absorb fraud loss by default
  (all three transcripts imply this, none state it) `[ASSUMPTION - VALIDATE]`

### What Would Change Our Mind
* If disputers turn out to be mostly repeat disputers who know the process, the
  whole reassurance framing is wrong and v1 should optimise for speed instead.

### Graduation Criteria
* Pains, job, and two quotes from primary research, n > 5. Currently n = 3.
* Two `[ASSUMPTION - VALIDATE]` tags outstanding.
* Stays a proto-persona until both clear.

### Assumptions to Validate
- That liability anxiety outranks refund speed - ask five recent disputers to
  rank them.
- That first-timers are the majority, not repeat disputers - pull the dispute
  table by customer, one query.
- That churn spreads socially after a bad dispute - check whether churned
  disputers cluster by referral cohort.
```

---

## What this example is meant to teach

1. **The placeholder is the lesson.** The gap between calling and hearing back is
   exactly where the product lives, and there was no evidence for it. Writing
   `[PLACEHOLDER - NEEDS RESEARCH]` there — rather than a plausible sentence — is
   what turned it into the first interview question.
2. **Behaviour over demographics.** "Sees charges via push alert, not statements"
   changed the entry point of the entire flow. "34, Recife" changed nothing, and
   is justified in the artifact or it would have been cut.
3. **Two assumption tags survived on purpose.** Both are plausible, neither is
   evidenced, and both are cheap to test. Tagging them is what makes the
   confident parts trustworthy.
4. **The mind-changer section forces falsifiability.** If disputers are mostly
   repeat disputers, this persona is wrong — and that is a one-query check.

---

## Provenance

Example built on the canvas in `prompts/proto-persona-profile.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Camila and all transcripts are fictional.
