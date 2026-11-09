# -*- coding: utf-8 -*-
import json
import glob
import os
import urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r"C:\Users\Nacho\.gemini\antigravity\scratch\radar-icf-usm\data"
main_json_path = os.path.join(data_dir, "data.json")

with open(main_json_path, encoding="utf-8") as f:
    base_data = json.load(f)

print(f"Base dataset items: {len(base_data)}")

cluster_files = sorted(glob.glob(os.path.join(data_dir, "cluster*.json")))
print(f"Found {len(cluster_files)} cluster files to audit and merge.")

REQUIRED_KEYS = {"kind", "name", "org", "area", "scope", "city", "desc", "fund", "req", "deadline", "status", "apply", "src", "note"}
VALID_KINDS = {"prof", "ind", "beca", "desc"}
VALID_STATUS = {"abierta", "permanente", "reabre"}

existing_names = {item["name"].strip().lower() for item in base_data}
added_count = 0
rejected_count = 0
sanitized_reqs = 0

for cf in cluster_files:
    try:
        with open(cf, encoding="utf-8") as f:
            c_items = json.load(f)
        if not isinstance(c_items, list):
            print(f"[WARN] {os.path.basename(cf)} is not a list, skipping.")
            continue
        for item in c_items:
            # 1. Structural check
            if not isinstance(item, dict) or not REQUIRED_KEYS.issubset(item.keys()):
                rejected_count += 1
                continue
            name_clean = item["name"].strip()
            if name_clean.lower() in existing_names:
                continue
            
            # 2. URL credibility check
            apply_url = (item.get("apply") or "").strip()
            src_url = (item.get("src") or "").strip()
            p_apply = urllib.parse.urlparse(apply_url)
            p_src = urllib.parse.urlparse(src_url)
            if p_apply.scheme not in ("http", "https") or not p_apply.netloc or "example.com" in p_apply.netloc:
                rejected_count += 1
                continue
            if p_src.scheme not in ("http", "https") or not p_src.netloc or "example.com" in p_src.netloc:
                item["src"] = f"{p_apply.scheme}://{p_apply.netloc}"

            # 3. Validate kind & status
            kinds = [k for k in item.get("kind", []) if k in VALID_KINDS]
            if not kinds:
                rejected_count += 1
                continue
            item["kind"] = kinds
            if item.get("status") not in VALID_STATUS:
                item["status"] = "permanente"

            # 4. Strict Requirement Sanitization (Never invent university courses)
            req_val = (item.get("req") or "No informados").strip()
            if item.get("scope") == "Chile" and "beca" not in kinds and "desc" not in kinds:
                if req_val != "No informados":
                    item["req"] = "No informados"
                    sanitized_reqs += 1
            elif any(bad in req_val.lower() for bad in ["ramos aprobados", "asignaturas de", "promedio mínimo de"]):
                if "beca" not in kinds:
                    item["req"] = "No informados"
                    sanitized_reqs += 1

            base_data.append(item)
            existing_names.add(name_clean.lower())
            added_count += 1
    except Exception as e:
        print(f"[ERROR] reading {os.path.basename(cf)}: {e}")

with open(main_json_path, "w", encoding="utf-8") as f:
    json.dump(base_data, f, ensure_ascii=False, indent=2)

print(f"Audit complete:")
print(f"  + Added verified items: {added_count}")
print(f"  * Sanitized requirements to 'No informados': {sanitized_reqs}")
print(f"  - Rejected invalid/duplicate items: {rejected_count}")
print(f"  = Total verified items in Radar ICF: {len(base_data)}")
