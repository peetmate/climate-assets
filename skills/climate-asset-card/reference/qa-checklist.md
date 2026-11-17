# Adversarial QA checklist for asset cards

Run this as a hostile reviewer: assume each field is wrong until the web proves it right. Verify
against the primary source (fetch the URL; if blocked, search the DOI/title). Never invent a
correction you can't source — write "unverifiable" and flag `⚠ NEEDS REVIEW`.

## Per-entry checks (severity)

**HIGH — a user would be misled or emailed the wrong person:**
- `lead_contact.name` — is this really the first/corresponding author? (Not the last-listed author.)
- `lead_contact.email` — is it the actual published address? Watch for the fabrication signature:
  initials of one author + surname of another; a personal gmail with no corroboration. If not
  clearly published → clear it.
- `organisations` — real affiliations of the actual authors/host? Not invented acronyms.
- `licence` — matches the real licence, and is it the *content/data* licence (not the code licence
  of an associated repo)? `reusable` must follow (permissive only).
- `description` — any invented numbers, findings, or claims not in the source?
- duplicate — is this the same resource as another entry?
- `source` — is it the provider/journal, not the hosting platform (Power BI / Loom / GitHub Pages)?

**MED — wrong but low-harm:**
- `date` — correct year? (online vs issue date is fine.)
- `title` — verbatim / accurate, not embellished or a placeholder ("Journal article s41597-…").
- `type` — matches what the URL serves.
- `themes` — ≤2, topical, primary correct.
- `source`/`notes` — no raw URLs or internal verification notes leaking into a display field.

**LOW — polish:**
- `spatial_resolution`/`temporal_coverage` present where the source states them.
- `image` not a generic/CAPTCHA/placeholder.
- tags not contradictory or missing an obvious one (e.g. an Africa dataset without `africa`).

## Structural checks (deterministic, run over the whole file)
- Schema-valid; unique ids; ≤2 themes; no empty core fields (title/description/url/themes).
- No `reusable=true` with an NC/ND/proprietary/empty licence. Permissive = CC0, CC-BY, CC-BY-SA,
  MIT, BSD, Apache, GPL/LGPL/AGPL, ODbL, Etalab-2.0, OGL, public domain (see SKILL.md §4). Run
  `python3 scripts/validate_catalogue.py --check` — it does every structural check in this section.
- No entry whose author line, source line and org line are all the same string (repetition bug).
- Near-duplicate titles (>0.86 similarity) reviewed by hand.
- Undated & non-ongoing entries listed (completeness gap, not necessarily an error).

## Dataset mapping checks

- Cross-check each badge against its provider source. Verify the federation decision uses the same release and route for selective reads, redistribution rights and anonymous data access.
- Verify download bytes and the count/unit independently against the dated provider inventory. Check release versus subset, including archive contents or ancillary files. Keep missing quantities explicit in the handoff.
- Check that gated datasets have a request or access route where documented. Log unanswered questions and conflicting evidence. Keep validation local.

## Output
Return the [dataset mapping summary](../SKILL.md#dataset-mapping-summary) for each dataset, including those with no QA findings. Report findings in a severity-ranked table: `id | field | problem | correct value (with source) | severity`. Fix HIGH
and MED; note the systemic caveat that author/email is the least-reliable field and must be verified
before any card is used to contact someone or is published.
