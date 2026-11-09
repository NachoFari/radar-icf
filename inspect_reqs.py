# -*- coding: utf-8 -*-
import json

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total items: {len(data)}")

# Let's inspect all req fields
for i, o in enumerate(data):
    req = o.get("req", "")
    print(f"{i}: [{o.get('name')}] -> {req}")
