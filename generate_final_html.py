# -*- coding: utf-8 -*-
import json
from compile_complete_dataset import all_items

print(f"Total entries: {len(all_items)}")

# Convert all_items to JSON string to embed in HTML
data_json_str = json.dumps(all_items, ensure_ascii=False, indent=2)

html_content = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Radar ICF · Becas y Prácticas — Ingeniería Civil Física UTFSM</title>
<style>
  :root {{
    --bg:#0a0e1a; --bg2:#0f1526; --card:#141b2e; --card2:#1a2340;
    --border:#243048; --border2:#2f3d5c;
    --txt:#e6ebf5; --muted:#8a97b2; --faint:#5e6b88;
    --accent:#6ea8ff; --accent2:#9b8cff;
    --red:#ff5a6e; --orange:#ff9d42; --green:#36d399; --gray:#6b7891; --purple:#b388ff; --yellow:#ffd166;
  }}
  * {{ box-sizing:border-box }}
  body {{ margin:0; background:radial-gradient(1200px 600px at 70% -10%,#16213f 0%,var(--bg) 55%);
    color:var(--txt); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    line-height:1.5; padding:0 16px 80px }}
  .wrap {{ max-width:1180px; margin:0 auto }}
  header {{ padding:30px 0 10px }}
  .header-top {{ display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px }}
  h1 {{ font-size:1.85rem; margin:0 0 6px; font-weight:700; letter-spacing:-.02em }}
  h1 .q {{ background:linear-gradient(90deg,var(--accent),var(--accent2)); -webkit-background-clip:text; background-clip:text; color:transparent }}
  .sub {{ color:var(--muted); font-size:.95rem; margin:0 }}
  .top-actions {{ display:flex; gap:8px; align-items:center; flex-wrap:wrap }}
  .btn-top {{ background:var(--card); border:1px solid var(--border2); color:var(--txt); font-size:.8rem; font-weight:600; padding:7px 13px; border-radius:9px; cursor:pointer; transition:.15s; text-decoration:none; display:inline-flex; align-items:center; gap:6px }}
  .btn-top:hover {{ border-color:var(--accent); color:var(--accent) }}
  .edition {{ display:inline-flex; align-items:center; gap:7px; margin-top:12px; font-size:.82rem; color:var(--muted); background:var(--card); border:1px solid var(--border); padding:5px 12px; border-radius:999px }}
  .dot {{ width:7px; height:7px; border-radius:50%; background:var(--green); box-shadow:0 0 8px var(--green) }}
  
  .tabs {{ display:flex; gap:8px; flex-wrap:wrap; margin:20px 0 4px }}
  .tab {{ flex:1 1 160px; background:var(--card); border:1px solid var(--border); border-radius:14px; padding:12px 16px; cursor:pointer; transition:.15s }}
  .tab:hover {{ border-color:var(--border2) }}
  .tab.on {{ border-color:var(--accent); background:linear-gradient(180deg,#1c2a4d,var(--card)) }}
  .tab .n {{ font-size:1.6rem; font-weight:700; line-height:1 }}
  .tab .l {{ font-size:.73rem; color:var(--muted); text-transform:uppercase; letter-spacing:.05em; margin-top:6px }}
  
  .counters {{ display:flex; flex-wrap:wrap; gap:8px; margin:12px 0 6px }}
  .counter {{ background:var(--bg2); border:1px solid var(--border); border-radius:10px; padding:7px 12px; font-size:.78rem; color:var(--muted) }}
  .counter b {{ font-size:.95rem; margin-right:4px }}
  .c-red b {{ color:var(--red) }} .c-orange b {{ color:var(--orange) }} .c-green b {{ color:var(--green) }} .c-gray b {{ color:var(--gray) }} .c-purple b {{ color:var(--purple) }}
  
  .controls {{ position:sticky; top:0; z-index:20; background:linear-gradient(180deg,var(--bg) 80%,rgba(10,14,26,0)); padding:14px 0 }}
  .search-row {{ display:flex; gap:8px }}
  .search {{ flex:1; background:var(--card); border:1px solid var(--border2); border-radius:12px; color:var(--txt); font-size:.95rem; padding:12px 16px; outline:none }}
  .search:focus {{ border-color:var(--accent) }}
  .area-select {{ background:var(--card); border:1px solid var(--border2); border-radius:12px; color:var(--txt); font-size:.85rem; padding:0 14px; outline:none; cursor:pointer }}
  .area-select:focus {{ border-color:var(--accent) }}
  
  .filters {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:10px }}
  .fgroup {{ display:flex; flex-wrap:wrap; gap:6px; align-items:center }}
  .fgroup .lab {{ font-size:.7rem; color:var(--faint); text-transform:uppercase; letter-spacing:.06em; margin-right:2px }}
  .chip {{ background:var(--card); border:1px solid var(--border); color:var(--muted); font-size:.8rem; padding:5px 11px; border-radius:999px; cursor:pointer; user-select:none; transition:.15s }}
  .chip:hover {{ color:var(--txt); border-color:var(--border2) }}
  .chip.on {{ background:var(--accent); border-color:var(--accent); color:#06101f; font-weight:600 }}
  .sep {{ width:1px; background:var(--border); align-self:stretch; margin:2px 4px }}
  
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(340px,1fr)); gap:16px; margin-top:8px }}
  .card {{ background:linear-gradient(180deg,var(--card2),var(--card)); border:1px solid var(--border); border-radius:16px; padding:18px; display:flex; flex-direction:column; gap:10px; position:relative; overflow:hidden; transition:transform .15s }}
  .card:hover {{ transform:translateY(-2px) }}
  .card.fav {{ border-color:rgba(255,209,102,.5); box-shadow:0 0 12px rgba(255,209,102,.1) }}
  .card::before {{ content:""; position:absolute; left:0; top:0; bottom:0; width:3px }}
  .card.k-beca::before {{ background:var(--green) }} .card.k-ind::before {{ background:var(--orange) }} .card.k-prof::before {{ background:var(--accent2) }}
  
  .card-top {{ display:flex; justify-content:space-between; align-items:flex-start; gap:10px }}
  .inst {{ font-weight:700; font-size:1.02rem; line-height:1.3 }}
  .pi {{ color:var(--muted); font-size:.82rem; margin-top:3px }}
  .badge {{ flex:none; font-size:.72rem; font-weight:700; padding:5px 9px; border-radius:8px; white-space:nowrap; text-align:center; line-height:1.15 }}
  .badge small {{ display:block; font-weight:500; font-size:.63rem; opacity:.85 }}
  .b-red {{ background:rgba(255,90,110,.14); color:var(--red); border:1px solid rgba(255,90,110,.3) }}
  .b-orange {{ background:rgba(255,157,66,.14); color:var(--orange); border:1px solid rgba(255,157,66,.3) }}
  .b-green {{ background:rgba(54,211,153,.13); color:var(--green); border:1px solid rgba(54,211,153,.3) }}
  .b-gray {{ background:rgba(107,120,145,.14); color:var(--gray); border:1px solid rgba(107,120,145,.3) }}
  .b-purple {{ background:rgba(179,136,255,.15); color:var(--purple); border:1px solid rgba(179,136,255,.3) }}
  
  .tags {{ display:flex; flex-wrap:wrap; gap:5px }}
  .tag {{ font-size:.7rem; padding:3px 8px; border-radius:6px; background:var(--bg2); border:1px solid var(--border); color:var(--muted) }}
  .tag.t-beca {{ color:var(--green); border-color:rgba(54,211,153,.25) }}
  .tag.t-ind {{ color:var(--orange); border-color:rgba(255,157,66,.25) }}
  .tag.t-prof {{ color:var(--accent2); border-color:rgba(155,140,255,.25) }}
  .tag.area {{ color:var(--accent); font-weight:600 }}
  
  .desc {{ font-size:.86rem; opacity:.92; line-height:1.4 }}
  .fund {{ font-size:.8rem; color:var(--green); background:rgba(54,211,153,.09); border:1px solid rgba(54,211,153,.2); padding:6px 10px; border-radius:8px }}
  .req {{ font-size:.78rem; color:var(--muted); line-height:1.35 }} .req b {{ color:var(--txt); font-weight:600 }}
  .note {{ font-size:.76rem; color:var(--faint); font-style:italic }}
  
  .links {{ display:flex; gap:7px; margin-top:auto; padding-top:4px }}
  .lnk {{ flex:1; text-align:center; text-decoration:none; font-size:.8rem; font-weight:600; padding:8px 8px; border-radius:8px; cursor:pointer; border:none; font-family:inherit; transition:.15s }}
  .lnk.apply {{ background:var(--accent); color:#06101f }}
  .lnk.apply:hover {{ filter:brightness(1.1) }}
  .lnk.src {{ background:transparent; border:1px solid var(--border2); color:var(--muted) }}
  .lnk.src:hover {{ color:var(--txt); border-color:var(--accent) }}
  .lnk.cal {{ flex:none; background:transparent; border:1px solid var(--border2); color:var(--muted); padding:0 9px; font-size:.85rem; display:flex; align-items:center; justify-content:center }}
  .lnk.cal:hover {{ color:var(--accent); border-color:var(--accent) }}
  .star {{ flex:none; background:none; border:1px solid var(--border2); border-radius:8px; color:var(--faint); font-size:1rem; padding:0 10px; cursor:pointer; transition:.15s }}
  .star:hover {{ color:var(--yellow) }}
  .star.on {{ color:var(--yellow); border-color:rgba(255,209,102,.5) }}
  
  .empty {{ text-align:center; color:var(--muted); padding:60px 20px; display:none }}
  .disc {{ background:var(--card); border:1px solid var(--border); border-radius:12px; padding:14px 16px; margin-top:24px; font-size:.82rem; color:var(--muted) }}
  footer {{ margin-top:30px; padding-top:20px; border-top:1px solid var(--border); color:var(--faint); font-size:.8rem }}
  
  /* Modal Reglamento */
  .modal-overlay {{ position:fixed; inset:0; background:rgba(0,0,0,.75); z-index:100; display:none; align-items:center; justify-content:center; padding:16px }}
  .modal-overlay.open {{ display:flex }}
  .modal {{ background:var(--bg2); border:1px solid var(--border2); border-radius:16px; max-width:640px; width:100%; max-height:85vh; overflow-y:auto; padding:24px; position:relative }}
  .modal-close {{ position:absolute; right:16px; top:16px; background:none; border:none; color:var(--muted); font-size:1.4rem; cursor:pointer }}
  .modal h2 {{ margin:0 0 12px; font-size:1.3rem; color:var(--txt) }}
  .modal h3 {{ margin:16px 0 6px; font-size:1rem; color:var(--accent) }}
  .modal p, .modal li {{ font-size:.86rem; color:var(--muted); line-height:1.5 }}
  .modal ul {{ padding-left:20px; margin:6px 0 }}
  
  @media (max-width:680px) {{
    .search-row {{ flex-direction:column }}
    .header-top {{ flex-direction:column }}
    .grid {{ grid-template-columns:1fr }}
  }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="header-top">
    <div>
      <h1>Radar <span class="q">ICF UTFSM</span> · Becas y Prácticas</h1>
      <p class="sub">Oportunidades de becas de pregrado, práctica industrial y práctica profesional — Biofísica, Finanzas Cuantitativas, Max Planck, Minería, Astronomía y más</p>
      <div class="edition"><span class="dot"></span><span id="editionLabel"></span></div>
    </div>
    <div class="top-actions">
      <button class="btn-top" id="btnModal">📋 Reglamento Prácticas USM</button>
      <button class="btn-top" id="btnExport">📥 Exportar Favoritos</button>
    </div>
  </div>
  
  <div class="tabs" id="tabs"></div>
  <div class="counters" id="counters"></div>
</header>

<div class="controls">
  <div class="search-row">
    <input class="search" id="search" type="text" placeholder="Buscar por institución, empresa, ciudad, área o palabra clave…" autocomplete="off">
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
  <strong>💡 Tip para postular:</strong>
  Para las oportunidades con fecha límite, haz clic en el botón <b>📅</b> para agendar el deadline automáticamente en tu Google Calendar.
  Guarda en favoritos con la ⭐ tus opciones prioritarias y expórtalas cuando quieras.
</div>

<footer>
  Radar ICF UTFSM · Convocatorias verificadas para Ingeniería Civil Física · Edición <span id="editionFoot"></span>
</footer>
</div>

<!-- Modal Reglamento USM -->
<div class="modal-overlay" id="modalOverlay">
  <div class="modal">
    <button class="modal-close" id="modalClose">&times;</button>
    <h2>Reglamento de Prácticas · Ing. Civil Física UTFSM</h2>
    <p>Para titularte de Ingeniero Civil Físico en la Santa María debes completar dos prácticas reglamentarias aprobadas por el Departamento de Física:</p>
    
    <h3>1. Práctica Industrial (I)</h3>
    <ul>
      <li><b>Objetivo:</b> Primer contacto formal con el ambiente productivo e industrial de una organización.</li>
      <li><b>Duración:</b> ~320 horas cronológicas (equivalente a 8 semanas de jornada completa).</li>
      <li><b>Cuándo se hace:</b> Habitualmente entre el 5º y 7º semestre de la carrera.</li>
      <li><b>Ámbitos típicos:</b> Plantas de procesos, minería, manufactura, control de calidad, energías, servicios técnicos industriales.</li>
    </ul>

    <h3>2. Práctica Profesional (II)</h3>
    <ul>
      <li><b>Objetivo:</b> Aplicación de habilidades ingenieriles avanzadas (modelamiento físico-matemático, análisis cuantitativo, instrumentación, I+D).</li>
      <li><b>Duración:</b> ~320 horas cronológicas (8 semanas completas).</li>
      <li><b>Cuándo se hace:</b> En los últimos semestres, previa a la inscripción de la Memoria de Título.</li>
      <li><b>Ámbitos típicos:</b> Observatorios astronómicos, centros de investigación (CCTVal, AC3E, CINV), banca/riesgo, biofísica, física médica, data science o grandes mineras.</li>
    </ul>

    <h3>Pasos Administrativos Obligatorios:</h3>
    <ul>
      <li><b>Validación previa:</b> Verifica con la Jefatura de Carrera del Depto. de Física que las funciones propuestas califiquen para tu práctica.</li>
      <li><b>Seguro Escolar:</b> Debes tramitar con la DRE el Seguro de Accidentes de Práctica antes del primer día laboral (requisito legal en Chile).</li>
      <li><b>Inscripción en SIGA:</b> Inscribe la práctica en el portal académico institucional.</li>
      <li><b>Cierre y Aprobación:</b> Al terminar, debes entregar un Informe Técnico según la pauta del departamento y la empresa debe enviar la evaluación confidencial de tu supervisor.</li>
    </ul>
  </div>
</div>

<script>
const EDITION = "2026-10-30";
const DATA = {data_json_str};

const today = new Date(); today.setHours(0,0,0,0);
const fmt = new Intl.DateTimeFormat("es-CL",{{day:"numeric",month:"short",year:"numeric"}});
document.getElementById("editionLabel").textContent = "Base: " + EDITION + " · Fecha actual: " + fmt.format(today);
document.getElementById("editionFoot").textContent = EDITION;

const KIND = {{beca:"Beca", ind:"Práctica industrial", prof:"Práctica profesional"}};
const favs = new Set(JSON.parse(localStorage.getItem("radarICF_favs")||"[]"));
const saveFavs = ()=>localStorage.setItem("radarICF_favs", JSON.stringify([...favs]));

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
    ["beca","Becas",DATA.filter(o=>o.kind.includes("beca")).length],
    ["ind","Práctica industrial",DATA.filter(o=>o.kind.includes("ind")).length],
    ["prof","Práctica profesional",DATA.filter(o=>o.kind.includes("prof")).length],
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

// Dropdown de áreas con conteos
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
    console.error("Error rendering card for", o, err);
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

// Modal
const modalOverlay = document.getElementById("modalOverlay");
document.getElementById("btnModal").addEventListener("click", ()=>modalOverlay.classList.add("open"));
document.getElementById("modalClose").addEventListener("click", ()=>modalOverlay.classList.remove("open"));
modalOverlay.addEventListener("click", e=>{{ if(e.target===modalOverlay) modalOverlay.classList.remove("open"); }});

// Exportar favoritos
document.getElementById("btnExport").addEventListener("click", ()=>{{
  if(favs.size===0){{
    alert("No tienes favoritos guardados aún. Haz clic en la estrella ⭐ de cualquier oportunidad para guardarla.");
    return;
  }}
  const favItems = DATA.filter(o=>favs.has(o.id));
  let text = "=== MIS OPORTUNIDADES GUARDADAS (RADAR ICF UTFSM) ===\\n\\n";
  favItems.forEach((o, i)=>{{
    text += `${{i+1}}. ${{o.name}} — ${{o.org}}\\n`;
    text += `   Área: ${{o.area}} | Ámbito: ${{o.scope}} (${{o.city}})\\n`;
    text += `   Plazo: ${{o.deadline || o.status}}\\n`;
    text += `   Postular: ${{o.apply}}\\n\\n`;
  }});
  navigator.clipboard.writeText(text).then(()=>{{
    alert(`¡Se copiaron ${{favItems.length}} favoritos al portapapeles! Puedes pegarlos en WhatsApp, Notion o donde prefieras.`);
  }}).catch(()=>{{
    console.log(text);
    alert(text);
  }});
}});

render();
</script>
</body>
</html>"""

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated complete index.html successfully.")
