# -*- coding: utf-8 -*-
import json
import re

# Additional verified entries to add
extra_items = [
    {
        "kind": ["beca", "prof"],
        "name": "MPQ — Max Planck Institute of Quantum Optics",
        "org": "Max Planck Society",
        "area": "Cuántica",
        "scope": "Internacional",
        "city": "Garching, Alemania",
        "desc": "Pasantías de investigación en computación cuántica, óptica cuántica, simulación y attosegundos (laboratorios de Immanuel Bloch, Ignacio Cirac, etc.).",
        "fund": "Estipendio mensual (~€900–1.100/mes) según grupo de investigación",
        "req": "Estudiante avanzado de física, ingeniería o afines; excelente expediente y carta de motivación.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.mpq.mpg.de/career",
        "src": "https://www.mpq.mpg.de",
        "note": "Postulación por contacto directo con directores de división o vía portal de vacantes."
    },
    {
        "kind": ["beca", "prof"],
        "name": "MPI for Biophysics (Pasantías de investigación)",
        "org": "Max Planck Institute of Biophysics",
        "area": "Biofísica",
        "scope": "Internacional",
        "city": "Frankfurt am Main, Alemania",
        "desc": "Biofísica molecular y estructural, biología de membranas, criomicroscopía electrónica y simulación de dinámica molecular.",
        "fund": "Contrato de estudiante de investigación / estipendio mensual",
        "req": "Pregrado en física, biofísica o química; interés en modelamiento o técnicas experimentales avanzadas.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.biophys.mpg.de/career",
        "src": "https://www.biophys.mpg.de",
        "note": "Revisar posiciones abiertas para estudiantes de pregrado (HiWi / intern) o contactar al PI."
    },
    {
        "kind": ["prof"],
        "name": "Quantitative Trading / Research Internships",
        "org": "Jane Street · Citadel · Susquehanna (SIG)",
        "area": "Econofísica y finanzas",
        "scope": "Internacional",
        "city": "Nueva York / Londres / Remoto",
        "desc": "Trading cuantitativo y modelamiento estocástico de mercados. Buscan activamente físicos y matemáticos por su habilidad en resolución de problemas complejos.",
        "fund": "Altamente remunerada (salario competitivo global + pasajes + alojamiento corporativo)",
        "req": "Habilidades excepcionales en matemáticas, probabilidad, algoritmos (Python/C++/OCaml).",
        "deadline": "2026-12-31",
        "status": "abierta",
        "apply": "https://www.janestreet.com/join-jane-street/programs-and-events/",
        "src": "https://www.janestreet.com",
        "note": "Postulaciones abiertas para el verano del hemisferio norte (jun–ago 2027). Muy selectivo."
    },
    {
        "kind": ["prof"],
        "name": "Advanced Analytics & Quant Consulting",
        "org": "McKinsey QuantumBlack · BCG X Chile",
        "area": "Econofísica y finanzas",
        "scope": "Chile",
        "city": "Santiago",
        "desc": "Consultoría estratégica de analítica avanzada, machine learning aplicado y modelamiento predictivo en minería, retail y banca chilena.",
        "fund": "Práctica pagada (arriba del mercado local)",
        "req": "Estudiante de ingeniería civil en últimos años; sólidos conocimientos en Python, estadística y modelamiento.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://www.mckinsey.com/capabilities/quantumblack/careers",
        "src": "https://www.mckinsey.com",
        "note": "Postulaciones a través de los portales de talento joven de McKinsey y BCG Chile."
    },
    {
        "kind": ["prof"],
        "name": "Laboratorio de Biofísica y Materia Condensada Blanda",
        "org": "FCFM U. de Chile / PUC Física",
        "area": "Biofísica",
        "scope": "Chile",
        "city": "Santiago",
        "desc": "Estudios experimentales y teóricos de reología celular, motilidad bacteriana, pinzas ópticas y materia activa.",
        "fund": "Posible viático / financiamiento de proyecto FONDECYT/Millennium",
        "req": "Contacto directo con el profesor guía; convalidable como práctica profesional previa autorización USM.",
        "deadline": None,
        "status": "permanente",
        "apply": "https://fisica.fcfm.uchile.cl",
        "src": "https://fisica.fcfm.uchile.cl",
        "note": "Convenios interuniversitarios facilitan la estadía de investigación de verano."
    },
    {
        "kind": ["prof", "ind"],
        "name": "Colbún — Energía Renovable y Almacenamiento",
        "org": "Colbún S.A.",
        "area": "Energía y plasmas",
        "scope": "Chile",
        "city": "Quillota (V Región) / Santiago / Faenas",
        "desc": "Prácticas en plantas de generación térmica, parques solares/eólicos, sistemas BESS de baterías y optimización del despacho energético.",
        "fund": "Asignación mensual de práctica + transporte",
        "req": "Alumno regular; seguro escolar vigente.",
        "deadline": None,
        "status": "reabre",
        "apply": "https://www.colbun.cl/trabaja-con-nosotros",
        "src": "https://www.colbun.cl",
        "note": "Complejo Nehuenco en Quillota queda muy cercano a Valparaíso. Convocatoria de verano ~octubre."
    },
    {
        "kind": ["prof", "ind"],
        "name": "Laboratorio de Información Cuántica UdeC",
        "org": "Universidad de Concepción",
        "area": "Cuántica",
        "scope": "Chile",
        "city": "Concepción",
        "desc": "Líneas de investigación en óptica cuántica experimental, comunicación cuántica satelital y criptografía (QKD).",
        "fund": "Apoyo de proyecto según disponibilidad",
        "req": "Contacto con investigadores del grupo de óptica/cuántica.",
        "deadline": None,
        "status": "permanente",
        "apply": "http://optica.udec.cl/",
        "src": "http://optica.udec.cl/",
        "note": "Colaboran estrechamente con el Instituto Milenio MIRO."
    }
]

print(f"Added {len(extra_items)} extra specialized entries.")
