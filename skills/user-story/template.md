# User Story - Output Templates

Two schemas: the single story, and the story map. Field names are a stability
contract — these get imported into Jira and Azure DevOps.

---

## 1. Single story

```markdown
### User Story <ID>

- **Summary**: <brief, memorable title carrying the value delivered to the persona>

#### Use Case:
- **As a** <named persona, or role - never "user">
- **I want to** <action taken to reach the outcome>
- **so that** <the outcome the persona actually wants>

#### Acceptance Criteria:
- **Scenario**: <human-readable scenario, aligned to the As a actor>
- **Given**: <initial precondition>
- **and Given**: <additional precondition>
- **and Given**: <as many preconditions as required>
- **When**: <one triggering action, aligned to I want to>
- **Then**: <one expected outcome, aligned to so that>

#### Negative Case:
- **Given**: <precondition>
- **When**: <trigger>
- **Then**: <what must NOT happen>

#### Notes
- **Split Signal Rule**: if a second When or Then is needed, this is two stories.
  Hand off to `epic-breakdown-advisor`.
- **Open questions**: <undecided behaviour - do not invent criteria for it>
- **Estimate**: <leave blank; engineering owns this>
```

---

## 2. User story map

```markdown
## User Story Map: <Initiative>

### Who

#### Segment:
- <target segment>

#### Persona:
- <persona and the characteristics that matter here>

### Backbone

#### Narrative:
- <the journey in one line, or the JTBD objective>

#### Activities (left to right, in the order they happen):
1. <Activity 1>
2. <Activity 2>
3. <Activity 3 - up to about five>

#### Steps:

For <Activity 1>:
- Step 1: <step>
- Step 2: <step>
- <3 to 5 steps per activity>

For <Activity 2>:
- Step 1: <step>

#### Stories:

Under <Activity 1, Step 1>:
- <US-1> <story summary>
- <US-2> <story summary>

### Release Slices

#### Slice 1 - Walking Skeleton
- <the thinnest end-to-end path a real user could complete>
- Stories: <US-1, US-4, US-7 - note these span the whole backbone, not one activity>

#### Slice 2
- <what this slice adds, and for whom>
- Stories: <ids>

#### Slice 3
- <what this slice adds>
- Stories: <ids>

### Out of the Map
- <activity or step deliberately excluded, and why>

### Assumptions to Validate
- <Assumption 1>
- <Assumption 2>
```

**Sticky-Note Rule** applies to map items: 4-8 words, ASCII only, no emoji.

---

## 3. Split-signal report

Emit this instead of a widened story when the rule fires.

```markdown
### Split Signal Detected: <ID>

**Why**: <second When, or second Then, quoted>

**Proposed stories:**
1. <US-a> - <summary> - When <trigger a> / Then <outcome a>
2. <US-b> - <summary> - When <trigger b> / Then <outcome b>

**Which ships first, and why**: <the one that completes a thinner end-to-end path>

**Handoff**: run `epic-breakdown-advisor` for the full pattern evaluation.
```

---

## Provenance

Adapted from `prompts/user-story-prompt-template.md` and
`prompts/user-story-mapping.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0.
