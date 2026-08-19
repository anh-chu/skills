#!/usr/bin/env node
/**
 * Measure each `.page` element's true content height against the A4 sheet, so you catch
 * overflow (which `overflow:hidden` would silently clip) BEFORE exporting the PDF.
 *
 * Usage:
 *   node measure-pages.js <url> [pageSelector]
 *   node measure-pages.js http://localhost:8799/kit.html
 *
 * Prints one row per page: index, label, content px, and `over` (px beyond A4).
 * Any page with over > ~5 will clip — trim that page and re-measure.
 *
 * Serve the file first (python3 -m http.server) so fonts/images load like the real render.
 */
const path = require('path');

function resolvePuppeteer() {
  for (const p of ['puppeteer',
                   path.join(process.env.HOME, '.claude/skills/html-to-pdf/node_modules/puppeteer')]) {
    try { return require(p); } catch (_) {}
  }
  console.error('puppeteer not found — run: cd ~/.claude/skills/html-to-pdf && npm install');
  process.exit(1);
}

(async () => {
  const url = process.argv[2];
  const sel = process.argv[3] || '.page';
  if (!url) { console.error('usage: node measure-pages.js <url> [selector]'); process.exit(1); }

  const puppeteer = resolvePuppeteer();
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 1300, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 1200));

  const rows = await page.evaluate((sel) => {
    const A4 = 1122.52; // 297mm @96dpi
    return [...document.querySelectorAll(sel)].map((p, i) => {
      const o = p.style.overflow, h = p.style.height, m = p.style.minHeight;
      p.style.overflow = 'visible'; p.style.height = 'auto'; p.style.minHeight = '0';
      const sh = p.scrollHeight;
      p.style.overflow = o; p.style.height = h; p.style.minHeight = m;
      const label = (p.querySelector('h2,h1')?.textContent || 'page').trim().slice(0, 34);
      return { i, label, px: Math.round(sh), over: Math.round(sh - A4) };
    });
  }, sel);

  await browser.close();

  const worst = Math.max(...rows.map(r => r.over));
  for (const r of rows) {
    const flag = r.over > 5 ? '  <-- OVERFLOW (clips)' : (r.over > -20 ? '  (tight)' : '');
    console.log(`  page ${String(r.i).padStart(2)}  ${String(r.px).padStart(5)}px  over ${String(r.over).padStart(5)}px  ${r.label}${flag}`);
  }
  console.log(`\nmax overflow: ${worst}px  ${worst > 5 ? '— FIX the flagged pages' : '— all pages fit'}`);
  process.exit(worst > 5 ? 3 : 0);
})();
