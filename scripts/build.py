"""Generate the standalone SVG catalog and static bilingual preview."""
from pathlib import Path
import json
import html

root = Path(__file__).resolve().parents[1]
icons = {
    "bank": ("Bank", "بنك", '<path d="m3 9 9-5 9 5M4 10h16M5 20h14M7 11v7m5-7v7m5-7v7M3 20h18"/>'),
    "wallet": ("Wallet", "محفظة", '<path d="M5 7V5a2 2 0 0 1 2-2h11M4 7h15a2 2 0 0 1 2 2v3h-5a2 2 0 0 0 0 4h5v3a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2Z"/><path d="M21 12v4h-5a2 2 0 0 1 0-4h5Z"/><circle cx="16" cy="14" r=".6"/>'),
    "card": ("Card", "بطاقة", '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6 15h4"/>'),
    "transfer": ("Transfer", "تحويل", '<path d="M4 8h15m-4-4 4 4-4 4M20 16H5m4-4-4 4 4 4"/>'),
    "send": ("Send", "إرسال", '<path d="m3 11 18-8-8 18-2.7-7.3L3 11Z"/><path d="M10.3 13.7 21 3"/>'),
    "receive": ("Receive", "استلام", '<path d="M12 3v12m-4-4 4 4 4-4M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/>'),
    "exchange": ("Exchange", "صرف عملات", '<circle cx="8" cy="9" r="5"/><path d="M4 9h8m-4-5c-2 2-2 8 0 10m0-10c2 2 2 8 0 10M17 10v9m-3-3 3 3 3-3M14 5h6"/>'),
    "receipt": ("Receipt", "إيصال", '<path d="M5 3h14v18l-2.5-1.5L14 21l-2-1.5L9.5 21 7 19.5 5 21V3Z"/><path d="M8 8h8M8 12h8M8 16h4"/>'),
    "history": ("History", "السجل", '<path d="M3 12a9 9 0 1 0 2.4-6.1M3 4v4h4"/><path d="M12 7v5l3 2"/>'),
    "shield": ("Protection", "حماية", '<path d="m12 2 8 3v6c0 5.1-3.3 8.6-8 11-4.7-2.4-8-5.9-8-11V5l8-3Z"/><path d="m9 12 2 2 4-4"/>'),
    "lock": ("Lock", "قفل", '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M7 10V7a5 5 0 0 1 10 0v3"/><circle cx="12" cy="15.5" r=".9"/>'),
    "verify": ("Verified", "موثّق", '<path d="m12 2 2.7 2 3.3-.2.7 3.3 2.3 2.4-1.5 3 0 3.3-3.1 1.4-2 2.7-3.1-.8-3.2.8-1.9-2.7-3.1-1.4v-3.3l-1.5-3 2.3-2.4.7-3.3 3.3.2L12 2Z"/><path d="m8.5 11.8 2.4 2.4 4.6-4.6"/>'),
    "savings": ("Savings", "ادخار", '<path d="M6 9a6 6 0 0 1 5-3h4a5 5 0 0 1 4 2l2 1v7l-3 1.5V20h-2v-2H9v2H7v-2.5A6 6 0 0 1 4 13V9h2Z"/><path d="M11 9h4M4 11H2v2h2"/><circle cx="17" cy="11" r=".7"/>'),
    "fees": ("Fees", "رسوم", '<path d="M7 3h10a2 2 0 0 1 2 2v16l-3-2-4 2-4-2-3 2V5a2 2 0 0 1 2-2Z"/><path d="M9 9h6M9 13h6M9 17h3"/>'),
    "globe": ("International", "دولي", '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c-3 3-3 15 0 18m0-18c3 3 3 15 0 18M5 7h14M5 17h14"/>'),
    "phone": ("Mobile payment", "دفع بالموبايل", '<rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M10 5h4M10 19h4m-5-7h6m-2-2 2 2-2 2"/>'),
}
catalog = {name: {"en": en, "ar": ar} for name, (en, ar, _) in icons.items()}
(root / "icons.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(root / "icons").mkdir(exist_ok=True)
for name, (_, _, drawing) in icons.items():
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{drawing}</svg>\n'
    (root / "icons" / f"{name}.svg").write_text(svg, encoding="utf-8")
cards = "\n".join(
    f'<article><div class="glyph"><img src="../icons/{name}.svg" alt="" width="36" height="36"></div><strong>{html.escape(en)}</strong><span lang="ar" dir="rtl">{html.escape(ar)}</span><code>{name}.svg</code></article>'
    for name, (en, ar, _) in icons.items()
)
page = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Arabic Finance Icons</title>
<style>
:root{font-family:Inter,system-ui,sans-serif;color:#e9f2f2;background:#0b151b}
*{box-sizing:border-box}body{margin:0;padding:clamp(24px,6vw,80px);max-width:1440px;margin-inline:auto}
header{display:flex;justify-content:space-between;gap:20px;align-items:end;flex-wrap:wrap;margin-bottom:44px}
h1{font-size:clamp(36px,5vw,76px);letter-spacing:-.065em;line-height:1;margin:0 0 14px}
p{max-width:620px;color:#a8bec3;line-height:1.6;margin:0}
.eyebrow{color:#74ebc6;font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:18px}
.pill{padding:10px 15px;border:1px solid #34525a;border-radius:30px;color:#a8bec3}
main{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px}
article{border:1px solid #254048;border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:5px;background:#102029}
.glyph{height:90px;display:flex;align-items:center;color:#74ebc6}
.glyph img{filter:invert(84%) sepia(28%) saturate(669%) hue-rotate(97deg) brightness(100%)}
strong{font-size:17px}span{color:#b0c7c7;align-self:start}code{font-size:11px;color:#778f94;margin-top:14px}
</style>
<header><div><div class="eyebrow">Open source / SVG collection</div><h1>Arabic Finance Icons<span aria-hidden="true" style="color:#74ebc6">.</span></h1><p>Clear, original symbols for financial interfaces across Arabic and English. Free to use, easy to edit, and designed on a consistent 24 px grid.</p></div><div class="pill">16 icons · MIT license</div></header>
<main>''' + cards + '''</main></html>'''
(root / "preview").mkdir(exist_ok=True)
(root / "preview" / "index.html").write_text(page, encoding="utf-8")
print(f"Built {len(icons)} SVGs and preview")
