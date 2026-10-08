# Adversarial Review — CGIAR Climate Data Hub "New & Notable Climate Assets" catalogue

**Catalogue:** `climate-assets.json` (v0.1-draft, generated 2026-07-23, 143 entries)
**Reviewer stance:** adversarial. Two passes — (1) structural/logic scan over all 143 entries, (2) web spot-check of ~20 of the most suspicious entries plus calibration picks.
**Provenance caveat under test:** descriptions were auto-enriched from web-SEARCH snippets (page-fetch was down), so description → theme/tag cascades are the expected weak point.

---

## 1. Summary verdict

**Fit to publish as a draft — with fixes — yes; fit to publish as-is — no.** The catalogue is fundamentally sound: schema-valid, controlled vocabularies respected, and (importantly) the access flags on the Nature-family journals are handled *carefully* rather than carelessly — Scientific Data / Nature Communications / npj / Lancet Planetary Health / Gates Open Research are correctly `open`, while Nature / Nature Climate Change / Nature Sustainability / Nature Food are correctly `paywall`. That is the opposite of the "everything marked open" failure mode I went hunting for.

The real problems are: (a) a cluster of ~10 placeholder entries with non-informative titles and filler descriptions that are honestly flagged but not publishable as real records; (b) a genuine **duplicate** the merge missed (Google Agricultural Understanding = AnthroKrishi); (c) a handful of **misleading classifications** — a theme or tag or note that a user would read as fact and be misled by; and (d) a systematic under-application of `open` to gold-OA journals outside the Nature family (JAMES, IJAEOG, Weather & Climate Extremes).

**Entries with HIGH issues: 6** (one of which spans a duplicate pair, so 7 entry-ids touched).

---

## 2. Counts of issues by severity

| Severity | Count |
|---|---|
| HIGH | 6 |
| MED | 26 |
| LOW | 9 |
| **Total** | **41** |

---

## 3. HIGH issues

| id | field | problem | correct / suggested fix (source if web-verified) |
|---|---|---|---|
| `google-agricultural-understanding-platform` + `anthrokrishi-agricultural-understanding-platform-demo` | duplicate | These are the **same product**. `agri.withgoogle.com` IS the AnthroKrishi "Agricultural Understanding" platform; the second entry is just its demo map. The first entry is a near-empty placeholder ("Detailed content could not be retrieved", region empty, access unknown) while the second carries the real detail. | Merge into one entry. Make `agri.withgoogle.com` the canonical platform record (region India, access `login`/`request` per FAQ), and fold the demo map URL into `notes`. Confirmed same platform via [Google AnthroKrishi FAQ](https://agri.withgoogle.com/faq/) and [Google blog](https://blog.google/technology/ai/how-ai-is-improving-agriculture-sustainability-in-india/). |
| `nature-climate-change-article-s41558-025-02372-4` | title + theme | Placeholder title ("Nature Climate Change article s41558-025-02372-4") **and** wrong primary theme `Adaptation`. The paper is about extreme-weather-event attribution and public climate-policy support. | Real title ≈ *"Extreme weather event attribution predicts climate policy support across the world"* (per search; verify on nature.com). Theme should be `Hazards & impacts` + `Socio-economic & gender`, **not** `Adaptation`. Drop meta-tag `publication`. |
| `synthesizing-scientific-literature-with-retrieval-augmented-language-models` | theme | Primary theme `Adaptation` is misleading. This is OpenScholar — an AI/LLM scientific-literature-synthesis system. It has nothing to do with climate adaptation; it was auto-filed under Adaptation only because it sits in the "methods: LLMs" section. | No topic facet fits an AI tooling paper cleanly; `Socio-economic & gender` is the least-wrong, or flag for a taxonomy gap. Remove `Adaptation`. Title/access verified correct: published in Nature, Feb 2026, paywall ([Nature](https://www.nature.com/articles/s41586-025-10072-4), [Ai2](https://allenai.org/blog/openscholar-nature)). |
| `dynamical-org-catalog` | tags + notes | Tags `africa` and `seasonal-forecast` are wrong, and the `notes` value ("E2E framework for seasonal predictions for Africa") is a **mis-merged note from a different resource**. dynamical.org is a global short/medium-range NWP catalog (GFS, GEFS, HRRR, IFS ENS, MRMS, AIFS) — not Africa-specific, not seasonal. | Remove `africa` and `seasonal-forecast` tags; replace note. Verified via [dynamical.org](https://dynamical.org/) and [AWS Open Data registry](https://registry.opendata.aws/dynamical-noaa-gfs/). Description text itself is accurate. |
| `loom-video-demo-291e886a` | theme (fabricated) | Theme `Land, soil & ecosystems` is assigned to a Loom video whose content the pipeline explicitly says it "could not inspect". Placeholder title, access unknown. Assigning a topic to unseen content is an unfounded, misleading classification. | Either resolve the video's actual subject (human input needed) or strip the invented theme and mark clearly as unclassified. Could not verify content via search. |
| `scientific-data-s41597-025-05257-5` | title + existence | Placeholder title ("Scientific Data article s41597-025-05257-5"), generic filler description, and the record **could not be located** in search (nearby DOIs exist, this one did not surface). Possible wrong/dead identifier. | Do not publish as a real entry until the DOI resolves and a real title is confirmed. Web search returned no match. |

---

## 4. MED issues

| id | field | problem | fix |
|---|---|---|---|
| `adaptation-finance-power-bi-dashboard` | access | `login` is likely wrong — `app.powerbi.com/view?r=...` is a *publish-to-web* link, which is publicly viewable with no login. | Set `access: open` (verify by opening incognito). |
| `mercury-multi-resolution-...` | access + title | `access: unknown`, but JAMES (AGU) is a **fully open-access** journal. Title also truncated. | `access: open`; full title *"MERCURY: A fast and versatile multi-resolution based global emulator of compound climate hazards"* ([Wiley/JAMES](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024MS004905)). |
| `yield-forecasting-remote-sensing-article-ijaeo` | access + title | `access: paywall`, but Int. J. Applied Earth Observation & Geoinformation is ~99.9% **gold OA**. Title is a generic descriptor, not the real article title. | `access: open` ([Elsevier OA info](https://www.sciencedirect.com/journal/international-journal-of-applied-earth-observation-and-geoinformation/publish/open-access-options)); confirm real title. |
| `a-new-class-of-climate-hazard-metrics-...` | access | `unknown`; *Weather and Climate Extremes* (Elsevier) is gold OA. | Likely `open`; verify. |
| `wri-drivers-of-forest-loss-1km` | access | `unknown` on a Google Earth Engine catalog asset; GEE public catalog datasets are open. | Set `open` after confirming. |
| `xclim-climate-indicators` | tags | Tagged `r-package` — xclim is a **Python** library (already correctly tagged `python`). | Remove `r-package`. |
| `global-renewables-watch` | tags + coverage | Missing the single most obvious keyword: no `renewables`/`energy` tag on a renewable-energy asset. Empty `temporal_coverage` though known. | Add `energy`/`renewables`; set coverage 2017Q4–2024Q2. Repo confirmed real ([microsoft/global-renewables-watch](https://github.com/microsoft/global-renewables-watch)). |
| `spatially-explicit-harmonized-global-dataset-of-critical-infrastructure` | theme | Primary `Socio-economic & gender` is a poor fit for an infrastructure/exposure dataset. | Primary `Population & exposure` (or `Hazards & impacts`). |
| `digital-earth-africa-aws-open-data` | theme | Secondary `Weather & forecasting` is wrong — CHIRPS is *historical* rainfall, not forecasting. | Drop it or use `Climate projections & reanalysis`. |
| `nature-positive-agrifood-systems-toolkit` | type | `tool-software`, but it is a curated platform of tools + case studies (its own section is "Hubs & Atlases"). | `atlas-hub`. |
| `destination-earth-vizlab` | type | `tool-software` for what is an interactive visualisation portal. | Arguably `atlas-hub`. |
| `alphaearth-foundations-helps-map-our-planet-...` | type | `model`, but the resource is a **DeepMind blog announcement**, not the model. The model paper is a separate entry (`alphaearth-foundations`, arXiv). | `media`. |
| `cmip7-forcing-datasets` | type | `publication` for a WCRP overview/landing web page. | `atlas-hub` or `dataset`. |
| `input4mips-cvs-documentation` | type | `publication` for a Read-the-Docs documentation site. | `tool-software`/`atlas-hub`. |
| `copernicus-era6-reanalysis-production-starts` | type | `publication` for what is a news announcement. | `media`. |
| `choosegcm-toolkit-to-select-general-circulation-models-in-r` | type | `tool-software`, but the `url` points to the **Wiley journal article**, not the software (which is on CRAN/GitHub/Zenodo). | `publication` (keep `r-package` tag), or repoint URL to the package. |
| `kenya-crop-type-detection-dataset-kaggle` | type | `dataset`, but the URL is a Kaggle *discussion/announcement thread*, not the dataset. Possible topical overlap with `helmets-labeling-crops-kenya-crop-type-dataset`. | `media`/`publication`; check for overlap. |
| `climate-analogues-homologues-agricultural-systems` | title | Title is a hand-written descriptor; real title/authors unconfirmed (self-flagged). | Resolve real title before publishing. |
| `eth-cocoa-suitability-map` | url | No URL at all (`""`), access `unknown`. | Needs a link (TBC) — not publishable as a live card yet. |
| `zenodo-record-14961636` | title/existence | Placeholder title, speculative description ("likely a crop-yield dataset"), **unverifiable** — search returned nothing. | Resolve or hold. |
| `zenodo-record-17627111` | title/existence | Placeholder title, filler description, unverifiable. | Resolve or hold. |
| `zenodo-record-14443334` | title/existence | Placeholder title, speculative ("most likely WorldPop-related"), unverifiable. | Resolve or hold. |
| `water-resources-research-article-2024wr039773` | title | Placeholder title, content unconfirmed; meta-tag `publication`. | Resolve title; drop `publication` tag. |
| `nature-communications-s41467-026-72715-y` | title | Placeholder title, content unconfirmed. (`access: open` is correct — Nat Comms is OA.) | Resolve title. |
| `nature-article-s44458-026-00071-5` | title/theme | Placeholder title; theme `Land, soil & ecosystems` assigned to unconfirmed content. | Resolve title; re-check theme. |
| `wfp-document-0000172936` | title | Placeholder title, document ID unidentified via search; served from a raw download API. | Resolve title or drop. |

---

## 5. LOW issues

- **Meta-tag `publication` used as a topic tag** on `water-resources-research-article-2024wr039773` and `nature-climate-change-article-s41558-025-02372-4` — `tags` should carry topic/approach/region, not the format (that's `type`).
- **`socioeconomic-predictors-vulnerability-flood-induced-displacement`** — `food-security` tag is not clearly relevant to a flood-displacement study.
- **`meta-wri-global-canopy-height-map`** — `spatial_resolution` left empty though title/description state 1 m.
- **`openlandmap-soildb-global-30m-soil-datacube`** — `spatial_resolution` empty though 30 m is stated in the description.
- **`acasa-...`** — `spatial_resolution: "~25 sq km grid"` is awkward (a 25 km² pixel is ~5×5 km); reword.
- **`climate-change-drives-a-decline-in-global-grazing-systems`** — description says "1.4 billion livestock"; the paper says up to **1.6 billion** grazing animals ([PNAS](https://www.pnas.org/doi/10.1073/pnas.2534015123)). Minor number drift.
- **Honestly-flagged generic descriptions** (`deadtrees-earth`, `ecosystem-integrity-index`, `soil-erosion-watch`, `geedl`, `global-renewables-watch`) — transparent gaps, but still filler ("Detailed content could not be retrieved").
- **`global-livestock-dynamics` (media) vs `annual-global-gridded-livestock-mapping-1961-2021` (dataset)** — same underlying data (insight article about the dataset); not a duplicate, but a cross-reference in `notes` would help.
- **`harmonised-dataset-for-earth-system-foundation-models` (WorldTensor)** — `type: publication` for what is primarily a dataset descriptor; defensible as an arXiv preprint but `dataset` would be arguable. Verified real ([arXiv 2607.03298](https://arxiv.org/abs/2607.03298)).

---

## 6. Systematic patterns

1. **`type=publication` over-applied to non-paper web resources.** Overview/landing pages, docs sites, and news announcements were catalogued as `publication`: `cmip7-forcing-datasets`, `input4mips-cvs-documentation`, `copernicus-era6-reanalysis-production-starts`. Conversely `model`/`tool-software` were applied to a blog post (`alphaearth-...-helps-map`) and to journal-article URLs (`choosegcm`). Rule of thumb the pipeline missed: classify by *what the URL actually serves*, not by what the thing is about.

2. **`open` under-applied to gold-OA journals outside the Nature family.** JAMES (`mercury-...`), Int. J. Applied Earth Observation & Geoinformation (`yield-forecasting-...-ijaeo`), and Weather & Climate Extremes (`a-new-class-of-...`) were left `unknown`/`paywall` despite being fully open access. **Counter-note (a genuine strength):** the Nature-portfolio access flags were done *well* — Scientific Data / Nature Communications / npj / Lancet PH correctly `open`; Nature / NCC / Nat Sust / Nat Food correctly `paywall`. So this is a journal-coverage gap, not blanket carelessness.

3. **Placeholder entries.** ~10 records have non-informative "Journal article s41597-…" / "Zenodo record N" / "WFP Document …" titles with filler descriptions. They're honestly flagged in `notes`, but they read as broken cards and should be resolved or withheld from a public draft.

4. **Tag/note leakage from the merge.** Free-text notes and tags bled between resources (`dynamical-org-catalog`'s Africa/seasonal note and tags) and stray format meta-tags (`publication`) slipped into `tags`.

5. **`login`/`unknown` over-applied to what are actually open embeds/catalogs.** Publish-to-web Power BI (`adaptation-finance-power-bi-dashboard`) and GEE catalog assets (`wri-drivers-of-forest-loss-1km`) are openly viewable.

6. **Theme facet strained by AI/tooling items.** OpenScholar, the ADK/GEE agents, canopy/embedding models etc. have no natural home in a topic taxonomy built around climate/agriculture subjects, so they got mis-filed (e.g., OpenScholar → `Adaptation`). Consider a cross-cutting handling for pure-methods/AI items rather than forcing a topic.

---

## 7. What I could NOT verify (searches that failed)

- `scientific-data-s41597-025-05257-5` — no matching record surfaced; nearby SciData DOIs exist but not this one.
- `zenodo-record-14961636`, `zenodo-record-17627111`, `zenodo-record-14443334` — Zenodo search returned nothing for these IDs.
- `nature-communications-s41467-026-72715-y`, `nature-article-s44458-026-00071-5` — titles not confirmable via search.
- `wfp-document-0000172936` — document ID not identifiable.
- `water-resources-research-article-2024wr039773` — title not confirmable.
- `loom-video-demo-291e886a` — video content not inspectable.
- `nature-climate-change-article-s41558-025-02372-4` — a plausible title surfaced in a search summary but was not confirmed against nature.com directly; treat as "likely", not certain.

*Verification method: WebSearch only (page-fetch/curl not used). Where a search returned nothing, it is reported above rather than guessed.*
