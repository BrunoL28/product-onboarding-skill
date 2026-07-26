# Product Onboarding - Worked Example: Aurora Bank "Disputa Express"

A condensed five-phase run. Every figure is invented; the point is the shape of
the conversation, the gates, and how each artifact feeds the next.

**Scenario.** Aurora Bank is a fictional mid-size digital bank. Card fraud
disputes are handled by phone, take 11 days to acknowledge, and generate the
highest call volume of any journey. The proposed product, *Disputa Express*, lets
a cardholder open and track a dispute in-app.

---

## Kickoff

**User:** I need to onboard a new product. We want to let cardholders open fraud
disputes in the app instead of calling. Attaching the support team's Q2 deck.

**Agent:**

> Read the deck first. Here is what I have:
>
> **Found** - dispute volume 4,200/month; 11-day median acknowledgement; disputes
> are 31% of call minutes; the current flow is Genesys plus a manual back-office
> queue.
> **Inferred** - the protagonist is a retail cardholder, not a business customer
> (the deck only breaks out consumer cards).
> **Still missing** - who the primary stakeholder is, and whether the backlog
> should land on a board.
>
> Four questions max, one at a time. At any point say "take your best guess," or
> drop in more notes to skip ahead.
>
> **Question 1 of 4: the protagonist.** The deck splits consumer from business
> cards but not by behaviour. Who is v1 actually for?
>
> 1. **The blindsided first-timer** - never disputed before, does not know the
>    word "chargeback," wants reassurance more than status. Highest call volume.
> 2. **The repeat disputer** - three or more disputes a year, knows the process,
>    wants speed and no re-explaining. Smallest group, loudest complaints.
> 3. **The high-balance saver** - low dispute rate, high churn cost if handled
>    badly. Strategic, but a thin evidence base.
> 4. Other - type your own, or combine numbers.

**User:** 1. Support says most callers have never done it before and just want to
know they are not on the hook for the money.

**Agent:** Noted - v1 is for the first-timer, which makes reassurance a
requirement and not a nice-to-have. *(Questions 2-4 covered stakeholder, board
target, and regulatory constraints. Stakeholder: Head of Cards. Board: Jira.
Constraint: Bacen resolution timelines apply, flagged for legal.)*

> Working folder `./product-onboarding/disputa-express/`, `INDEX.md` written,
> twelve artifacts pending. Starting Phase 1.

---

## Phase 1 - Discovery

**`company-research`** searched Aurora's investor updates and two competitors'
help centres. Key sourced finding: both competitors ship in-app disputes with a
72-hour acknowledgement SLA, published on their help pages. Labelled **Fact**
with URLs. Aurora's own 11 days came from the deck.

**`pestel-analysis`** found one factor that changed the scope: a **Legal** entry
on Bacen's dispute-handling timelines, which turn acknowledgement speed from a
CX nicety into a compliance surface. Two factors were honestly marked low impact
(Environmental, Political) rather than padded.

**`proto-persona`** produced **Cardholder Camila**, 34, Recife, salaried,
banks on mobile only. Her quotes came from three real support transcripts. One
field she wanted - household income - had no evidence, so it shipped as
`[PLACEHOLDER - NEEDS RESEARCH]` instead of a plausible invention.

**`problem-statement`** produced the line the rest of the work hangs on:

> **I am** a cardholder who has just seen a charge I did not make.
> **Trying to** get the money back and stop being liable for it.
> **But** the only way in is a phone queue, and after the call nothing tells me
> anything.
> **Because** the dispute lives in a back-office queue with no customer-facing
> state.
> **Which makes me feel** unprotected by the bank I trusted with my money.

**Gate.** Read back to two cardholders from the support panel. The first said
"unprotected" was too soft - the word she used was *robbed twice*. That went into
the artifact as a real quote. Gate passed.

---

## Phase 2 - Requirements and Scope

**`lean-ux-canvas`** named the riskiest assumption, and it was not the one the
team expected. Not *will people use in-app disputes* - obviously yes. It was:
**will a visible status actually reduce calls, or will people check the app and
call anyway?** Box 8's answer: instrument the existing IVR to ask callers whether
they already checked the app. Two weeks, no build.

**`user-story`** built the map. Backbone: *Notice charge -> Open dispute ->
Submit evidence -> Track status -> Get resolution*. Release slice 1 is the
walking skeleton: open a dispute, see one status, get one notification.

One story failed the split signal test - it had two `When`s - and got split:

> **Given** a dispute is open, **When** the back office changes its state,
> **Then** Camila sees the new state in the app.

**`write-spec`** did the useful, unpopular work of writing non-goals. The loudest:
**no evidence upload in v1.** Support data showed 78% of first-timer disputes
need no document at all, and photo upload was two-thirds of the estimate.

**Gate.** Every P0 challenged out loud. Two demoted to P1. Gate passed.

---

## Phase 3 - PRD

**`prd-development`** consolidated it. Two things worth noting:

The Technical Architecture section explicitly named the system of record: **the
back-office queue remains authoritative; the app is a read model.** Naming it
stopped a real argument two weeks later about where dispute state lived.

And one section stayed deliberately unfinished. Whether Bacen's timeline applies
from customer submission or from bank acknowledgement was an open legal question.
It shipped as an **ADR marked Proposed, not Accepted**, with Legal as owner - not
quietly resolved to make the document look complete.

---

## Phase 4 - Delivery Planning

**`epic-breakdown-advisor`** ran INVEST first. One epic failed *Valuable* - "build
the dispute state API" - and got reframed as the vertical slice it should always
have been: Camila sees one real status change, end to end.

Splitting used **Workflow Steps** for the main flow and **Simple/Complex** for
notifications (push first, email and SMS later). One genuine unknown - whether
the Genesys webhook can even fire on state change - became a two-day **spike**
instead of an estimate someone would have pretended to believe.

Output: 6 epics, 28 stories, `board_import.csv`.

**`roadmap-planning`** sequenced it Now / Next / Later, walking skeleton first,
and mapped each epic to an outcome rather than a feature name.

Before pushing to Jira the agent showed all 28 cards and waited. The user caught
two duplicates first.

---

## Phase 5 - Strategy Session

**`product-strategy-session`** stress-tested the whole chain and found the thing
that mattered: the roadmap optimised for **dispute submission speed**, but the
problem statement was about **liability anxiety**. Those are not the same. A fast
form that still says nothing for eleven days solves the wrong half.

That reordered the roadmap. Status visibility moved ahead of submission polish.

---

## Closing readout (excerpt)

```markdown
## Riskiest assumption
That visible status reduces calls rather than adding a second channel people
check before calling anyway. Test: two-week IVR question, no build required.

## Decisions needing an owner
| Decision | Owner | Needed by | Blocking? |
|---|---|---|---|
| Bacen timeline start point | Legal | before v1 scope lock | Yes |
| Genesys webhook feasibility | Platform | end of spike, week 2 | Yes |
| Evidence upload in v1 or v2 | Head of Cards | v2 planning | No |
```

---

## What this example is meant to teach

1. **The gates earn their cost.** Phase 5 caught a roadmap that solved the wrong
   half of the problem. Nothing earlier in the chain would have.
2. **Placeholders beat plausible inventions.** Camila's income field stayed empty
   and nobody was misled by a number.
3. **Open decisions stay open.** The Bacen ADR shipped as Proposed. A PRD that
   looks finished but is not is worse than one with a visible hole.
4. **Non-goals do the real scoping.** "No evidence upload in v1" removed
   two-thirds of the estimate and cost 22% of cases a slower path.

---

## Provenance

Original example, MIT, Bruno Lima Soares. Aurora Bank, Disputa Express, and
Cardholder Camila are fictional; all figures are invented.
