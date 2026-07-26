# Proto Persona - Output Template

The canonical Proto Persona Canvas. Section names are a stability contract — these
get pasted into design docs, decks, and tickets.

**Evidence tags (required where applicable):**

- `[PLACEHOLDER - NEEDS RESEARCH]` — no evidence exists. Never replace this with
  a plausible invention.
- `[ASSUMPTION - VALIDATE]` — a working guess the team is proceeding on.
- Sourced items name their source: `(support transcript, 2026-06)`.

---

```markdown
## Proto Persona Canvas

> **Status: PROTO.** This is a hypothesis built from limited evidence, not
> validated research. Graduation criteria at the foot of this document.

### Name
* <alliterative, memorable name - e.g. "Cardholder Camila">

### Bio & Demographics
* <behavioural fact that changes a product decision>
* <behavioural fact>
* <demographic detail, only if it changes a decision>
* <channel and device reality - where they actually are>

### Quotes
* "<verbatim quote>" (<source, date>)
* "<verbatim quote>" (<source, date>)
* `[PLACEHOLDER - NEEDS RESEARCH]` - <what you would ask to fill this>

### Pains
* <pain, specific to this product, not generic to the role>
* <pain>
* <pain> `[ASSUMPTION - VALIDATE]`

### What is this Person Trying to Accomplish
* <observable behaviour - what they do today instead>
* <observable behaviour>
* <the outcome they are actually after, not the task>

### Goals
* **Short term:** <what they want this week>
* **Long term:** <what they want this year>
* **Personal:** <what matters to them beyond the transaction>

### Attitudes & Influences
* **Decision Making Authority** - <can this person choose or buy? if unknown, tag it>
* **Decision Influencers** - <who they listen to>
* **Beliefs & Attitudes** - <beliefs that affect adoption, and their source>

### What Would Change Our Mind
* <the finding that would invalidate this persona>

### Graduation Criteria
* Pains, job, and at least two quotes come from primary research, n > 5.
* No `[ASSUMPTION - VALIDATE]` tag remains on a load-bearing claim.
* Until both hold, this stays a proto-persona regardless of polish.

### Assumptions to Validate
- <Assumption 1> - <the research that would settle it>
- <Assumption 2> - <the research that would settle it>
- <Assumption 3> - <the research that would settle it>
```

---

## Anti-persona add-on (when `anti_persona` is on)

Often the sharper scoping tool. Naming who you are not building for kills more
scope creep than any prioritisation framework.

```markdown
## Anti-Persona: <name>

### Who this is
* <one line>

### Why we are not building for them in v1
* <reason, tied to the problem statement>

### What we would have to add if we did
* <capability we are deliberately not building>

### The signal that we should reconsider
* <what would have to be true>
```

---

## Provenance

Adapted from `prompts/proto-persona-profile.md` in
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts)
by Dean Peters, CC BY-NC-SA 4.0. Canvas inspired by the Productside Product
Manager's Playbook.
