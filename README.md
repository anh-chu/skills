# skills

A small collection of portable, agent-agnostic [Agent Skills](https://code.claude.com/docs/en/skills).
Each skill is a self-contained folder with a `SKILL.md`. They avoid hardcoded identities,
org-specific IDs, and specific tool names so any agent with comparable integrations can use them.

## Skills

| Skill | What it does |
|-------|--------------|
| [`release-kit`](release-kit/) | Create a polished, on-brand, print-ready release/launch kit (paged HTML → PDF) for a product change, feature launch, or GA. |
| [`gtm-update`](gtm-update/) | Gather and synthesize the week's customer / GTM updates from email, chat, and calendar into a dated, paste-ready section. |
| [`prd`](prd/) | Turn a chat discussion plus supporting context into a comprehensive, implementable PRD, then optionally publish it to a wiki. |
| [`google-developers-style-guide`](google-developers-style-guide/) | Make agent writing clear, precise, and structured across both chat responses and files the agent writes or edits. Ships an on-demand skill and an always-on `AGENTS.md`. |

## Install

Clone into your agent's skills directory (for Claude Code, `~/.claude/skills/`):

```bash
git clone https://github.com/anh-chu/skills.git
# then symlink or copy individual skill folders into ~/.claude/skills/
```

Or copy a single skill folder wherever your agent loads skills from.

## Conventions

- Every skill has a `SKILL.md` with `name` + `description` frontmatter.
- Skills are tool-agnostic: they describe capabilities (email, chat, wiki, issue tracker)
  rather than requiring a specific MCP server.
- Skills confirm any needed configuration (products, destinations, identities) at runtime
  instead of baking it in.
