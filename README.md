# New & Notable Climate Assets — structured catalogue

This folder turns the running "Awesome Datasets & Resources" and "Methods" Slack docs into a
structured, machine-readable catalogue that can drive a **climate assets "news" section** with
toggleable **newsfeed** and **dashboard** views, search, comments, and star ratings.

## Files

| File | What it is |
|------|------------|
| `climate-assets.json` | The catalogue: `meta` block + `assets[]` array. The master copy. |
| `climate-assets.schema.json` | JSON Schema (draft-07) defining a valid entry. Authoritative. |
| `scripts/validate_catalogue.py` | Validates every entry, recomputes `meta.counts`, resyncs the copies. Run it after any edit. |
| `skills/climate-asset-card/` | The skill for adding/enriching/QA-ing an entry (`SKILL.md` + `reference/`). |
| `whats-new-astro/` | The Astro build of the What's-New tab. Reads its **own copy** of the JSON. |
| `README.md` | This document — schema explainer, provenance, and the UI/feature design note. |

## What's in it

153 entries — the original 143 collated from two internal Alliance Slack docs (an Assets list and
a Methods list), plus later additions logged one URL at a time, minus a merged duplicate:

- **By collection:** 131 assets, 22 methods.
- **By type:** 44 atlas/hubs, 43 publications, 28 datasets, 25 tools/software, 9 media, 4 models.
- **By access:** 119 open, 17 paywall, 9 login, 6 unknown, 2 on-request.

> The numbers above are a snapshot and drift as entries are added. `meta.counts` inside the JSON is
> the live figure — regenerate it with `python3 scripts/validate_catalogue.py`, never by hand.

Entries can carry more than one theme, and items that appeared under two headings are merged into a
single entry with a `Cross-listed:` note.

## The standard entry

Every resource — whether a dataset, an interactive atlas, a GitHub tool, a foundation model, a
journal paper, a slide deck, or a useful contact — uses **one common schema**, with a few fields
that only apply to some types. Full definitions live in `climate-assets.schema.json`; in short:

`id`, `title`, `type`, `url`, `themes[]`, `source`, `description`, `region`,
`spatial_resolution`, `temporal_coverage`, `access`, `collection`, `section`, `shared_by`,
`notes`, `date_added`, and an optional `rating` object.

### Three independent facets

Classification uses three orthogonal axes so filtering doesn't fight itself:

1. **`type` — format (one per entry).** What kind of thing it is.
   `dataset` · `atlas-hub` · `tool-software` · `model` · `publication` · `media` · `contact`
2. **`themes` — topic (1–2 per entry, primary first).** What it's *about*. Format words and
   approaches are deliberately excluded here.
   Adaptation · Production & yields · Emissions & mitigation · Climate projections & reanalysis ·
   Weather & forecasting · Hazards & impacts · Population & exposure · Socio-economic & gender ·
   Land, soil & ecosystems · Crop & land management · Cross-cutting / AI & methods
   (the last holds pure tooling/AI/method items — e.g. literature-synthesis LLMs — that have no
   single subject domain, so they aren't force-fitted into a topic like Adaptation).
3. **`tags` — free-form search keywords.** Cross-cutting descriptors: approach (`ai`,
   `machine-learning`, `foundation-model`, `remote-sensing`, `earth-engine`, `downscaling`),
   region (`africa`, `south-asia`, `vietnam`), technique/commodity (`livestock`, `soils`,
   `coffee`, `crop-mapping`), and access/format cues (`open-data`, `dashboard`, `api`, `real-time`).

Plus `access` (`open` · `login` · `paywall` · `request` · `unknown`) and the dataset-only fields
`spatial_resolution` / `temporal_coverage` (populated where stated, empty otherwise).

Current spread: themes now sit at 1–2 per entry (down from an average of 3.8), balanced across the
ten topics; the most common tags are `global`, `open-data`, `remote-sensing`, `high-resolution`,
`machine-learning`, `food-security`, `africa`, and `ai`.

## How this maps to the "news" section

The catalogue is designed so a single JSON file drives both views. Nothing in the schema is
view-specific, so the front end can present the same records two ways and let users toggle:

- **Newsfeed view** — reverse-chronological by `date_added`; each card shows title, type badge,
  theme tags, access badge, a one-line description, `shared_by`, and the link. Reads like a feed of
  "what's new".
- **Dashboard view** — the same records as a filterable/sortable grid or table, faceted by
  `theme`, `type`, `access`, and `region`, with `tags` as chips and full-text search over
  `title` + `description` + `source` + `tags`. Reads like a searchable inventory.

Because both views read the identical array, the toggle is purely a rendering choice.

### Comments and ratings (per your plan: giscus now-ish, backend later)

Neither belongs in the static JSON — both are user-generated and mutable — so the schema keeps a
clean seam for them:

- **Comments → giscus.** Key each asset's comment thread by its `id` (the same pattern as the
  existing review pages, building the giscus iframe directly). One GitHub Discussion per `id`.
- **Star ratings → backend later.** The optional `rating` object (`{average, count}`) is a
  placeholder the front end can hydrate from a lightweight service (e.g. Supabase/Firebase) once
  it exists. Until then the field is simply absent and the UI shows "unrated".

Keeping `id` stable is what makes both features durable — it's the join key for comments, ratings,
and permalinks, so avoid renaming ids once published.

## Provenance & data-quality caveats — please read

- Entries were enriched **automatically**. During generation the page-fetch tool was unavailable,
  so most descriptions were built from **web-search results rather than full-page reads**. Treat
  descriptions, resolutions, and access flags as **draft — verify before publishing**.
- Fields that couldn't be confirmed are marked `TBC` or left empty; some `notes` say
  "description from URL/title only".
- `date_added` is `TBC` for the original Slack-doc intake — those docs carry no per-item dates.
  Entries logged since then carry a real `date_added`. Feed order uses the asset's own `date` with
  `ongoing` resources pinned to the top, so the TBCs do not break sorting.
- A couple of source-doc items had no link (e.g. the ETH cocoa suitability map) and are included
  with an empty `url` and a note.

## Suggested next steps

1. **Verify a first tranche** (the ones you'd feature first) — I can re-run enrichment per-URL once
   fetching is working, or you can correct entries directly in the JSON.
2. **Backfill `date_added` and `shared_by`** where you can, so the newsfeed ordering is meaningful.
3. **Confirm the theme taxonomy** — happy to split/rename (e.g. separate "Soils", "Livestock") or
   collapse thin themes.
4. Then I can build the **prototype newsfeed/dashboard page** (single HTML reading this JSON) with
   search, the view toggle, giscus threads, and rating placeholders.

---
_Generated for the CGIAR Climate Data Hub. Source: internal Alliance Slack docs (Assets and Methods)._
