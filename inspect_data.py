import json
import re

with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.js', encoding='utf-8') as f:
    text = f.read()

# count objects
matches = re.findall(r'\{kind:\[(.*?)\]', text)
print(f"Total entries: {len(matches)}")

areas = re.findall(r'area:"(.*?)"', text)
from collections import Counter
c = Counter(areas)
print("\nAreas breakdown:")
for k, v in c.most_common():
    print(f"  - {k}: {v}")
