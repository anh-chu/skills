---
name: release-kit
description: >-
  Create a polished, on-brand, print-ready release/launch kit (paged HTML → PDF) for a
  product change, feature launch, rollout, or GA. Use when the user asks for a "release
  kit", "launch kit", "launch briefing", "GTM/enablement doc", "rollout one-pager/deck",
  "stakeholder briefing", or "a paged PDF explaining <change> for <teams>". Handles the
  whole flow: gather context (GitHub issues/PRs, memory, docs), pick the audience and
  register, capture real product screenshots, study the company's actual brand from its
  website, build a crafted paged HTML with embedded fonts + images, export to PDF, and
  verify each page fits with no overflow.
---

# Release / Launch Kit builder

Produce a **single self-contained paged HTML** (fonts + images embedded) that exports to a
pixel-perfect multi-page **PDF**. The output looks like it came from the company's own brand
team — not a generic AI template.

Work through the phases in order. Skip a phase only when the user has already supplied its
output. Keep the user in the loop on the two decisions that shape everything: **audience** and
**what's actually shipping**.

## Phase 1 — Gather the real story (don't invent it)

Pull the facts from where they live; never fabricate rollout dates, metrics, gates, or owners.

- **GitHub** (`gh`): find the tracking issue / PRD, the implementation + QA PRs, the rollout
  plan, the gates, and the fast-follow / known-issue list. `gh issue view <n> --repo <o/r>`,
  `gh search issues "<topic>" --repo <o/r>`.
- **Memory & repo docs**: check auto-memory and `docs/` for specs, prior context, decisions.
- **Ask the user** for anything unresolved: exact go-live date, the flag/mechanism, the real
  owner names, whether it's going to 100% or phased.

Capture: what's changing (before→after), why now, who's affected, when, rollback, how it's
gated/proven, what's still coming, and how success is measured.

## Phase 2 — Pick the audience and register (ask if unclear)

The single biggest quality lever. Two common modes:

- **Internal eng/product** — issue numbers, flag names, code paths, A/B guardrails are fine.
- **Cross-functional / non-technical** (Marketing, Sales, CS, Support, Docs, Leadership) —
  plain language, "what your team must do", benefits and user impact up front; push flag
  names / issue numbers / metrics-jargon into a small "for the record" appendix.

Write copy from the reader's side of the screen. Name things the way users see them
("a tab on the right edge", not "a 24px rail"). Active voice, sentence case, no filler.

## Phase 3 — Capture real product screenshots (Claude in Chrome)

Real screenshots beat schematics. Load the browser tools (see the claude-in-chrome skill),
open the live app, and capture the key states with `save_to_disk: true`:

- the hero / main screen (the "after"),
- each headline feature in its own state (e.g. command palette, AI panel, expanded menu,
  collapsed menu),
- a genuine "before" if an old version is still reachable (otherwise draw a clean schematic).

Wait for the app to finish loading (`document.fonts.ready` + a short wait) so charts/content
render before shooting. Note the saved paths — they get embedded in Phase 6.

## Phase 4 — Study the ACTUAL brand (this is what makes it not look AI)

Do NOT invent a look. Extract the company's real system from its marketing site.

1. Open the site in Chrome. Screenshot the hero and a couple of content sections.
2. Run `javascript_tool` to read computed styles — capture exact values:
   - `getComputedStyle` on `<h1>`/`<body>` → **display font, body font, weights, color**;
   - the primary CTA button → **action color, radius, border style**;
   - scan elements for the most-used background colors and any **gradient** (often the brand's
     signature device) → build a 5–8 value **named palette (hex)**;
   - note section patterns (pills/eyebrows, dark bands, card style, the product's own sidebar).
3. Write down a compact token system: colors, the 2–3 fonts by role, radius, the signature
   accent. Everything in the kit derives from these.

Grounding the design in the real brand is mandatory — a "distinctive but invented" direction
is the wrong answer here. If the user names a site, use it; otherwise ask which URL is canonical.

## Phase 5 — Build the paged HTML

Start from `assets/kit.css` (a print-ready, brand-neutral component system: cover, section
headers, cards, callouts, ruled tables, figures, the product-sidebar list, timeline steps,
metric tiles). **Swap the `:root` BRAND TOKENS block** with the Phase-4 palette and fonts.

Structure (drop sections that don't apply; reorder for the audience):

1. Cover — brand-colored, signature accent, big display headline, go-live pill, meta row.
2. Contents.
3. The change at a glance (+ "what each team does" table for cross-functional audiences).
4. Before & after (schematic + the real hero screenshot + a where-things-moved table).
5. Feature tour (+ a screenshots page from Phase 3).
6. "Where did it go?" migration/moved-items map — the highest-value page for customer teams.
7. Timeline & how the rollout/switch works.
8. Why it's ready (evidence, sign-offs) · What's still coming (fast-follows) · Safety net (rollback).
9. Marketing / Documentation / Support-CS-Sales action pages.
10. How success is measured.
11. Appendix — quick reference, contacts, and the "for the record (technical)" block.

Rules that matter for print:
- `@page { size: A4; margin: 0; }`; every page is one `.page` block (full-bleed, its own padding).
- Put page-background color on the `.page` element, never `html/body` (avoids blank pages).
- Footers: `position:absolute` inside each full-height `.page` — **never `position:fixed`**
  (fixed repeats every page's footer on every sheet).
- Keep it self-contained: no external CSS/JS/fonts/images at render time.

Leave a `/*FONTS*/` marker at the top of `<style>` and `{{IMG_*}}` placeholders on `<img src>`.

## Phase 6 — Embed fonts + screenshots (offline-true PDF)

Fonts must be embedded so the PDF renders identically anywhere.

```bash
# 1. Fetch the brand's fonts as base64 @font-face (latin subset):
python3 scripts/fetch-fonts.py fonts.css "Inter:wght@400;500;600" "Inter Tight:wght@500;600;700"
# 2. Inject the fonts (into /*FONTS*/) and the screenshots (into {{IMG_*}}):
python3 scripts/embed.py kit.html --fonts fonts.css \
  --img "{{IMG_HERO}}=/path/hero.jpg" --img "{{IMG_PALETTE}}=/path/palette.jpg"
```

`fetch-fonts.py` picks the latin block per weight so the file stays small (~45KB/weight).
If the brand's font isn't on Google Fonts, fall back to the closest system stack
(`-apple-system`/`system-ui`) — the layout still holds.

## Phase 7 — Export to PDF (html-to-pdf skill)

Use the sibling **html-to-pdf** skill (Puppeteer/headless Chrome). One-time: `cd
~/.claude/skills/html-to-pdf && npm install`.

```bash
node ~/.claude/skills/html-to-pdf/scripts/html-to-pdf.js \
  kit.html kit.pdf --format=A4 --margin=0 --wait=2500 --no-page-check
```

`--margin=0` + the CSS `@page` (via `preferCSSPageSize`) makes the PDF match the HTML exactly.
`--no-page-check` because the kit is intentionally multi-page.

## Phase 8 — Verify every page fits (mandatory)

Overflow silently clips content (`overflow:hidden`). Measure, don't eyeball.

```bash
# serve, then measure each .page's true content height vs A4:
(cd <dir> && python3 -m http.server 8799 &)
node scripts/measure-pages.js http://localhost:8799/kit.html
```

Any page with `over > ~5px` will clip. Fix by trimming that page (remove duplicate content,
shrink an oversized image, tighten spacing/line-height, add global headroom) — then re-measure.
Then **render the suspect pages to PNG and look at them** (the native PDF viewer can't be
screenshotted, but element rendering works):

```bash
node scripts/render-pages.js http://localhost:8799/kit.html 2,3 /tmp   # 0-indexed .page
```

Read the PNGs, confirm nothing is cut off and footers are intact, regenerate the PDF, done.

## Deliverable

One `*.pdf` (self-contained, one section per page) plus its source `*.html`. Tell the user the
regenerate command (Phase 7) so they can tweak copy and re-export themselves.

## Notes

- The `html-to-pdf` script is third-party; it's already vetted here (a thin Puppeteer wrapper).
- Don't publish/impersonate: this is an internal briefing. Use the real logo only if the user
  provides it; otherwise use a neutral brand lockup.
- Convert relative dates to absolute. Never invent metrics or dates — pull or ask.
