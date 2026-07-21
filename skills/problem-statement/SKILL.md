---
name: problem-statement
description: Write a user-centered problem statement with who is blocked, what they are trying to do, why it matters, and how it feels. Use when framing discovery, prioritization, or a PRD.
---

## Purpose
Articulate a problem from the user's perspective using an empathy-driven framework that captures who they are, what they're trying to do, what's blocking them, why, and how it makes them feel. Use this to align stakeholders on the problem before jumping to solutions, framing product work around user outcomes rather than feature requests.

This is not a requirements doc—it's a human-centered problem narrative that ensures you're solving a problem worth solving.

## The Problem Framing Framework
**Problem Framing Narrative:**
- **I am:** [persona experiencing the problem]
- **Trying to:** [desired outcomes the persona cares about]
- **But:** [barriers preventing the outcomes]
- **Because:** [root cause of the problem]
- **Which makes me feel:** [emotional impact]

**Context & Constraints:** geographic, technological, time-based, demographic factors.
**Final Problem Statement:** single, concise, empathetic summary.

### Anti-Patterns (What This Is NOT)
- Not a solution in disguise.
- Not a business problem (revenue/churn are symptoms).
- Not a feature request.
- Not generic.

## Application

### Step 1: Gather User Context
User interviews/research, JTBD insights, persona clarity, constraints data. If missing context, run discovery—don't fabricate.

### Step 2: Draft the Problem Framing Narrative
Fill I am / Trying to / But / Because / Which makes me feel. Quality checks: persona specificity; outcome (not task) clarity; real barriers; root cause (not symptom); authentic emotions from research.

### Step 3: Document Context & Constraints
Enumerate factors that directly impact the problem; concrete enough to inform design.

### Step 4: Craft the Final Problem Statement
Formula: `[Persona] needs a way to [desired outcome] because [root cause], which currently [emotional/practical impact].` One sentence, measurable, empathetic, shareable.

### Step 5: Validate and Socialize
Read aloud to people who experience the problem ("Yes, exactly!"); share with stakeholders; iterate.

## Common Pitfalls
1. Solution smuggling → reframe around the outcome.
2. Business problem disguised as user problem → dig into why users churn / what they want.
3. Generic personas → get specific.
4. Symptom instead of root cause → keep asking why.
5. Fabricated emotions → use real interview quotes.

### Provenance
Adapted from `prompts/framing-the-problem-statement.md` in the `deanpeters/product-manager-prompts` repo. Bundled in the product-onboarding plugin; upstream is the source of truth.
