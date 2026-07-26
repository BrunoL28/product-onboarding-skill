# Lean UX Canvas v2 - Output Template

Box numbers and names are a stability contract. This canvas gets photographed on
whiteboards, pasted into decks, and compared across quarters.

**Sticky-Note Rule (required):** every bullet 4-8 words, ASCII only, no emoji.

---

```markdown
## Lean UX Canvas (v2): <Initiative>

- **Date**: <YYYY-MM-DD>
- **Team**: <who was in the room>
- **Iteration**: <n> (Boxes 7-8 loop; this is loop n)

### 1. Business Problem
- <what changed in the world; why now>
- <the cost of leaving it unsolved>

### 2. Business Outcomes
- <measurable behaviour change: metric, current value, target>
- <secondary metric with a number>
- <guardrail metric that must not degrade>

### 3. Users
- <the persona to focus on first>
- <how many of them, and how to reach five tomorrow>

### 4. User Outcomes & Benefits
- <why a user would seek this out>
- <what they gain, as a feeling or a relief>
- <no metrics in this box - if there is a percentage here, it belongs in Box 2>

### 5. Solutions
- <solution 1>
- <solution 2>
- <solution 3 - at least three genuinely different shapes>

### 6. Hypotheses
- We believe <business outcome> will be achieved if <user> attains <benefit>
  with <solution>
- <one per solution that matters; each must be falsifiable>

### 7. What Is Most Important to Learn First?
- <the single riskiest assumption right now>
- **Risk type**: value / usability / feasibility / viability
- **If false, we waste**: <the work this would invalidate>

### 8. What Is the Least Work to Learn It?
- **Method**: <the smallest experiment>
- **Pass signal**: <stated in advance - what result means proceed>
- **Fail signal**: <what result means stop or rethink>
- **Timebox**: <how long, and what it costs>

### Assumptions to Validate
- <Box 7 assumption - the top one by definition>
- <runner-up, which becomes the next loop>
- <runner-up>
```

---

## Box quality checks

```markdown
| Box | Check | Result |
|---|---|---|
| 1 | Names a change in the world, not an absent feature | pass / fail |
| 2 | Contains a number and a direction | pass / fail |
| 3 | Could recruit five of these tomorrow | pass / fail |
| 4 | Contains no metrics | pass / fail |
| 5 | At least three genuinely different solutions | pass / fail |
| 6 | Every hypothesis could be proven false | pass / fail |
| 7 | Exactly one assumption, and it is the expensive one | pass / fail |
| 8 | Method, pass/fail signal, and timebox all present | pass / fail |
```

---

## Loop record (iterations 2+)

```markdown
### Loop <n> - what the last experiment taught

- **Ran**: <the Box 8 experiment>
- **Result**: <what happened, against the pre-stated signal>
- **Verdict**: validated / invalidated / inconclusive
- **New Box 7**: <the next riskiest assumption, or: confident enough to build>
```

---

## Provenance

Adapted from `prompts/lean-ux-canvas-prompt-template.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Canvas by Jeff Gothelf, *Lean UX* (O'Reilly).
