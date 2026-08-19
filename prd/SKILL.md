---
name: prd
description: >-
  Turn a chat discussion (e.g. a Slack channel or thread), plus supporting context from
  your docs and issue tracker, into a comprehensive, implementable Product Requirement
  Document — then optionally publish it to a wiki/Confluence page. Use when the user asks
  to "write a PRD", "draft a PRD from this Slack thread", "turn this discussion into a
  spec", or "create a product requirements doc".
---

# PRD Builder

Create a comprehensive, implementable PRD from a discussion and its surrounding context,
then publish it on request.

**Input:** a chat channel/thread name, topic, or brief description of what the PRD is about.
May also include a target wiki/Confluence space or parent page.

This skill is tool-agnostic: use whatever chat, docs/wiki, and issue-tracker integrations
the running agent has. Tool names below are examples — substitute your own.

## Before you start — confirm configuration

Ask the user (or accept as arguments) for anything not already known. Do not assume an
identity, org, space, or IDs — these must come from the user or be discovered:

- **Source discussion** — which channel / thread / topic to base the PRD on.
- **Author / owner** — who the PRD is authored on behalf of (for the header table).
- **Destination** — target wiki/Confluence space and parent page (only needed to publish).
- **House style** — any existing PRD template or "launch PRD" to match patterns from.

## Step 1 — Find and read the source discussion
1. If a channel name is given, locate it (include private channels) and read it in full.
2. If a topic/keyword is given, search chat broadly using relevant terms.
3. Read all thread replies to capture the complete discussion.
4. Extract: key participants, the core request/problem, decisions made, disagreements,
   and any referenced documents or tickets.

## Step 2 — Gather supporting context (in parallel)
- **Docs / wiki** — search relevant spaces for related pages using keywords from the
  discussion; read the most relevant (especially any existing template/launch PRD).
- **Issue tracker** — search for related tickets (keywords, relevant project keys); read
  key tickets for description, status, assignee, and comments.
- **Broader chat** — search other channels for prior discussion, architectural context,
  or constraints from key stakeholders.
- **Screenshots / attachments** — analyze any images the user provides for UI context or
  reference designs; if messages reference images you can't see, ask for them.

## Step 3 — Synthesize and draft the PRD
Write the PRD in markdown with these sections:

1. **Header table** — Owner, Stakeholders, Status (Draft), Last Updated, primary ticket,
   related tickets.
2. **Background** — what exists today, why it matters, what triggered the request.
3. **Problem Statement** — 2–3 crisp problems faced today.
4. **Goal** — one-sentence goal + a success-metrics table (3–4 measurable targets).
5. **Approach Decision** — present 2–3 options, recommend one with rationale, referencing
   prior team discussion/decisions.
6. **Scope** — in-scope (table with IDs) and out-of-scope (bullets).
7. **UX Behavior** — at least 3 ASCII mockups: default/initial state, primary interaction,
   and an edge case (error, out-of-scope, or empty state).
8. **Technical Mapping** (if applicable) — how user-facing concepts map to implementation.
9. **Functional Requirements** — tables with ID, Requirement, Priority (P0/P1/P2), grouped
   by area (e.g. Frontend / Backend / Domain).
10. **Open Questions** — table with ID, Question, Owner, Status.
11. **Dependencies** — table with Dependency, Team, Status.
12. **References** — links to every doc, ticket, and discussion consulted.
13. **Changelog** — Date, Version, Author, Changes.

### Writing guidelines
- Concise and implementable — an engineer should be able to build from it.
- Attribute specific prior decisions (e.g. "per <name>'s <date> message").
- Action-oriented requirement language.
- Match any existing house PRD patterns the user pointed you to.
- Prefer user-facing names over internal/technical code names.
- Include enough context that someone not in the original discussion understands the full
  picture.

## Step 4 — Save locally
Save the PRD as a markdown file with a descriptive kebab-case filename (e.g.
`capability-selector-prd.md`) in the user's working directory or a location they specify.

## Step 5 — Summarize before publishing
Present a brief summary and **wait for confirmation**:
```
## PRD Ready: [Title]

**Sections:** [key sections]
**Mockups:** [count] ASCII mockups
**Requirements:** [count] functional requirements
**References:** [count] sources consulted

**Target location:**
- Space: [space]
- Parent: [parent page]

Shall I publish?
```
If the user wants changes, iterate before publishing.

## Step 6 — Publish (after confirmation)
Create the page in the target wiki/Confluence space and parent, using markdown content,
then return the page URL.

**Wiki/Confluence markdown tips:**
- Code blocks with box-drawing characters (┌─┐│└) often render poorly — convert to `+---+`
  ASCII style.
- Standard pipe-syntax tables render well.
- Links to other wiki pages are usually auto-resolved from their URLs.

## Important behaviors
- **Never publish without confirmation** — always show the summary first.
- **Never fabricate context** — only reference materials you actually read.
- **Ask** when you need screenshots, product access, or requirement clarification.
- **Credit sources** — attribute decisions to whoever made them.
- Use the user-specified destination over any default.
- If the source discussion is thin, say so and ask for additional context.
