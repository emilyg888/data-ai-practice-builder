# MVP 2 Dashboard

This folder contains the MVP 2 local-first dashboard for the AI Accelerator.

## What it does

- scans the practice knowledge base Markdown files
- extracts lightweight metadata from front matter and headings
- provides seven Streamlit modules:
  - Capability Browser
  - Pattern Browser
  - AWS GenAI Reference Browser
  - AWS GenAI Pattern Graph
  - Maturity Heatmap
  - Control Matrix
  - Client Assessment
- stores assessments locally as JSON
- exports assessment outputs as Markdown and CSV

## Run locally

1. Create a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
streamlit run app.py
```

Run the command from this folder:

`ai-accelerator-builder/10_dashboard/dashboard`

## Notes

- The knowledge repository remains the source of truth.
- The loader is tolerant of sparse or inconsistent front matter and derives metadata from paths, headings, and sections when needed.
- AWS GenAI reference notes under `05_reference_architectures/aws/` are surfaced as reusable reference-architecture IP.
- Those notes are integrated through Pattern Browser, AWS GenAI Reference Browser, AWS GenAI Pattern Graph, Control Matrix, and Client Assessment.
- Assessments are stored in `data/assessments/`.
