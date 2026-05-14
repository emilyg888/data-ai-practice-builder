from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_ROOT = Path(__file__).resolve().parent
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from components.sidebar_nav import render_sidebar_nav
from services.content_loader import load_repository_content


st.set_page_config(
    page_title="AI Accelerator",
    page_icon=":material/account_tree:",
    layout="wide",
)


content = load_repository_content()
render_sidebar_nav("app.py")

st.title("AI Accelerator Dashboard")
st.caption("MVP 2: navigation, assessment, and decision-support over the Markdown knowledge base")

hero_left, hero_right = st.columns([2, 1])
with hero_left:
    st.markdown(
        """
        This dashboard is the local-first consultant workbench for the practice knowledge scaffold.
        The repository remains the source of truth. The app reads the Markdown assets, normalizes metadata,
        and supports capability discovery, pattern selection, maturity assessment, control mapping, and
        engagement-ready summaries.
        """
    )
with hero_right:
    st.markdown(
        """
        **Modules**

        - Capability Browser
        - Pattern Browser
        - AWS GenAI Reference Browser
        - AWS GenAI Pattern Graph
        - Maturity Heatmap
        - Control Matrix
        - Client Assessment
        """
    )

metric_columns = st.columns(5)
metric_columns[0].metric("Capabilities", len(content["capabilities"]))
metric_columns[1].metric("Patterns", len(content["patterns"]))
metric_columns[2].metric("AWS references", len(content["aws_references"]))
metric_columns[3].metric("Controls", len(content["controls"]))
metric_columns[4].metric("Playbooks", len(content["playbooks"]))

left, right = st.columns([1.2, 1])
with left:
    st.subheader("Repository Diagnostics")
    if content["validation_errors"]:
        st.warning("Some files are missing preferred metadata. The dashboard is using fallback parsing.")
        for issue in content["validation_errors"][:20]:
            st.write(f"- {issue}")
    else:
        st.success("No metadata validation issues detected in the scanned scope.")

    st.subheader("Maturity Scale")
    for level in content["maturity_levels"]:
        st.write(f"**{level['level']} - {level['name']}**: {level['description']}")

with right:
    st.subheader("How To Use")
    st.write("1. Start in Capability Browser to inspect the practice library.")
    st.write("2. Use Pattern Browser to shortlist reusable patterns.")
    st.write("3. Use AWS GenAI Reference Browser to inspect implementation notes.")
    st.write("4. Use AWS GenAI Pattern Graph to inspect the technical knowledge graph.")
    st.write("5. Score current and target capability maturity in Maturity Heatmap.")
    st.write("6. Review required controls in Control Matrix.")
    st.write("7. Save an engagement view and export the summary in Client Assessment.")

    st.subheader("Scanned Source")
    st.code(str(content["knowledge_root"]))
