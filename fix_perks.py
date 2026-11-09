# -*- coding: utf-8 -*-
import json

path = r"C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json"
with open(path, encoding="utf-8") as f:
    data = json.load(f)

fixes = {
    "GitHub Student Developer Pack (Copilot, JetBrains, Azure y más)": {
        "desc": "Acceso 100% gratuito a GitHub Copilot (asistente IA), licencias Pro de JetBrains, $200 USD en DigitalOcean, dominios .me gratis en Namecheap, Stripe, Termius y más de 80 herramientas líderes de desarrollo.",
        "fund": "Herramientas valoradas en más de $200.000 USD gratuitas"
    },
    "JetBrains All Products Pack (CLion, PyCharm Pro, DataSpell)": {
        "fund": "100% gratis (precio regular ~$289 USD/año)"
    },
    "Microsoft Azure for Students & Office 365 Education": {
        "desc": "$100 USD en créditos de Azure Cloud renovables anualmente sin necesidad de tarjeta de crédito, acceso gratuito a máquinas virtuales Linux/Windows, bases de datos SQL y suite Office 365 (Word, Excel, PowerPoint, 1TB OneDrive).",
        "fund": "$100 USD en créditos cloud + Office 365 ProPlus gratis"
    },
    "Notion Plus para Estudiantes (Espacio Pro Gratuito)": {
        "fund": "100% gratuito (ahorro de ~$120 USD/año)"
    },
    "Spotify Premium para Estudiantes Universitarios": {
        "fund": "50% de descuento (~$2.500 CLP/mes)"
    },
    "YouTube Premium para Estudiantes": {
        "fund": "Tarifa reducida (~$2.890 CLP/mes vs ~$4.900 CLP)"
    },
    "Apple Education Pricing & Apple Music Estudiantes": {
        "desc": "Descuentos directos en compra de Mac (MacBook Air/Pro) y iPad para educación en tiendas oficiales, además de tarifa reducida en Apple Music (~$2.250 CLP/mes) que incluye suscripción a Apple TV+ sin costo adicional.",
        "fund": "Descuentos de hasta $180.000 CLP en equipos + Apple TV+ gratis con Music"
    },
    "Tableau for Students (Tableau Desktop & Prep)": {
        "fund": "100% gratis (precio comercial ~$840 USD/año)"
    },
    "Google AI Pro / Gemini Advanced & NotebookLM Plus for Students": {
        "fund": "100% Gratuito por 12 meses para estudiantes universitarios verificados (ahorro ~$240 USD/año)"
    }
}

for item in data:
    if item["name"] in fixes:
        for k, v in fixes[item["name"]].items():
            item[k] = v

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixed dollar amounts in data.json! Total items:", len(data))
