# Adversarial Review #2 — enriched catalogue (images, dates, authors, orgs, licences, links)

_Date: 2026-07-24. Method: deterministic structural scan (Python) + three mean web-verification agents over all 141 entries. Focus: duplication, missing data, and hallucinated author/email/org/licence/date/description fields._

## Verdict

The structure is sound (no empty core fields, no exact-dup URLs, no reusable-vs-licence contradictions). The weak point is exactly the auto-harvested **author / contact / organisation** fields: the audit found **5 HIGH issues, all wrong lead authors or fabricated/mismatched contact emails**, plus assorted MED/LOW (garbled source fields, one wrong title, questionable licences, two duplicate pairs). All HIGH and most MED/LOW have been fixed in `climate-assets.json`; see 'Fixes applied' at the end.

## Deterministic scan summary
- Near-duplicate title pairs: 2 (GROW-Africa descriptor+dataset = real dup, merged; Global Nature Watch vs Global Pasture Watch = distinct, kept).
- Empty core fields (title/desc/url/themes): 0.
- Empty author-name-with-affiliation: 8 (render bug fixed — now shows org cleanly).
- reusable-vs-licence contradictions: 0.
- Undated & non-ongoing: 17 (completeness gap, not error).
- Suspect emails: 2 (CRA5 gmail — since cleared).

---

# Adversarial fact-check — adv_in_1.json

Audit of 44 catalogue entries. Only entries with a problem are listed. Clean entries are omitted.
Verification method: web_fetch of source URLs plus WebSearch on titles/DOIs. Where a claim could not be
confirmed or refuted from public sources, it is marked "unverifiable" rather than corrected.

| id | field | problem | correct value (with source) | severity |
|----|-------|---------|------------------------------|----------|
| impacts-of-climate-change-on-global-agriculture-accounting-for-adaptation | lead_contact.name / affiliation / organisations | Names **Jiacan Yuan (Fudan University)** as lead contact. Yuan is the LAST of ~25 authors. The paper is universally "Hultgren et al." — first author and corresponding author is Andrew Hultgren. Naming Yuan as lead, and listing only "Fudan University" as the organisation, is wrong/misleading. | Corresponding & first author: **Andrew Hultgren**, Dept of Agricultural and Consumer Economics, **University of Illinois Urbana-Champaign** (a Climate Impact Lab collaboration incl. UC Berkeley, EPIC-Chicago, Rhodium, Rutgers). Source: https://www.nature.com/articles/s41586-025-09085-w (author list; ✉ = Hultgren) and https://experts.illinois.edu/en/publications/ | HIGH |
| harveststat-africa | lead_contact.name / affiliation | Names **Carsten Meyer (Martin Luther University Halle-Wittenberg)** as lead contact. Meyer is a genuine co-author but NOT the corresponding author. | Corresponding authors are **Donghoon Lee** and **Weston Anderson** (first author Donghoon Lee). Source: https://www.nature.com/articles/s41597-025-05001-z and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12022251/ | HIGH |
| zenodo-record-14961636 / scientific-data-s41597-025-05257-5 | duplicate | Two entries cover the same underlying resource (GROW-Africa): the Scientific Data data-descriptor and the Zenodo dataset it describes. Both typed "dataset", same contacts (Geyman / Hausmann), same organisations. Likely a duplicate/overlap pair rather than two distinct catalogue items. | Same resource — descriptor: https://www.nature.com/articles/s41597-025-05257-5 ; data: https://zenodo.org/records/14961637 | MED |
| annual-global-gridded-livestock-1961-2021 | date / title / url | Labelled "(preprint)" and points at the ESSD preprint page. The paper is now formally published, so "preprint" is stale. Lead "Z. Du" is correct. | Published: ESSD vol. 17, pp. 5543–5556, 2025 — https://essd.copernicus.org/articles/17/5543/2025/ | LOW |
| ecosystem-integrity-index | licence | Licence stated as **Apache-2.0** (a software licence) with reusable=true, but this is a data/index platform (The Landbanking Group / UNEP-WCMC) and the entry itself admits "detailed content could not be retrieved". Apache-2.0 for this resource is questionable and could not be confirmed. | unverifiable — no licence confirmable at https://ecosystemintegrityindex.org/ | LOW |
| eth-cocoa-suitability-map | organisations | Lists "KMPT" as an organisation — no such co-author affiliation could be verified. Confirmed author institutions are ETH Zürich (EcoVision Lab) and University of Cambridge (Rachael Garrett), plus in-country partners. "KMPT" appears spurious. | Authors: Kalischek, Lang, Renier, Caye Daudt, Addoah, Thompson, Blaser-Hart, Garrett, Schindler, Wegner — ETH Zürich / Univ. Cambridge. Source: https://arxiv.org/abs/2206.06119 | LOW |
| agmrv-knowledge-portal | date | Oddly precise date "2018-06-11" for a standing portal; likely a repository record artefact, not the resource date. Could not be verified. | unverifiable — https://www.agmrv.org/knowledge-portal/ | LOW |
| unfccc-ghg-data-interface | date | Oddly precise date "2019-11-08" for a long-running data interface; not verifiable as a meaningful publication date. | unverifiable — https://data.unfccc.int/ | LOW |

## Notes on entries checked and cleared (not flagged)
- **harmonised-dataset-for-earth-system-foundation-models (WorldTensor)** — authors Carlos Rodriguez-Pardo & Massimo Tavoni, affiliations (Politecnico di Milano; RFF-CMCC; CMCC), date 2026-07, description all confirmed. arXiv 2607.03298.
- **what-climate-smart-agriculture-means-for-smallholder-farmers** — lead Chania Frost confirmed as an author (with Kartik Jayaram, Gillian Pais); "33 measures" and India/Ethiopia/Mexico confirmed.
- **global-adaptation-mapping-initiative (GAMI)** — Dona van Eeden (Programme Coordinator, UCT), email and project-lead Nicholas Simpson confirmed.
- **world-bank-data360-climate-atlas** — Thijs Benschop confirmed as story author; date 2026-05 confirmed.
- **eth-cocoa-suitability-map** — description numbers verified (37.4% CIV / 13.5% Ghana protected-area forest loss; up to 40% underestimate in Ghana).
- **cropgrids** (Maggi), **global-spatially-explicit-crop-water-consumption** (Vanham, IWMI confirmed), **spatial-frameworks-...-yield-gaps** (Grassini) — named contacts are the senior/corresponding authors with correct affiliations; accepted despite not being first authors (first authors are Tang, Chukalla, and Rattalino Edreira respectively).

---

# Adversarial fact-check — adv_in_2.json

Audited 44 entries against live web sources (Nature/Springer metadata, publisher pages, WebSearch). Only entries with a problem are listed. Entries not listed were checked and found acceptable (e.g. Cael/uchicago email confirmed; Sapkota-Singh-Mukherji authorship confirmed; grazing PNAS first author Chaohui Li confirmed; Jiang crop-water first author confirmed; Lizana degree-days first author confirmed; Ton "7 billion" first author confirmed; Kummu GDP confirmed; CRA5 licence CC-BY-NC-ND confirmed).

| id | field | problem | correct value (with source URL) | severity |
|---|---|---|---|---|
| cra5-compressed-reanalysis-atmospheric-dataset | lead_contact.email | `hantao10200@gmail.com` is NOT a published contact for this paper. The Data Descriptor names two corresponding authors with institutional emails; the gmail appears nowhere in the article. Tao Han is first author but not a listed corresponding author. | Corresponding authors: **Song Guo — songguo@cse.ust.hk** and **Lei Bai — bailei@pjlab.org.cn** ([nature.com/articles/s41597-026-07381-2](https://www.nature.com/articles/s41597-026-07381-2)) | HIGH |
| global-gridded-multi-temporal-datasets-human-population-distribution-modelling | lead_contact.name | Maksym Bondarenko is neither the first nor the corresponding author — he is the last-listed author. The article explicitly states the corresponding author, who is also first author. | **Dorothea Woods** (first author AND "Corresponding author: Dorothea Woods") ([gatesopenresearch.org/articles/9-72](https://gatesopenresearch.org/articles/9-72)) | HIGH |
| cropland-ghg-emissions-removals-climate-action-food-systems | title | Title does not match the article at this DOI. Catalogue title ("Cropland greenhouse gas emissions and removals for climate action in food systems") and description ("removals … mitigation trade-offs with food productivity") appear embellished vs the actual paper, which is an emissions assessment. "(Cao et al. 2026)" attribution is correct (Peiyu Cao is first author; Herrero corresponding). | Real title: **"Spatially explicit global assessment of cropland greenhouse gas emissions circa 2020"**, Nat. Clim. Chang. vol 16, pp 354–363 ([nature.com/articles/s41558-026-02558-4](https://www.nature.com/articles/s41558-026-02558-4)) | MED |
| nature-climate-change-article-s41558-025-02372-4 | source | `source` field is garbled: `"https://www.nature.com/articles/s41558-025-02372-4 (confirmed via Nazarbayev, Vienna, Macquarie, Aston, Vienna institutional repositories; EurekAlert)"` — this is an internal verification note, not a source. Should be the journal name. Lead contact Sander van der Linden (corresponding author) verified correct. | source should read **"Nature Climate Change"** (vol 15(7), 725–735) ([nature.com/articles/s41558-025-02372-4](https://www.nature.com/articles/s41558-025-02372-4)) | MED |
| cra5-dataset-github | lead_contact.email | `hantao10200@gmail.com` could not be corroborated as the maintainer's real/published address from any source; the associated paper uses institutional emails only. Repo owner is `taohan10200`. Treat gmail as unverified. | unverifiable (repo: [github.com/taohan10200/CRA5](https://github.com/taohan10200/CRA5)) | MED |
| nature-climate-change-article-s41558-025-02372-4 | licence | `licence: proprietary` is questionable — article is open access ("© 2025 The Author(s)", free to read). Exact CC variant not confirmed. | likely open-access CC licence, not proprietary — unverifiable exact variant ([nature.com/articles/s41558-025-02372-4](https://www.nature.com/articles/s41558-025-02372-4)) | LOW |
| climate-change-drives-a-decline-in-global-grazing-systems | date | `2026-02-09` differs from the published issue date (PNAS vol 123(7), 17 Feb 2026). Minor (online vs issue date). | 2026-02-17 issue ([pubmed.ncbi.nlm.nih.gov/41662520](https://pubmed.ncbi.nlm.nih.gov/41662520/)) | LOW |
| cra5-dataset-github / cra5-compressed-reanalysis-atmospheric-dataset | duplicate | Two entries for the same underlying CRA5 resource (GitHub repo vs the Scientific Data descriptor paper). Distinct resource types, but overlapping — flag for de-dup review. | n/a | LOW |

## Notes on entries checked and cleared
- **spatially-explicit-harmonized-global-dataset-of-critical-infrastructure**: first author is Sadhana Nirandjan, but lead_contact **Jeroen Aerts is the corresponding author** (Nature metadata `dc.creator`/`citation_author` = Aerts) — acceptable.
- **climateaf-high-resolution-climate-africa**: first author is Sarah A. Namiiro; lead_contact Andreas Hamann is second author and plausibly corresponding — acceptable, email is his known ualberta address.
- Author-name checks that PASSED: cropland (Cao/Herrero), grazing (Li), crop-water (Jiang), degree-days (Lizana), MERCURY (Nath), Ton, Kummu, Cael (uchicago confirmed), Sapkota (Sapkota/Singh/Mukherji).

---

# Adversarial fact-check — adv_in_3.json

Audited 44 catalogue items against the live web. Only items with a problem are listed. Items not listed were spot-checked and found acceptable (author, licence, date, and description claims verified where possible).

## Findings

| id | field | problem | correct value (with source URL) | severity |
|---|---|---|---|---|
| methods-for-assessing-climate-vulnerability-in-africa | lead_contact.email | Email `EAOdipo@kemri-wellcome.org` is inconsistent and appears fabricated. It fuses the corresponding author's initials ("EA", Emelda A. Okiro) with the first author's surname (Odipo). It matches neither person's standard institutional address (Odipo would be ~EOdipo; the corresponding author is Okiro). | Corresponding author is **Emelda A. Okiro** (authors: Odipo E, Onyango SA, Macharia PM, Kiti MC, Okiro EA). Contact email should be Okiro's, not a blended Odipo address. Source: https://link.springer.com/article/10.1186/s44329-025-00041-7 | HIGH |
| methods-for-assessing-climate-vulnerability-in-africa | lead_contact.name | Names first author Emily Odipo as the contact but pairs her with an email that is not hers; corresponding author (the actual contact) is Emelda A. Okiro. | See above — Okiro is corresponding author. https://link.springer.com/article/10.1186/s44329-025-00041-7 | MED |
| nature-communications-s41467-026-72715-y | organisations | Only "University of Delaware" listed. The paper has two authors; the **first author, Marta Tuninetti**, and her institution are omitted entirely. | Add Marta Tuninetti's affiliation (Politecnico di Torino, Italy). Author list confirmed: Marta Tuninetti (Aff1) & Kyle Frankel Davis (Univ. Delaware). Source: https://www.nature.com/articles/s41467-026-72715-y | MED |
| cgiar-on-hugging-face | lead_contact | A specific individual (Jawoo Koo) with affiliation "CGIAR Accelerator on Digital Transformation" is attributed as lead_contact to a generic Hugging Face organisation page that publishes no named contact. Attribution is unverifiable and the affiliation label does not match a documented CGIAR entity (Koo's documented affiliation is IFPRI). | Unverifiable — the HF org page (https://huggingface.co/CGIAR) lists no lead contact. | MED |
| nature-article-s44458-026-00071-5 | source | The `source` field contains a raw URL ("https://www.nature.com/articles/s44458-026-00071-5") instead of the journal name. The description correctly identifies the journal. | Journal is **Communications Sustainability** (Nature Portfolio). https://www.nature.com/articles/s44458-026-00071-5 | LOW |
| choosegcm-toolkit-to-select-general-circulation-models-in-r | licence | Item is typed as a `publication` in Global Change Biology (Wiley) but licence is given as "MIT". MIT is the chooseGCM R-package code licence, not the article licence. Potentially misleading for a journal article. | MIT applies to the software; the Wiley article carries its own (CC-BY or standard Wiley) licence. https://onlinelibrary.wiley.com/doi/10.1111/gcb.70008 | LOW |
| alphaearth-foundations / alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail | duplicate | Possible content overlap: the arXiv model entry and the DeepMind blog entry describe the same AlphaEarth Foundations release in two forms (both dated late July 2025, same lead Christopher F. Brown). Legitimate as separate artifact types (paper vs blog) but flag as near-duplicate content. | Same underlying resource; retain intentionally or de-duplicate. https://arxiv.org/abs/2507.22291 / https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/ | LOW |

## Items verified as OK (no action)

- global-assessment-population-exposure... — Stalhandske (ETH Zurich) lead, 2025, confirmed.
- merge-dataset... — Scales lead (UNMC), licence CC-BY-NC-ND-4.0 confirmed correct.
- socioeconomic-predictors-vulnerability-flood-induced-displacement — Mester (PIK) lead confirmed; description accurate.
- projections-of-future-agricultural-management... — Baojing Gu corresponding (Zhejiang); Wang first author; IIASA/Sichuan Agric. affiliations confirmed.
- helmets-labeling-crops... — Nakalembe first/corresponding, UMD, vol 12 art 1496 (2025) confirmed.
- earth-observations-for-climate-adaptation... — Connors (ESA) lead, 2025-11-11 confirmed.
- climate-analogues-homologues-agricultural-systems — Vandamme (IITA) first author confirmed; title matches.
- building-and-managing-local-databases...geeLite — Kurbucz (World Bank), WP 11115 confirmed.
- farm-level-in-season-crop-identification-for-india — Deshpande (Google) lead; date 2025-06-30 confirmed (arXiv 2507.02972).
- synthesizing-scientific-literature... (OpenScholar) — Hajishirzi is senior/corresponding author (first author Akari Asai); acceptable; 2026-02 confirmed.

Note: several other named-lead emails (bjgu@zju.edu.cn, jan.petzold@lmu.de, audrey.jolivot@cirad.fr, cnakalem@umd.edu, sscales@unmc.edu, generic org addresses) were checked against author/affiliation and are consistent/plausible; none showed the fabrication signature seen in the Odipo entry.

---

## Fixes applied (this pass)

**HIGH — wrong lead author / fabricated email (all corrected or cleared):**
- impacts-of-climate-change...adaptation → lead **Andrew Hultgren** (Univ. of Illinois); orgs corrected.
- harveststat-africa → lead **Donghoon Lee** (was Carsten Meyer).
- global-gridded...population (Gates) → lead **Dorothea Woods** (was Bondarenko, last author).
- cra5-compressed... & cra5-dataset-github → fabricated gmail **cleared** (kept Tao Han as first author).
- methods...vulnerability-in-africa → contact **Emelda A. Okiro**; blended fake email **cleared**.

**MED/LOW:**
- GROW-Africa duplicate merged (Zenodo folded into the Scientific Data descriptor).
- cropland-ghg title corrected to the real paper title; description de-embellished.
- Two garbled `source` fields (verification-note / raw URL) → journal names (Nature Climate Change; Communications Sustainability).
- nature-communications drought-hotspots → added Politecnico di Torino (Tuninetti).
- cgiar-on-hugging-face → unverifiable lead contact cleared.
- Livestock 'preprint' → published (ESSD 2025) + link.
- Questionable licences cleared (ecosystem-integrity-index Apache-2.0; chooseGCM MIT = code not article; NCC article proprietary→open/unknown).
- eth-cocoa spurious org 'KMPT' removed; portal artefact dates cleared (AgMRV, UNFCCC); grazing date corrected.

## Systemic caveat
Lead-author name and especially **contact email are the least-reliable fields** — they were harvested from page metadata/search and the fabrication pattern (blending initials+surname, first-vs-corresponding-author confusion, personal gmail) recurs. **Verify the contact on any entry before it is published or used to email someone.** Emails are only retained where a genuine published address was confirmed.
