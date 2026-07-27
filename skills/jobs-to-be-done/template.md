# Jobs to be Done - Output Template

One canvas, seven sections, in this order. **The section order is a stability
contract** - teams paste this into discovery docs, PRDs, and story maps, and diff
it across quarters. Add sections at the end; never rename or reorder.

**Sticky-Note Rule:** every bullet 4-8 words, ASCII only, no emoji. The job
statement and the desired outcome statements are the only exceptions.

**Evidence labels:** every material claim ends with `(Fact)`, `(Inference)`, or
`(Assumption)`. A bullet with no label reads as fact, and usually is not.

---

## The canvas

```markdown
## Jobs to be Done: <persona or segment>

- **Situation in scope**: <the circumstance, not the person>
- **Decision this informs**: <what changes depending on the answer>
- **Evidence base**: <n interviews / n tickets / team knowledge only>
- **Date**: <YYYY-MM-DD>

### 0. Job Statement

- **Main job**: <verb> <object of the job> <contextual clarifier>
- **Job story**: When <situation>, I want to <motivation>, so I can
  <expected outcome>.
- **Solution-swap check**: <what else could be hired for this job today>
- **Stability check**: <would this hold if we shipped nothing? yes / no>

### 1. Customer Jobs

#### Functional Jobs
- <task the customer must get done> (Fact | Inference | Assumption)
- <task>

#### Emotional Jobs
- <state they seek or avoid, in their words>
- <state>

#### Social Jobs
- <how they want to be perceived, or not>
- <perception>

### 2. Forces of Progress

#### Push of the Situation (toward change)
- <what made today different>

#### Pull of the New Solution (toward change)
- <what they imagine afterwards>

#### Habit of the Present (against change)
- <what is comfortable or already learned>

#### Anxiety of the New (against change)
- <what could go wrong, in their words>

### 3. Pains

#### Challenges
- <obstacle in the customer's world>

#### Costliness
- <too much time, money, or effort>

#### Common Mistakes
- <frequent error a solution could prevent>

#### Unresolved Problems
- <problem no current option solves>

### 4. Gains

#### Expectations
- <where current options fall short>

#### Savings
- <time, money, or effort saved>

#### Adoption Factors
- <what would raise likelihood of adoption>

#### Life Improvement
- <what would make life easier or better>

### 5. Desired Outcome Statements

| # | Outcome statement | Importance | Satisfaction | Source |
|---|---|---|---|---|
| 1 | Minimize the time it takes to <object of control> <clarifier> | 1-10 | 1-10 | measured / assumed |
| 2 | Increase the likelihood that <object of control> <clarifier> | 1-10 | 1-10 | measured / assumed |

**Unmet needs** (high importance, low satisfaction): <outcome numbers>

### 6. Assumptions to Validate
- <assumption> - test: <cheapest thing that would settle it>
- <assumption> - test: <...>
- <assumption> - test: <...>
```

---

## The forces diagram

Render this alongside the canvas whenever the forces section has content in all
four cells. A visibly empty right-hand column is the point of the diagram.

```
          PROMOTING CHANGE                    RESISTING CHANGE
   +--------------------------------+ +--------------------------------+
   | PUSH of the situation          | | HABIT of the present           |
   |  - <4-8 words>                 | |  - <4-8 words>                 |
   |  - <4-8 words>                 | |  - <4-8 words>                 |
   +--------------------------------+ +--------------------------------+
   | PULL of the new solution       | | ANXIETY of the new             |
   |  - <4-8 words>                 | |  - <4-8 words>                 |
   |  - <4-8 words>                 | |  - <4-8 words>                 |
   +--------------------------------+ +--------------------------------+

   Switch happens when   (push + pull)  >  (habit + anxiety)
```

---

## Field rules

- **Main job** contains no product name, yours or anyone's.
- **Job story** situation is a circumstance ("just saw a charge she does not
  recognise"), not an attribute ("is 34 and banks on mobile").
- **Emotional and social jobs** without a quote or observation behind them get an
  `(Assumption)` label and an entry in section 6. Never both blank and confident.
- **Pains** describe the customer's world. A pain that names the absence of your
  feature is a solution written backwards - rewrite it as the struggle.
- **Outcome statements** start with Minimize or Increase and end measurable. If
  you cannot say what instrument would read it, it is a gain, not an outcome.
- **Importance and satisfaction** are blank or labelled `assumed` until someone
  surveys. A number with no source is the most expensive kind of decoration.
- **Assumptions to Validate** is never empty. A canvas with nothing to validate
  has been written from imagination or is a summary of finished research.

---

## Provenance

Adapted from `prompts/jobs-to-be-done.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Method: Clayton Christensen, *Competing Against
Luck*; Bob Moesta, *Demand-Side Sales 101* (forces of progress); Tony Ulwick,
*Jobs to be Done: Theory to Practice* (desired outcome statements). Jobs, pains,
and gains structure influenced by Alexander Osterwalder's Value Proposition
Canvas.
