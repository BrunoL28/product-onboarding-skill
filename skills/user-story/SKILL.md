---
name: user-story
description: Create user stories with Mike Cohn format and Gherkin acceptance criteria. Use when turning user needs into development-ready work with clear outcomes and testable conditions.
---

## Purpose
Create clear, concise user stories that combine Mike Cohn's user story format with Gherkin-style acceptance criteria. Translate user needs into actionable work focused on outcomes, with testable success criteria and shared understanding between product and engineering.

This is not a feature spec—it's a conversation starter capturing *who* benefits, *what* they're trying to do, *why* it matters, and *how* you'll know it works.

## The Mike Cohn + Gherkin Format
**Use Case:** As a [persona] / I want to [action] / so that [outcome].
**Acceptance Criteria (Gherkin):** Scenario / Given [context] / (and Given ...) / When [trigger] / Then [expected outcome].

### Rules that matter
- **"As a" specificity:** a concrete persona, not "user".
- **"I want to":** the action/outcome, not the UI widget.
- **"So that":** the real motivation, not a restatement.
- **One When and one Then per story.** Multiple → split the story.
- Acceptance criteria are testable; cover happy path, errors, edge cases; avoid vague words.

### Anti-Patterns
Not a technical task; not a feature list (too big → split); not vague; not a contract.

## Application
1. Gather context: persona, problem, desired outcome, constraints.
2. Write the use case (As a / I want to / so that).
3. Write acceptance criteria (Given/When/Then), one When + one Then.
4. Add a short, value-focused summary title.
5. Validate: read aloud; can QA write test cases?; split if too big; ensure testability.

For a full initiative, assemble stories into an end-to-end **user story map**: a backbone of activities left-to-right, stories beneath each, and horizontal release slices (walking skeleton first).

## Common Pitfalls
1. Technical tasks disguised as stories.
2. "As a user" (too generic).
3. "So that" restates "I want to".
4. Multiple When/Then (split).
5. Untestable acceptance criteria.

### Provenance
Mike Cohn, *User Stories Applied*; Gherkin (Cucumber); INVEST. Adapted from `deanpeters/product-manager-prompts`. Bundled in the product-onboarding plugin.
