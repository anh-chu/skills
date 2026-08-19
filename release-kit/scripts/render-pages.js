#!/usr/bin/env node
/**
 * Render specific `.page` elements to PNG for visual QA. The native browser PDF viewer can't
 * be screenshotted by the automation tools, but rendering the source .page elements shows
 * exactly what each PDF page will look like (same CSS via preferCSSPageSize).
 *
 * Usage:
 *   node render-pages.js <url> <indices> [outDir]
 *   node render-pages.js http://localhost:8799/kit.html 0,2,3 /tmp
 *
 * indices are 0-based .page positions (0 = cover). Writes <outDir>/page<N>.png, then Read them.
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
  const idxs = (process.argv[3] || '').split(',').map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n));
  const outDir = process.argv[4] || '/tmp';
  if (!url || !idxs.length) { console.error('usage: node render-pages.js <url> <indices> [outDir]'); process.exit(1); }

  const puppeteer = resolvePuppeteer();
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 1300, deviceScaleFactor: 2 });
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 1500));

  const pages = await page.$$('.page');
  for (const i of idxs) {
    if (!pages[i]) { console.error(`  no .page at index ${i}`); continue; }
    const out = path.join(outDir, `page${i}.png`);
    await pages[i].screenshot({ path: out });
    console.log(`  wrote ${out}`);
  }
  await browser.close();
})();
