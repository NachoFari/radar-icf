# -*- coding: utf-8 -*-
import json
import re

# Read data.js and clean it up into a proper Python list of dicts
raw_js = open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.js', encoding='utf-8').read()

# We need to parse all objects from data.js
# Let's inspect data.js lines to extract entries
entries = []

# Pattern to extract object literals
# We can find all {kind:...} or {"kind":...}
# Let's write a robust parser
# Since data.js has valid JS object literals, let's normalize keys and values
lines = raw_js.splitlines()
current_obj_str = ""
in_obj = False

for line in lines:
    stripped = line.strip()
    if stripped.startswith("//") or not stripped:
        continue
    if "const DATA =" in stripped or stripped == "];":
        continue
    if stripped.startswith("{"):
        in_obj = True
        current_obj_str = line
        if stripped.endswith("},") or stripped.endswith("}"):
            entries.append(current_obj_str)
            current_obj_str = ""
            in_obj = False
    elif in_obj:
        current_obj_str += "\n" + line
        if stripped.endswith("},") or stripped.endswith("}"):
            entries.append(current_obj_str)
            current_obj_str = ""
            in_obj = False

print(f"Parsed {len(entries)} raw entries from data.js")

# Now let's parse each entry into a Python dict
parsed_items = []
for idx, entry_str in enumerate(entries):
    s = entry_str.strip()
    if s.endswith(","):
        s = s[:-1].strip()
    
    # If it's pure JSON
    try:
        obj = json.loads(s)
        parsed_items.append(obj)
        continue
    except Exception:
        pass
    
    # Otherwise, convert JS keys to JSON keys: kind: -> "kind":
    # Replace unquoted keys with quoted keys
    def repl_key(match):
        return f'"{match.group(1)}":'
    
    # Matches key followed by colon
    converted = re.sub(r'([a-zA-Z0-9_]+)\s*:', repl_key, s)
    # Fix trailing commas inside lists or objects
    converted = re.sub(r',\s*([\]\}])', r'\1', converted)
    
    try:
        obj = json.loads(converted)
        parsed_items.append(obj)
    except Exception as e:
        print(f"Error parsing item {idx}: {e}\nString was:\n{converted[:150]}...")

print(f"Successfully converted {len(parsed_items)} items to dicts.")

# Let's check unique names to ensure no duplicates
seen_names = set()
unique_items = []
for it in parsed_items:
    name = it.get("name")
    if name not in seen_names:
        seen_names.add(name)
        unique_items.append(it)

print(f"Total unique items: {len(unique_items)}")

# Let's save unique_items as clean JSON
with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.json', 'w', encoding='utf-8') as f:
    json.dump(unique_items, f, ensure_ascii=False, indent=2)

print("Saved clean data.json")
