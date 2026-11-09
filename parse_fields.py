# -*- coding: utf-8 -*-
import json
import re

# We can parse the fields accurately with regex for each key
with open(r'C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data\data.js', encoding='utf-8') as f:
    text = f.read()

# Pattern for each object
# In data.js, each object starts with {kind:[...]
# Let's extract lines that define objects
items = []

keys = ["kind", "name", "org", "area", "scope", "city", "desc", "fund", "req", "deadline", "status", "apply", "src", "note"]

# Let's read the subagents' clean definitions or extract field by field
# Subagent 1 (international), Subagent 2 (Chile practices), Subagent 3 (Chile becas)
# We can combine the items directly from the three sources!
