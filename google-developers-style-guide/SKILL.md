---
name: google-developers-style-guide
description: Produce and refine clear, concise, structured, globally understandable writing in both chat responses and files the agent writes or edits (documentation, READMEs, reports, procedures, summaries, UI copy, code comments, commit messages, and explanatory text inside other artifacts). Use whenever an agent drafts, rewrites, summarizes, explains, documents, or edits any output containing prose, headings, labels, instructions, tables, captions, or links. Apply as a quality layer after task-specific requirements; preserve facts, exact names, code, UI labels, and project-specific style, and never override higher-priority safety, legal, format, or user instructions.
---

# Google developers style guide (clear agent writing)

Use this skill as a quality layer for writing the agent produces, in two places:

- **Chat responses** to the user.
- **Files the agent writes or edits** — documentation, READMEs, reports, procedures, code comments, commit messages, and prose inside other artifacts.

Optimize for the reader's task, not for sounding polished. This is a synthesis of the Google developer documentation style guide, adapted for agent output — not a verbatim copy.

## Priority order

Apply guidance in this order:

1. Follow explicit user, project, product, legal, and format requirements.
2. Preserve factual and technical correctness, exact code, names, and UI labels.
3. Make the output easy for the intended reader to understand and act on.
4. Apply this skill's style rules.
5. Prefer internal consistency over mechanically enforcing a rule that harms clarity.

When rules conflict, choose the wording that is clearest for the audience and use it consistently.

## Operating method

Before drafting:

- Identify the reader, their goal, and the decision or action the output should enable.
- Determine the smallest amount of context needed to succeed.
- Separate known facts, reasonable inferences, recommendations, and uncertainty.
- Choose a structure that exposes the important information early.

While drafting:

- Lead with the answer, outcome, recommendation, or critical constraint.
- Use active voice and present tense unless another tense is more accurate.
- Address the reader as "you" when instructions or guidance are directed at them.
- Use imperative verbs for actions: "Open", "Choose", "Run", "Compare".
- Put conditions and goals before the instruction they qualify.
- Keep one main idea per paragraph; prefer short sentences and short paragraphs.
- Use simple, specific words. Define necessary jargon on first use.
- Prefer one recommended path when the task calls for a decision; discuss alternatives only when their trade-offs matter.
- Put caveats next to the claim or action they constrain, not in a distant disclaimer section.
- Preserve useful nuance without burying the main point.

## Structure for scanning

- Use sentence case for headings and titles.
- Make headings descriptive and unique.
- For task headings, prefer a bare infinitive: "Configure authentication".
- For concept headings, prefer a noun phrase: "Authentication options".
- Keep heading hierarchy logical; do not skip levels merely for visual effect.
- Use numbered lists for sequences and priorities.
- Use bullets for unordered collections.
- Keep list items parallel in grammar and level of detail.
- Introduce lists, tables, code samples, and images with enough context to explain why they are present.
- Use tables for genuine multi-column comparison or structured data, not for page layout or simple lists.

## Language quality

- Prefer precise nouns and strong verbs over vague abstractions.
- Avoid filler, throat-clearing, pre-announcements, repeated conclusions, and self-referential commentary.
- Avoid unnecessary intensifiers, superlatives, hype, and claims such as "guaranteed", "best", or "secure" unless demonstrably true in context.
- Avoid "easy", "simple", "quick", and similar judgments about task difficulty.
- Avoid idioms, slang, cliches, figurative language, and culture-specific references when plain language works.
- Avoid anthropomorphism when it obscures the actual actor or behavior.
- Use common contractions when they improve naturalness; avoid obscure or stacked contractions.
- Include articles such as "a", "an", and "the" when standard English requires them.
- Prefer clear repetition over ambiguous pronouns or compressed wording.

## Global, inclusive, and accessible writing

- Write so readers with different levels of English proficiency can understand the text.
- Avoid unnecessary phrasal verbs and words used in unusual senses.
- Keep subjects, verbs, and objects easy to identify.
- Avoid directional references such as "above", "below", "left", or "right" when labels or structural references work.
- Use gender-neutral language and singular "they" when gender is unknown or irrelevant.
- Avoid ableist, dehumanizing, graphic, exclusionary, or culturally loaded terminology.
- Use community-preferred terminology when writing about disability or identity.
- Do not rely on color, position, icons, or images as the only way to convey meaning.
- Write descriptive link text that makes sense out of context; avoid "click here".

## Technical and product text

- Put code, commands, filenames, paths, API identifiers, literal values, and user-entered strings in code font when the output format supports it.
- Put visible UI labels in bold when the output format supports it.
- Preserve the exact spelling and capitalization of code and UI labels.
- Use all-uppercase underscore-delimited placeholders such as `PROJECT_ID` unless the target syntax requires another convention.
- Explain placeholders the first time they appear.
- Make command examples directly usable when possible; omit optional flags that are not needed for the task.
- Introduce code samples with a sentence explaining what the sample does.
- Do not use code identifiers as ordinary English verbs or awkward possessives; rewrite around them.
- For procedures, make each step action-focused and keep optional steps explicitly marked.
- Describe software behavior directly rather than implying intent or emotion.

For detailed technical conventions, read `references/technical-content.md`.

## Claims, time, and uncertainty

- State facts as facts and recommendations as recommendations.
- Do not imply certainty that the evidence does not support.
- Avoid unverifiable performance, security, cost, and quality claims.
- Avoid future promises or undocumented future features.
- Prefer timeless wording. Remove "currently", "new", "latest", "soon", and similar words unless the time reference is essential and anchored to a date or version.
- Use explicit, unambiguous dates when relative dates could confuse readers.

## Formatting defaults

- Use US English spelling and punctuation unless the project requires another locale.
- Use the serial comma.
- Use sentence case rather than title case for general headings.
- Use straight quotation marks in source-like technical text.
- Avoid exclamation marks in technical and reference content.
- Avoid semicolons when two shorter sentences are clearer.
- Use em dashes sparingly for interruption; do not substitute hyphens for em dashes.
- Avoid slashes as a substitute for "and" or "or" unless the slash has a technical meaning or space is constrained.

For detailed grammar, punctuation, numbers, units, dates, lists, tables, and formatting rules, read `references/mechanics.md`.

## Terminology decisions

- Prefer established project terminology when it is clear and intentional.
- Otherwise prefer the most common, precise, inclusive term for the reader's domain.
- Define unfamiliar abbreviations and domain terms on first use unless they are universally familiar to the target audience.
- Do not vary terms merely for stylistic variety; one concept should usually have one name.
- If a legacy or non-inclusive term must be mentioned for compatibility, identify it once and use the preferred term afterward.

For detailed terminology and inclusion guidance, read `references/terminology-and-inclusion.md`.

## Final quality pass

Before returning user-facing output, silently check:

1. Is the main answer or required action visible early?
2. Can a reader tell what is fact, inference, recommendation, and uncertainty?
3. Is every sentence necessary, specific, and unambiguous?
4. Are paragraphs, headings, and lists doing real organizational work?
5. Are terminology, capitalization, formatting, and grammatical structures consistent?
6. Are conditions, prerequisites, risks, and exceptions placed next to the relevant action?
7. Are links, code, UI labels, numbers, dates, units, and examples formatted clearly?
8. Does any wording overclaim, patronize, exclude, depend on culture, or become stale quickly?
9. Can anything be removed without losing meaning or usability? Remove it.

Use `references/core-rules.md` when a longer editing task needs a more complete prose-quality checklist.

## Source and maintenance

This skill is an adaptation and synthesis of the Google developer documentation style guide, not a verbatim copy. For the scanned source inventory and maintenance notes, read `references/google-style-source-map.md`.
