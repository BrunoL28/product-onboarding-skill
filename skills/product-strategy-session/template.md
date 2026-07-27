# Product Strategy Session - Output Template(s)

One file, `STRATEGY_SESSION.md`: the **session frame**, then the five schemas
this skill exists to produce - **artifact inventory**, **coherence check
report**, **premortem**, **biggest-bet test**, **decision log** - closing with a
sponsor **read-out** assembled from them and **Assumptions to Validate**.

**Stability contract.** Fixed: the decision log's column order, the seven seam
rows, the premortem watchlist. Change one only as a labelled new version with a
migration note; never rename a section, and never delete an empty table - write
`none recorded`, so a reader can tell an unasked question from a skipped one.
Dissent stays in `workshop-facilitation`'s session record, in the dissenter's
words, referenced here by its `X` id. This skill keeps no rival register.

---

## 1. Session frame

```markdown
# <Product> Strategy Session
- **Mode**: closing-session / standalone (Path B phases run: <list>)
- **Date**: <YYYY-MM-DD>  **Timebox**: <planned> / <actual>, inside an
  engagement window of <start> to <end> (ceiling: 4 weeks)
- **Sponsor**: <name, role> - can decide <scope / budget / headcount; none of
  the three makes this a preparation session, declared here>
- **Sponsor has read**: <which artifacts, not "the pack">
- **Decision owner**: <name> - decides when the room does not agree
- **Session record**: <link, if workshop-facilitation ran the room>
- **Premortem horizon**: <12 months / launch + 90 days>

### Participants
| Name | Role | Brings | Present for |
|---|---|---|---|
| <name> | <role> | <the knowledge only they have> | <all / minutes n-m> |

- **Not in the room but affected**: <names - they get the follow-up note>
```

## 2. Artifact inventory

```markdown
## Artifact inventory
| Artifact | Version | Date | Status | Read? | Stale? |
|---|---|---|---|---|---|
| <file> | <n.n> | <date> | draft / agreed / superseded | yes | <older than the decision it supports> |

- **Missing**: <artifact the set should contain, and what its absence costs>
- **Stale**: <artifact older than the decision resting on it>
```

## 3. Coherence check report

```markdown
## Coherence check
| # | Seam | Verdict | Finding |
|---|---|---|---|
| S1 | Positioning vs problem statement | holds / contradiction | <one line, or what was checked to conclude it holds> |
| S2 | Problem statement vs PRD scope | | |
| S3 | PRD metrics vs the stated outcome | | |
| S4 | Roadmap sequence vs riskiest assumption | | |
| S5 | Backlog P0s vs PRD scope and non-goals | | |
| S6 | Open decisions vs committed sequence | | |
| S7 | Evidence base vs the weight on it | | |

### C<n>: <the contradiction, in one line>

- **Side A** - <artifact, section>: "<quote>"
- **Side B** - <artifact, section>: "<quote>"
- **Not a wording problem because**: <what breaks downstream if both stand>
- **Confirmed real by**: <name, in the room>. **Resolved here?**: no -> <log id>
  / yes -> <what changed, in which artifact>
```

Every seam gets a verdict. One the session cannot honestly settle is never
reconciled in prose - it becomes a dated, owned row in the log.

## 4. Premortem

```markdown
## Premortem - <horizon>
### Failure narrative (past tense, 3-5 sentences)
<What failure looked like on the ground. Not "adoption was low".>

### Causes, all five categories
- **Market and customer**: <cause> | <cause>
- **Product and solution**: <cause> | <cause>
- **Organizational and political**: <cause> | <cause>
- **Execution and delivery**: <cause> | <cause>
- **Self-inflicted**: <cause> | <cause>

### Ranked top five, then converted to risks
| # | Assumed cause of death | Category | L x D | Risk, restated | Owner | Early-warning signal | Falsifier | Mitigation |
|---|---|---|---|---|---|---|---|---|
| R1 | <what killed it> | <category> | <H x H> | <the risk we carry> | <named person> | <what we see first> | <metric, threshold, date> | <what we do now> |

### Watchlist - unowned
| Cause | Why unowned | First decision |
|---|---|---|
| <cause> | <nobody in the room can hold it> | who owns this, by <date> |
```

Silent writing first, senior voice last, never "the team" in Owner.

## 5. Biggest-bet test

```markdown
## The biggest bet
- **Named in silence by**: <name: their answer> | <name: their answer>
- **The disagreement itself**: <what the spread tells us>
- **The bet, as tested**: <one sentence>

| # | What would have to be true | Label | If false |
|---|---|---|---|
| B1 | <condition> | Fact / Inference / Assumption | <survivable / kills the bet> |

- **The killing condition**: <B<n>> - this, not the feature, is the bet
- **Sequenced first?**: yes / no - <what sits ahead of it, and why>
- **Cheapest thing that would tell us**: <smallest test, cost, owner, date>
```

## 6. Decision log

**Stability contract.** This is the artifact that leaves the process - teams
diff it across sessions and paste it into trackers. Fixed column order:
`ID, Decision or question, Status, Option chosen, Owner, Date, If the date passes`

```markdown
## Decision log
| ID | Decision or question | Status | Option chosen | Owner | Date | If the date passes |
|---|---|---|---|---|---|---|
| SS-1 | <the open thread, as a question> | open / decided / pending / blocked | <or "none - still open"> | <named person> | <YYYY-MM-DD> | <the default that takes effect, and who is told> |

- **Read back in the room?**: yes / no (corrections: <list>)
- **Carried from the session record**: <X and P ids>
- **Requested but not granted**: <what was asked of the sponsor, and by when>
```

Every open thread from sections 3-5 lands here or it leaks. `pending` means asked
and unanswered, never agreed. A role in Owner is allowed only where the person is
unidentified - then the first decision is **who**.

## 7. Strategy read-out, then Assumptions to Validate

```markdown
## Read-out
- **The contradiction**: <C<n>, one sentence, unresolved>
- **Top three risks**: <R1>, <R2>, <R3> - with owners
- **The bet and its killing condition**: <one sentence>
- **Cheapest next test**: <test, cost, date>
- **What needs approving, by whom, by when**: <the ask, marked pending>

## Assumptions to Validate
- <every biggest-bet condition labelled Assumption, with what settles it>
- <every premortem cause resting on belief rather than evidence>
- <every seam where the evidence is thinner than the weight on it>
- <every log row still open, with the date its answer arrives>
```

## Provenance

Adapted from `prompts/strategic-scrum-team-session-kickoff.md` and
`prompts/premortem-prompt-template.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, **CC BY-NC-SA 4.0**. See [ATTRIBUTION.md](../../ATTRIBUTION.md).
Premortem: Gary Klein, HBR 2007. Session mechanics and the Dissent register come
from `workshop-facilitation`.
