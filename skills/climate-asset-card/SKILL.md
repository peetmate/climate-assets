---
name: climate-asset-card
description: >-
  Turn a URL (or several) into a validated entry in the CGIAR Climate Data Hub
  "What's New in Climate Data" catalogue (climate-assets.json). Use whenever
  Pete/CDH wants to ADD, ENRICH, or QA a climate/agriculture data asset — a
  dataset, atlas/portal, tool, model, publication, or media item — for the
  radar/newsfeed tab. Handles classification, enrichment, cover image, licence &
  reuse, deduplication, and an adversarial fact-check before the card ships.
---

# Building a Climate Data Hub asset card

You are cataloguing "exciting, cutting-edge" climate/agriculture data assets for the CGIAR Climate
Data Hub. The deliverable is one JSON object per asset, appended to `climate-assets.json`, that
renders as a card in the What's-New tab. Follow this process; the failure modes listed here are all
real mistakes made before — do not repeat them.

## 0. Where things live
- Data: `climate-assets.json` (`meta` + `assets[]`).
- Schema (authoritative field list + controlled vocabularies): `climate-assets.schema.json` — read it and **validate every entry against it** (`jsonschema`).
- The tab: `whats-new-astro/` (Astro). Cover images in `whats-new-astro/public/images/`.

## 1. Classify by what the URL SERVES, not the topic
`type` ∈ dataset · atlas-hub · tool-software · model · publication · media · contact.
- A journal/preprint page → `publication` (even if it's *about* a dataset).
- An interactive portal/dashboard/map (incl. Power BI, ArcGIS, Earth Engine apps) → `atlas-hub`.
- A GitHub repo / R or Python package / CLI → `tool-software`.
- A foundation/ML/emulator model release → `model`.
- A blog post, slide deck, video, news item → `media`.
- A person/team worth knowing (no primary artifact) → `contact`.
> Pitfall: a docs site, a landing page, or a news announcement is **not** a `publication`. A Power BI
> dashboard is **not** `tool-software`.

## 2. Themes (topic) vs tags (everything else)
- `themes`: **1–2 topics only**, primary first, from the fixed list in the schema (Adaptation;
  Production & yields; Emissions & mitigation; Climate projections & reanalysis; Weather &
  forecasting; Hazards & impacts; Population & exposure; Socio-economic & gender; Land, soil &
  ecosystems; Crop & land management; Cross-cutting / AI & methods). Never put format ("hub"),
  approach ("AI"), or "methods" here — those are not topics.
- `tags`: free lowercase-kebab keywords for search — approach (`ai`, `machine-learning`,
  `remote-sensing`, `earth-engine`, `downscaling`), region (`africa`, `south-asia`), commodity/
  technique (`livestock`, `soils`, `coffee`, `crop-mapping`), and cues (`open-data`, `dashboard`,
  `real-time`).
> Pitfall: over-tagging themes. Aim for 1–2; if it feels like 4, you're conflating axes.

## 3. Source vs organisations vs author — keep them distinct and non-repetitive
- `source` = the **provider / journal / hosting body**. NEVER the platform the page runs on.
  Wrong: "Microsoft Power BI", "Loom", "GitHub Pages", "Google Sites", "Read the Docs". Right:
  "UNFCCC (Adaptation Committee)", "Nature Communications", "WFP", "Zenodo".
- `organisations` = author affiliations / developer / hosting institution. **Drop any org that
  equals the `source` or the lead author's affiliation** — otherwise the card repeats the same name
  three times (source line, author line, org line).
- `lead_contact`:
  - `name` = the **first author OR the corresponding author**. NEVER the last-listed author (a
    recurrent hallucination — e.g. naming author #25 as lead).
  - `affiliation` = that person's institution.
  - `email` = ONLY a genuinely **published** address (corresponding-author email on the paper, or a
    documented maintainer contact). NEVER construct one from initials+surname. Treat a personal
    gmail as unverified unless you can confirm it. If unsure → leave `email` empty.
  - If there is no named person (a portal/org product), leave `name` empty; the card will show a
    "✉ Contact" button from `email` instead of a fake person line.

## 4. Licence & reuse (the field with real consequences)
- `licence`: normalise (CC-BY-4.0, CC0-1.0, CC-BY-NC-ND-4.0, MIT, Apache-2.0, GPL-3.0, public
  domain, proprietary…). Distinguish **code licence vs article/data licence** — an R package may be
  MIT while the journal article is CC-BY or paywalled; don't put the code licence on the paper.
- `reusable` = **true only for a permissive or attribution licence**: CC0, CC-BY, CC-BY-SA, MIT,
  **BSD** (2/3/4-clause), Apache, GPL / LGPL / **AGPL**, **ODbL**, **Etalab-2.0**, **OGL** (UK Open
  Government Licence), public domain. NC, ND, proprietary, or unknown → **false**. Compute it from
  the licence; never trust a hand-set flag — `scripts/validate_catalogue.py` enforces this and its
  `PERMISSIVE` tuple is the machine-readable copy of this list, so change both together.
  > Copyleft counts as reusable but carries obligations: share-alike (CC-BY-SA, GPL, ODbL) binds
  > derivatives, and **AGPL extends that to network use** — hosting a modified instance obliges
  > publishing the source. Say so in `notes` rather than flipping `reusable` to false.
  > Where an asset aggregates many sources under mixed terms (e.g. national datasets, some NC),
  > leave `licence` empty, set `reusable` false, and list the per-source terms in `notes`.
- `data_availability`: "Open data" / "Open (with code)" / "Code only" / "On request" /
  "No associated data".

## 5. Date & ongoing
- `date` = publication/release date (`YYYY` or `YYYY-MM-DD`). Feed sorts newest-first on this.
- `ongoing` = true for **living resources** — portals, dashboards, live datasets, recurring reports
  (they have no single meaningful date and sort to the top as "current"). Rule of thumb:
  `type == atlas-hub`, or tags include `dashboard`/`real-time`, or it's a recurring series.

## 6. Cover image (`image`)
Priority: (1) the asset's own `og:image`; (2) for a paper/report, **render its first page**
(`pdftoppm -jpeg -singlefile -scale-to-x 560 <pdf> public/images/<id>`); (3) a live page screenshot
for screenshot-friendly sites; (4) else a themed banner (leave `image` empty — the UI generates it).
> Pitfall: DO NOT screenshot bot-walled publisher domains (nature.com, springer, sciencedirect,
> pnas.org, wiley, agupubs, rmets, tandfonline, thelancet, unicef.org, researchgate, oup, cell,
> gatesopenresearch) — the screenshot service returns a CAPTCHA/"are you a robot" page. Blocklist
> them and fall back to the themed banner. Save rendered images INTO the project, not a temp folder.

## 7. Deduplicate
Before adding, check for the same resource already present (same normalised URL, or a paper + its
dataset, or a repo + its descriptor). If it's genuinely the same thing, **merge into one entry** and
keep the extra URLs as labelled `links` (e.g. "Data (Zenodo)", "Paper (WRR)"). Distinct artifact
types of the same work (arXiv paper vs blog post) may stay separate but cross-reference in `notes`.

## 8. Links
Primary link is labelled by type (Data / Paper / Code · repo / Open portal / View). Add `links[]`
for associated data, code, preprints, mirrors, and — for paywalled items — an open-access
alternative (institutional repo / preprint / author copy).

## 9. Validate, then adversarially fact-check
Validate against the schema (0 errors, ≤2 themes, unique id, licence↔reusable consistent). Then run
the **mean QA pass** in `reference/qa-checklist.md` — assume fields are wrong until verified, and
especially re-check author (corresponding, not last), email (published, not fabricated), licence,
date, and duplicates. Leave genuinely unknown fields empty; never fill with a guess. Mark anything
unresolved `⚠ NEEDS REVIEW` in `notes` and hold it from publication.

## Reference files
- `reference/qa-checklist.md` — the adversarial checklist + severity guide.
- `reference/entry-template.json` — a blank entry with every field.
- `climate-assets.schema.json` (in the catalogue folder) — the authoritative schema.

## Brand (for any rendering work)
CGIAR Climate Action identity: green `#033529`/`#02211A`, teal `#17F1BD`/`#57FAD3`, program blue
`#1955A6`/`#63A9FE`; Noto Serif headings + Noto Sans body (Times New Roman / Arial fallback); ClimAct
white logo on the dark-green header. Cards: source line, author line only if a named person,
organisations minus source/affiliation, licence shown once, contact button when nameless.
