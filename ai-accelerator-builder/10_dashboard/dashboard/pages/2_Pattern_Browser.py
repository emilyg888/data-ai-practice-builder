from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_ROOT = Path(__file__).resolve().parents[1]
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from components.cards import render_tag_list
from services.content_loader import load_repository_content
from services.export_service import records_to_csv
from services.recommendation_engine import recommend_patterns


def compact_list(values: list[str], limit: int = 3) -> str:
    if not values:
        return "None mapped"
    if len(values) <= limit:
        return ", ".join(values)
    return ", ".join(values[:limit]) + f" +{len(values) - limit} more"


def render_match_badge(match_band: str) -> str:
    styles = {
        "Recommended": ("#0f3d2e", "#d7f5e6"),
        "Relevant": ("#214260", "#d6ebff"),
        "Possible": ("#5b4211", "#ffe9b3"),
        "Low match": ("#4a2b2b", "#ffd5d5"),
    }
    background, foreground = styles.get(match_band, ("#2c2c34", "#f5f5f5"))
    return (
        f"<span style='display:inline-block; padding:4px 10px; border-radius:999px; "
        f"background:{background}; color:{foreground}; font-size:0.78rem; font-weight:700;'>"
        f"{match_band}</span>"
    )


def inject_page_css() -> None:
    st.markdown(
        """
        <style>
        .pb-toolbar-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.75rem;
            margin-top: 0.8rem;
        }
        .pb-metric {
            background: rgba(255,255,255,0.035);
            border-radius: 14px;
            padding: 0.8rem 0.9rem;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .pb-metric-label {
            color: rgba(255,255,255,0.65);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .pb-metric-value {
            font-size: 1.45rem;
            font-weight: 700;
            margin-top: 0.2rem;
        }
        .pb-result-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.035), rgba(255,255,255,0.02));
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 1rem 1.1rem;
            margin-bottom: 0.9rem;
        }
        .pb-result-title {
            font-size: 1.1rem;
            font-weight: 700;
            margin: 0.15rem 0 0.55rem 0;
        }
        .pb-result-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.6rem 1rem;
            margin-top: 0.85rem;
        }
        .pb-label {
            color: rgba(255,255,255,0.6);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 0.18rem;
        }
        .pb-value {
            font-size: 0.95rem;
            line-height: 1.45;
        }
        .pb-detail {
            background: rgba(255,255,255,0.025);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 1.2rem 1.25rem;
            margin-top: 0.6rem;
        }
        @media (max-width: 1100px) {
            .pb-toolbar-grid,
            .pb-result-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


st.set_page_config(page_title="Pattern Browser", page_icon=":material/schema:", layout="wide")

inject_page_css()

content = load_repository_content()
patterns = content["patterns"]
capabilities = content["capabilities"]
controls = content["controls"]
aws_references = content["aws_references"]

st.title("Pattern Browser")
st.caption("Select reusable architecture patterns and link them to AWS GenAI implementation references.")

practice_tab, aws_tab = st.tabs(["Practice patterns", "AWS-linked references"])

with practice_tab:
    with st.sidebar:
        domain = st.selectbox("BFSI domain", [""] + sorted({domain for pattern in patterns for domain in pattern.get("business_domains", [])}))
        ai_role = st.selectbox("AI role", [""] + sorted({impact for pattern in patterns for impact in pattern.get("ai_impact", [])}))
        risk_level = st.selectbox("Risk level", [""] + sorted({pattern.get("risk_level", "") for pattern in patterns if pattern.get("risk_level", "")}))
        selected_capabilities = st.multiselect("Required capability", [item["capability_name"] for item in capabilities])
        selected_controls = st.multiselect("Control requirement", [item["control_name"] for item in controls])

    recommended = recommend_patterns(
        patterns,
        domain=domain,
        ai_role=ai_role,
        risk_level=risk_level,
        selected_capabilities=selected_capabilities,
        selected_controls=selected_controls,
    )

    visible = recommended[:12]
    selected_options = [item["pattern_name"] for item in visible] or [item["pattern_name"] for item in recommended]

    action_col, export_col = st.columns([1.2, 0.8], vertical_alignment="bottom")
    with action_col:
        st.write(f"{len(recommended)} recommended patterns returned.")
    with export_col:
        st.download_button(
            "Export recommendations to CSV",
            data=records_to_csv(
                recommended,
                [
                    ("Pattern", "pattern_name"),
                    ("Match band", "match_band"),
                    ("Score", "recommendation_score"),
                    ("Risk", "risk_level"),
                    ("Domains", "business_domains"),
                    ("Controls", "related_controls"),
                ],
            ),
            file_name="pattern_recommendations.csv",
            use_container_width=True,
        )

    st.markdown(
        f"""
        <div class="pb-toolbar-grid">
            <div class="pb-metric">
                <div class="pb-metric-label">Patterns returned</div>
                <div class="pb-metric-value">{len(recommended)}</div>
            </div>
            <div class="pb-metric">
                <div class="pb-metric-label">Top band</div>
                <div class="pb-metric-value">{recommended[0]["match_band"] if recommended else "None"}</div>
            </div>
            <div class="pb-metric">
                <div class="pb-metric-label">Capabilities selected</div>
                <div class="pb-metric-value">{len(selected_capabilities)}</div>
            </div>
            <div class="pb-metric">
                <div class="pb-metric-label">Controls selected</div>
                <div class="pb-metric-value">{len(selected_controls)}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not recommended:
        st.info("No patterns are available for the current selection.")
    else:
        selected_name = st.selectbox("Pattern detail", selected_options, help="Choose a pattern to inspect.")
        list_col, insight_col = st.columns([1.15, 0.85], vertical_alignment="top")
        with list_col:
            for pattern in visible:
                st.markdown(
                    f"""
                    <div class="pb-result-card">
                        <div>{render_match_badge(pattern["match_band"])}</div>
                        <div class="pb-result-title">{pattern["pattern_name"]}</div>
                        <div class="pb-value">{pattern["problem_solved"] or "No summary available."}</div>
                        <div class="pb-result-grid">
                            <div>
                                <div class="pb-label">Score</div>
                                <div class="pb-value">{pattern["recommendation_score"]}</div>
                            </div>
                            <div>
                                <div class="pb-label">Risk</div>
                                <div class="pb-value">{pattern["risk_level"]}</div>
                            </div>
                            <div>
                                <div class="pb-label">Domains</div>
                                <div class="pb-value">{compact_list(pattern["business_domains"])}</div>
                            </div>
                            <div>
                                <div class="pb-label">Controls</div>
                                <div class="pb-value">{compact_list(pattern["related_controls"])}</div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        selected_pattern = next((item for item in recommended if item["pattern_name"] == selected_name), recommended[0])
        linked_aws = [
            note
            for note in aws_references
            if set(note.get("related_controls", [])).intersection(set(selected_pattern.get("related_controls", [])))
        ][:10]
        with insight_col:
            st.markdown('<div class="pb-detail">', unsafe_allow_html=True)
            st.markdown(f"## {selected_pattern['pattern_name']}")
            detail_meta = st.columns(3)
            detail_meta[0].metric("Match", selected_pattern["match_band"])
            detail_meta[1].metric("Score", selected_pattern["recommendation_score"])
            detail_meta[2].metric("Risk", selected_pattern["risk_level"])
            st.write(selected_pattern["problem_solved"] or "No problem statement available.")
            if selected_pattern["match_reasons"]:
                render_tag_list("Why it matched", selected_pattern["match_reasons"])
            render_tag_list("Business domains", selected_pattern["business_domains"])
            render_tag_list("AI impact", selected_pattern["ai_impact"])
            render_tag_list("Required capabilities", selected_pattern["related_capabilities"])
            render_tag_list("Required controls", selected_pattern["related_controls"])
            if linked_aws:
                render_tag_list("Linked AWS references", [note["title"] for note in linked_aws[:4]])
            st.markdown(f"**Source file:** `{selected_pattern['file_path']}`")
            st.markdown("</div>", unsafe_allow_html=True)

        summary_tab, delivery_tab, aws_linked_tab = st.tabs(["Summary", "Capability and controls", "AWS references"])
        with summary_tab:
            st.write(selected_pattern["problem_solved"] or "No summary available.")
            if selected_pattern["when_to_use"]:
                st.markdown("**When to use**")
                st.write(selected_pattern["when_to_use"])
        with delivery_tab:
            left, right = st.columns(2)
            with left:
                st.markdown("**Required capabilities**")
                for item in selected_pattern["related_capabilities"] or ["No capability dependencies mapped."]:
                    st.write(f"- {item}" if item != "No capability dependencies mapped." else item)
            with right:
                st.markdown("**Required controls**")
                for item in selected_pattern["related_controls"] or ["No control dependencies mapped."]:
                    st.write(f"- {item}" if item != "No control dependencies mapped." else item)
        with aws_linked_tab:
            if linked_aws:
                st.download_button(
                    "Export linked AWS references",
                    data=records_to_csv(
                        linked_aws,
                        [
                            ("Title", "title"),
                            ("Family", "aws_family"),
                            ("Services", "aws_services"),
                            ("Controls", "related_controls"),
                            ("Source", "file_path"),
                        ],
                    ),
                    file_name="linked_aws_references.csv",
                )
                for note in linked_aws:
                    st.markdown(f"### {note['title']}")
                    st.caption(note["file_path"])
                    st.write(note["summary"] or "No summary available.")
                    render_tag_list("AWS family", [note["aws_family"]] if note.get("aws_family") else [])
                    render_tag_list("AWS services", note.get("aws_services", []))
                    render_tag_list("Control themes", note.get("related_controls", []))
            else:
                st.info("No AWS references matched the selected pattern controls.")

with aws_tab:
    st.caption("Search AWS GenAI implementation notes as reusable reference-architecture IP.")
    left, right = st.columns([1, 3], vertical_alignment="top")
    with left:
        search = st.text_input("Search AWS references")
        families = st.multiselect("Pattern family", sorted({note["aws_family"] for note in aws_references if note.get("aws_family")}))
        services = st.multiselect("AWS service", sorted({service for note in aws_references for service in note.get("aws_services", [])}))
        control_themes = st.multiselect("Control theme", sorted({control for note in aws_references for control in note.get("related_controls", [])}))

    filtered_aws = aws_references
    if search:
        lowered = search.lower()
        filtered_aws = [
            note for note in filtered_aws
            if lowered in note["title"].lower() or lowered in note["summary"].lower() or lowered in note["file_path"].lower()
        ]
    if families:
        filtered_aws = [note for note in filtered_aws if note.get("aws_family") in families]
    if services:
        filtered_aws = [note for note in filtered_aws if set(note.get("aws_services", [])).intersection(set(services))]
    if control_themes:
        filtered_aws = [note for note in filtered_aws if set(note.get("related_controls", [])).intersection(set(control_themes))]

    with right:
        st.write(f"{len(filtered_aws)} AWS references")
        st.download_button(
            "Export AWS references to CSV",
            data=records_to_csv(
                filtered_aws,
                [
                    ("Title", "title"),
                    ("Family", "aws_family"),
                    ("Services", "aws_services"),
                    ("Controls", "related_controls"),
                    ("Source", "file_path"),
                ],
            ),
            file_name="aws_reference_browser.csv",
        )
        if filtered_aws:
            selected_note_title = st.selectbox("AWS reference detail", [note["title"] for note in filtered_aws])
            selected_note = next(note for note in filtered_aws if note["title"] == selected_note_title)
            st.markdown(f"## {selected_note['title']}")
            st.caption(selected_note["file_path"])
            st.write(selected_note["summary"] or "No summary available.")
            render_tag_list("AWS family", [selected_note["aws_family"]] if selected_note.get("aws_family") else [])
            render_tag_list("AWS services", selected_note.get("aws_services", []))
            render_tag_list("Control themes", selected_note.get("related_controls", []))
        else:
            st.info("No AWS references match the current filters.")
