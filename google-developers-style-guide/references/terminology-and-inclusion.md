# Terminology, inclusion, and global-audience rules

Use this reference when naming choices, inclusivity, localization, or word choice need closer review.

## Terminology hierarchy

1. Follow explicit project/product terminology when it is intentional and clear.
2. Follow established usage in the relevant domain.
3. Prefer the clearest common term for the target audience.
4. When no project convention exists, use standard US English spelling and dictionary usage.
5. Deviate from a mechanical rule if the alternative is clearly better for readers; remain consistent after choosing.

## Consistency

- Use one term for one concept unless a distinction is meaningful.
- Do not swap synonyms merely to make prose sound varied.
- Keep capitalization, hyphenation, and abbreviation treatment consistent.
- Preserve exact product, feature, API, code, and UI names.

## Jargon and abbreviations

- Avoid jargon that is unnecessary for the audience.
- Use a domain term when it is more precise than a plain-language substitute and the reader is likely to know it.
- If a necessary term may be unfamiliar, define it briefly on first use or link to a definition.
- Avoid internet slang and niche abbreviations in general documentation.
- Prefer specific verbs and nouns over overloaded business or technical buzzwords.

## Global audience

- Use clear, concise, literal language.
- Prefer short sentences and familiar words.
- Avoid idioms, puns, jokes, slang, pop-culture references, sports metaphors, and culture-specific shorthand.
- Avoid phrasal verbs when a simple verb is clearer; keep established technical phrases such as "log in" when they are the standard term.
- Use words in their primary/common sense.
- Keep modifier chains short.
- Use articles, relative pronouns, and helper words when they aid parsing or translation.
- Avoid references to seasons for dates or schedules intended for a global audience.
- Use diverse, non-stereotypical example names and locations.
- Do not put essential translatable text only inside images.

## Inclusive language

- Use gender-neutral role nouns and singular "they" when gender is unknown or irrelevant.
- Avoid language that assumes a default gender, culture, nationality, family structure, ability, or life experience.
- Avoid ableist words used as metaphors for failure, irrationality, or poor quality.
- Avoid graphic or violent metaphors when a neutral technical description works.
- Avoid collective labels that remove personhood, such as "the disabled".
- When writing about disability, research and respect the terminology preferred by the community or individual; preferences may differ between person-first and identity-first language.
- Avoid euphemistic or patronizing labels for disability.
- Avoid describing nondisabled people as "normal" or "healthy" by contrast.
- Avoid non-inclusive technical pairs such as `master/slave` or `blacklist/whitelist` when a precise alternative such as `primary/replica` or `allowlist/denylist` fits.
- Do not mechanically replace a legacy term if doing so changes technical meaning; choose a domain-accurate replacement.
- If compatibility requires a legacy term, mention it once as an alias and use the preferred term afterward.

## Names and examples

- Never invent realistic PII that could belong to a real person.
- Use reserved example domains such as `example.com`, `example.org`, and `example.net` for generic internet examples.
- Use documentation-reserved IP ranges for example IP addresses when relevant.
- Use descriptive project and resource names rather than meaningless placeholders when the name itself teaches something.
- Keep examples diverse without calling attention to diversity as a performance.

## Product and trademark names

- Preserve official spelling and capitalization.
- Do not use trademarks or product names as generic verbs.
- Avoid pluralizing or making possessives from trademarks when a rewrite is easy.
- Feature names are often ordinary lowercase terms unless the official UI/product convention says otherwise.

## Anthropomorphism

Avoid language that assigns human intent, perception, or emotion to software when direct behavior is clearer.

Prefer:

- "The service rejects the request."
- "The client detects the device."
- "The object specifies the delimiter."

Over:

- "The service doesn't like the request."
- "The client sees the device."
- "The object tells the parser what to do."

Natural shorthand is acceptable when no ambiguity is introduced, but behavior should remain technically accurate.

## Claims and hype

Avoid claims that are subjective, unverifiable, or likely to age badly:

- best
- fastest
- cheapest
- perfectly secure
- guaranteed
- ensures
- always, when exceptions exist

Prefer measurable or scoped claims. Cite a source when a performance or benchmark claim matters.

Do not disparage competing products. Describe relevant differences factually.

## Timeless terminology

Avoid vague time markers such as "new", "latest", "currently", and "soon" when they are not tied to a date or release. Prefer the present product state or an explicit version/date reference.
