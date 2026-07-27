# Prioritization - Output Templates

Five schemas: framework selection record, input ledger, scored ranking,
sensitivity note plus Assumptions to Validate, and the flat CSV. The **selection
record is not optional**: a rank without the framework rationale beside it is an
opinion with arithmetic on top. Column orders in sections 3 and 5 are a stability
contract - teams build spreadsheet formulas against them.

---

## 1. Framework selection record

```markdown
## Framework Selection
- **Chosen**: <RICE | ICE | Value vs Effort | Kano | MoSCoW | WSJF | Opportunity Scoring>
- **Because**: <one sentence tying stage, data availability, and audience>
- **Selection-table row**: <the row that matched>
- **Constraint allocated**: <one sprint | one quarter | one team | fixed date>

### Rejected candidates
| Framework | Why not, this time |
|---|---|
| <name> | <what it needed that we lack, or what it would hide> |

### Failure mode we are guarding against
- **This framework hides**: <its characteristic failure mode>
- **Guarded by**: <who owns challenging it in this session>
- **Cross-check**: <secondary framework over the top 3, or "none">
```

---

## 2. Input ledger

One row per item per scored field, every cell labelled.

```markdown
| Item | Field | Value | Evidence | Label |
|---|---|---|---|---|
| <ID> | Reach | <number + period> | <query, ticket count, analytics view> | Fact |
| <ID> | Impact | <scale value> | <comparable shipped, research finding> | Inference |
| <ID> | Confidence | <percent> | <what backs it> | Assumption |
| <ID> | Effort | <person-weeks or t-shirt> | <who gave it, when> | Fact |
```

Rules:

- **Reach** states a number **and a period**. A bare number is unusable next quarter.
- **Effort** records who supplied it. If nobody did, leave it blank, mark the item
  *insufficient evidence*, and do not score it.
- **Confidence** above 80% needs a shipped comparable or research in Evidence.
- Two or more Assumption labels in scoring fields flags the row.

---

## 3. Scored ranking

Use the column set for the chosen framework; do not mix.

```markdown
### RICE

| Rank | ID | Item | Reach | Impact | Confidence | Effort | RICE | Flags |
|---|---|---|---|---|---|---|---|---|

### ICE

| Rank | ID | Item | Impact | Confidence | Ease | ICE | Flags |
|---|---|---|---|---|---|---|---|

### WSJF

| Rank | ID | Item | Business Value | Time Criticality | Risk/Opportunity | CoD | Job Size | WSJF | Flags |
|---|---|---|---|---|---|---|---|---|---|

### MoSCoW

| Bucket | ID | Item | Effort | % of total effort | Rationale |
|---|---|---|---|---|---|
| Must | | | | | |
| Should | | | | | |
| Could | | | | | |
| Won't this time | | | | | |

**Must total**: <n>% of available effort. Cap 60%. Over it, prioritization has
not happened yet.

### Kano

| ID | Item | Functional answer | Dysfunctional answer | Category | n responses |
|---|---|---|---|---|---|

Categories: must-be / performance / attractive / indifferent / reverse. No
response count means it is not a Kano result.

### Opportunity Scoring

| ID | Outcome statement | Importance | Satisfaction | Opportunity | Flags |
|---|---|---|---|---|---|

Rows are **outcomes**, never feature names.

### Value vs Effort

| Quadrant | Items | Note |
|---|---|---|
| High value / low effort | | |
| High value / high effort | | |
| Low value / any effort | | |
```

`Flags` carries `insufficient evidence`, `promised`, `compliance`, `dependency`.

---

## 4. Sensitivity note and Assumptions to Validate

```markdown
## Sensitivity
- **<ID-B> overtakes <ID-A>** if <field> moves from <x> to <y>.
- **<ID-A> falls below <ID-C>** if <field> is <threshold> instead of <current>.

**Verdict**: <"the top three survive any single plausible input change" | "the top
three are a tie at this resolution; sequence by dependency and risk, not by score">

**Go measure this first**: <the one input whose uncertainty costs the most>

## Assumptions to Validate
- <every input cell labelled Assumption, with the item it belongs to>
- <the framework choice, if the team sat between two selection-table rows>
- <any Reach figure taken from a proxy rather than the real population>
```

Both blocks travel together: sensitivity says what could change the answer,
assumptions say what was never known.

---

## 5. Export CSV

Column order is a hard contract.

```csv
Rank,ID,Item,Framework,Score,Field1,Field2,Field3,Field4,Evidence Level,Flags,Sensitivity Note
```

- `Field1-4` hold the framework's own inputs in the order shown in section 3.
- `Evidence Level` is the weakest label on that row: Fact, Inference, or Assumption.
- `Score` is blank for unscored items - blank is honest, guessed is not. Quote any
  field containing a comma.

---

## Provenance

Original work, MIT, by the plugin maintainer. Schema conventions follow
`CONVENTIONS.md` section 7. Frameworks belong to their authors: RICE (Intercom),
ICE (Sean Ellis), Kano (Noriaki Kano), MoSCoW (Dai Clegg, DSDM), WSJF (SAFe,
after Don Reinertsen), Opportunity Scoring (Anthony Ulwick).
