# CLAUDE.md — climate-assets

## What this is

A structured catalogue of "new & notable" climate/agriculture data assets for the **CGIAR Climate
Data Hub**, plus the Astro build of the **"What's New in Climate Data"** tab that renders it. One
JSON file drives both a newsfeed and a dashboard view. Originally collated from two Alliance Slack
docs (an Assets list and a Methods list); entries are now added one URL at a time.

**Git repo, local disk**, pushed to `github.com/peetmate/climate-assets` (public). Moved out of
OneDrive on 2026-10-02 — a `.git` directory inside a synced folder risks index corruption, and two
sessions editing through OneDrive were clobbering each other. `whats-new-astro/preview/` is now
tracked (it was ignored back when OneDrive was the backup; it no longer is).

**Public repo — keep it clean.** Internal Slack doc IDs and colleague names were stripped before
publication; `shared_by` reads "Alliance colleague" where a name would identify someone. Contact
emails in the catalogue are published corresponding-author or institutional addresses only. Do not
add internal identifiers, personal emails or unpublished contacts.

## File map

| Path | Role |
|------|------|
| `climate-assets.json` | **Master** catalogue: `meta` + `assets[]`. 153 entries. |
| `climate-assets.schema.json` | **Authoritative** schema (draft-07, `additionalProperties: false`). |
| `scripts/validate_catalogue.py` | Validate + recompute `meta.counts` + resync copies. Run after every edit. |
| `skills/climate-asset-card/SKILL.md` | The process for adding/enriching/QA-ing an entry. Follow it. |
| `skills/climate-asset-card/reference/` | `qa-checklist.md` (adversarial QA), `entry-template.json`, schema copy. |
| `whats-new-astro/` | The tab. `src/pages/index.astro` is the whole UI; `public/images/` has 34 covers. |
| `whats-new-astro/src/data/themes.json` | Theme/subtheme vocabulary + definitions driving the facets. |
| `THEMES.md` | Prose write-up of the theme taxonomy and where each definition came from. |
| `adversarial-review.md`, `-2.md` | Two completed QA passes. Read `-2.md`'s "Systemic caveat". |
| `images/` | Source cover images (mirrored into the Astro `public/images/`). |

Legacy / dead — do not edit or read as source of truth:
- `whats-new-tab.html` (209 KB) — superseded single-file prototype, kept as a snapshot.
- `skills/zidHq6wp` — a **zip archive** of the skill with a mangled name (binary; don't `cat` it).
- `skills/climate-asset-card.skill` — 0 bytes, junk.

## The copy gotcha

`climate-assets.json` exists in **three** places and the schema in **two**:

- master `climate-assets.json` → copy at `whats-new-astro/src/data/climate-assets.json` (**the
  Astro build reads the copy**, so an unsynced master means the site serves stale data);
- master schema → copy at `skills/climate-asset-card/reference/climate-assets.schema.json`.

Never hand-copy them. After any edit to the master:

```bash
python3 scripts/validate_catalogue.py          # validate + recount + resync everything
python3 scripts/validate_catalogue.py --check  # validate only, writes nothing
python3 scripts/validate_catalogue.py --add new-entry.json   # validate then append one entry
```

It exits non-zero on failure and writes nothing, so it is safe to run first and often. There is no
`jsonschema` module on this machine — the script implements the draft-07 subset the schema uses.

## Adding an entry

Follow `skills/climate-asset-card/SKILL.md`. The rules that get broken most often:

1. **Classify by what the URL serves**, not the topic. Also check the rendered primary-link label in
   `index.astro` (`PRIMARY_LABEL`): `tool-software` renders "Code / repo", so pointing that type at
   a landing page makes the card lie.
2. **`themes` = 1–2 topics** from the fixed list; approach and format words belong in `tags`. Pick
   tags that match a subtheme's `match_tags` in `themes.json` or the entry misses those facets.
3. **`source` is the provider/journal**, never the hosting platform. Drop `organisations` that
   repeat `source` or the lead author's affiliation.
4. **`lead_contact` is the least reliable field in the catalogue** — use the first or corresponding
   author (never the last-listed), and only a genuinely published email. Never construct one.
   Leaving it empty is always acceptable; a nameless entry with an email renders a "✉ Contact".
5. **Compute `reusable` from `licence`**, per SKILL.md §4. Mixed-source terms (some NC) → empty
   `licence`, `reusable` false, per-source terms spelled out in `notes`. Copyleft is reusable but
   obliges share-alike; AGPL extends that to network use.
6. **`image`**: prefer the asset's own `og:image`. Leave it empty and the UI screenshots the page
   via thum.io — except for the publisher domains in `index.astro`'s `NOSHOT` list, which return
   CAPTCHAs.
7. Then run the QA checklist, and hold anything unresolved with `⚠ NEEDS REVIEW` in `notes`.

## Known state and debt

- `date_added` is `TBC` across the original Slack-doc intake (those docs carry no dates); entries
  logged since carry real dates. Feed order uses the asset's own `date`, with `ongoing` pinned top.
- Completeness gaps, as reported by the script: **61 entries without an image, 80 without a
  licence, 17 undated and not ongoing**. Not errors — the backlog to chase before publication.
- Author/contact fields were auto-harvested and the fabrication pattern recurred; verify before any
  card is used to email someone. See `adversarial-review-2.md`.
- **Comments (giscus) and star ratings are unwired.** Ratings persist in `localStorage` as a
  stand-in; swap `getRating`/`setRating` in `index.astro` for a real endpoint. Both key on the
  asset `id`, so **never rename an id once published** — it is the join key for comments, ratings
  and permalinks.
- `SUBMIT.repo` in `index.astro` is empty, so "Suggest an asset" and "Report" fall back to a
  mailto to `p.steward@cgiar.org`. Set it to `"org/repo"` to route to GitHub Issues instead.
- A desktop Claude Code session also edits this folder. Two sessions writing
  `climate-assets.json` will clobber each other — read immediately before writing, and prefer
  `--add` over rewriting the file.

## Commands

```bash
cd whats-new-astro
npm install
npm run dev      # http://localhost:4321
npm run build    # static site into ./dist
npm run preview  # serve ./dist
```
Node 18+. `preview/index.html` opens without a build (snapshot, not the source of truth).

## Brand (CGIAR Climate Action)

Green `#033529` / `#02211A` / `#065F4A`; teal `#17F1BD` / `#57FAD3`; program blue `#1955A6` /
`#63A9FE`. Noto Serif headings, Noto Sans body (Times New Roman / Arial fallbacks). ClimAct white
logo on the dark-green header.

## Session log

- **2026-10-07** — Merged the Earth Engine access route into `global-pasture-watch` (it was already
  catalogued under its Land & Carbon Lab page) and cleared a stale "fetch timed out" note from its
  `notes`. Scrubbed internal Slack doc IDs and colleague names ahead of the repo going public,
  tracked `whats-new-astro/preview/`, and rebuilt the git history as a single clean commit.

- **2026-10-02** — Added `open-climate-ai`, `fao-livestock-hub`, `fao-ex-act-webapp` (151–153).
  Extended the permissive-licence list (BSD, AGPL/LGPL, ODbL, Etalab-2.0, OGL) across SKILL.md, the
  QA checklist and the schema — BSD was missing, so `climsight` false-flagged on every audit. Added
  `scripts/validate_catalogue.py` and pointed both READMEs at it. Refreshed the stale entry counts
  (README said 143, the Astro README said 141).
- **2026-09-10** — Added `fields-of-the-world-ftw` (150). Licence is a per-country mosaic including
  NC and GPL components, so `reusable` is false by design.
- **2026-09-07** — Added `esgf-metagrid-east-index` (149). First pass that recomputed `meta.counts`,
  which had drifted three ways (146 actual vs 143 and 141 in the two READMEs).
