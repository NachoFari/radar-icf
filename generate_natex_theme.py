# -*- coding: utf-8 -*-
import json

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', encoding='utf-8') as f:
    items = json.load(f)

print(f"Loaded {len(items)} items for HTML generation.")
data_json_str = json.dumps(items, ensure_ascii=False, indent=2)

html_content = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Radar de Oportunidades · Ingeniería Física — Creado por NachoFari</title>
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
    margin-bottom: 8px;
    letter-spacing: .02em;
  }}
  .brand-badge .dot {{
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 8px var(--accent);
  }}
  h1 {{
    font-size: 1.95rem;
    margin: 0 0 6px;
    font-weight: 800;
    letter-spacing: -.02em;
  }}
  h1 .q {{
    background: linear-gradient(90deg, #ff7a45, #ffa154);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }}
  .sub {{ color: var(--muted); font-size: .92rem; margin: 0; max-width: 720px }}
  
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
    color: var(--accent);
    box-shadow: 0 0 12px var(--accent-glow);
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
  
  /* Tabs */
  .tabs {{ display:flex; gap: 10px; flex-wrap:wrap; margin: 22px 0 6px }}
  .tab {{
    flex: 1 1 170px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 13px 18px;
    cursor: pointer;
    transition: all .18s ease;
    user-select: none;
  }}
  .tab:hover {{
    border-color: var(--border2);
    background: var(--card2);
  }}
  .tab.on {{
    border-color: var(--accent);
    background: linear-gradient(180deg, #241c19, var(--card));
    box-shadow: 0 4px 18px var(--accent-glow);
  }}
  .tab .n {{
    font-size: 1.7rem;
    font-weight: 800;
    line-height: 1;
    color: var(--txt);
  }}
  .tab.on .n {{ color: var(--accent2) }}
  .tab .l {{
    font-size: .74rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: .06em;
    margin-top: 6px;
    font-weight: 600;
  }}
  .tab.on .l {{ color: var(--txt) }}
  
  /* Counters */
  .counters {{ display:flex; flex-wrap:wrap; gap: 8px; margin: 12px 0 6px }}
  .counter {{
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 6px 12px;
    font-size: .76rem;
    color: var(--muted);
  }}
  .counter b {{ font-size: .92rem; margin-right: 5px }}
  .c-red b {{ color: var(--red) }}
  .c-orange b {{ color: var(--accent) }}
  .c-green b {{ color: var(--green) }}
  .c-gray b {{ color: var(--muted) }}
  .c-purple b {{ color: var(--purple) }}
  
  /* Controls */
  .controls {{
    position: sticky;
    top: 0;
    z-index: 25;
    background: linear-gradient(180deg, var(--bg) 82%, rgba(14,15,19,0));
    padding: 14px 0 12px;
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
  .links {{ display:flex; gap: 7px; margin-top: auto; padding-top: 4px }}
  .lnk {{
    flex: 1;
    text-align: center;
    text-decoration: none;
    font-size: .8rem;
    font-weight: 700;
    padding: 8px 8px;
    border-radius: 8px;
    cursor: pointer;
    border: none;
    font-family: inherit;
    transition: all .15s ease;
  }}
  .lnk.apply {{
    background: linear-gradient(135deg, #ff7a45 0%, #ff5224 100%);
    color: #fff;
    box-shadow: 0 2px 8px rgba(255,107,53,0.25);
  }}
  .lnk.apply:hover {{
    filter: brightness(1.1);
    box-shadow: 0 4px 14px rgba(255,107,53,0.4);
  }}
  .lnk.src {{
    background: transparent;
    border: 1px solid var(--border2);
    color: var(--muted);
  }}
  .lnk.src:hover {{
    color: var(--txt);
    border-color: var(--accent);
  }}
  .lnk.cal {{
    flex: none;
    background: transparent;
    border: 1px solid var(--border2);
    color: var(--muted);
    padding: 0 10px;
    font-size: .85rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .lnk.cal:hover {{
    color: var(--accent);
    border-color: var(--accent);
  }}
  .star {{
    flex: none;
    background: none;
    border: 1px solid var(--border2);
    border-radius: 8px;
    color: var(--faint);
    font-size: 1rem;
    padding: 0 10px;
    cursor: pointer;
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
  
  /* Footer NaTex Studio */
  footer {{
    margin-top: 36px;
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
    padding: 5px 12px;
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
  
  @media (max-width: 680px) {{
    .search-row {{ flex-direction: column }}
    .header-top {{ flex-direction: column }}
    .grid {{ grid-template-columns: 1fr }}
    footer {{ flex-direction: column; text-align:center }}
  }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="header-top">
    <div>
      <div class="brand-badge"><span class="dot"></span> Creado por NachoFari</div>
      <h1>Radar de <span class="q">Ingeniería Física</span></h1>
      <p class="sub">Directorio de prácticas industriales, profesionales, pasantías y descuentos de software/hardware para estudiantes de física e ingeniería — Deep Tech, Finanzas Cuantitativas, Biofísica, Astronomía, Minería y Perks Universitarios.</p>
    </div>
    <div class="top-actions">
      <button class="btn-top" id="btnModal">📋 Guía de Prácticas</button>
      <button class="btn-top btn-accent" id="btnExport">📥 Exportar Favoritos</button>
    </div>
  </div>
  
  <div class="tabs" id="tabs"></div>
  <div class="counters" id="counters"></div>
</header>

<div class="controls">
  <div class="search-row">
    <input class="search" id="search" type="text" placeholder="Buscar por empresa, startup, centro de investigación, ciudad o palabra clave…" autocomplete="off">
    <select class="area-select" id="areaSelect">
      <option value="all">Todas las áreas (Todas)</option>
    </select>
  </div>
  <div class="filters">
    <div class="fgroup" id="fScope"><span class="lab">Alcance</span></div>
    <div class="sep"></div>
    <div class="fgroup" id="fStatus"><span class="lab">Estado</span></div>
  </div>
</div>

<div class="grid" id="grid"></div>
<div class="empty" id="empty">Sin resultados con los filtros actuales.</div>

<div class="disc">
  <strong>💡 Tip de postulación:</strong> Haz clic en <b>📅</b> en cualquier oportunidad con fecha límite para agendar el recordatorio directo en tu Google Calendar. Marca con la estrella ⭐ las empresas o centros que te interesen y usa <b>Exportar Favoritos</b> para respaldar tu lista de postulaciones.
</div>

<footer>
  <div>
    Desarrollado con ❤️ para la comunidad de física e ingeniería · <b>Creado por NachoFari</b>
  </div>
  <div>
    <a href="https://github.com/NachoFari" target="_blank" rel="noopener" class="foot-gh">
      <svg height="15" width="15" viewBox="0 0 16 16" fill="currentColor" style="vertical-align:text-bottom"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
      github.com/NachoFari
    </a>
  </div>
</footer>
</div>

<!-- Modal Guía de Prácticas Universal -->
<div class="modal-overlay" id="modalOverlay">
  <div class="modal">
    <button class="modal-close" id="modalClose">&times;</button>
    <h2>Guía de Prácticas para Estudiantes de Física e Ingeniería</h2>
    <p>Para convalidar tus prácticas en carreras de física e ingeniería en universidades chilenas, las pautas académicas estándar se dividen en dos niveles:</p>
    
    <h3>1. Práctica Industrial (I) — Operativa y de Procesos</h3>
    <ul>
      <li><b>Propósito:</b> Conocer el funcionamiento de plantas productivas, faenas, industrias o empresas en terreno.</li>
      <li><b>Duración típica:</b> Entre 160 y 320 horas cronológicas (4 a 8 semanas de jornada completa).</li>
      <li><b>Lugares recomendados:</b> Refinerías (ENAP), faenas mineras (Codelco, BHP, Anglo American, SQM), empresas de ensayos no destructivos (SGS, TÜV Rheinland), manufactura y plantas de energía.</li>
    </ul>

    <h3>2. Práctica Profesional (II) — Nivel Ingeniería e I+D</h3>
    <ul>
      <li><b>Propósito:</b> Resolver problemas de alto impacto utilizando modelamiento físico-matemático, análisis cuantitativo, instrumentación o desarrollo de tecnología.</li>
      <li><b>Duración típica:</b> ~320 horas cronológicas (8 semanas completas), previa a la memoria/tesis.</li>
      <li><b>Lugares recomendados:</b> Empresas Deep Tech (SeQure Quantum, Synopsys, CoreDevX), observatorios astronómicos (ALMA, ESO, Rubin), finanzas cuantitativas (Banco Central, mesas de dinero), biofísica (CINV, FALP), centros de investigación (CCTVal, AC3E, CCHEN) o pasantías en el extranjero (Max Planck, CERN).</li>
    </ul>

    <h3>Checklist Administrativo Relevante:</h3>
    <ul>
      <li><b>Validación previa:</b> Presenta el plan de trabajo a la Jefatura de Carrera o Comisión de Prácticas de tu universidad antes de comenzar.</li>
      <li><b>Seguro Escolar (Ley 16.744):</b> Es obligatorio tramitar el certificado de seguro contra accidentes universitarios con tu oficina de asuntos estudiantiles antes del primer día laboral.</li>
      <li><b>Evaluación e Informe:</b> Al terminar, tu supervisor en la empresa debe completar la pauta confidencial de evaluación y tú debes entregar el informe técnico final.</li>
    </ul>
  </div>
</div>

<script>
const EDITION = "2026-11-09";
const DATA = {data_json_str};

const today = new Date(); today.setHours(0,0,0,0);
const fmt = new Intl.DateTimeFormat("es-CL", {{day:"numeric", month:"short", year:"numeric"}});
const KIND = {{beca:"Beca / Pasantía", ind:"Práctica industrial", prof:"Práctica profesional", desc:"Descuento Estudiantil"}};
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
DATA.sort((a,b)=>order[a.status]-order[b.status] || (a._days??999)-(b._days??999));

function badge(o){{
  if(o.status==="permanente") return {{cls:"b-gray", main:"Permanente", sub:"postulación continua"}};
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

const state = {{kind:"all", q:"", area:"all", scope:"all", status:"all"}};

function buildTabs(){{
  const defs=[
    ["all","Todo",DATA.length],
    ["prof","Práctica profesional",DATA.filter(o=>o.kind.includes("prof")).length],
    ["ind","Práctica industrial",DATA.filter(o=>o.kind.includes("ind")).length],
    ["beca","Becas y Movilidad",DATA.filter(o=>o.kind.includes("beca")).length],
    ["desc","🎁 Descuentos Estudiantiles",DATA.filter(o=>o.kind.includes("desc")).length],
    ["fav","⭐ Favoritos",favs.size]
  ];
  document.getElementById("tabs").innerHTML = defs.map(([k,l,n])=>{{
    return `<div class="tab${{state.kind===k?' on':''}}" data-k="${{k}}"><div class="n">${{n}}</div><div class="l">${{l}}</div></div>`;
  }}).join("");
}}

document.getElementById("tabs").addEventListener("click", e=>{{
  const t = e.target.closest(".tab"); if(!t) return;
  state.kind = t.dataset.k;
  render();
}});

function buildAreaSelect(){{
  const select = document.getElementById("areaSelect");
  const areas = [...new Set(DATA.map(o=>o.area))].sort();
  select.innerHTML = `<option value="all">Todas las áreas (${{DATA.length}})</option>` + 
    areas.map(a=>{{
      const count = DATA.filter(o=>o.area===a).length;
      return `<option value="${{a}}">${{a}} (${{count}})</option>`;
    }}).join("");
  
  select.addEventListener("change", e=>{{
    state.area = e.target.value;
    render();
  }});
}}
buildAreaSelect();

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
  if(state.kind==="fav" ? !favs.has(o.id) : (state.kind!=="all" && !o.kind.includes(state.kind))) return false;
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
    const mainKind = (o.kind && o.kind[0]) || "prof";
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
        <a class="lnk apply" href="${{esc(o.apply)}}" target="_blank" rel="noopener">Postular / Info</a>
        <a class="lnk src" href="${{esc(o.src)}}" target="_blank" rel="noopener">Fuente</a>
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
  buildTabs();
  const list = DATA.filter(match);
  buildCounters(list);
  document.getElementById("grid").innerHTML = list.map(card).join("");
  document.getElementById("empty").style.display = list.length ? "none" : "block";
}}

const modalOverlay = document.getElementById("modalOverlay");
document.getElementById("btnModal").addEventListener("click", ()=>modalOverlay.classList.add("open"));
document.getElementById("modalClose").addEventListener("click", ()=>modalOverlay.classList.remove("open"));
modalOverlay.addEventListener("click", e=>{{ if(e.target===modalOverlay) modalOverlay.classList.remove("open"); }});

document.getElementById("btnExport").addEventListener("click", ()=>{{
  if(favs.size===0){{
    alert("No tienes favoritos guardados aún. Haz clic en la estrella ⭐ de cualquier oportunidad para guardarla.");
    return;
  }}
  const favItems = DATA.filter(o=>favs.has(o.id));
  let text = "=== MIS OPORTUNIDADES GUARDADAS · RADAR FÍSICA (NachoFari) ===\\n\\n";
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

render();
</script>
</body>
</html>"""

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated new NaTex themed index.html successfully.")
