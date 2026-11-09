# -*- coding: utf-8 -*-
import json
import datetime

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data)} items for HTML generation.")
data_json_str = json.dumps(data, ensure_ascii=False)

MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]
hoy = datetime.date.today()
fecha_actualizacion = f"{hoy.day} de {MESES[hoy.month - 1]} de {hoy.year}"

html_content = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Radar ICF — Creado por NachoFari</title>
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="assets/radar-favicon.png">
<link rel="apple-touch-icon" href="assets/radar-favicon.png">
<style>
  :root {{
    /* Paleta NaTex Studio: Dark Charcoal con Acento Naranja Vibrante y Cian */
    --bg: #0e0f13;
    --bg2: #14161b;
    --card: #181a20;
    --card2: #1e2027;
    --card-hover: #22252e;
    --border: #262933;
    --border2: #343846;
    --txt: #f0f2f5;
    --muted: #8e93a0;
    --faint: #595e6d;
    
    /* Acentos NaTex Studio */
    --accent: #ff6b35;
    --accent2: #ff8c42;
    --accent-glow: rgba(255, 107, 53, 0.28);
    --cyan: #38bdf8;
    --green: #2ecc71;
    --red: #ef4444;
    --purple: #a855f7;
    --yellow: #fbbf24;
  }}
  * {{ box-sizing:border-box }}
  body {{
    margin:0;
    background: radial-gradient(1100px 550px at 65% -5%, #241c18 0%, var(--bg) 60%);
    color: var(--txt);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.5;
    padding: 0 18px 80px;
    -webkit-font-smoothing: antialiased;
  }}
  .wrap {{ max-width: 1180px; margin: 0 auto }}
  
  /* Header NaTex Style */
  header {{ padding: 28px 0 12px }}
  .header-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 14px;
  }}
  .badges-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
    margin-bottom: 10px;
  }}
  .brand-badge {{
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: linear-gradient(135deg, rgba(255,107,53,0.18), rgba(255,140,66,0.08));
    border: 1px solid rgba(255,107,53,0.38);
    color: var(--accent2);
    font-size: .78rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 999px;
    letter-spacing: .02em;
  }}
  .update-badge {{
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.28);
    color: var(--cyan);
    font-size: .76rem;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 999px;
  }}
  .pulse-dot {{
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 8px var(--green);
  }}
  .fox-icon-mini {{ width: 15px; height: 15px; vertical-align: -2px; border-radius: 3px; display: inline-block }}
  .fox-icon-btn {{ width: 18px; height: 18px; vertical-align: -3px; border-radius: 3px; display: inline-block }}
  .fox-icon-nav {{ width: 26px; height: 26px; border-radius: 5px; flex-shrink: 0 }}
  .fox-icon-hero {{ width: 48px; height: 48px; vertical-align: -10px; margin-right: 10px; border-radius: 10px }}

  h1 {{
    font-size: 2.15rem;
    margin: 0 0 6px;
    font-weight: 850;
    letter-spacing: -.02em;
  }}
  h1 .q {{
    background: linear-gradient(90deg, #ff7a45, #ffa154);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }}
  .sub {{ color: var(--muted); font-size: .92rem; margin: 0; max-width: 740px }}
  
  .top-actions {{ display:flex; gap: 8px; align-items:center; flex-wrap:wrap }}
  .btn-top {{
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--txt);
    font-size: .8rem;
    font-weight: 600;
    padding: 8px 14px;
    border-radius: 10px;
    cursor: pointer;
    transition: all .15s ease;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }}
  .btn-top:hover {{
    border-color: var(--accent);
    background: var(--card2);
  }}
  .btn-top.btn-accent {{
    background: linear-gradient(135deg, #ff7a45 0%, #ff5224 100%);
    border: none;
    color: #fff;
    box-shadow: 0 2px 10px rgba(255,107,53,0.3);
  }}
  .btn-top.btn-accent:hover {{
    filter: brightness(1.1);
  }}

  /* Main 4-Window Navigation Bar in Header */
  .main-nav {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 24px 0 14px;
  }}
  .nav-btn {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 14px 16px;
    color: var(--txt);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 12px;
    text-align: left;
    transition: all .18s ease;
    position: relative;
    overflow: hidden;
  }}
  .nav-btn:hover {{
    border-color: var(--border2);
    background: var(--card2);
    transform: translateY(-1px);
  }}
  .nav-btn.active {{
    border-color: var(--accent);
    background: linear-gradient(180deg, rgba(255,107,53,0.16), var(--card));
    box-shadow: 0 6px 20px var(--accent-glow);
  }}
  .nav-btn.nav-natex {{
    border-color: rgba(255, 107, 53, 0.35);
    background: linear-gradient(135deg, rgba(255, 107, 53, 0.1), var(--card));
  }}
  .nav-btn.nav-natex.active {{
    border-color: #ff8c42;
    background: linear-gradient(135deg, rgba(255, 107, 53, 0.28), #1d1716);
    box-shadow: 0 6px 24px rgba(255, 107, 53, 0.38);
  }}
  .nav-icon {{
    font-size: 1.55rem;
    line-height: 1;
    flex-shrink: 0;
  }}
  .nav-txt {{
    display: flex;
    flex-direction: column;
    gap: 2px;
  }}
  .nav-title {{
    font-size: .95rem;
    font-weight: 800;
    color: #fff;
  }}
  .nav-sub {{
    font-size: .75rem;
    color: var(--muted);
  }}
  .nav-btn.active .nav-sub {{
    color: #ffb38a;
  }}

  /* Sub-Tabs inside Catalog Views */
  .tabs {{ display:flex; gap: 10px; flex-wrap:wrap; margin: 12px 0 8px }}
  .tab {{
    flex: 1 1 160px;
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 10px 16px;
    cursor: pointer;
    transition: all .16s ease;
    user-select: none;
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 8px;
  }}
  .tab:hover {{
    border-color: var(--border2);
    background: var(--card);
  }}
  .tab.on {{
    border-color: var(--accent);
    background: rgba(255, 107, 53, 0.12);
  }}
  .tab .n {{
    font-size: 1.2rem;
    font-weight: 800;
    color: #fff;
  }}
  .tab.on .n {{
    color: var(--accent);
  }}
  .tab .l {{ font-size: .82rem; color: var(--muted); font-weight: 600 }}
  .tab.on .l {{ color: var(--txt) }}
  
  /* Counters */
  .counters {{ display:flex; gap: 8px; flex-wrap:wrap; margin: 10px 0 6px }}
  .counter {{
    display: flex;
    align-items: center;
    gap: 7px;
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 4px 12px;
    font-size: .75rem;
    color: var(--muted);
  }}
  .counter b {{ font-size: .85rem; color: var(--txt) }}
  .counter.c-red {{ border-color: rgba(239, 68, 68, 0.35); color: #fca5a5 }}
  .counter.c-red b {{ color: #f87171 }}
  .counter.c-orange {{ border-color: rgba(255, 107, 53, 0.4); color: #fdba74 }}
  .counter.c-orange b {{ color: var(--accent) }}
  .counter.c-green {{ border-color: rgba(46, 204, 113, 0.35); color: #86efac }}
  .counter.c-green b {{ color: var(--green) }}
  .counter.c-gray {{ border-color: #2f3340 }}
  .counter.c-purple {{ border-color: rgba(168, 85, 247, 0.35); color: #d8b4fe }}
  .counter.c-purple b {{ color: #c084fc }}
  
  /* Controls */
  .controls {{
    position: sticky;
    top: 0;
    z-index: 25;
    background: linear-gradient(180deg, var(--bg) 82%, rgba(14,15,19,0));
    padding: 12px 0 12px;
  }}
  .search-row {{ display:flex; gap: 8px }}
  .search {{
    flex: 1;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--txt);
    font-size: .92rem;
    padding: 12px 16px;
    outline: none;
    transition: border-color .15s ease;
  }}
  .search:focus {{
    border-color: var(--accent);
    box-shadow: 0 0 10px var(--accent-glow);
  }}
  .area-select {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--txt);
    font-size: .84rem;
    padding: 0 14px;
    outline: none;
    cursor: pointer;
    transition: border-color .15s ease;
  }}
  .area-select:focus {{
    border-color: var(--accent);
    box-shadow: 0 0 10px var(--accent-glow);
  }}
  
  .filters {{ display:flex; flex-wrap:wrap; gap: 8px; margin-top: 10px; align-items:center }}
  .fgroup {{ display:flex; flex-wrap:wrap; gap: 6px; align-items:center }}
  .fgroup .lab {{ font-size: .7rem; color: var(--faint); text-transform: uppercase; letter-spacing: .06em; margin-right: 2px; font-weight:700 }}
  .chip {{
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: .79rem;
    padding: 5px 12px;
    border-radius: 999px;
    cursor: pointer;
    user-select: none;
    transition: all .15s ease;
  }}
  .chip:hover {{ color: var(--txt); border-color: var(--border2) }}
  .chip.on {{
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
    font-weight: 700;
    box-shadow: 0 2px 8px var(--accent-glow);
  }}
  .sep {{ width: 1px; background: var(--border); align-self: stretch; margin: 2px 4px }}
  
  /* Grid & Cards */
  .grid {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; margin-top: 10px }}
  .card {{
    background: linear-gradient(180deg, var(--card2), var(--card));
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    position: relative;
    overflow: hidden;
    transition: transform .15s ease, border-color .15s ease, box-shadow .15s ease;
  }}
  .card:hover {{
    transform: translateY(-2px);
    border-color: var(--border2);
  }}
  .card.fav {{
    border-color: rgba(251, 191, 36, 0.45);
    box-shadow: 0 0 14px rgba(251, 191, 36, 0.12);
  }}
  .card::before {{ content:""; position:absolute; left:0; top:0; bottom:0; width: 3px }}
  .card.k-beca::before {{ background: var(--cyan) }}
  .card.k-ind::before {{ background: var(--accent) }}
  .card.k-prof::before {{ background: #c084fc }}
  .card.k-desc::before {{ background: #10b981 }}
  
  .card-top {{ display:flex; justify-content:space-between; align-items:flex-start; gap: 10px }}
  .inst {{ font-weight: 750; font-size: 1.02rem; line-height: 1.3; color: #fff }}
  .pi {{ color: var(--muted); font-size: .82rem; margin-top: 3px }}
  
  /* Urgency Badges */
  .badge {{
    flex: none;
    font-size: .72rem;
    font-weight: 700;
    padding: 5px 9px;
    border-radius: 8px;
    white-space: nowrap;
    text-align: center;
    line-height: 1.15;
  }}
  .badge small {{ display:block; font-weight: 500; font-size: .63rem; opacity: .88 }}
  .b-red {{ background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3) }}
  .b-orange {{ background: rgba(255, 107, 53, 0.15); color: #ff8c5c; border: 1px solid rgba(255, 107, 53, 0.35) }}
  .b-green {{ background: rgba(46, 204, 113, 0.15); color: #2ecc71; border: 1px solid rgba(46, 204, 113, 0.3) }}
  .b-gray {{ background: rgba(142, 147, 160, 0.14); color: #9aa0b0; border: 1px solid rgba(142, 147, 160, 0.25) }}
  .b-purple {{ background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3) }}
  
  /* Tags */
  .tags {{ display:flex; flex-wrap:wrap; gap: 5px }}
  .tag {{
    font-size: .7rem;
    padding: 3px 8px;
    border-radius: 6px;
    background: var(--bg2);
    border: 1px solid var(--border);
    color: var(--muted);
  }}
  .tag.t-beca {{ color: var(--cyan); border-color: rgba(56, 189, 248, 0.28) }}
  .tag.t-ind {{ color: var(--accent); border-color: rgba(255, 107, 53, 0.3) }}
  .tag.t-prof {{ color: #c084fc; border-color: rgba(192, 132, 252, 0.28) }}
  .tag.t-desc {{ color: #34d399; border-color: rgba(52, 211, 153, 0.3) }}
  .tag.area {{ color: #ffa26b; font-weight: 700; border-color: rgba(255, 162, 107, 0.25) }}
  
  .desc {{ font-size: .86rem; color: #d6d9e0; line-height: 1.42 }}
  .fund {{
    font-size: .8rem;
    color: var(--green);
    background: rgba(46, 204, 113, 0.08);
    border: 1px solid rgba(46, 204, 113, 0.2);
    padding: 6px 10px;
    border-radius: 8px;
  }}
  .req {{ font-size: .78rem; color: var(--muted); line-height: 1.35 }}
  .req b {{ color: var(--txt); font-weight: 600 }}
  .note {{ font-size: .76rem; color: var(--faint); font-style: italic }}
  
  /* Links & CTAs */
  .links {{ display:flex; gap: 7px; margin-top: auto; padding-top: 8px; align-items:center }}
  .lnk {{
    text-decoration: none;
    font-size: .79rem;
    font-weight: 700;
    padding: 8px 13px;
    border-radius: 9px;
    transition: all .15s ease;
    text-align: center;
  }}
  .lnk.apply {{
    background: var(--accent);
    color: #fff;
    flex: 1;
    box-shadow: 0 2px 10px rgba(255,107,53,0.25);
  }}
  .lnk.apply:hover {{ background: #ff7f50 }}
  .lnk.src {{
    background: var(--bg2);
    color: var(--muted);
    border: 1px solid var(--border);
  }}
  .lnk.src:hover {{ color: var(--txt); border-color: var(--border2) }}
  .lnk.cal {{
    background: var(--bg2);
    color: var(--cyan);
    border: 1px solid rgba(56, 189, 248, 0.25);
    padding: 7px 10px;
  }}
  .lnk.cal:hover {{ background: rgba(56, 189, 248, 0.12) }}
  .star {{
    background: var(--bg2);
    border: 1px solid var(--border);
    color: var(--faint);
    font-size: 1rem;
    width: 34px;
    height: 34px;
    border-radius: 9px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all .15s ease;
  }}
  .star:hover {{ color: var(--yellow); border-color: var(--yellow) }}
  .star.on {{ color: var(--yellow); border-color: rgba(251, 191, 36, 0.5) }}
  
  .empty {{ text-align:center; color: var(--muted); padding: 60px 20px; display:none }}
  .disc {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    margin-top: 24px;
    font-size: .82rem;
    color: var(--muted);
  }}

  /* Dedicated NaTex Full-Page Window (#natexView) */
  #natexView {{
    display: none;
    margin-top: 18px;
    animation: fadeIn .22s ease;
  }}
  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(6px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  .natex-page-card {{
    background: linear-gradient(180deg, #191b24 0%, #12131a 100%);
    border: 1px solid rgba(255, 107, 53, 0.38);
    border-radius: 20px;
    padding: 36px 32px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.6), 0 0 40px rgba(255, 107, 53, 0.1);
  }}
  .natex-hero {{
    text-align: center;
    max-width: 780px;
    margin: 0 auto 28px;
  }}
  .natex-hero h2 {{
    font-size: 2.3rem;
    margin: 0 0 8px;
    color: #fff;
    font-weight: 850;
  }}
  .natex-tagline {{
    color: #ff9b6a;
    font-size: 1.12rem;
    font-weight: 700;
    margin-bottom: 12px;
  }}
  .natex-badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    margin: 14px 0 18px;
  }}
  .nbadge {{
    font-size: .76rem;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.12);
    color: #e2e8f0;
  }}
  .nbadge.orange {{ background: rgba(255, 107, 53, 0.15); border-color: rgba(255, 107, 53, 0.4); color: #ff9b6a }}
  .nbadge.cyan {{ background: rgba(56, 189, 248, 0.15); border-color: rgba(56, 189, 248, 0.4); color: var(--cyan) }}
  .nbadge.green {{ background: rgba(46, 204, 113, 0.15); border-color: rgba(46, 204, 113, 0.4); color: var(--green) }}

  .natex-gif-wrap {{
    max-width: 920px;
    margin: 0 auto 32px;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(255, 107, 53, 0.35);
    box-shadow: 0 14px 40px rgba(0,0,0,0.65);
    background: #000;
  }}
  .natex-showcase-gif {{
    width: 100%;
    height: auto;
    display: block;
  }}
  .natex-section-title {{
    text-align: center;
    font-size: 1.35rem;
    font-weight: 800;
    color: #fff;
    margin: 0 0 20px;
  }}
  .natex-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
    gap: 16px;
    margin-bottom: 30px;
  }}
  .natex-feat {{
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 18px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
    transition: border-color .15s ease, transform .15s ease;
  }}
  .natex-feat:hover {{
    border-color: rgba(255, 107, 53, 0.4);
    transform: translateY(-2px);
  }}
  .natex-feat-icon {{
    font-size: 1.65rem;
    line-height: 1;
    background: rgba(255, 107, 53, 0.12);
    border: 1px solid rgba(255, 107, 53, 0.25);
    padding: 10px;
    border-radius: 12px;
    flex-shrink: 0;
  }}
  .natex-feat-title {{
    font-weight: 750;
    color: #fff;
    font-size: 0.98rem;
    margin-bottom: 5px;
  }}
  .natex-feat-desc {{
    color: var(--muted);
    font-size: 0.85rem;
    line-height: 1.45;
  }}
  .natex-cta-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    justify-content: center;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.08);
  }}
  .btn-natex-cta {{
    background: linear-gradient(135deg, #ff6b35, #ff8c5c);
    color: #fff;
    font-weight: 800;
    font-size: 1rem;
    padding: 14px 28px;
    border-radius: 12px;
    text-decoration: none;
    box-shadow: 0 4px 20px rgba(255, 107, 53, 0.45);
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 9px;
  }}
  .btn-natex-cta:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(255, 107, 53, 0.65);
  }}
  .btn-natex-sub {{
    background: rgba(255,255,255,0.06);
    color: var(--txt);
    border: 1px solid rgba(255,255,255,0.16);
    font-weight: 700;
    font-size: 0.95rem;
    padding: 14px 24px;
    border-radius: 12px;
    text-decoration: none;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }}
  .btn-natex-sub:hover {{
    background: rgba(255,255,255,0.12);
    border-color: rgba(255,255,255,0.3);
    color: #fff;
  }}

  /* Footer NaTex Studio */
  footer {{
    margin-top: 40px;
    padding-top: 22px;
    border-top: 1px solid var(--border);
    color: var(--faint);
    font-size: .82rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }}
  footer a {{
    color: var(--accent);
    text-decoration: none;
    font-weight: 700;
  }}
  footer a:hover {{ text-decoration: underline }}
  .foot-gh {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--card);
    border: 1px solid var(--border);
    padding: 6px 13px;
    border-radius: 8px;
    color: var(--txt);
  }}
  .foot-gh:hover {{
    border-color: var(--accent);
    color: var(--accent);
  }}
  
  /* Modal */
  .modal-overlay {{
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.8);
    backdrop-filter: blur(4px);
    z-index: 100;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 16px;
  }}
  .modal-overlay.open {{ display:flex }}
  .modal {{
    background: var(--bg2);
    border: 1px solid var(--border2);
    border-radius: 16px;
    max-width: 660px;
    width: 100%;
    max-height: 85vh;
    overflow-y: auto;
    padding: 26px;
    position: relative;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  }}
  .modal-close {{
    position: absolute;
    right: 16px;
    top: 16px;
    background: none;
    border: none;
    color: var(--muted);
    font-size: 1.4rem;
    cursor: pointer;
  }}
  .modal h2 {{ margin: 0 0 12px; font-size: 1.35rem; color: #fff }}
  .modal h3 {{ margin: 18px 0 6px; font-size: 1.02rem; color: var(--accent) }}
  .modal p, .modal li {{ font-size: .88rem; color: var(--muted); line-height: 1.55 }}
  .modal ul {{ padding-left: 20px; margin: 6px 0 }}
  
  @media (max-width: 900px) {{
    .main-nav {{ grid-template-columns: repeat(2, 1fr) }}
  }}
  @media (max-width: 680px) {{
    .main-nav {{ grid-template-columns: 1fr }}
    .search-row {{ flex-direction: column }}
    .header-top {{ flex-direction: column }}
    .grid {{ grid-template-columns: 1fr }}
    .natex-page-card {{ padding: 22px 16px }}
    footer {{ flex-direction: column; text-align:center }}
  }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="header-top">
    <div>
      <div class="badges-row">
        <div class="brand-badge"><img src="assets/fox.png" class="fox-icon-mini" alt="fox"> Creado por NachoFari</div>
        <div class="update-badge"><span class="pulse-dot"></span> Última actualización: {fecha_actualizacion}</div>
      </div>
      <h1>Radar <span class="q">ICF</span></h1>
      <p class="sub" id="viewSubtitle">Directorio de prácticas industriales, prácticas profesionales, becas y beneficios estudiantiles para Ingeniería Civil Física / Ingeniería Física.</p>
    </div>
    <div class="top-actions">
      <button class="btn-top btn-accent" id="btnExport">📥 Exportar Favoritos</button>
    </div>
  </div>
  
  <!-- Barra Principal de 4 Ventanas -->
  <nav class="main-nav" id="mainNav">
    <button class="nav-btn active" data-view="practicas">
      <span class="nav-icon">🏭</span>
      <div class="nav-txt">
        <span class="nav-title">Prácticas y Pasantías</span>
        <span class="nav-sub" id="navCountPracticas">Industrial y Profesional</span>
      </div>
    </button>
    <button class="nav-btn" data-view="becas">
      <span class="nav-icon">🎓</span>
      <div class="nav-txt">
        <span class="nav-title">Becas y Fondos</span>
        <span class="nav-sub" id="navCountBecas">Movilidad, Verano y Tesis</span>
      </div>
    </button>
    <button class="nav-btn" data-view="descuentos">
      <span class="nav-icon">🎁</span>
      <div class="nav-txt">
        <span class="nav-title">Descuentos Estudiantiles</span>
        <span class="nav-sub" id="navCountDesc">Software & Perks (@usm.cl)</span>
      </div>
    </button>
    <button class="nav-btn nav-natex" data-view="natex">
      <img src="assets/fox.png" class="fox-icon-nav" alt="fox">
      <div class="nav-txt">
        <span class="nav-title">NaTex Studio</span>
        <span class="nav-sub">Editor LaTeX Colaborativo</span>
      </div>
    </button>
  </nav>
</header>

<!-- VISTA CATÁLOGO (Prácticas, Becas, Descuentos) -->
<div id="catalogView">
  <div class="tabs" id="tabs"></div>
  <div class="counters" id="counters"></div>

  <div class="controls">
    <div class="search-row">
      <input class="search" id="search" type="text" placeholder="Buscar por empresa, centro de investigación, beneficio, ciudad o palabra clave…" autocomplete="off">
      <select class="area-select" id="areaSelect">
        <option value="all">Todas las áreas</option>
      </select>
    </div>
    <div class="filters">
      <div class="fgroup" id="fScope"><span class="lab">Alcance</span></div>
      <div class="sep"></div>
      <div class="fgroup" id="fStatus"><span class="lab">Estado</span></div>
    </div>
  </div>

  <div class="grid" id="grid"></div>
  <div class="empty" id="empty">Sin resultados con los filtros actuales en esta ventana.</div>

  <div class="disc">
    <strong>💡 Tip de postulación:</strong> Haz clic en <b>📅</b> en cualquier oportunidad con fecha límite para agendar el recordatorio directo en tu Google Calendar. Marca con la estrella ⭐ las opciones que te interesen (se guardan de forma privada en tu navegador) y usa <b>Exportar Favoritos</b> para respaldar tu lista.
  </div>
</div>

<!-- VISTA DEDICADA NATEX STUDIO (#natexView) -->
<div id="natexView">
  <div class="natex-page-card">
    <div class="natex-hero">
      <h2><img src="assets/fox.png" class="fox-icon-hero" alt="fox">NaTex Studio</h2>
      <div class="natex-tagline">El entorno de edición LaTeX rápido, visual, libre y colaborativo</div>
      <div class="natex-badges">
        <span class="nbadge orange">Versión v1.3.0</span>
        <span class="nbadge green">100% Gratuito & Open Source</span>
        <span class="nbadge cyan">Compilador Tectonic</span>
        <span class="nbadge">Colaboración en Tiempo Real</span>
        <span class="nbadge">21 Temas Personalizables</span>
      </div>
      <p style="color:var(--muted); font-size:0.95rem; line-height:1.55; margin:0 auto">
        Creado por <b>NachoFari</b> especialmente para estudiantes de física, matemáticas e ingeniería. Redacta informes de laboratorio, papers IEEE, presentaciones Beamer y memorias de título sin instalaciones pesadas de TeX Live ni suscripciones mensuales.
      </p>
      <div class="natex-cta-row" style="border-top:none; padding-top:18px; margin-bottom:6px">
        <a href="https://github.com/NachoFari/NaTex" target="_blank" rel="noopener" class="btn-natex-cta">
          <svg height="20" width="20" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
          Explorar en GitHub & Dar Estrella ⭐
        </a>
        <a href="https://github.com/NachoFari/NaTex/releases/latest" target="_blank" rel="noopener" class="btn-natex-sub">
          📥 Descargar Instalador Windows (.exe)
        </a>
      </div>
    </div>

    <div class="natex-gif-wrap">
      <img src="assets/gallery_showcase.gif" onerror="this.src='https://raw.githubusercontent.com/NachoFari/NaTex/main/docs/screenshots/gallery_showcase.gif'" alt="Demostración de NaTex Studio en acción" class="natex-showcase-gif">
    </div>

    <h3 class="natex-section-title">¿Por qué se recomienda NaTex Studio?</h3>
    <div class="natex-grid">
      <div class="natex-feat">
        <div class="natex-feat-icon">👥</div>
        <div>
          <div class="natex-feat-title">Colabora con Quien Quieras y Cuantos Quieras</div>
          <div class="natex-feat-desc">Edición simultánea en tiempo real sin límites de participantes. Comparte un enlace o código QR y trabaja en equipo en tus informes de física y proyectos de ingeniería.</div>
        </div>
      </div>

      <div class="natex-feat">
        <div class="natex-feat-icon">⌨️</div>
        <div>
          <div class="natex-feat-title">Teclado para Fórmulas Matemáticas</div>
          <div class="natex-feat-desc">Más de 300 símbolos y estructuras en 10 categorías científicas (Cálculo, Álgebra Lineal, Física Cuántica Bra-Ket, Matrices y Griegas) con vista previa KaTeX en vivo.</div>
        </div>
      </div>

      <div class="natex-feat">
        <div class="natex-feat-icon">🎨</div>
        <div>
          <div class="natex-feat-title">Full Customización: 21 Temas a tu Gusto</div>
          <div class="natex-feat-desc">Adapta tu entorno de estudio con 21 temas oscuros y claros, mascotas pixel-art de 32x32 (Zorro Clásico, Sakura, Dino Jade, Cosmos Estelar, Pantera OLED) y partículas ambientales.</div>
        </div>
      </div>

      <div class="natex-feat">
        <div class="natex-feat-icon">📊</div>
        <div>
          <div class="natex-feat-title">Editor Visual de Tablas Científicas</div>
          <div class="natex-feat-desc">Crea tablas de datos experimentales de forma interactiva o pega celdas directamente desde hojas de cálculo (Ctrl+V) para obtener el código LaTeX formateado al instante.</div>
        </div>
      </div>

      <div class="natex-feat">
        <div class="natex-feat-icon">⚡</div>
        <div>
          <div class="natex-feat-title">Compilación Ultrarrápida sin TeX Live</div>
          <div class="natex-feat-desc">Olvídate de instalar 6 GB de paquetes. Su motor Tectonic descarga bajo demanda solo lo necesario y compila tu documento en milisegundos con SyncTeX bidireccional.</div>
        </div>
      </div>

      <div class="natex-feat">
        <div class="natex-feat-icon">🤖</div>
        <div>
          <div class="natex-feat-title">Plantillas Académicas & Asistente IA</div>
          <div class="natex-feat-desc">Incluye 10 plantillas listas (Paper IEEE, Tesis, Informe de Laboratorio, Pósters de Congreso, Beamer) y diagnóstico inteligente de errores de compilación en 1 clic.</div>
        </div>
      </div>
    </div>

    <div class="natex-cta-row">
      <a href="https://github.com/NachoFari/NaTex" target="_blank" rel="noopener" class="btn-natex-cta">
        Ir al Repositorio Oficial github.com/NachoFari/NaTex ↗
      </a>
    </div>
  </div>
</div>

<footer>
  <div>
    <b>Radar ICF</b> · Última actualización: <b>{fecha_actualizacion}</b> · Creado por <b>NachoFari</b>
  </div>
  <div style="display:flex; gap:8px; flex-wrap:wrap">
    <a href="https://github.com/NachoFari/NaTex" target="_blank" rel="noopener" class="foot-gh">
      <img src="assets/fox.png" class="fox-icon-mini" alt="fox"> Proyecto NaTex
    </a>
    <a href="https://github.com/NachoFari" target="_blank" rel="noopener" class="foot-gh">
      <svg height="15" width="15" viewBox="0 0 16 16" fill="currentColor" style="vertical-align:text-bottom"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
      github.com/NachoFari
    </a>
  </div>
</footer>
</div>

<script>
const EDITION = "{hoy.isoformat()}";
const DATA = {data_json_str};

const today = new Date(); today.setHours(0,0,0,0);
const fmt = new Intl.DateTimeFormat("es-CL", {{day:"numeric", month:"short", year:"numeric"}});
const KIND = {{beca:"Beca / Fondo", ind:"Práctica industrial", prof:"Práctica profesional", desc:"Descuento Estudiantil"}};
const favs = new Set(JSON.parse(localStorage.getItem("radarFisica_favs")||"[]"));
const saveFavs = ()=>localStorage.setItem("radarFisica_favs", JSON.stringify([...favs]));

DATA.forEach(o=>{{
  o.id = o.name;
  if(o.deadline){{
    o._days = Math.ceil((new Date(o.deadline+"T23:59:59") - today)/864e5);
    if(o._days < 0){{
      o.status = "reabre";
      o.note = (o.note ? o.note+" " : "") + "(plazo cerrado)";
      o.deadline = null;
      o._days = null;
    }}
  }}
}});

const order = {{abierta:0, permanente:1, reabre:2}};
DATA.sort((a,b)=>{{
  // Keep NaTex Studio first inside discounts
  if(a.name.startsWith("NaTex")) return -1;
  if(b.name.startsWith("NaTex")) return 1;
  return order[a.status]-order[b.status] || (a._days??999)-(b._days??999);
}});

function badge(o){{
  if(o.kind && o.kind.includes("desc")) return {{cls:"b-green", main:"Beneficio activo", sub:"acceso directo"}};
  if(o.status==="permanente") return {{cls:"b-gray", main:"Permanente", sub:"acceso continuo"}};
  if(o.status==="reabre") return {{cls:"b-purple", main:"Reabre pronto", sub:"vigilar portal"}};
  if(!o.deadline) return {{cls:"b-green", main:"Abierta", sub:"ver portal"}};
  try {{
    const d = o._days;
    const cls = (d!=null && d<=7) ? "b-red" : (d!=null && d<=21) ? "b-orange" : "b-green";
    const dateObj = new Date(o.deadline+"T12:00:00");
    if(isNaN(dateObj.getTime())) return {{cls:"b-green", main:"Abierta", sub:"ver portal"}};
    const sub = d===0 ? "¡hoy!" : d===1 ? "mañana" : (d!=null ? d+" días" : "activa");
    return {{cls, main:fmt.format(dateObj), sub}};
  }} catch(e) {{
    return {{cls:"b-green", main:"Abierta", sub:"ver portal"}};
  }}
}}

// Main state: view can be 'practicas' | 'becas' | 'descuentos' | 'natex'
const state = {{view:"practicas", subKind:"all", q:"", area:"all", scope:"all", status:"all"}};

function belongsToView(o, viewName){{
  if(viewName==="practicas") return o.kind.includes("prof") || o.kind.includes("ind");
  if(viewName==="becas") return o.kind.includes("beca");
  if(viewName==="descuentos") return o.kind.includes("desc");
  return false;
}}

function updateNavCounts(){{
  const nPrac = DATA.filter(o=>belongsToView(o, "practicas")).length;
  const nBeca = DATA.filter(o=>belongsToView(o, "becas")).length;
  const nDesc = DATA.filter(o=>belongsToView(o, "descuentos")).length;
  document.getElementById("navCountPracticas").textContent = `${{nPrac}} lugares (Industrial / Profesional)`;
  document.getElementById("navCountBecas").textContent = `${{nBeca}} programas y fondos`;
  document.getElementById("navCountDesc").textContent = `${{nDesc}} beneficios (@usm.cl y más)`;
}}

function buildTabs(){{
  const viewItems = DATA.filter(o=>belongsToView(o, state.view));
  const favCount = viewItems.filter(o=>favs.has(o.id)).length;
  let defs = [];
  if(state.view==="practicas"){{
    defs = [
      ["all","Todas las Prácticas", viewItems.length],
      ["prof","Práctica Profesional", viewItems.filter(o=>o.kind.includes("prof")).length],
      ["ind","Práctica Industrial", viewItems.filter(o=>o.kind.includes("ind")).length],
      ["fav","⭐ Favoritos", favCount]
    ];
  }} else if(state.view==="becas"){{
    defs = [
      ["all","Todas las Becas y Fondos", viewItems.length],
      ["fav","⭐ Favoritos", favCount]
    ];
  }} else if(state.view==="descuentos"){{
    defs = [
      ["all","Todos los Descuentos y Perks", viewItems.length],
      ["fav","⭐ Favoritos", favCount]
    ];
  }}
  document.getElementById("tabs").innerHTML = defs.map(([k,l,n])=>{{
    return `<div class="tab${{state.subKind===k?' on':''}}" data-k="${{k}}"><div class="l">${{l}}</div><div class="n">${{n}}</div></div>`;
  }}).join("");
}}

document.getElementById("tabs").addEventListener("click", e=>{{
  const t = e.target.closest(".tab"); if(!t) return;
  state.subKind = t.dataset.k;
  render();
}});

function buildAreaSelect(){{
  const select = document.getElementById("areaSelect");
  const viewItems = DATA.filter(o=>belongsToView(o, state.view));
  const areas = [...new Set(viewItems.map(o=>o.area))].sort();
  if(state.area !== "all" && !areas.includes(state.area)){{
    state.area = "all";
  }}
  select.innerHTML = `<option value="all">Todas las áreas (${{viewItems.length}})</option>` + 
    areas.map(a=>{{
      const count = viewItems.filter(o=>o.area===a).length;
      return `<option value="${{a}}"${{state.area===a?' selected':''}}>${{a}} (${{count}})</option>`;
    }}).join("");
}}

document.getElementById("areaSelect").addEventListener("change", e=>{{
  state.area = e.target.value;
  render();
}});

document.getElementById("mainNav").addEventListener("click", e=>{{
  const btn = e.target.closest(".nav-btn");
  if(!btn) return;
  const v = btn.dataset.view;
  state.view = v;
  state.subKind = "all";
  state.area = "all";
  document.querySelectorAll("#mainNav .nav-btn").forEach(b=>b.classList.toggle("active", b.dataset.view===v));
  
  const catView = document.getElementById("catalogView");
  const natView = document.getElementById("natexView");
  const subTxt = document.getElementById("viewSubtitle");

  if(v==="natex"){{
    catView.style.display = "none";
    natView.style.display = "block";
    subTxt.textContent = "Conoce NaTex Studio: El entorno de edición LaTeX colaborativo, visual y personalizable creado por NachoFari.";
  }} else {{
    catView.style.display = "block";
    natView.style.display = "none";
    if(v==="practicas") subTxt.textContent = "Empresas, centros de I+D, observatorios y faenas para realizar tu Práctica Industrial o Práctica Profesional.";
    if(v==="becas") subTxt.textContent = "Becas de movilidad internacional, pasantías de investigación financiadas y fondos para tesis/emprendimiento.";
    if(v==="descuentos") subTxt.textContent = "Software científico gratuito, licencias Pro y descuentos estudiantiles utilizando tu correo institucional (@usm.cl u otra universidad).";
    buildAreaSelect();
    render();
  }}
}});

function buildChips(id, items, key){{
  const c = document.getElementById(id);
  [["all","Todas"],...items.map(x=>Array.isArray(x)?x:[x,x])].forEach(([v,l])=>{{
    const el = document.createElement("span");
    el.className = "chip" + (v==="all"?" on":"");
    el.textContent = l;
    el.dataset.val = v;
    c.appendChild(el);
  }});
  c.addEventListener("click", e=>{{
    if(!e.target.dataset.val) return;
    state[key] = e.target.dataset.val;
    c.querySelectorAll(".chip").forEach(ch=>ch.classList.toggle("on", ch.dataset.val===state[key]));
    render();
  }});
}}
buildChips("fScope", ["Chile","Internacional"], "scope");
buildChips("fStatus", [["abierta","Abiertas"],["permanente","Permanentes"],["reabre","Reabren"]], "status");

document.getElementById("search").addEventListener("input", e=>{{
  state.q = e.target.value.toLowerCase().trim();
  render();
}});

const esc = s => (s||"").replace(/[&<>"]/g, c=>({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}}[c]));

function match(o){{
  if(!belongsToView(o, state.view)) return false;
  if(state.subKind==="fav"){{
    if(!favs.has(o.id)) return false;
  }} else if(state.subKind!=="all"){{
    if(!o.kind.includes(state.subKind)) return false;
  }}
  if(state.area!=="all" && o.area!==state.area) return false;
  if(state.scope!=="all" && o.scope!==state.scope) return false;
  if(state.status!=="all" && o.status!==state.status) return false;
  if(state.q){{
    const hay = (o.name+" "+o.org+" "+o.city+" "+o.desc+" "+o.area+" "+(o.req||"")+" "+(o.note||"")).toLowerCase();
    if(!hay.includes(state.q)) return false;
  }}
  return true;
}}

function getGCalUrl(o){{
  if(!o.deadline) return null;
  const d = o.deadline.replace(/-/g,"");
  const dates = d + "/" + d;
  const title = encodeURIComponent("Deadline: " + o.name);
  const details = encodeURIComponent(o.desc + "\\n\\nEnlace: " + o.apply);
  const loc = encodeURIComponent(o.org + " (" + o.city + ")");
  return `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${{title}}&dates=${{dates}}&details=${{details}}&location=${{loc}}`;
}}

function card(o){{
  try {{
    const b = badge(o);
    let mainKind = (o.kind && o.kind[0]) || "prof";
    if(state.view==="practicas" && o.kind.includes("prof") && !o.kind.includes("ind")) mainKind = "prof";
    if(state.view==="practicas" && o.kind.includes("ind")) mainKind = "ind";
    if(state.view==="becas") mainKind = "beca";
    if(state.view==="descuentos") mainKind = "desc";

    const kt = (o.kind || []).map(k=>`<span class="tag t-${{k}}">${{KIND[k]||k}}</span>`).join("");
    const gcal = getGCalUrl(o);
    
    return `<div class="card k-${{mainKind}}${{favs.has(o.id)?' fav':''}}">
      <div class="card-top">
        <div>
          <div class="inst">${{esc(o.name)}}</div>
          <div class="pi">${{esc(o.org)}}</div>
        </div>
        <div class="badge ${{b.cls}}">${{esc(b.main)}}<small>${{esc(b.sub)}}</small></div>
      </div>
      <div class="tags">
        ${{kt}}
        <span class="tag area">${{esc(o.area)}}</span>
        <span class="tag">📍 ${{esc(o.city)}}</span>
        <span class="tag">${{esc(o.scope)}}</span>
      </div>
      <div class="desc">${{esc(o.desc)}}</div>
      <div class="fund">💰 ${{esc(o.fund)}}</div>
      ${{o.req ? `<div class="req"><b>Requisitos:</b> ${{esc(o.req)}}</div>` : ""}}
      ${{o.note ? `<div class="note">${{esc(o.note)}}</div>` : ""}}
      <div class="links">
        ${{o.kind && o.kind.includes("desc") ? `
          <a class="lnk apply" href="${{esc(o.apply)}}" target="_blank" rel="noopener">LINK ↗</a>
        ` : `
          <a class="lnk apply" href="${{esc(o.apply)}}" target="_blank" rel="noopener">Postular / Info</a>
          <a class="lnk src" href="${{esc(o.src)}}" target="_blank" rel="noopener">Fuente</a>
        `}}
        ${{gcal ? `<a class="lnk cal" href="${{gcal}}" target="_blank" rel="noopener" title="Agendar deadline en Google Calendar">📅</a>` : ""}}
        <button class="star${{favs.has(o.id)?' on':''}}" data-id="${{esc(o.id)}}" title="Guardar en favoritos">★</button>
      </div>
    </div>`;
  }} catch(err) {{
    console.error("Error rendering card:", o, err);
    return "";
  }}
}}

document.getElementById("grid").addEventListener("click", e=>{{
  const s = e.target.closest(".star"); if(!s) return;
  const id = s.dataset.id;
  favs.has(id) ? favs.delete(id) : favs.add(id);
  saveFavs();
  render();
}});

function buildCounters(list){{
  const ab = list.filter(o=>o.status==="abierta");
  const defs = [
    ["c-red", ab.filter(o=>o._days<=7).length, "≤ 7 días"],
    ["c-orange", ab.filter(o=>o._days>7 && o._days<=21).length, "≤ 21 días"],
    ["c-green", ab.length, "con plazo abierto"],
    ["c-gray", list.filter(o=>o.status==="permanente").length, "permanentes"],
    ["c-purple", list.filter(o=>o.status==="reabre").length, "reabren pronto"]
  ];
  document.getElementById("counters").innerHTML = defs.map(([c,n,l])=>{{
    return `<div class="counter ${{c}}"><b>${{n}}</b>${{l}}</div>`;
  }}).join("");
}}

function render(){{
  updateNavCounts();
  buildTabs();
  const list = DATA.filter(match);
  buildCounters(list);
  document.getElementById("grid").innerHTML = list.map(card).join("");
  document.getElementById("empty").style.display = list.length ? "none" : "block";
}}

document.getElementById("btnExport").addEventListener("click", ()=>{{
  if(favs.size===0){{
    alert("No tienes favoritos guardados aún. Haz clic en la estrella ⭐ de cualquier oportunidad para guardarla.");
    return;
  }}
  const favItems = DATA.filter(o=>favs.has(o.id));
  let text = "=== MIS OPORTUNIDADES GUARDADAS · RADAR ICF (NachoFari) ===\\n\\n";
  favItems.forEach((o, i)=>{{
    text += `${{i+1}}. ${{o.name}} — ${{o.org}}\\n`;
    text += `   Área: ${{o.area}} | Ámbito: ${{o.scope}} (${{o.city}})\\n`;
    text += `   Plazo: ${{o.deadline || o.status}}\\n`;
    text += `   Postular: ${{o.apply}}\\n\\n`;
  }});
  navigator.clipboard.writeText(text).then(()=>{{
    alert(`¡Se copiaron ${{favItems.length}} favoritos al portapapeles!`);
  }}).catch(()=>{{
    alert(text);
  }});
}});

buildAreaSelect();
render();
</script>
</body>
</html>"""

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated new 4-window Radar ICF index.html successfully.")
