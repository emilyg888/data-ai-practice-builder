---
type: design_doc
design_doc_id: mvp2_dashboard_runtime_notes
status: draft
---

# MVP 2 Dashboard Runtime Notes

This folder contains the runnable Streamlit implementation of MVP 2.

## Core modules

1. Capability Browser
2. Pattern Browser
3. AWS GenAI Reference Browser
4. Maturity Heatmap
5. Control Matrix
6. Client Assessment

## Principle

The dashboard is the navigation and assessment layer, not the source of truth.

## AWS GenAI IP integration

The AWS GenAI reference architecture notes under `05_reference_architectures/aws/` are surfaced through:

- Pattern Browser
- AWS GenAI Reference Browser
- Control Matrix
- Client Assessment

The dashboard parses YAML front matter and infers AWS pattern families, service families, and control themes from each reference note.
