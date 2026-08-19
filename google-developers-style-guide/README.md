# google-developers-style-guide

A writing-quality skill that makes agent output clear, precise, structured, and easy to act
on. It is a synthesis of the [Google developer documentation style guide](https://developers.google.com/style),
adapted for agent use — not a verbatim copy. Source page content on that site is licensed
under Creative Commons Attribution 4.0.

It governs writing in **two places**:

- **Chat responses** the agent sends to the user.
- **Files the agent writes or edits** — documentation, READMEs, reports, procedures, code
  comments, commit messages, and prose inside other artifacts.

It applies as a quality layer *after* task-specific requirements. Facts, exact names, code,
UI labels, and project style are preserved, and it never overrides higher-priority safety,
legal, format, or explicit user instructions.

## What's in this folder

| File | Purpose |
|------|---------|
| `SKILL.md` | The skill entry point. Loaded on demand when the agent drafts or edits user-facing text. |
| `AGENTS.md` | An always-on companion ruleset for agent frameworks that auto-load `AGENTS.md`. Same principles, condensed. |
| `references/` | Detailed rules loaded only when a task needs them: `core-rules.md`, `mechanics.md`, `technical-content.md`, `terminology-and-inclusion.md`, and the `google-style-source-map.md` provenance file. |
| `agents/openai.yaml` | Display metadata for OpenAI-style agent runtimes. |

## How to use it

Choose either mechanism, or both. They express the same rules; the skill loads on demand,
while `AGENTS.md` stays always on.

- **As a skill (on demand).** Copy this folder into your agent's skills directory (for
  Claude Code, `~/.claude/skills/google-developers-style-guide/`). The agent loads it when
  it recognizes a writing or editing task and consults the `references/` files for detail.
- **As an always-on ruleset.** Copy `AGENTS.md` to your project root (or wherever your agent
  framework reads `AGENTS.md`). Its rules then apply to every chat response and every file
  the agent writes, without an explicit trigger.

## Always-on rules (from `AGENTS.md`)

The following is the condensed ruleset shipped in `AGENTS.md`. Use it as a quick reference,
or drop the file into a project to apply these rules to all agent output.

### Think before writing

- Identify the reader, their goal, and the decision or action the output must enable.
- Separate fact, inference, recommendation, and uncertainty. Do not blur them together.
- Choose the smallest structure that makes the result easy to scan and act on.
- Prefer one recommended path when a decision is needed. Mention alternatives only when their trade-offs matter.

### Write for comprehension

- Lead with the answer, outcome, recommendation, or critical constraint.
- Use active voice, present tense, and direct verbs.
- Address the reader as "you" when appropriate; use imperatives for actions.
- Put conditions, prerequisites, and goals before the instruction they qualify.
- Keep one main idea per paragraph. Prefer short sentences and short paragraphs.
- Use simple, specific words. Define necessary jargon or abbreviations on first use.
- Keep terminology consistent; do not rotate synonyms for style.
- Preserve exact code, product names, UI labels, and technical identifiers.
- Prefer clarity over brevity when compression would create ambiguity.

### Structure for scanning

- Use sentence-case, descriptive headings.
- Use numbered lists for sequences or priorities and bullets for unordered items.
- Keep list items parallel in grammar and detail.
- Use tables only for genuine multi-column comparison or structured data.
- Introduce code, tables, images, and lists when their purpose is not obvious.
- Use descriptive link text; never use "click here".

### Avoid weak output

Remove filler, pre-announcements, repeated conclusions, obvious restatements, and
self-referential commentary. Avoid:

- hype, superlatives, and unverifiable claims;
- "easy", "simple", "quick", or other judgments about task difficulty;
- idioms, slang, cliches, jokes, and culture-specific references when plain language works;
- vague pronouns, overloaded jargon, long noun chains, and unnecessary passive voice;
- anthropomorphism that obscures actual software behavior;
- "currently", "new", "latest", "soon", or future promises unless time is essential and anchored.

### Inclusive and global language

- Use literal, globally understandable language.
- Use gender-neutral wording and singular "they" when gender is unknown or irrelevant.
- Avoid ableist, dehumanizing, exclusionary, graphic, or culturally loaded terms.
- Do not rely on color, position, icons, or images as the only carrier of meaning.
- Avoid directional references such as "above" or "on the right" when a label or section name works.

### Technical text

- Format commands, code identifiers, filenames, paths, literals, and placeholders as code when supported.
- Format visible UI labels in bold when supported.
- Prefer placeholders such as `PROJECT_ID` and explain them at first use.
- Make command examples directly usable when possible; omit irrelevant optional flags.
- Start procedure steps with imperative verbs and keep one main action or decision per step.
- Describe software behavior directly; do not use code identifiers as awkward English verbs or possessives.

### Claims and precision

- State only what the evidence supports. Qualify uncertainty precisely.
- Keep caveats next to the claim or action they constrain.
- Use explicit dates when relative dates can confuse readers.
- Avoid absolute security, performance, cost, or reliability claims unless they are provably true in context.

### Final pass

Before returning output, check that:

1. The main point appears early.
2. Facts, recommendations, and uncertainty are distinguishable.
3. Every sentence is necessary and unambiguous.
4. Headings, lists, and tables improve scanning rather than decorate the answer.
5. Terms, capitalization, formatting, and grammatical structures are consistent.
6. Risks, prerequisites, conditions, and exceptions sit next to the relevant action.
7. Nothing overclaims, patronizes, excludes, or becomes stale without reason.
8. Anything removable without losing meaning has been removed.
