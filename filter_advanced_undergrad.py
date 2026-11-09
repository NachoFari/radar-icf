# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', encoding='utf-8') as f:
    data = json.load(f)

# Identify items to remove
# Target: 3rd to 5th year university students looking for:
# - Prácticas industriales
# - Prácticas profesionales
# - Pasantías de investigación / fellowships remunerados internacionales
#
# REMOVE:
# - All first-year admission / high-school / PAES scholarships:
#   FUAS, Gratuidad, Beca Bicentenario, Beca Juan Gómez Millas, BEA, Beca Hijos de Profesionales, FSCU, BAES, BPR, Beca Indígena, Beca Residencia Indígena, TNE
# - Starting degree from scratch abroad (MEXT pregrado completo de 5 años con 1 año de japonés para egresados de media, GKS pregrado completo para egresados de media)
# - Internal USM tuition/support scholarships (Arancel Ajustado, Matrícula USM, Apoyo DRE)

bad_names = [
    "fuas", "gratuidad", "bicentenario", "gómez millas", "gomez millas",
    "excelencia académica", "bea", "hijos de profesionales", "fondo solidario",
    "fscu", "baes", "presidente de la república", "indígena", "tne", "arancel ajustado",
    "matrícula usm", "mext de pregrado", "global korea scholarship"
]

clean_data = []
removed = []

for o in data:
    name_l = o.get("name", "").lower()
    org_l = o.get("org", "").lower()
    desc_l = o.get("desc", "").lower()
    area = o.get("area", "")
    
    if area in ["Becas estatales", "Becas USM"]:
        removed.append(o["name"])
        continue
    
    should_remove = False
    for bn in bad_names:
        if bn in name_l:
            should_remove = True
            break
            
    # Also check if it's high school graduation / admission related
    if "ingresan a primer año" in desc_l or "egreso de enseñanza media" in desc_l or "carrera universitaria completa de 5 años en japón" in desc_l or "carrera completa en corea" in desc_l:
        should_remove = True
        
    if should_remove:
        removed.append(o["name"])
    else:
        clean_data.append(o)

print(f"Removed {len(removed)} admission/irrelevant items:")
for r in removed:
    print(" -", r)

print(f"\nRemaining clean items for 3rd-5th year: {len(clean_data)}")

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', 'w', encoding='utf-8') as f:
    json.dump(clean_data, f, ensure_ascii=False, indent=2)
