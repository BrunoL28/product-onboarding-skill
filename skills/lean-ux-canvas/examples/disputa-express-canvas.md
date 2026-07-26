# Lean UX Canvas - Worked Example

Canvas for Aurora Bank's *Disputa Express*, run after the problem statement.
Fictional throughout.

The part worth studying is **Box 7**, where the team's first answer was the
comfortable assumption and not the expensive one.

---

## Collapse and gates

**Agent:**

> `PROBLEM_STATEMENT.md` and `PROTO_PERSONA.md` are upstream, so Boxes 1, 3, and 4
> are largely written already. Here is what I drew and from where:
>
> - **Box 1** from the problem statement's root cause: the queue was built for ops.
> - **Box 3** from the persona: first-time disputers, mobile-only.
> - **Box 4** from her quote, robbed twice - the benefit is liability certainty,
>   not speed.
>
> Box 2 is where the real work starts, because nothing upstream commits to a
> number. Starting there.
>
> **Box 2: Business Outcomes.** What behaviour change would tell you this worked?
>
> 1. **Contact rate per active card** - down. Directly attacks the 31% of call
>    minutes, and it is the metric the competitor's PM apparently owns.
> 2. **Repeat calls per dispute** - down. Narrower, but closer to the pain the
>    read-aloud gate surfaced (re-explaining).
> 3. **Time to acknowledgement** - down. Compliance-relevant, but it measures the
>    back office, not this product.
> 4. Other.

**User:** 1 and 2. And we can't let dispute approval rates drop just because it's
easier to open one.

**Agent:** That third one is a guardrail, which is the right instinct — making a
flow easier usually raises the volume of weak cases. Adding it as a guardrail
metric.

> Want to refine Box 2, or move on to Box 5: Solutions?

**User:** Move on.

*(Boxes 5 and 6 gated similarly.)*

---

## Box 7, first attempt

**User:** The riskiest thing is whether people can find the dispute entry point in
the app.

**Agent:**

> That is a usability assumption, and it is real — but it is cheap to test and
> cheap to fix. Being wrong about it costs you a navigation change.
>
> Try the question the other way: **which assumption, if false, would waste the
> most work?** You are proposing to build submission plus a status read model plus
> push notifications, on the premise that showing status deflects calls.
>
> If Camila checks the app *and calls anyway* — because what she wants is a human
> saying she is not liable, not a status chip saying under review — then the entire
> build lands and the call volume does not move. That is the expensive one, and it
> is a **value** assumption, not a usability one.

**User:** ...yeah. That's the one.

---

## Output

```markdown
## Lean UX Canvas (v2): Disputa Express

- **Date**: 2026-07-21
- **Team**: PM, design, tech lead, CX lead
- **Iteration**: 1

### 1. Business Problem
- Dispute queue built for ops, not customers
- Silence drives 31% of call minutes
- Volume grows with card growth alone

### 2. Business Outcomes
- Contact rate per active card: 0.14 to 0.10
- Repeat calls per dispute: 3.1 to 1.5
- Guardrail: dispute approval rate stays flat

### 3. Users
- First-time disputers, mobile-only
- 4,200 disputes monthly, panel access exists

### 4. User Outcomes & Benefits
- Knows she is not liable
- Never re-explains her story again
- Stops feeling robbed twice

### 5. Solutions
- In-app status timeline over existing queue
- Push notification on every state change
- Immediate provisional credit at submission
- Plain-language explainer at dispute entry

### 6. Hypotheses
- We believe contact rate will fall if first-time disputers attain liability
  certainty with push notifications on state change
- We believe repeat calls will fall if disputers attain not-re-explaining with an
  in-app status timeline
- We believe contact rate will fall furthest if disputers attain liability
  certainty with immediate provisional credit

### 7. What Is Most Important to Learn First?
- Does visible status actually deflect calls, or add a channel people check before
  calling anyway?
- **Risk type**: value
- **If false, we waste**: submission flow, status read model, push pipeline - the
  whole v1

### 8. What Is the Least Work to Learn It?
- **Method**: add one IVR question to the existing dispute line - did you check
  the app before calling? - plus five follow-up interviews with callers who said yes
- **Pass signal**: fewer than 30% of callers had already checked, and interviews
  say status would have prevented the call
- **Fail signal**: over 50% had already checked and called anyway - status alone
  will not deflect; provisional credit becomes the lead solution instead
- **Timebox**: two weeks, no engineering build, IVR change only

### Assumptions to Validate
- That visible status deflects calls rather than adding a checkpoint (Box 7)
- That liability certainty outranks refund speed - n = 3 currently
- That push reaches her, given zero email engagement
```

---

## What this example is meant to teach

1. **Box 7's first answer is usually the comfortable one.** Findability was real
   and cheap. The value assumption — does status deflect calls at all — was the one
   worth two weeks of protection.
2. **Box 8's fail signal changed the roadmap in advance.** The team agreed *before
   running it* that a result above 50% promotes provisional credit over status.
   That is what makes it an experiment rather than a survey.
3. **The guardrail metric came from the user, not the framework.** We cannot let
   approval rates drop is the instinct that stops a team optimising a funnel into
   a fraud vector.
4. **Box 4 has no numbers and Box 2 has nothing but.** Stops feeling robbed twice
   would be meaningless as a metric, and contact rate 0.14 to 0.10 would be
   meaningless as empathy. Keeping them separate keeps both usable.
5. **Two weeks and no build beat a quarter and a rewrite.** The experiment cost an
   IVR prompt.

---

## Provenance

Example built on the canvas in `prompts/lean-ux-canvas-prompt-template.md` from
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Canvas by Jeff Gothelf, *Lean UX*. Aurora Bank
is fictional; all figures are invented.
