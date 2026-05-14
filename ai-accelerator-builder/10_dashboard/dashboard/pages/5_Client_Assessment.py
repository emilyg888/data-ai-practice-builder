from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_ROOT = Path(__file__).resolve().parents[1]
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from components.heatmap import build_maturity_rows
from components.sidebar_nav import render_sidebar_nav
from components.tables import render_markdown_table
from services.assessment_store import save_assessment
from services.content_loader import load_repository_content
from services.export_service import build_assessment_summary
from services.metadata_parser import slugify
from services.recommendation_engine import recommend_patterns


def build_assessment_roadmap(rows: list[dict], patterns: list[dict]) -> list[str]:
    high_gap_capabilities = [row["capability"] for row in rows if row["priority"] == "High"][:3]
    pattern_names = [pattern["pattern_name"] for pattern in patterns[:3]]
    return [
        "Stabilise foundation and control gaps in " + (", ".join(high_gap_capabilities) or "priority capabilities"),
        "Implement governed reusable patterns: " + (", ".join(pattern_names) or "confirm target patterns"),
        "Pilot with controlled users, then industrialise evaluation, monitoring, and governance evidence.",
    ]


def strip_summary_sections(markdown_text: str, headings: set[str]) -> str:
    lines = markdown_text.splitlines()
    output: list[str] = []
    skipping = False
    for line in lines:
        if line.strip() in headings:
            skipping = True
            continue
        if skipping and line.startswith("## "):
            skipping = False
        if not skipping:
            output.append(line)
    return "\n".join(output).strip()


st.set_page_config(page_title="Client Assessment", page_icon=":material/assignment:", layout="wide")
render_sidebar_nav("pages/5_Client_Assessment.py")

content = load_repository_content()
capabilities = content["capabilities"]
patterns = content["patterns"]
controls = content["controls"]
aws_references = content["aws_references"]

st.title("Client Assessment")
st.caption("Create an engagement-level view with recommended patterns, required controls, and a reusable summary.")

details_col, scope_col = st.columns(2)
with details_col:
    client_name = st.text_input("Client name")
    business_unit = st.text_input("Business unit")
    business_domain = st.text_input("Domain")
    use_case = st.text_input("Use case")
with scope_col:
    ai_role = st.text_input("AI role")
    risk_level = st.selectbox("Risk level", ["low", "medium", "high", "very_high"], index=2)
    decision_impact = st.text_input("Decision impact")
    selected_capabilities = st.multiselect("Relevant capabilities", [item["capability_name"] for item in capabilities])
    platform_focus = st.multiselect("Platform focus", ["aws", "azure", "snowflake", "databricks", "hybrid"], default=["aws"])

current_scores: dict[str, int] = {}
target_scores: dict[str, int] = {}

with st.expander("Maturity scoring", expanded=True):
    for capability in capabilities:
        if selected_capabilities and capability["capability_name"] not in selected_capabilities:
            continue
        cols = st.columns([2.4, 1, 1])
        cols[0].write(capability["capability_name"])
        current_scores[capability["capability_id"]] = cols[1].number_input(
            "Current",
            min_value=0,
            max_value=5,
            value=1,
            key=f"assessment_current_{capability['capability_id']}",
            label_visibility="collapsed",
        )
        target_scores[capability["capability_id"]] = cols[2].number_input(
            "Target",
            min_value=0,
            max_value=5,
            value=3,
            key=f"assessment_target_{capability['capability_id']}",
            label_visibility="collapsed",
        )

recommended = recommend_patterns(
    patterns,
    domain=business_domain,
    ai_role=ai_role,
    risk_level=risk_level,
    selected_capabilities=selected_capabilities,
)
default_patterns = [item["pattern_name"] for item in recommended[:3]]
selected_patterns = st.multiselect(
    "Recommended patterns",
    [item["pattern_name"] for item in recommended],
    default=default_patterns,
)
available_aws_families = sorted({note["aws_family"] for note in aws_references if note.get("aws_family")})
selected_aws_families = st.multiselect(
    "AWS GenAI reference families",
    available_aws_families,
    default=[family for family in ["bedrock_knowledge_bases", "bedrock_guardrails", "evaluation_monitoring", "lambda_orchestration"] if family in available_aws_families],
)

selected_pattern_records = [item for item in recommended if item["pattern_name"] in selected_patterns]
selected_aws_records = [note for note in aws_references if note.get("aws_family") in selected_aws_families]
required_controls = sorted(
    {
        control_name
        for pattern in selected_pattern_records
        for control_name in pattern.get("related_controls", [])
    }
    | {
        control_name
        for note in selected_aws_records
        for control_name in note.get("related_controls", [])
    }
)
control_records = [item for item in controls if item["control_name"] in required_controls or item["control_id"] in {slugify(name) for name in required_controls}]

rows = build_maturity_rows(capabilities, current_scores, target_scores)
focused_rows = [row for row in rows if not selected_capabilities or row["capability"] in selected_capabilities]
roadmap = build_assessment_roadmap(focused_rows, selected_pattern_records)

assessment = {
    "assessment_id": slugify(f"{client_name}_{business_domain}_{use_case}") or "client_assessment",
    "client_name": client_name,
    "business_unit": business_unit,
    "business_domain": business_domain,
    "use_case": use_case,
    "ai_role": ai_role,
    "decision_impact": decision_impact,
    "risk_level": risk_level,
    "platform_focus": platform_focus,
    "current_scores": current_scores,
    "target_scores": target_scores,
    "selected_patterns": [item["pattern_id"] for item in selected_pattern_records],
    "selected_aws_families": selected_aws_families,
    "required_controls": required_controls,
    "roadmap": roadmap,
}

summary_left, summary_right = st.columns([1.15, 1])
with summary_left:
    st.subheader("Recommended Patterns")
    render_markdown_table(
        selected_pattern_records,
        [
            ("Pattern", "pattern_name"),
            ("Match", "match_band"),
            ("Score", "recommendation_score"),
            ("Risk", "risk_level"),
        ],
        "No pattern recommendations selected.",
    )
    st.subheader("Required Controls")
    if control_records:
        render_markdown_table(
            control_records,
            [
                ("Control", "control_name"),
                ("Type", "control_type"),
                ("Evidence", "evidence_required"),
            ],
            "No controls found.",
        )
    else:
        for control_name in required_controls:
            st.write(f"- {control_name}")
    st.subheader("AWS GenAI References")
    st.caption("Review detailed AWS reference notes in the AWS GenAI Reference Browser page.")
    st.write(f"{len(selected_aws_records)} AWS reference notes are in scope for this assessment.")
with summary_right:
    st.subheader("Roadmap")
    for step in roadmap:
        st.write(f"1. {step}")
    st.subheader("Executive Summary")
    summary_markdown = build_assessment_summary(assessment, focused_rows, selected_pattern_records, control_records, selected_aws_records)
    summary_preview = strip_summary_sections(summary_markdown, {"## Required Controls", "## AWS GenAI Reference Notes"})
    st.markdown(summary_preview)

action_left, action_right = st.columns(2)
with action_left:
    if st.button("Save client assessment"):
        save_assessment(assessment)
        st.success(f"Saved {assessment['assessment_id']}.")
with action_right:
    st.download_button(
        "Export executive summary",
        data=summary_markdown,
        file_name=f"{assessment['assessment_id']}_executive_summary.md",
    )
