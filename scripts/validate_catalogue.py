#!/usr/bin/env python3
"""Validate climate-assets.json, recompute meta.counts, resync the Astro copy.

Usage:
  python3 scripts/validate_catalogue.py            # validate + recount + resync
  python3 scripts/validate_catalogue.py --check    # validate only, write nothing
  python3 scripts/validate_catalogue.py --add e.json  # validate+append one new entry

Needs no third-party packages: the schema checks below are derived from
climate-assets.schema.json itself (draft-07 subset: required, type, enum,
pattern, min/maxItems, additionalProperties:false, nested objects).
Exit code is non-zero if anything fails, so it is safe to use in a hook or CI.
"""
import json, re, shutil, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "climate-assets.json"
SCHEMA_PATH = ROOT / "climate-assets.schema.json"
ASTRO_COPY = ROOT / "whats-new-astro" / "src" / "data" / "climate-assets.json"
# The skill ships its own copy of the schema; it drifts the moment the master changes.
SKILL_SCHEMA_COPY = ROOT / "skills" / "climate-asset-card" / "reference" / "climate-assets.schema.json"

# Keep in step with SKILL.md "Licence & reuse" and the schema's `reusable` description.
PERMISSIVE = ("cc0", "cc-by", "mit", "bsd", "apache", "gpl", "odbl",
              "etalab", "ogl", "public domain")
NON_PERMISSIVE = ("-nc", "-nd", "noncommercial", "non-commercial", "proprietary")

PY_TYPES = {"string": str, "array": list, "object": dict, "boolean": bool,
            "number": (int, float), "integer": int, "null": type(None)}


def validate(obj, props, required, path="entry"):
    errs = []
    for r in required:
        if r not in obj:
            errs.append(f"{path}: missing required '{r}'")
    for key, val in obj.items():
        if key not in props:
            errs.append(f"{path}: additionalProperty '{key}' not allowed")
            continue
        spec = props[key]
        declared = spec.get("type")
        types = declared if isinstance(declared, list) else [declared]
        if declared and not any(isinstance(val, PY_TYPES[t]) for t in types if t in PY_TYPES):
            errs.append(f"{path}.{key}: type {type(val).__name__} not in {types}")
            continue
        if "enum" in spec and val not in spec["enum"]:
            errs.append(f"{path}.{key}: '{val}' not in enum")
        if isinstance(val, str) and val and "pattern" in spec and not re.match(spec["pattern"], val):
            errs.append(f"{path}.{key}: '{val}' fails pattern {spec['pattern']}")
        if isinstance(val, list):
            items = spec.get("items", {})
            if "minItems" in spec and len(val) < spec["minItems"]:
                errs.append(f"{path}.{key}: {len(val)} < minItems {spec['minItems']}")
            if "maxItems" in spec and len(val) > spec["maxItems"]:
                errs.append(f"{path}.{key}: {len(val)} > maxItems {spec['maxItems']}")
            for i, item in enumerate(val):
                if items.get("type") == "object":
                    errs += validate(item, items.get("properties", {}),
                                     items.get("required", []), f"{path}.{key}[{i}]")
                else:
                    if "enum" in items and item not in items["enum"]:
                        errs.append(f"{path}.{key}[{i}]: '{item}' not in enum")
                    if "pattern" in items and not re.match(items["pattern"], item):
                        errs.append(f"{path}.{key}[{i}]: '{item}' fails pattern")
        if isinstance(val, dict) and spec.get("type") == "object" and "properties" in spec:
            errs += validate(val, spec["properties"], spec.get("required", []), f"{path}.{key}")
    return errs


def licence_contradiction(entry):
    """reusable=true is only legitimate under a permissive/attribution licence."""
    lic = (entry.get("licence") or "").lower()
    if not entry.get("reusable"):
        return None
    if any(n in lic for n in NON_PERMISSIVE):
        return f"reusable=true under restrictive licence '{entry.get('licence')}'"
    if not any(p in lic for p in PERMISSIVE):
        return f"reusable=true with unrecognised/empty licence '{entry.get('licence')}'"
    return None


def normalise_url(url):
    return re.sub(r"^https?://(www\.)?|/+$", "", (url or "").lower())


def scan(assets, schema):
    errs = []
    for a in assets:
        errs += validate(a, schema["properties"], schema["required"], a.get("id", "?"))
    dup_ids = [k for k, v in Counter(a.get("id") for a in assets).items() if v > 1]
    dup_urls = [k for k, v in Counter(normalise_url(a.get("url")) for a in assets).items()
                if v > 1 and k]
    bad_lic = [(a["id"], msg) for a in assets if (msg := licence_contradiction(a))]
    return errs, dup_ids, dup_urls, bad_lic


def recount(doc):
    assets = doc["assets"]
    doc["meta"]["entry_count"] = len(assets)
    doc["meta"]["counts"] = {
        "by_collection": dict(sorted(Counter(a.get("collection") for a in assets).items())),
        "by_type": dict(sorted(Counter(a.get("type") for a in assets).items())),
        "by_access": dict(sorted(Counter(a.get("access") for a in assets).items())),
        "by_theme_primary": dict(sorted(Counter(a["themes"][0] for a in assets
                                                if a.get("themes")).items())),
    }


def write(doc):
    MASTER.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copy(MASTER, ASTRO_COPY)  # the Astro build reads the copy, not the master
    if schema_drift():
        shutil.copy(SCHEMA_PATH, SKILL_SCHEMA_COPY)
        print("resynced the skill's reference copy of the schema")


def schema_drift():
    """True when the skill's reference schema no longer matches the authoritative one."""
    if not SKILL_SCHEMA_COPY.exists():
        return True
    return (json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
            != json.loads(SKILL_SCHEMA_COPY.read_text(encoding="utf-8")))


def main():
    args = sys.argv[1:]
    check_only = "--check" in args
    add_path = None
    if "--add" in args:
        add_path = Path(args[args.index("--add") + 1])

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    doc = json.loads(MASTER.read_text(encoding="utf-8"))
    assets = doc["assets"]

    if add_path:
        new = json.loads(add_path.read_text(encoding="utf-8"))
        errs = validate(new, schema["properties"], schema["required"])
        if new.get("id") in {a.get("id") for a in assets}:
            errs.append(f"duplicate id '{new.get('id')}'")
        nu = normalise_url(new.get("url"))
        for a in assets:
            if nu and normalise_url(a.get("url")) == nu:
                errs.append(f"duplicate url with '{a['id']}'")
            for link in a.get("links", []):
                if nu and normalise_url(link.get("url")) == nu:
                    errs.append(f"url already a link on '{a['id']}'")
        if msg := licence_contradiction(new):
            errs.append(msg)
        if errs:
            print("REJECTED — new entry did not validate:")
            for e in errs:
                print("  -", e)
            return 1
        print(f"new entry OK: {new['id']}")
        assets.append(new)

    errs, dup_ids, dup_urls, bad_lic = scan(assets, schema)
    print(f"{len(assets)} entries | schema errors: {len(errs)} | "
          f"duplicate ids: {len(dup_ids)} | duplicate urls: {len(dup_urls)} | "
          f"licence contradictions: {len(bad_lic)}")
    for e in errs[:20]:
        print("  schema:", e)
    for d in dup_ids:
        print("  duplicate id:", d)
    for d in dup_urls:
        print("  duplicate url:", d)
    for i, msg in bad_lic:
        print(f"  licence: {i} — {msg}")

    # Completeness gaps: not errors, but what to chase before publication.
    gaps = {
        "no image": sum(1 for a in assets if not a.get("image")),
        "no licence": sum(1 for a in assets if not a.get("licence")),
        "undated & not ongoing": sum(1 for a in assets
                                     if not a.get("date") and not a.get("ongoing")),
        "NEEDS REVIEW held": sum(1 for a in assets if "NEEDS REVIEW" in (a.get("notes") or "")),
    }
    print("gaps:", ", ".join(f"{k}: {v}" for k, v in gaps.items()))

    if errs or dup_ids or dup_urls or bad_lic:
        print("\nFAILED — nothing written.")
        return 1
    if schema_drift():
        print("  schema: skills/climate-asset-card/reference/ copy has drifted from the master")
    if check_only:
        print("\nOK (--check: nothing written).")
        return 0

    recount(doc)
    write(doc)
    print(f"\nOK — meta.counts recomputed, master written, Astro copy resynced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
