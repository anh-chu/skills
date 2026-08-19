---
name: gtm-update
description: >-
  Gather and synthesize customer / go-to-market (GTM) updates from the past week across
  your email, chat (e.g. Slack), and calendar, then format them as a dated GTM section
  ready to paste into a recurring meeting-notes or working-session doc (e.g. a wiki or
  Confluence page). Use when the user asks for a "GTM update", "weekly customer roundup",
  "customer update digest", "GTM section for the working session", or "what happened with
  customers this week".
---

# GTM Update

Produce a concise, dated GTM section summarizing the week's customer-facing activity, pulled
from the user's own connected sources, and formatted for a recurring meeting-notes doc.

This skill is tool-agnostic: use whatever email, chat, calendar, and docs/wiki integrations
the running agent has. The MCP/tool names below are examples — substitute your own.

## Before you start — confirm configuration

Ask the user (or accept as arguments) for anything not already known:

- **Products / topics to track** — the product names or keywords that define "relevant"
  (e.g. the product line, key initiatives).
- **Destination doc** — where the GTM section will eventually go (a wiki/Confluence page URL
  or ID, or "just give me the draft"). Only needed if they want you to publish.
- **Lookback window** — defaults to the last 7 days.
- **Sources available** — which of email, chat, and calendar the agent can search.

Do not hardcode customer names, stakeholders, space IDs, or cloud IDs — read them from the
user's config or discover them from the sources.

## Steps

### 1. Determine the date range
- End date = today.
- Start date = lookback window (default 7 days ago).
- If a destination doc is provided, glance at the most recent entry's date to avoid
  duplicating what's already captured.

### 2. Search all available sources in parallel

**Email** — search for the tracked product/topic terms since the start date.
- Focus on: customer emails, call recordings/summaries, POC threads, migration requests,
  integration questions, deal-related threads.
- Ignore: automated ticket notifications, code-review/PR notifications, digest emails.

**Chat (Slack or similar)** — search public + private channels for the tracked terms since
the start date, plus a deal-focused query (e.g. `<product> customer deal after:<date>`).
- Focus on: customer-facing channels, GTM/sales channels, product-GTM threads.
- Read thread replies for full context.
- Note key customer names, blockers, decisions, and next steps.

**Calendar** — look for events in the window tagged with the tracked products or customer
names (QBRs, POC syncs, escalation calls).

### 3. Learn the target format
If a destination doc is provided, read it to match its existing GTM format. A common shape:
- A **date header** (e.g. `2/26/2026`)
- A `# GTM` heading
- A **customer table** with columns: `Customer | Issues | Expected timeline | Teams`
  - Each `Issues` cell: a brief problem statement, the impact on the deal/adoption, then
    `→` followed by next steps or proposed resolution.
- Language is concise, direct, factual — no filler.

If no destination is given, use exactly this format for the draft.

### 4. Output the formatted GTM section
Produce a ready-to-paste section with:
- Today's date as the section header.
- A customer table populated with every relevant update from the window.
- Each row following the format above.
- The `Teams` column filled where identifiable.

### 5. Offer to publish
After presenting the draft, ask: "Should I add this to the working-session doc?"
- If yes and a destination is configured: prepend the new GTM section to the top of the
  page, preserving all existing content below.
- Never publish without explicit confirmation.

## Principles
- **Only report what you actually found** — never fabricate customer activity.
- **Attribute** decisions and next steps to the people/threads they came from.
- **Concise over complete** — a scannable table beats prose.
- **Respect privacy** — this pulls from the user's own inbox and chats; keep the output
  where the user directs it.
