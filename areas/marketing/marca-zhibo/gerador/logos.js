// Zhibo logo family generator: 3 signatures x 3 layouts x 4 colourways, symbol, avatars, watermarks.
// All text is converted to outlines (real vectors). Run: node logos.js <fontsDir> <outDir>
const fs = require('fs'), path = require('path');
const opentype = require(path.join(__dirname, '../kit-tools/node_modules/opentype.js'));
const [fontsDir, OUT] = process.argv.slice(2);

const C = { red: '#E5262A', ink: '#141010', paper: '#FFF7EC', white: '#FFFFFF', gold: '#FFC42E', deep: '#9E1418' };
const COLORWAYS = {
  Colorida: { sym: C.red, txt: C.ink },
  Negativa: { sym: C.red, txt: C.paper },   // colorida para fundos escuros
  Preta: { sym: C.ink, txt: C.ink },
  Branca: { sym: C.white, txt: C.white },
};
const FRONTS = { Institucional: null, Agencia: 'agência', Shop: 'shop' };

// ---------- symbol B (100x100 box, visual bounds incl. strokes) ----------
const SX = 0.79, VIS = { x0: 19.12, x1: 80.88, y0: 20, y1: 80 };
const VW = VIS.x1 - VIS.x0, VH = VIS.y1 - VIS.y0;
function tri(cx, cy, w, h) { const x1 = cx - w / 3; return [[x1, cy - h / 2], [x1, cy + h / 2], [x1 + w, cy]]; }
function symbol(color) {
  const t = tri(30, 50, 26, 32).map(p => p.map(v => +v.toFixed(3)).join(',')).join(' ');
  return `<g transform="translate(${SX} 0)"><polygon points="${t}" fill="${color}" stroke="${color}" stroke-width="6" stroke-linejoin="round"/>` +
    `<path d="M52 34 A22 22 0 0 1 52 66" fill="none" stroke="${color}" stroke-width="8" stroke-linecap="round"/>` +
    `<path d="M64 24 A34 34 0 0 1 64 76" fill="none" stroke="${color}" stroke-width="8" stroke-linecap="round"/></g>`;
}
// symbol placed so that its VISUAL box is (x, y, w=VW*k, h=VH*k)
const symAt = (x, y, k, color) => `<g transform="translate(${r(x - VIS.x0 * k)} ${r(y - VIS.y0 * k)}) scale(${r(k, 5)})">${symbol(color)}</g>`;
const r = (v, d = 3) => +v.toFixed(d);

// ---------- text to outlines ----------
const F800 = opentype.loadSync(path.join(fontsDir, 'Unbounded-800.ttf'));
const F500 = opentype.loadSync(path.join(fontsDir, 'Unbounded-500.ttf'));
function textPath(font, str, size, tracking) {
  let x = 0; const parts = []; let bb = { x1: Infinity, y1: Infinity, x2: -Infinity, y2: -Infinity };
  const gl = font.stringToGlyphs(str);
  gl.forEach((g, i) => {
    const p = g.getPath(x, 0, size); parts.push(p.toPathData(2));
    const b = p.getBoundingBox();
    if (isFinite(b.x1)) bb = { x1: Math.min(bb.x1, b.x1), y1: Math.min(bb.y1, b.y1), x2: Math.max(bb.x2, b.x2), y2: Math.max(bb.y2, b.y2) };
    const kern = i < gl.length - 1 ? font.getKerningValue(g, gl[i + 1]) : 0;
    x += (g.advanceWidth + kern) * size / font.unitsPerEm + tracking * size;
  });
  return { d: parts.join(' '), bb, w: bb.x2 - bb.x1 };
}
const F = 100;                               // wordmark font size (units)
const WM = textPath(F800, 'zhibo', F, -0.042);
const XH = -WM.bb.y1;                        // wordmark height above baseline (ascender of h/b) ~ 85
const ZX = (() => { const z = textPath(F800, 'z', F, 0); return -z.bb.y1; })();   // x-height of "z" = unit "x" of the system
const DSIZE = 0.5 * F;                       // descriptor size: always 50% of the wordmark size
const desc = s => textPath(F500, s, DSIZE, 0);
const place = (t, x, baseline, color) => `<path transform="translate(${r(x - t.bb.x1)} ${r(baseline)})" d="${t.d}" fill="${color}"/>`;

function svg(w, h, body, title) {
  return `<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${r(w)} ${r(h)}" width="${r(w * 4, 0)}" height="${r(h * 4, 0)}"><title>${title}</title>${body}</svg>\n`;
}

// Layout rules (documented in the manual):
//  Horizontal: symbol visual height = 1.1 x wordmark height, gap symbol->text = 0.32 x wordmark height,
//              descriptor on the same baseline, gap = 0.22 F.
//  Vertical:   symbol visual height = 1.3 x wordmark height, centred; gap 0.30 H; descriptor below, gap 0.28 F.
//  Compacta:   fronts -> symbol + wordmark over descriptor (block height); Institucional -> wordmark only.
function horizontal(front, cw) {
  const H = XH, k = 1.1 * H / VH, sw = VW * k, sh = VH * k, gap = 0.32 * H;
  const d = FRONTS[front] ? desc(FRONTS[front]) : null;
  const textW = WM.w + (d ? 0.22 * F + d.w : 0);
  const top = Math.min(-H, -H / 2 - sh / 2), bottom = Math.max(0, WM.bb.y2, -H / 2 + sh / 2, d ? d.bb.y2 : 0);
  const h = bottom - top, w = sw + gap + textW;
  const base = -top; // baseline y in the viewBox
  let b = symAt(0, base - H / 2 - sh / 2, k, cw.sym) + place(WM, sw + gap, base, cw.txt);
  if (d) b += place(d, sw + gap + WM.w + 0.22 * F, base, cw.txt);
  return { w, h, b };
}
function vertical(front, cw) {
  const H = XH, k = 1.3 * H / VH, sw = VW * k, sh = VH * k, g1 = 0.30 * H;
  const d = FRONTS[front] ? desc(FRONTS[front]) : null;
  const dH = d ? -d.bb.y1 : 0, g2 = 0.28 * F;
  const w = Math.max(sw, WM.w, d ? d.w : 0);
  const base1 = sh + g1 + H;
  let b = symAt((w - sw) / 2, 0, k, cw.sym) + place(WM, (w - WM.w) / 2, base1, cw.txt);
  let h = base1;
  if (d) { const base2 = base1 + g2 + dH; b += place(d, (w - d.w) / 2, base2, cw.txt); h = base2 + Math.max(0, d.bb.y2); }
  return { w, h, b };
}
function compacta(front, cw) {
  const H = XH;
  if (!FRONTS[front]) { return { w: WM.w, h: H + Math.max(0, WM.bb.y2), b: place(WM, 0, H, cw.txt) }; }
  const d = desc(FRONTS[front]); const dH = -d.bb.y1, g = 0.22 * F;
  const blockH = H + g + dH;                       // wordmark top -> descriptor baseline
  const k = blockH / VH, sw = VW * k, gap = 0.32 * H;
  const b = symAt(0, 0, k, cw.sym) + place(WM, sw + gap, H, cw.txt) + place(d, sw + gap, H + g + dH, cw.txt);
  return { w: sw + gap + Math.max(WM.w, d.w), h: blockH + Math.max(0, d.bb.y2), b };
}
const LAYOUTS = { Horizontal: horizontal, Vertical: vertical, Compacta: compacta };
const FRONT_NAME = { Institucional: 'Zhibo', Agencia: 'Zhibo Agência', Shop: 'Zhibo Shop' };
const FILE_FRONT = { Institucional: 'Zhibo_Institucional', Agencia: 'Zhibo_Agencia', Shop: 'Zhibo_Shop' };

const manifest = [];
function write(rel, content) { const p = path.join(OUT, rel); fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, content); }
for (const front of Object.keys(FRONTS)) for (const [lay, fn] of Object.entries(LAYOUTS)) for (const [cwn, cw] of Object.entries(COLORWAYS)) {
  const L = fn(front, cw);
  const name = `${FILE_FRONT[front]}_Logo_${lay}_${cwn}`;
  write(`logos/${FILE_FRONT[front]}/${name}.svg`, svg(L.w, L.h, L.b, `${FRONT_NAME[front]} — ${lay} — ${cwn}`));
  manifest.push({ front, layout: lay, colorway: cwn, file: `logos/${FILE_FRONT[front]}/${name}.svg`, w: r(L.w), h: r(L.h) });
}
// Shared symbol
for (const [cwn, col] of Object.entries({ Vermelho: C.red, Preto: C.ink, Branco: C.white, Creme: C.paper })) {
  const m = 0; write(`simbolo/Zhibo_Simbolo_${cwn}.svg`, svg(VW, VH, symAt(0, 0, 1, col), `Símbolo Zhibo — ${cwn}`));
}
// Avatars 1080-ready (square, full background; symbol 52% of width, optical centre = geometric centre)
const AV = { Institucional: { bg: C.ink, fg: C.red }, Agencia: { bg: C.gold, fg: C.ink }, Shop: { bg: C.red, fg: C.paper } };
for (const [front, a] of Object.entries(AV)) {
  const k = 52 / VW, sw = VW * k, sh = VH * k;
  write(`avatares/${FILE_FRONT[front]}_Avatar.svg`, svg(100, 100, `<rect width="100" height="100" fill="${a.bg}"/>` + symAt(50 - sw / 2, 50 - sh / 2, k, a.fg), `Avatar ${FRONT_NAME[front]}`));
}
// Watermarks (horizontal, white and black; opacity baked at 60%)
for (const front of Object.keys(FRONTS)) for (const [n, col] of Object.entries({ Branca: C.white, Preta: C.ink })) {
  const L = horizontal(front, { sym: col, txt: col });
  write(`marca_dagua/${FILE_FRONT[front]}_Marca_dAgua_${n}.svg`, svg(L.w, L.h, `<g opacity="0.6">${L.b}</g>`, `Marca-d'água ${FRONT_NAME[front]}`));
}
fs.writeFileSync(path.join(OUT, 'manifest.json'), JSON.stringify({ unitX: r(ZX), wordmarkH: r(XH), wordmarkW: r(WM.w), items: manifest }, null, 1));
console.log('ok', manifest.length, 'logos; x =', r(ZX), 'H =', r(XH));
