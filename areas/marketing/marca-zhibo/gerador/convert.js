// SVG -> PNG (transparent) and SVG -> vector PDF (tight page), in bulk.
// Usage: node convert.js <listFile.json>   where list = [{svg, png?, pngWidth?, pngPad?, pdf?}]
const fs = require('fs'); const path = require('path'); const { chromium } = require('playwright');
const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const j of jobs) {
    const svg = fs.readFileSync(j.svg, 'utf8');
    const vb = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/); const w = +vb[1], h = +vb[2];
    if (j.png) {
      const W = j.pngWidth || 3000, pad = j.pngPad || 0;
      const inner = W - 2 * pad, H = Math.round(inner * h / w) + 2 * pad;
      const data = await p.evaluate(async ({ svg, W, H, pad, inner }) => {
        const img = new Image(); img.src = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svg))); await img.decode();
        const c = document.createElement('canvas'); c.width = W; c.height = H;
        c.getContext('2d').drawImage(img, pad, pad, inner, H - 2 * pad); return c.toDataURL('image/png');
      }, { svg, W, H, pad, inner });
      fs.mkdirSync(path.dirname(j.png), { recursive: true });
      fs.writeFileSync(j.png, Buffer.from(data.split(',')[1], 'base64'));
    }
    if (j.pdf) {
      const mmW = j.pdfWidthMm || 100, mmH = mmW * h / w;
      await p.setContent(`<html><head><style>@page{size:${mmW}mm ${mmH}mm;margin:0}html,body{margin:0}svg{display:block;width:${mmW}mm;height:${mmH}mm}</style></head><body>${svg.replace(/<\?xml[^>]*>/, '')}</body></html>`);
      fs.mkdirSync(path.dirname(j.pdf), { recursive: true });
      await p.pdf({ path: j.pdf, width: `${mmW}mm`, height: `${mmH}mm`, printBackground: true, pageRanges: '1' });
    }
  }
  await b.close(); console.log('converted', jobs.length);
})();
