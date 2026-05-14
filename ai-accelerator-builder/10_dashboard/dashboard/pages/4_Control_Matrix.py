from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_ROOT = Path(__file__).resolve().parents[1]
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from components.cards import render_tag_list
from components.filters import filter_records, unique_values
from services.content_loader import load_repository_content
from services.export_service import records_to_csv


def compact_list(values: list[str], limit: int = 4) -> str:
    if not values:
        return "None mapped"
    if len(values) <= limit:
        return ", ".join(values)
    return ", ".join(values[:limit]) + f" +{len(values) - limit} more"


def inject_page_css() -> None:
    st.markdown(
        """
        <style>
        .cm-toolbar-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.75rem;
            margin-top: 0.8rem;
        }
        .cm-metric {
            background: rgba(255,255,255,0.035);
            border-radius: 14px;
            padding: 0.8rem 0.9rem;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .cm-metric-label {
            color: rgba(255,255,255,0.65);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .cm-metric-value {
            font-size: 1.45rem;
            font-weight: 700;
            margin-top: 0.2rem;
        }
        .cm-record-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.035), rgba(255,255,255,0.02));
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 1rem 1.1rem;
            margin-bottom: 0.9rem;
        }
        .cm-record-title {
            font-size: 1.08rem;
            font-weight: 700;
            margin: 0.15rem 0 0.55rem 0;
        }
        .cm-record-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.6rem 1rem;
            margin-top: 0.85rem;
        }
        .cm-label {
            color: rgba(255,255,255,0.6);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 0.18rem;
        }
        .cm-value {
            font-size: 0.95rem;
            line-height: 1.45;
        }
        .cm-detail {
            background: rgba(255,255,255,0.025);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 1.2rem 1.25rem;
            margin-top: 0.6rem;
        }
        @media (max-width: 1100px) {
            .cm-toolbar-grid,
            .cm-record-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def build_records(patterns: list[dict], reference_notes: list[dict]) -> list[dict]:
    return [{**item, "record_type": "pattern", "platform": ""} for item in patterns] + [
        {**item, "record_type": "reference_note"} for item in reference_notes
    ]


def matched_control_names(record: dict, controls: list[dict]) -> list[str]:
    related = [value.lower() for value in record.get("related_controls", [])]
    matches: list[str] = []
    for control in controls:
        control_name = control["control_name"]
        lowered = control_name.lower()
        if any(lowered in item or item in lowered for item in related):
            matches.append(control_name)
    return matches


st.set_page_config(page_title="Control Matrix", page_icon=":material/gpp_good:", layout="wide")

inject_page_css()

content = load_repository_content()
patterns = content["patterns"]
reference_notes = content["reference_notes"]
controls = content["controls"]
records = build_records(patterns, reference_notes)

st.title("Control Matrix")
st.caption("Map practice patterns and AWS reference notes to required controls and evidence expectations.")

with st.sidebar:
    record_types = st.multiselect("Record type", ["pattern", "reference_note"], default=["pattern", "reference_note"])
    selected_records = st.multiselect("Pattern or reference", [item.get("pattern_name") or item.get("title") for item in records])
    selected_domains = st.multiselect("Domain", unique_values(patterns, "business_domains"))
    selected_risks = st.multiselect("Risk level", unique_values(records, "risk_level"))
    selected_control_types = st.multiselect("Control type", unique_values(controls, "control_type"))
    selected_platforms = st.multiselect("Platform", unique_values(reference_notes, "platform"))

filtered_records = filter_records(
    records,
    equals_filters={
        "record_type": record_types,
        "business_domains": selected_domains,
        "risk_level": selected_risks,
        "platform": selected_platforms,
    },
)
if selected_records:
    filtered_records = [
        record
        for record in filtered_records
        if (record.get("pattern_name") or record.get("title")) in selected_records
    ]
if not filtered_records:
    filtered_records = records

filtered_controls = filter_records(controls, equals_filters={"control_type": selected_control_types})
if not filtered_controls:
    filtered_controls = controls

record_summaries = []
for record in filtered_records:
    label = record.get("pattern_name") or record.get("title") or record.get("reference_id") or "Unnamed record"
    matches = matched_control_names(record, filtered_controls)
    record_summaries.append(
        {
            "record": label,
            "record_type": record.get("record_type", ""),
            "platform": record.get("platform", ""),
            "risk_level": record.get("risk_level", ""),
            "matched_controls": matches,
            "matched_control_count": len(matches),
            "file_path": record.get("file_path", ""),
        }
    )

export_rows = [
    {
        "record": item["record"],
        "record_type": item["record_type"],
        "platform": item["platform"],
        "risk_level": item["risk_level"],
        "matched_control_count": item["matched_control_count"],
        "matched_controls": item["matched_controls"],
        "file_path": item["file_path"],
    }
    for item in record_summaries
]

action_col, export_col = st.columns([1.2, 0.8], vertical_alignment="bottom")
with action_col:
    st.write(f"{len(record_summaries)} records in scope across {len(filtered_controls)} controls.")
with export_col:
    st.download_button(
        "Export control matrix CSV",
        data=records_to_csv(
            export_rows,
            [
                ("Record", "record"),
                ("Type", "record_type"),
                ("Platform", "platform"),
                ("Risk", "risk_level"),
                ("Matched controls", "matched_controls"),
                ("Source", "file_path"),
            ],
        ),
        file_name="control_matrix.csv",
        use_container_width=True,
    )

st.markdown(
    f"""
    <div class="cm-toolbar-grid">
        <div class="cm-metric">
            <div class="cm-metric-label">Records returned</div>
            <div class="cm-metric-value">{len(record_summaries)}</div>
        </div>
        <div class="cm-metric">
            <div class="cm-metric-label">Controls in scope</div>
            <div class="cm-metric-value">{len(filtered_controls)}</div>
        </div>
        <div class="cm-metric">
            <div class="cm-metric-label">Patterns</div>
            <div class="cm-metric-value">{sum(1 for item in record_summaries if item['record_type'] == 'pattern')}</div>
        </div>
        <div class="cm-metric">
            <div class="cm-metric-label">AWS references</div>
            <div class="cm-metric-value">{sum(1 for item in record_summaries if item['record_type'] == 'reference_note')}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if not filtered_controls:
    st.info("No controls are available for the current selection.")
else:
    control_options = {item["control_name"]: item for item in filtered_controls}
    selected_control_name = st.selectbox("Control detail", list(control_options.keys()))
    selected_control = control_options[selected_control_name]
    records_for_selected_control = [
        item for item in record_summaries if selected_control_name in item["matched_controls"]
    ]

    list_col, detail_col = st.columns([1.15, 0.85], vertical_alignment="top")
    with list_col:
        st.subheader("Coverage by record")
        for item in record_summaries[:16]:
            st.markdown(
                f"""
                <div class="cm-record-card">
                    <div class="cm-record-title">{item["record"]}</div>
                    <div class="cm-record-grid">
                        <div>
                            <div class="cm-label">Type</div>
                            <div class="cm-value">{item["record_type"]}</div>
                        </div>
                        <div>
                            <div class="cm-label">Risk</div>
                            <div class="cm-value">{item["risk_level"] or "unknown"}</div>
                        </div>
                        <div>
                            <div class="cm-label">Platform</div>
                            <div class="cm-value">{item["platform"] or "practice"}</div>
                        </div>
                        <div>
                            <div class="cm-label">Matched controls</div>
                            <div class="cm-value">{item["matched_control_count"]}</div>
                        </div>
                        <div style="grid-column: 1 / -1;">
                            <div class="cm-label">Control preview</div>
                            <div class="cm-value">{compact_list(item["matched_controls"])}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        if len(record_summaries) > 16:
            st.caption(f"Showing the first 16 records. Export the CSV for the full coverage set.")

    with detail_col:
        st.markdown('<div class="cm-detail">', unsafe_allow_html=True)
        st.markdown(f"## {selected_control['control_name']}")
        meta = st.columns(3)
        meta[0].metric("Type", selected_control["control_type"])
        meta[1].metric("Matched records", len(records_for_selected_control))
        meta[2].metric(
            "AWS references",
            sum(1 for item in records_for_selected_control if item["record_type"] == "reference_note"),
        )
        st.write("Review this control across applicable patterns and required evidence.")
        render_tag_list("Evidence required", selected_control["evidence_required"])
        render_tag_list("Related patterns", selected_control["related_patterns"])
        render_tag_list("Related capabilities", selected_control["related_capabilities"])
        render_tag_list("Related reference notes", selected_control.get("related_reference_notes", []))
        if selected_control["file_path"]:
            st.markdown(f"**Source file:** `{selected_control['file_path']}`")
        st.markdown("</div>", unsafe_allow_html=True)

    summary_tab, impacted_tab = st.tabs(["Evidence and relationships", "Records requiring this control"])
    with summary_tab:
        left, right = st.columns(2)
        with left:
            st.markdown("**Evidence required**")
            if selected_control["evidence_required"]:
                for item in selected_control["evidence_required"]:
                    st.write(f"- {item}")
            else:
                st.write("No explicit evidence artefacts mapped.")
            st.markdown("**Related capabilities**")
            if selected_control["related_capabilities"]:
                for item in selected_control["related_capabilities"]:
                    st.write(f"- {item}")
            else:
                st.write("No capability mappings recorded.")
        with right:
            st.markdown("**Related practice patterns**")
            if selected_control["related_patterns"]:
                for item in selected_control["related_patterns"]:
                    st.write(f"- {item}")
            else:
                st.write("No practice pattern mappings recorded.")
            st.markdown("**Related reference notes**")
            if selected_control.get("related_reference_notes"):
                for item in selected_control["related_reference_notes"]:
                    st.write(f"- {item}")
            else:
                st.write("No AWS reference-note mappings recorded.")
    with impacted_tab:
        if records_for_selected_control:
            for item in records_for_selected_control:
                st.markdown(f"### {item['record']}")
                st.caption(f"{item['record_type']} | {item['platform'] or 'practice'} | {item['file_path']}")
                st.write(f"Matched controls: {compact_list(item['matched_controls'], limit=6)}")
        else:
            st.info("No records in the current selection require this control.")
