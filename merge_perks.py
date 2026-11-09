# -*- coding: utf-8 -*-
import glob
import json
import os
from collections import Counter

base_dir = r"C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data"
data_path = os.path.join(base_dir, "data.json")

with open(data_path, encoding="utf-8") as f:
    data = json.load(f)

def classify_perk_area(item):
    text = (item.get("name", "") + " " + item.get("org", "") + " " + item.get("desc", "")).lower()
    if any(w in text for w in ["pizza", "melt", "papa john", "little caesars", "burger king", "mcdonald", "sushi", "kami", "doggis", "juan maestro", "pedidosya", "work/café", "starbucks", "goodmeal", "cheaf", "baes", "ok panda", "foodlays", "tenedor libre", "comida", "cafetería", "supermercado"]):
        return "🍕 Comida, Cafés & Delivery"
    if any(w in text for w in ["puma", "adidas", "under armour", "mawi", "bonzer", "unidays", "student beans", "librería nacional", "zapatillas", "streetwear", "vestuario", "calzado", "ropa"]):
        return "👟 Ropa, Calzado & Librería"
    if any(w in text for w in ["spotify", "youtube premium", "mubi", "tidal", "diario financiero", "la tercera", "cineplanet", "insomnia", "normandie", "cineteca", "teatro municipal", "gam", "streaming", "cine"]):
        return "🎬 Streaming, Cine & Prensa"
    if any(w in text for w in ["turbus", "flixbus", "jetsmart", "efe ", "biotren", "tne (tarjeta", "parques nacionales", "conaf", "museos estatales", "planetario usach", "mim ", "artequin", "transporte", "pasajes"]):
        return "🚌 Transporte, Viajes & Cultura"
    if any(w in text for w in ["samsung", "apple education", "apple store", "lenovo", "hp store", "isic chile", "tarjeta joven injuv", "tui santander", "cuenta fan", "tenpo", "mach", "sportlife", "uno salud", "redsalud", "ópticas", "schilling", "rotter", "salcobrand", "farmacias", "casio", "texas instruments"]):
        return "👓 Hardware, Salud & Tarjetas"
    return "💻 Software, IA & Ciencia"

for item in data:
    if "desc" in item.get("kind", []):
        item["area"] = classify_perk_area(item)
        # Normalize scope so "Chile" filter works seamlessly
        if item.get("scope") in ["Nacional", "Chile"]:
            item["scope"] = "Chile"
        else:
            item["scope"] = "Online / Global"

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

desc_items = [x for x in data if "desc" in item.get("kind", []) or "desc" in x.get("kind", [])]
print("Total items:", len(data), "Total perks:", len(desc_items))
for k, v in Counter(x["area"] for x in desc_items).items():
    print("Category count:", v)
