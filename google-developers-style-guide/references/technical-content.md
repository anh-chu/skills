# Technical content rules

Use this reference for developer documentation, procedures, API/reference text, command-line examples, UI instructions, and code-adjacent prose.

## Procedures

- Give prerequisites before the steps they affect.
- Use numbered steps for multi-step procedures; use a bullet for a true single-step procedure.
- Begin each step with an imperative action.
- State context or location before the action when it helps the reader orient themselves.
- Put the goal before the action when the goal determines whether the step applies.
- Keep one main reader decision per step.
- Put the action before its result or justification.
- Mark nonrequired steps with "Optional:".
- Minimize interruptions, cross-links, and alternative branches inside a procedure.
- Prefer the best or simplest path for the target audience. Move materially different alternatives to separate sections when needed.
- Reference a reusable procedure instead of duplicating it.
- Avoid "please" and directional phrases such as "above" and "below".

## Prescriptive language

Use modal verbs precisely:

- `must`: a requirement.
- imperative: a required action in a procedure.
- `can`: an available or optional action, or a possible capability when unambiguous.
- `might`: a possible outcome.
- `We recommend ...` or a direct recommendation: a preferred action.

Avoid `should` when it could mean either requirement or recommendation. If the intended force is obvious and conventional, `should` can be acceptable, but clearer wording is usually better.

## Code in text

Use code font for code-shaped or literal technical items, including:

- commands and command-line tools;
- filenames, extensions, directories, and paths;
- classes, methods, functions, packages, namespaces, constants, and data types;
- environment variables;
- HTTP methods, status codes, content types, and literal request values;
- ports, literal IP addresses used in code/commands, and query parameters;
- literal strings, console output, and user-entered text;
- placeholders.

Do not use code font for product names, organization names, or ordinary prose references to a domain or URL unless the value is being treated as literal input.

Do not pluralize, possess, or verbify code identifiers when rewriting can avoid it.

## Placeholders

- Prefer uppercase words separated by underscores: `RESOURCE_NAME`, `PROJECT_ID`.
- Avoid first-person placeholders such as `MY_PROJECT`.
- Explain each placeholder at first use.
- For one placeholder, use a direct replacement instruction.
- For several placeholders, list them in order of appearance after the sample.
- Use a naming convention required by the target syntax when uppercase underscore placeholders are invalid.

## Code samples

- Follow the language or project code style before generic documentation style.
- Use spaces rather than tabs unless the language or project requires tabs.
- Keep samples focused on the concept being explained.
- Introduce each sample with a sentence stating what it demonstrates.
- Mark omitted source code with a language-appropriate comment, not an ellipsis.
- Wrap long lines when doing so does not change semantics.
- Do not present a partially omitted example as click-to-copy.

## Command-line documentation

- Link to the authoritative command reference when useful.
- In task procedures, include only arguments needed for the task.
- Prefer examples that users can copy and run without editing structural syntax.
- Avoid notation such as `[]`, `{}`, `|`, and `...` inside click-to-copy commands when it represents optional or alternative syntax.
- Use separate examples for materially different options when that is clearer.
- Use continuation characters required by the shell when wrapping commands.
- Separate command input from output.
- Include output only when it helps readers verify success, identify a value, or understand the next step.

## API reference text

For public API elements, describe behavior directly and concisely.

- Classes/interfaces/structs: start with purpose, then important usage guidance.
- Methods: start with what the method does, not what the developer can use it to do.
- Getter returning non-boolean: "Gets ..." is a useful default.
- Getter returning boolean: "Checks whether ..." is a useful default.
- Creation method: "Creates ...".
- Mutation method: use a precise verb such as "Sets", "Updates", "Deletes", or "Registers".
- Boolean parameter or return description: state the true and false behavior explicitly.
- Deprecation: put the replacement or required action in the first sentence, then explain why and when relevant.
- Document prerequisites, permissions, constraints, and important exceptions.
- Avoid repeating the identifier when the sentence can start directly with the behavior.

## UI instructions

- Refer to visible UI labels exactly and format them in bold when supported.
- Refer to an element by its label rather than by color, icon shape, or screen position.
- Use `click` for pointer interaction and `tap` for touch interaction when platform context matters.
- Use `select` and `clear` for checkboxes.
- Use `press` for keyboard keys.
- Use `enter` or `type` for text input; choose the verb that matches the interaction.
- Do not use a UI label as a verb if that makes the sentence unnatural or ambiguous.
- Use `in` for dialogs, fields, lists, menus, panes, and windows; use `on` for pages, tabs, and toolbars when those distinctions help.
- Avoid UI nicknames such as "hamburger icon" when a proper accessible label exists.
- If an element is difficult to find, add contextual location or a screenshot rather than relying on vague directions.

## Images and diagrams

- Use an image when it explains visual structure or UI more effectively than prose.
- Do not use an image of text, code, or terminal output when actual text works.
- Prefer vector images such as SVG for diagrams when practical.
- Introduce important figures in surrounding text.
- Give every meaningful image concise alt text that states its purpose or essential information.
- Use empty alt text for purely decorative images.
- Do not begin alt text with "Image of" unless that distinction is itself meaningful.
- Put complex image details in nearby prose, not only in alt text.
- Avoid PII in screenshots and examples.

## HTML and semantic formatting

- Use semantic elements for meaning, not visual appearance.
- Use heading elements only for hierarchy.
- Use `em` for emphasis and `strong` for importance; use `i` and `b` only when visual styling is intended without those semantics.
- Use CSS for layout; do not use tables or heading levels to create visual layout.
- Avoid forced `<br>` elements for prose spacing.
- Use spaces, not tabs, and follow the project's established indentation and line-length conventions.
