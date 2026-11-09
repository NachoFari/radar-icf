# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', encoding='utf-8') as f:
    data = json.load(f)

for i, o in enumerate(data):
    print(f"{i+1:2d}. [{o['area']}] {o['name']} -> req: {o['req']}")
