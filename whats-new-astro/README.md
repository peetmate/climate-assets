# What's New in Climate Data — Astro tab

A standalone [Astro](https://astro.build) build of the **"What's New in Climate Data"** radar for
the CGIAR Climate Data Hub: a browsable, filterable view of 161 cutting-edge climate/agriculture
data assets (datasets, atlases, tools, models, publications, methods) shared across the network.
Styled to the **CGIAR Climate Action** visual identity.

Intended to be handed to the Climate Data Hub web team and dropped into the Hub as a tab.

## Published site

```
https://peetmate.github.io/climate-assets
```

`../.github/workflows/deploy.yml` rebuilds and republishes on every push to `main` that touches
this directory, so the live page always reflects the committed catalogue. **GitHub Pages has not
been switched on for the repo yet** — until someone sets Settings → Pages → Source to *GitHub
Actions*, the build job passes and the deploy job 404s. There is deliberately no committed snapshot
of the built site: the one that used to live in `preview/` went stale at 148 assets and was removed.
Build locally instead (below).

## Run / build

```bash
npm install
npm run dev      # local dev server at http://localhost:4321
npm run build    # static site into ./dist
npm run preview  # serve the built ./dist locally
```

Node 18+ recommended.

## Structure

```
whats-new-astro/
├── astro.config.mjs        # static output; `site`/`base` set for the Pages sub-path
├── package.json
├── src/
│   ├── data/
│   │   └── climate-assets.json   # THE DATA — 161 assets (see schema in ../../climate-assets.schema.json)
│   │   └── themes.json            # theme/subtheme vocabulary + definitions for the facets
│   └── pages/
│       └── index.astro     # the whole tab: markup + brand styles + client-side UI logic
└── public/
    ├── brand/              # CGIAR Climate Action logos (white / green / stacked)
    └── images/             # rendered first-page cover images (34)
```

## How it works

> **Updating the catalogue.** `src/data/climate-assets.json` is a **copy** of the master catalogue
> at `../climate-assets.json`. Do not resync by hand — run `python3 scripts/validate_catalogue.py`
> from the project root, which validates the master, recomputes `meta.counts` and copies it here.
> Build from a stale copy and the site silently serves the old data. CI guards this: the deploy
> workflow diffs the two files and fails the build if they differ.

`index.astro` imports `src/data/climate-assets.json` at build time and embeds it in the page as a
JSON `<script>`. A small inline vanilla-JS script renders the feed/dashboard, facets, search, sort
and rating widgets client-side — no framework runtime, no external JS dependencies. To update the
catalogue, replace `src/data/climate-assets.json` (same schema) and rebuild.

## Features

- **Feed / Dashboard** toggle over the same data.
- **Filters:** Year (with an *Ongoing / continuous* bucket for living resources), Theme, Type,
  Access, plus click-a-tag and full-text search (title, description, source, tags, org, author,
  licence).
- **Sort:** Newest (default; ongoing pinned to top), Oldest, A–Z, Theme, Type, Access.
- **Cards** show cover image, type, theme(s), access, licence / **Reusable in Hub** badge,
  publication date or Ongoing, description, source, lead author + organisations (with a `mailto`
  where a public contact exists), data-availability, tags, and multiple resource links
  (Data / Paper / Code / mirrors / open-access alternatives).

## Branding

CGIAR Climate Action visual identity (`Climate_data_hub/comms/Branding`):

- **Colours:** CGIAR green `#033529` / dark `#02211A` / lighter `#065F4A`; teal `#17F1BD` / `#57FAD3`;
  program blue `#1955A6` / `#63A9FE`; greys `#1D1D1D`…`#E2E0DF`.
- **Type:** Noto Serif (headers/pull quotes), Noto Sans (body); Times New Roman / Arial as fallbacks.
- **Logo:** ClimAct white short logo in the header (`public/brand/`).

## Suggest an asset / report an error

The toolbar has a **＋ Suggest an asset** button and every card has a **⚑ Report** link (suggest a
correction / flag an error). Both are driven by the `SUBMIT` config near the top of the client
script in `index.astro`:

```js
const SUBMIT = { repo: "", email: "p.steward@cgiar.org" };
```

- **Default (repo empty):** opens a pre-filled **email** to the address given.
- **Recommended (set `repo` to `"org/repo"`):** routes to **GitHub Issues** using the structured
  issue forms in `../.github/ISSUE_TEMPLATE/` (`suggest-asset.yml`, `report-issue.yml` — they live
  at the repo root because GitHub only reads `.github/` from there). Set the repo to the hub's
  GitHub repository and submissions land as triageable, labelled issues
  (`new-asset`, `data-correction`) — the same GitHub backbone as giscus.

## To be wired by the web team

- **Comments — giscus.** Attach a giscus thread per card keyed on the asset `id` (one GitHub
  Discussion per id). The card's Comments button is the placeholder hook.
- **Star ratings — backend.** giscus cannot store numeric ratings. Add a tiny endpoint
  (e.g. Cloudflare Worker + KV, or Supabase) `GET/POST` keyed on the asset `id`. Ratings currently
  persist in `localStorage` as a stand-in; swap `getRating`/`setRating` in `index.astro` to call
  the real endpoint.
- **Cover images / screenshots.** 34 assets have rendered first-page covers in `public/images/`;
  others use their own `og:image`, and screenshot-friendly sites fall back to a live screenshot
  service (thum.io) — consider self-hosting captures for production.

## Data provenance & caveats

Descriptions/metadata were assembled semi-automatically and adversarially reviewed; licences and
data-availability especially should be spot-checked before anything is ingested into the Hub. See
`../README.md` and `../adversarial-review.md`.
