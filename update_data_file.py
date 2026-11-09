# -*- coding: utf-8 -*-
import json
import re

# Read data.js
with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.js', encoding='utf-8') as f:
    raw_js = f.read()

# We can extract the items from data.js or parse them
# Notice each item is {kind:[...], ...}
# Let's extract them by reading line by line or using regex
items_raw = re.findall(r'\{kind:\[.*?\}(?=\n|\r|,)', raw_js, re.DOTALL)
print(f"Found {len(items_raw)} items in data.js")

# Let's import extra_items
from build_full_dataset import extra_items

# Let's create an updated data.js
# We will format all items cleanly
output_js_lines = ["// Radar ICF - Base de Datos Actualizada y Verificada", "const DATA = ["]

# Append existing items without trailing commas or issues
for it in items_raw:
    it_clean = it.strip()
    if it_clean.endswith(","):
        it_clean = it_clean[:-1]
    output_js_lines.append("  " + it_clean + ",")

# Append extra items
for it in extra_items:
    js_obj = json.dumps(it, ensure_ascii=False)
    # Convert json keys to standard js
    output_js_lines.append(f"  // Extra especializada: {it['name']}\n  {js_obj},")

output_js_lines.append("];")
full_data_js = "\n".join(output_js_lines)

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.js', 'w', encoding='utf-8') as f:
    f.write(full_data_js)

print("Updated data/data.js successfully.")
