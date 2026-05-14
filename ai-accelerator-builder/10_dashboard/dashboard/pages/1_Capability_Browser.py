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


def compact_list(values: list[str], limit: int = 3) -> str:
    if not values:
        return "None mapped"
    if len(values) <= limit:
        return ", ".join(values)
    return ", ".join(values[:limit]) + f" +{len(values) - limit} more"


def inject_page_css() -> None:
    st.markdown(
        """
        <style>
        .cb-toolbar-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.75rem;
            margin: 0.8rem 0 1rem 0;
        }
        .cb-metric {
            background: rgba(255,255,255,0.035);
            border-radius: 14px;
            padding: 0.8rem 0.9rem;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .cb-metric-label {
            color: rgba(255,255,255,0.65);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .cb-metric-value {
            font-size: 1.45rem;
            font-weight: 700;
            margin-top: 0.2rem;
        }
        .cb-result-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.035), rgba(255,255,255,0.02));
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 1rem 1.1rem;
            margin-bottom: 0.9rem;
        }
        .cb-result-title {
            font-size: 1.1rem;
            font-weight: 700;
            margin: 0.15rem 0 0.55rem 0;
        }
        .cb-label {
            color: rgba(255,255,255,0.6);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 0.18rem;
        }
        .cb-value {
            font-size: 0.95rem;
            line-height: 1.45;
        }
        .cb-result-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.6rem 1rem;
            margin-top: 0.85rem;
        }
        .cb-detail {
            background: rgba(255,255,255,0.025);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 1.2rem 1.25rem;
            margin-top: 0.6rem;
        }
        @media (max-width: 1100px) {
            .cb-toolbar-grid,
            .cb-result-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


st.set_page_config(page_title="Capability Browser", page_icon=":material/view_list:", layout="wide")

inject_page_css()

content = load_repository_content()
capabilities = content["capabilities"]

st.title("Capability Browser")
st.caption("Browse practice capabilities by layer, domain, AI impact, risk, and metadata status.")

with st.sidebar:
    search = st.text_input("Search")
    selected_layers = st.multiselect("Capability layer", unique_values(capabilities, "capability_layer"))
    selected_domains = st.multiselect("BFSI domain", unique_values(capabilities, "bfsi_domains"))
    selected_impacts = st.multiselect("AI impact", unique_values(capabilities, "ai_impact"))
    selected_risks = st.multiselect("Risk level", unique_values(capabilities, "risk_level"))
    selected_status = st.multiselect("Status", unique_values(capabilities, "status"))

filtered = filter_records(
    capabilities,
    search=search,
    equals_filters={
        "capability_layer": selected_layers,
        "bfsi_domains": selected_domains,
        "ai_impact": selected_impacts,
        "risk_level": selected_risks,
        "status": selected_status,
    },
)

action_col, export_col = st.columns([1.2, 0.8], vertical_alignment="bottom")
with action_col:
    st.write(f"Showing {len(filtered)} of {len(capabilities)} capabilities.")
with export_col:
    st.download_button(
        "Export filtered capabilities to CSV",
        data=records_to_csv(
            filtered,
            [
                ("Capability", "capability_name"),
                ("Layer", "capability_layer"),
                ("Domains", "bfsi_domains"),
                ("AI impact", "ai_impact"),
                ("Risk", "risk_level"),
                ("Status", "status"),
                ("Source", "file_path"),
            ],
        ),
        file_name="capability_browser.csv",
        use_container_width=True,
    )

st.markdown(
    f"""
    <div class="cb-toolbar-grid">
        <div class="cb-metric">
            <div class="cb-metric-label">Capabilities returned</div>
            <div class="cb-metric-value">{len(filtered)}</div>
        </div>
        <div class="cb-metric">
            <div class="cb-metric-label">Layers selected</div>
            <div class="cb-metric-value">{len(selected_layers)}</div>
        </div>
        <div class="cb-metric">
            <div class="cb-metric-label">Domains selected</div>
            <div class="cb-metric-value">{len(selected_domains)}</div>
        </div>
        <div class="cb-metric">
            <div class="cb-metric-label">Risk filters</div>
            <div class="cb-metric-value">{len(selected_risks)}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Capability inventory")
if not filtered:
    st.info("No capabilities match the selected filters.")
else:
    visible = filtered[:12]
    selected_options = [item["capability_name"] for item in visible]
    selected_name = st.selectbox(
        "Capability detail",
        selected_options,
        help="Choose a capability to inspect in the detail section below.",
    )

    list_col, insight_col = st.columns([1.15, 0.85], vertical_alignment="top")
    with list_col:
        for capability in visible:
            st.markdown(
                f"""
                <div class="cb-result-card">
                    <div class="cb-result-title">{capability["capability_name"]}</div>
                    <div class="cb-value">{capability["summary"] or "No summary available."}</div>
                    <div class="cb-result-grid">
                        <div>
                            <div class="cb-label">Layer</div>
                            <div class="cb-value">{capability["capability_layer"]}</div>
                        </div>
                        <div>
                            <div class="cb-label">Risk</div>
                            <div class="cb-value">{capability["risk_level"]}</div>
                        </div>
                        <div>
                            <div class="cb-label">Domains</div>
                            <div class="cb-value">{compact_list(capability["bfsi_domains"])}</div>
                        </div>
                        <div>
                            <div class="cb-label">Patterns</div>
                            <div class="cb-value">{compact_list(capability["related_patterns"])}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        if len(filtered) > len(visible):
            st.caption(f"Showing the top {len(visible)} capabilities. Export the CSV for the full result set.")

    selected_capability = next(item for item in filtered if item["capability_name"] == selected_name)
    with insight_col:
        st.markdown('<div class="cb-detail">', unsafe_allow_html=True)
        st.markdown(f"## {selected_capability['capability_name']}")
        meta = st.columns(3)
        meta[0].metric("Layer", selected_capability["capability_layer"])
        meta[1].metric("Risk", selected_capability["risk_level"])
        meta[2].metric("Status", selected_capability["status"])
        st.write(selected_capability["summary"] or "No summary available.")
        render_tag_list("Architecture layers", selected_capability["architecture_layer"])
        render_tag_list("Domains", selected_capability["bfsi_domains"])
        render_tag_list("AI impact", selected_capability["ai_impact"])
        render_tag_list("Related patterns", selected_capability["related_patterns"])
        render_tag_list("Related controls", selected_capability["related_controls"])
        render_tag_list("Maturity applicability", selected_capability["maturity_applicability"])
        st.markdown(f"**Source file:** `{selected_capability['file_path']}`")
        st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Capability detail")
    tab_summary, tab_relationships = st.tabs(["Summary", "Relationships"])
    with tab_summary:
        st.write(selected_capability["summary"] or "No summary available.")
    with tab_relationships:
        left, right = st.columns(2)
        with left:
            st.markdown("**Related patterns**")
            if selected_capability["related_patterns"]:
                for item in selected_capability["related_patterns"]:
                    st.write(f"- {item}")
            else:
                st.write("No related patterns mapped.")
            st.markdown("**Related controls**")
            if selected_capability["related_controls"]:
                for item in selected_capability["related_controls"]:
                    st.write(f"- {item}")
            else:
                st.write("No related controls mapped.")
        with right:
            st.markdown("**Domains**")
            if selected_capability["bfsi_domains"]:
                for item in selected_capability["bfsi_domains"]:
                    st.write(f"- {item}")
            else:
                st.write("No domains mapped.")
            st.markdown("**AI impact**")
            if selected_capability["ai_impact"]:
                for item in selected_capability["ai_impact"]:
                    st.write(f"- {item}")
            else:
                st.write("No AI impact mapped.")
