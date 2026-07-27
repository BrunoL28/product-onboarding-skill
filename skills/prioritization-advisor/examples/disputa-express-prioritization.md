# Prioritization - Worked Example

Q3 planning for Aurora Bank's *Disputa Express*, the in-app card dispute journey.
Aurora Bank is fictional and **every figure below is invented**.

Two things are worth studying: the **framework selection**, where the team's
habitual choice was rejected out loud with a reason, and the **Confidence
column**, where the top-ranked item lost three places once scores met evidence.

---

## The candidate list

Seven items competing for one squad, one quarter.

| ID | Item |
|---|---|
| DE-1 | Open a dispute from the transaction row, in app |
| DE-2 | Dispute status in plain language, on demand |
| DE-3 | Push notification when dispute state changes |
| DE-4 | Upload evidence (receipt, police report) in app |
| DE-5 | Provisional credit within 48h |
| DE-6 | Guided reason-selection wizard |
| DE-7 | Re-platform the back-office dispute queue |

---

## Choosing the framework

**Agent:**

> Before scoring, three candidates. Aurora is instrumented (ops case counts,
> Genesys call logs), the items are mostly comparable in size, and the audience is
> a quarterly planning review, which puts you in the growth-stage row.
>
> 1. **RICE** - you can source real Reach from dispute volume, and seven
>    comparable items is exactly its range. It will hide wishful thinking in
>    Confidence, so we guard that column.
> 2. **WSJF** - fits DE-7 and DE-5, which are large and economic. But engineering
>    has not sized DE-7, and WSJF without an honest Job Size just ranks whoever
>    argued hardest. Not yet.
> 3. **MoSCoW** - fits if the quarter has a fixed external date. Does it?
>
> I recommend 1, with WSJF held back as a cross-check on DE-7 once it has a size.
> Which do we run?

**User:** RICE. We ran MoSCoW in Q2 and 11 of 13 items came out Must, so nobody
believes it any more. No fixed date this quarter.

**Agent:** That is the MoSCoW failure mode exactly - everything-is-Must unless
Must is capped at 60% of effort. Recording the rejection and its reason.

```markdown
## Framework Selection
- **Chosen**: RICE
- **Because**: instrumented product, seven comparable items, quarterly planning
  audience that wants a defensible order rather than an economic case
- **Selection-table row**: growth stage, analytics available
- **Constraint allocated**: one squad, one quarter (approx. 26 person-weeks)

### Rejected candidates
| Framework | Why not, this time |
|---|---|
| WSJF | DE-7 has no engineering Job Size; the denominator would be invented |
| MoSCoW | Q2 run produced 11 Musts of 13 items; no fixed date forces the trade |

### Failure mode we are guarding against
- **This framework hides**: wishful thinking in the Confidence column
- **Guarded by**: the engineering lead, who challenges any Confidence above 70%
- **Cross-check**: WSJF over DE-5 and DE-7 once engineering sizes them
```

---

## First pass, and the Confidence challenge

The team's first pass put Confidence at 100% on every row. Ranking:

| Rank | ID | RICE |
|---|---|---|
| 1= | DE-2 | 3680 |
| 1= | DE-6 | 3680 |
| 3 | DE-1 | 3450 |
| 4 | DE-5 | 2760 |
| 5 | DE-3 | 2300 |
| 6 | DE-4 | 1133 |

**Agent:** Confidence is 100% on all six. A column with one value in every cell
has left the formula. Take DE-6, the reason wizard: what tells you a guided wizard
raises dispute quality rather than abandonment?

**User:** It worked at my last company.

**Agent:** Different product, different population, unmeasured here. That is a
50%, and Impact is 1 not 2 until someone names the metric it moves. Same question
for DE-3, which depends on an unresolved back-office event spike.

**User:** Fair. DE-3 is a coin flip until the spike lands.

---

## Input ledger (excerpt)

```markdown
| Item | Field | Value | Evidence | Label |
|---|---|---|---|---|
| DE-1 | Reach | 9,200 disputers / quarter | Ops case export, Q2 | Fact |
| DE-1 | Impact | 3 | Whole journey moves from phone to app | Inference |
| DE-1 | Confidence | 80% | Comparable in-app flow shipped for card block | Fact |
| DE-1 | Effort | 8 person-weeks | Engineering lead, planning session | Fact |
| DE-4 | Reach | 3,400 / quarter | 37% of Q2 cases attached evidence | Inference |
| DE-5 | Confidence | 30% | Treasury and risk have not agreed the policy | Assumption |
| DE-6 | Confidence | 50% | Analogy to a different product, unmeasured | Assumption |
| DE-7 | Effort | (blank) | No engineering size exists | insufficient evidence |
```

DE-7 is listed, flagged, and left out of the ranking. A blank score is honest; an
invented 12 person-weeks would have placed it wherever its sponsor needed it.

---

## Scored ranking, after evidence

```markdown
| Rank | ID | Item | Reach | Impact | Conf | Effort | RICE | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | DE-2 | Status in plain language | 9,200 | 2 | 80% | 5 | 2944 | |
| 2 | DE-1 | Open dispute in app | 9,200 | 3 | 80% | 8 | 2760 | blocks DE-2 |
| 3 | DE-3 | Push on state change | 9,200 | 1 | 50% | 4 | 1150 | spike open |
| 4 | DE-6 | Reason wizard | 9,200 | 1 | 50% | 5 | 920 | |
| 5 | DE-5 | Provisional credit 48h | 9,200 | 3 | 30% | 10 | 828 | policy, promised |
| 6 | DE-4 | Evidence upload | 3,400 | 2 | 70% | 6 | 793 | |
| - | DE-7 | Back-office re-platform | - | - | - | - | - | insufficient evidence |
```

DE-6 fell from joint first to fourth on one honest Confidence score and one
honest Impact score. Nothing about the item changed.

---

## Sensitivity

```markdown
## Sensitivity
- **DE-1 overtakes DE-2** if DE-1's Effort comes in at 7.5 person-weeks instead of
  8, or if its Confidence rises from 80% to 86%.
- **DE-3 overtakes DE-6** already, but the gap closes to nothing if the spike
  fails and DE-3's Confidence drops to 40%.
- **DE-5 moves to rank 2** if treasury agrees the policy and Confidence goes to
  70% (score 1932).

**Verdict**: the top two are a tie at this resolution - a half-week of estimate
revision swaps them. Sequence by dependency, not by score: **DE-1 ships first
because DE-2 cannot exist without it.**

**Go measure this first**: the DE-3 spike. It is the only open question that
moves an item more than one rank.

## Assumptions to Validate
- DE-6 Impact 1 and Confidence 50%: no measurement of wizard effect on this
  population. A five-user test would settle it.
- DE-4 Reach: 37% evidence-attachment rate is a Q2 sample, not a full year.
- DE-5 Effort of 10 person-weeks assumes no core banking change. Unconfirmed.
- Framework choice: if DE-7 gets sized before the review, WSJF becomes the better
  frame for the DE-5 / DE-7 pair.
```

---

## Export CSV (excerpt)

```csv
Rank,ID,Item,Framework,Score,Field1,Field2,Field3,Field4,Evidence Level,Flags,Sensitivity Note
1,DE-2,"Status in plain language",RICE,2944,9200,2,0.8,5,Inference,,"Loses rank 1 if DE-1 effort is 7.5pw"
2,DE-1,"Open dispute in app",RICE,2760,9200,3,0.8,8,Fact,"blocks DE-2","Ships first regardless of rank"
,DE-7,"Back-office re-platform",RICE,,,,,,Assumption,"insufficient evidence","Not scored - no job size"
```

---

## What this example is meant to teach

1. **The framework choice is the decision.** MoSCoW was rejected on evidence from
   the team's own Q2, in writing, so Q4 need not re-argue it.
2. **A constant Confidence column is a missing Confidence column.** All-100% does
   not mean high confidence, it means the field was never filled in.
3. **One honest score reordered the quarter.** DE-6 went from joint first to
   fourth without anyone changing their mind about whether it was a good idea.
4. **Rank is not sequence.** DE-2 ranks first and ships second, because DE-1 is
   the thing that creates the dispute DE-2 displays.
5. **An unscored row is a legitimate output.** DE-7 stays visible and names the
   condition - an engineering Job Size - under which it re-enters the comparison.

---

## Provenance

Original work, MIT, by the plugin maintainer. RICE is Intercom's; MoSCoW is Dai
Clegg's (DSDM); WSJF is SAFe's, after Don Reinertsen. Aurora Bank and Disputa
Express are fictional; every number here was invented for the example.
