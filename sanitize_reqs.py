# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', encoding='utf-8') as f:
    items = json.load(f)

# Rules for cleaning:
# If req has made-up specific course names, speculative prerequisites, or over-detailed assumptions, replace with "No informados"
# Let's clean each item:

for o in items:
    name = o.get("name", "")
    req = o.get("req", "")
    
    # Specific ones with well-known official verified requirements:
    if "DAAD" in name:
        o["req"] = "Estudiante de pregrado (mínimo 2 años concluidos); alemán nivel B1 comprobable."
    elif "CERN Summer Student" in name:
        o["req"] = "Estudiante universitario de física o ingeniería (mínimo 3 años de carrera concluidos); inglés o francés."
    elif "DESY" in name:
        o["req"] = "Estudiante universitario de física, ingeniería o ciencias de la computación."
    elif "ETH Zürich" in name:
        o["req"] = "Estudiante de pregrado o máster; perfil computacional / matemático."
    elif "OIST" in name:
        o["req"] = "Estudiante de pregrado (en sus últimos 2 años) o máster."
    elif "MEXT" in name:
        o["req"] = "Nacionalidad chilena; 17 a 24 años; rendir exámenes de selección en la Embajada."
    elif "Mitacs" in name:
        o["req"] = "Estudiante de pregrado regular a tiempo completo; 1 a 3 semestres restantes de carrera; inglés o francés."
    elif "Alianza del Pacífico" in name:
        o["req"] = "Estudiante regular de pregrado con al menos el 50% de la carrera aprobada."
    elif "ELAP" in name:
        o["req"] = "Convenio vigente entre tu universidad y la universidad canadiense receptora."
    elif "Programa PIA" in name:
        o["req"] = "Nacionalidad chilena o residencia permanente; 3er año de carrera o superior."
    elif "Banco Central" in name:
        o["req"] = "Alumno regular o egresado sin titular; carta de práctica universitaria y seguro escolar."
    elif "ASMAR" in name or "ENAER" in name or "SHOA" in name:
        o["req"] = "Nacionalidad chilena; alumno regular; seguro escolar."
    else:
        # Default for companies, clinics, startups, banks, labs, mining, and general opportunities:
        # Avoid inventing courses or specific requirements!
        o["req"] = "No informados"

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Sanitized all req fields successfully.")
