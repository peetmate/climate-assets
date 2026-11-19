# WorldPop API update and local checks

Checked 19 November 2026. No metadata submitted to CDH; no account created, key requested or connector installed.

## Identity and update decision

Existing `worldpop-hub-population-dataset-category` actually links to **Future Population Projections**: 2025–2100 SSP scenarios, about 1 km; linked listing names version 0.2. Corrected its title, description and federated service draft while retaining its ID and adding a related API link. Closed its public discovery-access question; native SSP files were not tested.

New `worldpop-api-v3-mcp` describes a distinct service: API 3.0.0 over Global2 R2025A v1, annual population and age/sex estimates for 2015–2030. Added a related link back to the SSP category. The existing modelling-covariates record remains separate. Catalogue now contains 164 entries; dataset-card count remains 31.

## Provider sources and local observations

- [Assistant guide](https://api.worldpop.org/v3/assistants): MCP Streamable HTTP endpoint, anonymous access, optional keys and tools.
- [Catalogue](https://api.worldpop.org/v3/catalog): Global2 R2025A, 100 m, 2015–2030, CC BY 4.0, dataset citations, 246 countries and 4,491 administrative units. Coverage counts are not physical file counts.
- [Agent guide](https://api.worldpop.org/v3/llms.txt): cell-centre polygon inclusion, administrative-unit age/sex shares, null versus zero, weighted exposure and limits.
- [Health](https://api.worldpop.org/v3/health): version 3.0.0, healthy; anonymous limits 1,000/day, 60/minute, three concurrent counting requests, 100,000 km² polygon area. Limits are a dated snapshot.
- [Original-file discovery](https://api.worldpop.org/v3/countries/RWA/files?year=2025): Rwanda 2025 R2025A population and age/sex GeoTIFF and ZIP links, per-resolution citations and STAC references. Discovery only; original rasters not downloaded or classified as cloud-optimised.
- [SSP category](https://hub.worldpop.org/project/categories?id=21) and [release listing](https://hub.worldpop.org/geodata/listing?id=145): verified scope correction.

Anonymous REST GET `/point?lon=36.8219&lat=-1.2864&year=2026&include=agesex` returned HTTP 200, population **81.88 estimated people per grid cell**, cell area **0.008546 km²**, Nairobi, Kenya, 2026, plus 20 age-class female/male pairs. Coordinates use EPSG:4326. These are model estimates, not enumerated people or density values.

Anonymous MCP POST `/mcp`: `initialize` (protocolVersion `2025-03-26`) and `tools/list` succeeded; 23 tools advertised. `tools/call` with `population_at_point` and the same lon/lat/year returned the same **81.88** in structuredContent (summary text rounded to 82). MCP serverInfo version **1.30.0** is recorded separately from API version and source release. Requests used no credentials and no private input data.

These are author-run local service smoke checks, not a fresh independent-agent entry-only test. Tested service endpoints are recorded in the new YAML; its final SHA-256 is `c37039de225cee17085e54a276cb9bb1e8acf901e532d0cec0704c9af30215cd`.

## Local validation and retained gaps

Catalogue schema, duplicate and licence consistency checks passed for 164 entries; Astro production build passed. Both service YAMLs remain `draft_with_gaps`: new API lacks service-specific citation and identified licensor; existing category additionally lacks a service version and service-specific licence. Dataset DOI and version are not substituted for service metadata.

Five new API questions logged: licensor identity, preferred service citation, software redistribution/self-hosting licence, full-release bytes/file manifest, and native-file selective-read formats. Data CC BY 4.0 does not establish software licensing. Successful service queries do not establish that all underlying raster distributions qualify for direct federation. Exposure weighting describes a model assumption, not observed harm.

## Source-release mapping summary

| Dataset, release and route | Cloud format / preparation | Redistribution / conditions | Data access | Can federate? | Download size and scope | Element count and unit | Evidence and open questions |
|---|---|---|---|---|---|---|---|
| Global2 R2025A v1 population and age/sex via API v3 | Selective API queries verified; original GeoTIFF cloud layout and required preparation unknown | Data CC BY 4.0; cite applicable population/age-sex release; software licence unknown | Anonymous service reads verified; approved key optional for higher quotas; native file reads not tested | Service queries usable; native dataset federation unconfirmed | Full-release stored bytes unknown | Physical file count unknown; 246 countries/4,491 admin units are coverage counts | API catalogue, health, agent guide and Rwanda file-discovery response; checked 2026-11-19 |

One source release assessed through service discovery: zero newly verified native federatable datasets, zero confirmed full-release or subset byte totals, one unknown full-release byte total.
