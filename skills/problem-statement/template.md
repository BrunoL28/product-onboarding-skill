# Problem Statement - Output Template

The canonical Problem Framing Canvas. Section names and the five narrative lines
are a stability contract — teams diff this canvas across quarters to see whether
their understanding of the problem actually moved.

---

```markdown
## Problem Framing Canvas

### Problem Framing Narrative

**I am**: <the persona experiencing the problem, in a specific moment>
- <key pain point or characteristic 1>
- <key pain point or characteristic 2>
- <key pain point or characteristic 3>

**Trying to**:
- <one sentence: the outcome this persona actually cares about, not the task>

**But**:
- <the barrier preventing the outcome>
- <barrier 2>
- <barrier 3>

**Because**:
- <the root cause, in empathetic language - structurally different from "But">

**Which makes me feel**:
- <emotional impact, in the persona's own words where research provides them>

### Context & Constraints
- <geographic, technological, time-based, organisational, or demographic factors
  that directly bear on the problem - concrete enough to inform design>

### Final Problem Statement
- <Persona> needs a way to <desired outcome> because <root cause>, which
  currently <emotional or practical impact>.

### Evidence Base
- <what this framing rests on: interviews, transcripts, tickets, analytics>
- <n = how many, and how recent>

### Validation Record
- Read aloud to: <who, how many, when>
- Their words we adopted: "<quote>"
- Where they disagreed with our framing: <what changed>

### Assumptions to Validate
- <Assumption 1> - <the research that would settle it>
- <Assumption 2> - <the research that would settle it>
```

---

## Framing checks (self-check before shipping)

Run these on the draft. Include the table in the artifact only if the team finds
it useful.

```markdown
### Framing Checks

| Check | Question | Result |
|---|---|---|
| Solution smuggling | Does any line name a feature or screen? | pass / fail |
| User vs business | Would the persona call this their problem? | pass / fail |
| Root cause | Is "Because" structurally different from "But"? | pass / fail |
| Emotion provenance | Which interview produced that feeling word? | source |
| Specificity | Could a competitor paste this unchanged? | pass / fail |
```

---

## Stakeholder variants add-on (when `variants` is on)

The canonical statement does not change. These are translations of it.

```markdown
### Variants

**For executives** (one sentence, ties to a business outcome):
- <statement>

**For engineering** (one sentence, names the system constraint):
- <statement>

**For design** (one sentence, names the moment and the emotion):
- <statement>
```

---

## Provenance

Adapted from `prompts/framing-the-problem-statement.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0.
