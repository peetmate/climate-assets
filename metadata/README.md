# Federated CDH metadata

Each card in the [source catalogue](../climate-assets.json) has a YAML file linked from the [register](register.csv). Data and software stay with their providers. The register tracks the resource described, the provider route, the editing outcome and owner review. The first pass covers catalogue commit `2969f36` on 13 November 2026.

* [Records](records/) contain metadata ready for CDH submission. Each passed the CDH profile and cross-field validator. Owner review is tracked independently.
* [Drafts](drafts/) contain partial records. A missing access field in a draft means access still needs checking. The CDH standard interprets omission as public on publication.
* [Gaps](gaps.csv) lists blocking questions and optional enrichment by card and field. The provider route identifies the resource under discussion. Consult [evidence](evidence.csv) for request forms, source documents and public enquiry routes. An HTTP status records a retrieval attempt. It cannot establish rights, access to files or permission to reuse.

## Completing a record

1. Identify what a user will obtain. Keep the card ID for tracking. Check for an existing CDH record for that release. CROPGRIDS Figshare v1.08 and the FAO v2.0 republication illustrate why a title match alone is insufficient.
2. Start from verified provider metadata. Check the resource DOI, release, citation, copyright or licensing party, usage terms and actual location. Check variable definitions, units, resolution, geography, time coverage and limitations where applicable. Record the supporting URL and check date. Catalogue descriptions, contact leads, tags and terms are starting points in partial drafts. Resolve ambiguous wording before moving a draft to records.
3. Set access explicitly. Use `public` for a verified open resource. Use `restricted` for request, login or embargo and `non-public` for resources unavailable through public channels. Both require an `access_note`. Describe who may apply, where, what to include, and any provider conditions. For author-mediated access, use the published point of contact and give the resource name and version to request. Link forms with `create-form` and instructions or published contact routes with `help`. Prefer a stable data location. Where restricted data has no URL, the documented request or release page can serve as its location. A paywall on a paper, a failed fetch or a public abstract leaves file access unresolved.
4. Log missing facts in the gap register with a specific question. Try release metadata, repository documentation, licences, citation files and provider support before contacting an owner. Group remaining questions by owner, offer the populated draft for correction and record replies and dates. Keep correspondence private. Before sending email, show the recipients, subject and full draft to Pete and wait for his explicit approval of that draft.
5. Use the provider's version label. For genuinely unversioned resources, the standard allows an initial record version of 1. Check public release history first. CDH maintains these federated metadata records. Provider contacts describe their actual roles in producing, licensing and supplying the resource.
6. Validate against [CDH v0.5.0](https://github.com/CGIAR-Climate-Data-Hub/cdh-metadata-standard/tree/v0.5.0), including cross-field checks. From a checkout of that tag, install dependencies with `npm ci`, then run `node scripts/validate-yaml.js --profile spec/schemas/profiles/cdh.schema.json /absolute/path/to/metadata/records`. Check the resource-specific source and close resolved gaps. Move the YAML to records and update the register when all release blockers close.

## Methods and tools

The profile supports datasets, software, services and documents. ChooseGCM provides a worked software example with its package licence and the citation requested by its authors. WFP HumanitarianDataCube describes a STAC service with independently licensed collections. A methods paper can use document. Record which implementation, publication or endpoint was selected whenever a card describes several.

**Standards backlog.** The standalone DSSATLM-AgNeSy demo video (`loom-video-demo-291e886a`) has no audiovisual type in v0.5.0. Decide whether it should be discoverable as an independent resource, or linked to the software as a demonstration. Its draft and register row preserve that decision for later.

[CDH authoring guide](https://github.com/CGIAR-Climate-Data-Hub/cdh-metadata-standard/blob/v0.5.0/spec/authoring-guide.md)
