# Skill Authoring Conventions

Every skill in this plugin is written to one shared architecture. This file is
the contract. Read it before editing any `SKILL.md`, `template.md`, or example.

The conventions are adapted from Dean Peters' prompt methodology in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
(CC BY-NC-SA 4.0) — specifically `prompting-style-guide.md`,
`generative-guidance-pattern.md`, `interaction-modes.md`, and
`SUBMISSIONS-GUIDE.md`. See [ATTRIBUTION.md](ATTRIBUTION.md).

---

## 1. Why the conventions exist

A skill has two jobs, and a skill that does only the first one is a bad skill:

1. **Execute the PM task** — produce an artifact good enough to put in front of
   a stakeholder.
2. **Teach the method** — the person reading the output should come away better
   at the framework than when they started.

When the two conflict, prefer clarity and pedagogy over cleverness.

---

## 2. File layout per skill

```
skills/<skill-name>/
  SKILL.md      # the instruction set the model reads
  template.md   # the stable output contract (the schema)
  examples/     # at least one end-to-end worked example
```

`SKILL.md` tells the model *how to behave*. `template.md` tells it *what to
emit*. `examples/` shows *what good looks like* — including the conversation,
not just the artifact. Never inline a large template into `SKILL.md`; point at
`template.md` so the schema has exactly one home.

---

## 3. The Five-Block structure

Every `SKILL.md` body follows this order:

| Block | Answers | Contains |
|---|---|---|
| **Context** | Who is the model right now? | Role, expertise framing, what this is *not* |
| **Instruction** | How does it behave? | Interaction mode, required context keys, missing-context rule, the method itself |
| **Parameter** | What varies? | Inputs, options, knobs, defaults |
| **Output** | What gets emitted? | Pointer to `template.md`, format rules |
| **Validation** | How do we know it is good? | Quality gates, do-not-invent list, pitfalls, Final Step |

A hidden-curriculum HTML comment sits above the body, holding the pedagogic
notes, interaction mode, and attribution. It is invisible in rendered output but
teaches whoever opens the file.

---

## 4. Interaction modes — declare exactly one

Modes differ on one axis: **where does the context come from?**

| Mode | Context source | Human's role |
|---|---|---|
| **Facilitation** (Generative Guidance) | The human | Answers narrowing questions |
| **Checkpointed co-construction** | An artifact or template | Gates each section |
| **Autonomous investigation** | The world (search, filings, data) | Sets defaults, reviews evidence |

**The burden-shifting test:** if the model could answer its own intake
questions with a web search, facilitation is the wrong mode. Asking a user to
recite public facts is offloading work onto them. Use investigation.

A skill may borrow moves from another mode. It still declares one primary mode,
because the mode decides the defaults: who asks, who waits, and what happens
when nobody answers.

---

## 5. Generative Guidance v2 (for facilitation skills)

The loop, in full:

1. **Derive questions from the deliverable.** List what the artifact needs,
   order broadest-context to finest-detail, set a budget of 3-5.
2. **One question at a time.** Never stack. Never show the whole list.
3. **Three context-aware options plus Other.** Options 1-3 must each contain at
   least one specific detail from a prior answer. If an option could have been
   written before the conversation started, it is not good enough.
4. **Two standing bypasses, announced once and honored always:**
   - *"Take your best guess"* — the model answers, names the assumption, moves on.
   - *Bulk drop* — the user pastes notes or points at a document; the model reads
     it, reports found / inferred / still-missing, and asks only about real gaps.
5. **Loop-control verbs at any turn:** skip, go back, stop early.
6. **Acknowledge in one sentence, then advance.** Not a paragraph. Not a recap.
7. **Search when options would be generic.** Say that you are searching and why.
8. **Sharpen every turn.** By question 3 the options should be ones you could
   not have offered at question 1.
9. **Withhold the artifact until the loop closes.** Then summarize known /
   assumed / open, confirm, and only then build.
10. **Collapse on arrival context.** A user who arrives with a brief should not
    be interviewed. The scaffold is for thin context, not a ritual.

The canonical question shape:

```
[Question N of B: short title]

[One question about the next real decision, plus one sentence on why it matters.]

1. [Context-aware recommendation] - [why this one]
2. [Context-aware alternative] - [tradeoff]
3. [Context-aware alternative] - [tradeoff]
4. Other - type your own, or combine numbers with commentary.

At any point: say "take your best guess," or drop in your notes to skip ahead.
You can also skip, go back, or say "that's enough, build it."
```

---

## 6. Context intake rules (all modes)

- **Required Context Keys.** Every skill names the 3-5 facts it cannot work
  without.
- **Missing Context Rule.** If keys are missing, ask **at most 3** targeted
  questions, one at a time, then proceed with **clearly labeled assumptions**.
  Never stall, never silently invent.
- **Artifact-First Context Intake (AFCI).** Look in the session, the attached
  files, and prior phase artifacts *before* asking a human anything.
- **Workload inversion.** Do not make the user pre-design the artifact. Ask for
  minimum viable context, then propose 3 candidate shapes with a recommendation.
- **Persona-first framing.** Phrase options in the user's world first; add the
  business translation second.

---

## 7. Output rules

- **Template stability.** Output schemas are contracts, not styling. Teams
  export these into Jira, ADO, and Linear. Improve the intake and the
  facilitation freely; change a template section only as a **labeled new
  version** with a migration note. Never silently rename a section.
- **Sticky-Note Rule.** Bullets in canvas-style output are 4-8 words, ASCII
  only, no emoji. A sticky note that needs a paragraph is two sticky notes.
- **Evidence labels.** Mark material claims **Fact** (sourced), **Inference**
  (evidence-based reading), or **Assumption** (working guess). Short labels.
- **Assumptions to Validate.** Every artifact closes with this section. This is
  what keeps outputs honest and teaches the reader to separate evidence from
  inference.
- **Do-not-invent list.** Name where *this domain's* hallucinations live —
  competitor pricing, user quotes, market share, approvals, commitments.
  Generic "don't fabricate" is weaker than a specific list.

---

## 8. The Final Step contract

Every skill closes with exactly four numbered next options, recommended first:

```markdown
## Final Step

1. [Most useful next action] (Recommended)
2. [Second option]
3. [Third option]
4. [Fourth option]

Reply with `1`, `2`, `3`, `4`, a combination like `1 and 3`, or your own path.
```

Four, not three and not six. A consistent close means the user always knows the
conversation has somewhere to go, and never has to invent the next move.

---

## 9. Humans stay the decision owners

The model proposes, drafts, researches, and challenges. It does not approve,
commit, estimate on engineering's behalf, or decide. Any skill that writes to a
board, tracker, or shared doc asks first and shows what it is about to write.

---

## 10. Authoring checklist

Before committing a change to any skill:

- [ ] Frontmatter has `name` and a `description` that states **what it does**
      and **when to use it** — the description is the trigger surface.
- [ ] Hidden-curriculum comment present: pedagogic notes, mode, attribution.
- [ ] Five blocks present and in order.
- [ ] Exactly one interaction mode declared, and it passes the burden-shifting test.
- [ ] Required Context Keys and Missing Context Rule present.
- [ ] `template.md` exists and `SKILL.md` points to it rather than duplicating it.
- [ ] At least one example in `examples/` showing conversation **and** artifact.
- [ ] Do-not-invent list is domain-specific.
- [ ] Artifact closes with Assumptions to Validate.
- [ ] Final Step block has exactly 4 options, recommended first.
- [ ] Provenance and licence line present.
- [ ] `python3 scripts/validate_skills.py <skill-name>` passes. It catches the
      mechanical half of this list; the rest is on you. See section 11.

The script is a floor, not a ceiling. A skill can pass every check and still be
a bad skill.

---

## 11. The validation script

`scripts/validate_skills.py` enforces the part of section 10 that a script can
honestly verify. No dependencies, Python 3.9 or later.

```
python3 scripts/validate_skills.py             # every skill
python3 scripts/validate_skills.py --quiet      # errors only, no warnings
python3 scripts/validate_skills.py user-story   # one or more named skills
```

Exit code is 0 when everything passes and 1 otherwise, so it works unchanged as
a pre-commit hook or a CI step.

### What it checks

Errors - these fail the run:

- Frontmatter is delimited by `---`, has a `name` that matches the directory
  name, and a `description` between 120 and 1100 characters.
- A hidden-curriculum HTML comment exists after the frontmatter and contains
  Hidden Curriculum, Interaction Mode, and Attribution headings.
- Exactly one interaction mode is recognised in that comment. If more than one
  is named, the comment must mark one `Primary:`.
- The eight top-level headings are present and in order: Context Block,
  Instruction Block, Parameter Block, Output Block, Validation Block, Final
  Step, Examples, Provenance.
- The required subheadings exist: Required Context Keys, Missing Context Rule,
  Quality gates, Do not invent, Common pitfalls, Assumptions to Validate.
- Final Step has exactly four options numbered 1 to 4, the first marked
  `(Recommended)`, closing with the standard reply line.
- The Output Block mentions `template.md`.
- `template.md` exists, is at least 40 lines, has a fenced schema block, and has
  a Provenance section.
- `examples/` exists and holds at least one markdown file.
- No emoji anywhere in `SKILL.md`.

Warnings - these print with a `~` and do not fail the run:

- Non-ASCII characters outside a small allowed set.
- `SKILL.md` under 120 lines (probably still a stub) or over 320 lines
  (probably hoarding detail that belongs in `template.md`).
- An example under 60 lines, or an example with no sign of the conversation -
  only the finished artifact.
- `template.md` that never mentions Assumptions to Validate.

### What it cannot check

Everything that matters most:

- Whether the do-not-invent list is genuinely domain-specific, or a generic
  "do not fabricate" wearing a hat.
- Whether the declared interaction mode is the *right* one - the
  burden-shifting test in section 4 is a judgement call.
- Whether the facilitation options sharpen turn over turn, or could all have
  been written before the conversation started.
- Whether the worked example teaches the method or merely demonstrates the
  output format.
- Whether a template change is a labelled new version with a migration note, or
  a silent rename.

Run the script, then run the checklist. Passing the script means the skill is
shaped correctly. Only a reader can tell you it is any good.
