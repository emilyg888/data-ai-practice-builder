from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_ROOT = Path(__file__).resolve().parents[1]
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from components.heatmap import build_maturity_rows, render_heatmap_html
from components.tables import render_markdown_table
from services.assessment_store import default_assessment, list_assessments, load_assessment, save_assessment
from services.content_loader import load_repository_content
from services.export_service import build_assessment_summary, records_to_csv
from services.metadata_parser import slugify


def build_roadmap(rows: list[dict]) -> list[str]:
    high = [row["capability"] for row in rows if row["priority"] == "High"][:3]
    medium = [row["capability"] for row in rows if row["priority"] == "Medium"][:3]
    return [
        "Stabilise foundation capabilities: " + (", ".join(high) or "confirm baseline controls"),
        "Implement governed delivery patterns for medium-gap capabilities: " + (", ".join(medium) or "extend reusable workflow patterns"),
        "Industrialise control monitoring, evaluation, and operating model changes.",
    ]


def initial_focus_capabilities(assessment: dict, capabilities: list[dict]) -> list[str]:
    selected_ids = set(assessment.get("focus_capability_ids", []))
    if not selected_ids:
        return []
    selected_names = [
        capability["capability_name"]
        for capability in capabilities
        if capability["capability_id"] in selected_ids
    ]
    return selected_names


st.set_page_config(page_title="Maturity Heatmap", page_icon=":material/heat_pump:", layout="wide")

content = load_repository_content()
capabilities = content["capabilities"]
saved_assessments = list_assessments()

st.title("Maturity Heatmap")
st.caption("Score current and target maturity, calculate gaps, and prioritize delivery themes.")

assessment_options = ["New assessment"] + [item["assessment_id"] for item in saved_assessments]
selected_assessment_id = st.selectbox("Load assessment", assessment_options)
assessment = (
    load_assessment(selected_assessment_id)
    if selected_assessment_id != "New assessment"
    else default_assessment()
)
assessment = assessment or default_assessment()
saved_focus_capabilities = initial_focus_capabilities(assessment, capabilities)
all_capability_names = [item["capability_name"] for item in capabilities]
use_all_capabilities_default = not saved_focus_capabilities or len(saved_focus_capabilities) == len(all_capability_names)

top_left, top_right = st.columns(2)
with top_left:
    client_name = st.text_input("Client name", value=assessment.get("client_name", ""))
    business_domain = st.text_input("Business domain", value=assessment.get("business_domain", ""))
    use_case = st.text_input("Use case", value=assessment.get("use_case", ""))
with top_right:
    ai_role = st.text_input("AI role", value=assessment.get("ai_role", ""))
    risk_level = st.selectbox("Risk level", ["low", "medium", "high", "very_high"], index=["low", "medium", "high", "very_high"].index(assessment.get("risk_level", "high")))
    use_all_capabilities = st.checkbox("Use all capabilities", value=use_all_capabilities_default)
    if use_all_capabilities:
        focus_capabilities = all_capability_names
        st.caption(f"All {len(all_capability_names)} capabilities are included.")
    else:
        focus_capabilities = st.multiselect(
            "Focus capabilities",
            all_capability_names,
            default=saved_focus_capabilities,
            help="Select a smaller subset when you want a focused maturity assessment.",
        )
        if not focus_capabilities:
            st.warning("Select at least one capability, or turn on `Use all capabilities`.")

current_scores = dict(assessment.get("current_scores", {}))
target_scores = dict(assessment.get("target_scores", {}))

st.subheader("Capability Scoring")
for capability in capabilities:
    if capability["capability_name"] not in focus_capabilities:
        continue
    cols = st.columns([2.5, 1, 1, 1.2])
    cols[0].write(capability["capability_name"])
    current_scores[capability["capability_id"]] = cols[1].number_input(
        "Current",
        min_value=0,
        max_value=5,
        value=int(current_scores.get(capability["capability_id"], 0)),
        key=f"current_{capability['capability_id']}",
        label_visibility="collapsed",
    )
    target_scores[capability["capability_id"]] = cols[2].number_input(
        "Target",
        min_value=0,
        max_value=5,
        value=int(target_scores.get(capability["capability_id"], max(int(current_scores[capability["capability_id"]]), 3))),
        key=f"target_{capability['capability_id']}",
        label_visibility="collapsed",
    )
    cols[3].write(capability["risk_level"])

rows = build_maturity_rows(capabilities, current_scores, target_scores)
filtered_rows = [row for row in rows if row["capability"] in focus_capabilities]

metrics = st.columns(3)
metrics[0].metric("Average current", f"{sum(row['current'] for row in filtered_rows) / len(filtered_rows):.1f}" if filtered_rows else "0.0")
metrics[1].metric("Average target", f"{sum(row['target'] for row in filtered_rows) / len(filtered_rows):.1f}" if filtered_rows else "0.0")
metrics[2].metric("High-priority gaps", sum(1 for row in filtered_rows if row["priority"] == "High"))

st.subheader("Heatmap")
st.markdown(render_heatmap_html(filtered_rows), unsafe_allow_html=True)

st.subheader("Priority Gaps")
render_markdown_table(
    sorted(filtered_rows, key=lambda row: (-row["gap"], row["capability"])),
    [
        ("Capability", "capability"),
        ("Current", "current"),
        ("Target", "target"),
        ("Gap", "gap"),
        ("Risk", "risk"),
        ("Priority", "priority"),
    ],
    "No maturity rows available.",
)

roadmap = build_roadmap(filtered_rows)
st.subheader("Suggested Roadmap")
for step in roadmap:
    st.write(f"1. {step}")

assessment_payload = {
    "assessment_id": assessment.get("assessment_id") or slugify(f"{client_name}_{business_domain}_{use_case}") or "assessment",
    "client_name": client_name,
    "business_domain": business_domain,
    "use_case": use_case,
    "ai_role": ai_role,
    "risk_level": risk_level,
    "focus_capability_ids": [
        capability["capability_id"]
        for capability in capabilities
        if capability["capability_name"] in focus_capabilities
    ],
    "current_scores": current_scores,
    "target_scores": target_scores,
    "selected_patterns": assessment.get("selected_patterns", []),
    "required_controls": assessment.get("required_controls", []),
    "roadmap": roadmap,
}

save_col, export_col = st.columns(2)
with save_col:
    if st.button("Save assessment"):
        save_assessment(assessment_payload)
        st.success(f"Saved {assessment_payload['assessment_id']}.")
with export_col:
    st.download_button(
        "Export maturity CSV",
        data=records_to_csv(
            filtered_rows,
            [
                ("Capability", "capability"),
                ("Current", "current"),
                ("Target", "target"),
                ("Gap", "gap"),
                ("Risk", "risk"),
                ("Priority", "priority"),
            ],
        ),
        file_name=f"{assessment_payload['assessment_id']}_maturity.csv",
    )

st.download_button(
    "Export assessment summary",
    data=build_assessment_summary(assessment_payload, filtered_rows, [], []),
    file_name=f"{assessment_payload['assessment_id']}_summary.md",
)
