# -*- coding: utf-8 -*-
import json
import re

# Load current data
with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', encoding='utf-8') as f:
    current_data = json.load(f)

print(f"Initial items: {len(current_data)}")

# 1. Filter out Chilean governmental scholarships & USM internal scholarships
# We remove: area == "Becas estatales", area == "Becas USM", and any item with internal USM arancel/ayudantia
filtered = []
for o in current_data:
    area = o.get("area", "")
    name = o.get("name", "")
    org = o.get("org", "")
    
    # Remove governmental scholarships
    if area == "Becas estatales":
        continue
    # Remove USM internal scholarships
    if area == "Becas USM":
        continue
    if "FUAS" in name or "Gratuidad" in name or "Beca Bicentenario" in name or "Juan Gómez Millas" in name:
        continue
    if "BAES" in name or "Presidente de la República" in name or "Beca Indígena" in name or "TNE" in name:
        continue
    if "Arancel Ajustado" in name or "Beca de Matrícula USM" in name or "Becas internas de apoyo USM" in name or "Ayudantías Depto. de Física USM" in name:
        continue
    if "Intercambio Estudiantil UTFSM" in name:
        # We can generalize this to "Convenios Bilaterales de Intercambio Universitario"
        o["name"] = "Programas de Intercambio Bilateral y Movilidad Internacional"
        o["org"] = "Direcciones de Relaciones Internacionales (Universidades Chilenas)"
        o["desc"] = "Semestre o año académico de intercambio en universidades socias de Europa, América y Asia con exención de arancel en destino y posibles becas Erasmus+ KA171."
        o["req"] = "Tener al menos el 40-50% del plan de estudios aprobado en tu universidad; buen rendimiento académico e idioma según destino."
    
    # Remove UTFSM specific tag in general labs
    if "Laboratorios Experimentales Depto. de Física UTFSM" in name:
        o["name"] = "Laboratorios de Investigación Universitaria (Estadías de I+D)"
        o["org"] = "Departamentos e Institutos de Física en Chile (UChile, PUC, UdeC, USACH, USM, etc.)"
        o["desc"] = "Estadías de investigación de verano o semestrales en laboratorios de materia condensada, magnetismo, óptica aplicada y plasmas en universidades nacionales."
        o["city"] = "Santiago / Valparaíso / Concepción"
    
    if "CCTVal" in name:
        o["desc"] = "Desarrollo de detectores para el experimento ATLAS en CERN, electrónica rápida, supercómputo y física médica experimental. Abierto a tesistas y practicantes de diversas universidades."

    filtered.append(o)

print(f"Items after removing state & internal USM becas: {len(filtered)}")

# 2. Add New Deep Tech, Geofísica, END, and Patentes items
new_items = [
    # --- Deep Tech & Hardware Cuántico / Microelectrónica ---
    {
        "kind": ["prof"],
        "name": "SeQure Quantum (Criptografía Cuántica & QRNG)",
        "org": "SeQure Quantum (Spin-off UdeC / MIRO)",
        "area": "Deep Tech y Hardware",
        "scope": "Chile",
        "city": "Concepción / Santiago / Remoto",
        "desc": "Pioneros en América Latina en hardware de ciberseguridad cuántica: desarrollo de generadores cuánticos de números aleatorios (QRNG), óptica integrada y criptografía post-cuántica (PQC).",
        "fund": "Práctica remunerada / contratos para tesistas y desarrolladores de hardware",
        "req": "Estudiante de ingeniería física, óptica o electrónica; bases en óptica cuántica, física de semiconductores o programación de hardware.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://sequrequantum.com/",
        "src": "https://sequrequantum.com/",
        "note": "Spin-off premiado como Startup del Año; contacto a través de su formulario o LinkedIn."
    },
    {
        "kind": ["prof", "ind"],
        "name": "CoreDevX (Computación Cuántica, Robótica & IA)",
        "org": "CoreDevX — Lab de I+D y Tecnologías de Frontera",
        "area": "Deep Tech y Hardware",
        "scope": "Chile",
        "city": "Santiago (Providencia)",
        "desc": "Centro de desarrollo e innovación aplicada: investigación y prototipado en computación cuántica (algoritmos Qiskit), robótica con ROS e integración de modelos de IA con hardware.",
        "fund": "Práctica profesional y pasantías remuneradas",
        "req": "Estudiantes de ingeniería con sólidos conocimientos en Python, física computacional, robótica o computación cuántica.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://coredevx.com/site/",
        "src": "https://coredevx.com/",
        "note": "Mantienen convenios de pasantías con universidades chilenas; vacantes en Get on Board y portal corporativo."
    },
    {
        "kind": ["prof"],
        "name": "Synopsys Chile (Diseño de Microchips & EDA)",
        "org": "Synopsys Inc. — Centro de I+D Chile",
        "area": "Deep Tech y Hardware",
        "scope": "Chile",
        "city": "Santiago (Vitacura)",
        "desc": "Líder mundial en automatización del diseño electrónico (EDA) y semiconductores. En su centro de Vitacura desarrollan algoritmos para la física y modelamiento de circuitos integrados a escala nanométrica.",
        "fund": "Pasantías de alto nivel remuneradas + beneficios",
        "req": "Estudiante de ingeniería civil física, eléctrica o informática; física del estado sólido, microelectrónica, C++ o Python.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.synopsys.com/careers.html",
        "src": "https://www.synopsys.com/",
        "note": "Convenios con centros como AC3E y universidades chilenas para memorias y pasantías en microelectrónica."
    },
    {
        "kind": ["prof"],
        "name": "Lihuen Quantum (Láseres & Hardware Óptico Cuántico)",
        "org": "Lihuen Quantum (Startup Ciencia ANID)",
        "area": "Deep Tech y Hardware",
        "scope": "Chile",
        "city": "Concepción / Santiago",
        "desc": "Fabricación nacional de sistemas láser ultraestables e instrumentación óptica de precisión para laboratorios de información cuántica y metrología.",
        "fund": "Asignación según fondos de proyecto ANID",
        "req": "Estudiantes de física o ingeniería con experiencia de laboratorio en láseres, óptica y montajes experimentales.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://uchile.cl",
        "src": "https://anid.cl",
        "note": "Iniciativa surgida en laboratorios de física de la UdeC y U. de Chile con apoyo de Startup Ciencia."
    },
    {
        "kind": ["prof", "ind"],
        "name": "MiningTAG & Enaex Robótica (Sensores & Robótica Extrema)",
        "org": "MiningTAG · Enaex Robotics",
        "area": "Deep Tech y Hardware",
        "scope": "Chile",
        "city": "Santiago / Faenas",
        "desc": "Diseño y fabricación de hardware tecnológico chileno: sensores de telemetría física subterránea (RFID de largo alcance, acústica) y robots autónomos para carguío de explosivos.",
        "fund": "Práctica remunerada",
        "req": "Ingeniería física, electrónica o mecánica; programación en C/Python y ensamblaje de sensores.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://miningtag.com/",
        "src": "https://enaex.com/",
        "note": "Oportunidades publicadas en sus plataformas o envío de CV a talento joven."
    },

    # --- Geofísica de Exploración y Prospección ---
    {
        "kind": ["prof", "ind"],
        "name": "Southern Rock Geophysics (Exploración Geofísica)",
        "org": "Southern Rock Geophysics",
        "area": "Geofísica de Exploración",
        "scope": "Chile",
        "city": "Santiago / Antofagasta",
        "desc": "Adquisición y procesamiento de datos geofísicos de alta resolución para la gran minería y aguas subterráneas: magnetometría terrestre/drone, sondeos electromagnéticos (TEM) y gravimetría.",
        "fund": "Práctica remunerada + viáticos y traslados de faena",
        "req": "Estudiantes de ingeniería física, geofísica o geología; electromagnetismo clásico, física de ondas y disponibilidad para terreno.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://southernrockgeophysics.com/",
        "src": "https://southernrockgeophysics.com/",
        "note": "Física experimental aplicada directamente en campañas en el norte de Chile."
    },
    {
        "kind": ["prof", "ind"],
        "name": "Zonge International Chile (Métodos Eléctricos & EM)",
        "org": "Zonge International",
        "area": "Geofísica de Exploración",
        "scope": "Chile",
        "city": "Santiago / Terreno",
        "desc": "Especialistas globales en prospección eléctrica: polarización inducida compleja (CR), resistividad e inversión numérica 2D/3D para depósitos minerales y recursos hídricos.",
        "fund": "Asignación mensual de práctica + campamento",
        "req": "Fuerte comprensión de ecuaciones de Maxwell, métodos computacionales e inversión de datos.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://zonge.com/",
        "src": "https://zonge.com/",
        "note": "Recepción continua de CV para estudiantes interesados en geofísica aplicada."
    },
    {
        "kind": ["prof", "ind"],
        "name": "Geoexploraciones / Fugro Chile",
        "org": "Geoexploraciones S.A. · Fugro",
        "area": "Geofísica de Exploración",
        "scope": "Chile",
        "city": "Santiago / Faenas mineras y marinas",
        "desc": "Prospección geofísica marina y terrestre: sísmica de refracción/reflexión (MASW), georadar (GPR), batimetría acústica e hidrogeología física.",
        "fund": "Práctica remunerada",
        "req": "Estudiante de ingeniería civil física o geofísica; seguro escolar al día.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.geoexploraciones.cl/",
        "src": "https://www.fugro.com/",
        "note": "Postulaciones a través de su portal de contacto."
    },

    # --- Ensayos No Destructivos (END) y Control de Calidad ---
    {
        "kind": ["ind", "prof"],
        "name": "SGS Chile — División Ensayos No Destructivos (END)",
        "org": "SGS del Perú y Chile",
        "area": "Ensayos No Destructivos (END)",
        "scope": "Chile",
        "city": "Santiago / Antofagasta / Concepción",
        "desc": "Ensayos físicos de integridad estructural: ultrasonido avanzado (Phased Array / TOFD), gammagrafía industrial, emisión acústica y partículas magnéticas en infraestructura crítica.",
        "fund": "Práctica profesional remunerada + seguro",
        "req": "Estudiante de física o ingeniería mecánica/materiales; bases en física ondulatoria, radiaciones y metrología.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.sgs.cl/es-es/our-services/industrial-manufacturing/industrial-and-asset-integrity-services/non-destructive-testing-ndt",
        "src": "https://www.sgs.cl/",
        "note": "Líder global en inspección técnica; vacantes frecuentes de prácticas en sus bases regionales."
    },
    {
        "kind": ["ind", "prof"],
        "name": "TÜV Rheinland Chile (Integridad de Materiales & Acústica)",
        "org": "TÜV Rheinland Group",
        "area": "Ensayos No Destructivos (END)",
        "scope": "Chile",
        "city": "Santiago (Providencia / Pudahuel)",
        "desc": "Laboratorios de física de materiales, inspección de soldaduras de alta presión, ensayos acústicos y verificación física de plantas termosolares y eólicas.",
        "fund": "Asignación mensual de práctica",
        "req": "Alumno regular de ingeniería civil; interés en física de materiales y ensayos experimentales.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.tuv.com/chile/es/",
        "src": "https://www.tuv.com/",
        "note": "Postulaciones periódicas a través de LinkedIn y portal de empleo."
    },
    {
        "kind": ["ind", "prof"],
        "name": "Bureau Veritas / CESMEC (Física de Materiales)",
        "org": "Bureau Veritas Chile · CESMEC",
        "area": "Ensayos No Destructivos (END)",
        "scope": "Chile",
        "city": "Santiago / Valparaíso / Antofagasta",
        "desc": "Laboratorio nacional de calibración y certificación: mecánica de fractura, radiografía con acelerador de partículas, espectrometría óptica y ensayos no destructivos.",
        "fund": "Práctica remunerada",
        "req": "Estudiante de ingeniería; seguro escolar.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.bureauveritas.cl/",
        "src": "https://www.bureauveritas.cl/",
        "note": "Amplia presencia en la Región de Valparaíso y Metropolitana."
    },

    # --- Propiedad Intelectual y Patentes Tecnológicas ---
    {
        "kind": ["prof"],
        "name": "INAPI — Examen de Patentes de Invención",
        "org": "Instituto Nacional de Propiedad Industrial (INAPI)",
        "area": "Propiedad Intelectual y Patentes",
        "scope": "Chile",
        "city": "Santiago (modalidad híbrida/remota)",
        "desc": "Análisis de novedad y mérito inventivo en solicitudes de patentes de nuevas tecnologías: física del estado sólido, microelectrónica, dispositivos médicos, óptica y mecánica avanzada.",
        "fund": "Convenio de práctica profesional universitaria",
        "req": "Estudiante en últimos años de ingeniería civil física o ciencias; excelente capacidad de lectura técnica analítica en español e inglés.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.inapi.cl/",
        "src": "https://www.inapi.cl/",
        "note": "Entorno ideal para entender cómo se protege y valoriza la tecnología de frontera a nivel global."
    },
    {
        "kind": ["prof"],
        "name": "Sargent & Krahn (Consultoría de Patentes Científicas)",
        "org": "Sargent & Krahn (Líder en Propiedad Intelectual)",
        "area": "Propiedad Intelectual y Patentes",
        "scope": "Chile",
        "city": "Santiago (Las Condes / Híbrido)",
        "desc": "Área de patentes e invenciones: redacción técnica y asesoría a centros científicos y empresas multinacionales para patentar hardware, nanotecnología y algoritmos.",
        "fund": "Práctica remunerada",
        "req": "Estudiantes avanzados con perfil científico-tecnológico riguroso y dominio avanzado de inglés.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.sargent.cl/",
        "src": "https://www.sargent.cl/",
        "note": "Los ingenieros físicos son sumamente valorados en estudios de patentes por su comprensión transversal de la ciencia."
    },
    {
        "kind": ["prof"],
        "name": "ClarkeModet Chile (Transferencia Tecnológica & Patentes)",
        "org": "ClarkeModet",
        "area": "Propiedad Intelectual y Patentes",
        "scope": "Chile",
        "city": "Santiago",
        "desc": "Auditoría de activos tecnológicos, vigilancia tecnológica y redacción de memorias de invención en telecomunicaciones, sensores y biotecnología.",
        "fund": "Práctica remunerada",
        "req": "Estudiante de ingeniería civil; capacidad de análisis técnico de papers y patentes.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.clarkemodet.com/contacto/chile/",
        "src": "https://www.clarkemodet.com/",
        "note": "Enviar manifestación de interés al departamento técnico de patentes."
    }
]

# Merge all
final_dataset = filtered + new_items
print(f"Total final compiled items: {len(final_dataset)}")

# Save to data.json
with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', 'w', encoding='utf-8') as f:
    json.dump(final_dataset, f, ensure_ascii=False, indent=2)

print("Saved updated data.json successfully.")
