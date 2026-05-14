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


st.set_page_config(page_title="AWS GenAI Reference Browser", page_icon=":material/cloud:", layout="wide")

content = load_repository_content()
aws_references = content["aws_references"]

st.title("AWS GenAI Reference Browser")
st.caption("Search and classify AWS GenAI reference architecture notes as reusable practice IP.")

metric_columns = st.columns(4)
metric_columns[0].metric("AWS reference notes", len(aws_references))
metric_columns[1].metric("Pattern families", len({note["aws_family"] for note in aws_references if note.get("aws_family")}))
metric_columns[2].metric("AWS services", len({service for note in aws_references for service in note.get("aws_services", [])}))
metric_columns[3].metric("Control themes", len({control for note in aws_references for control in note.get("related_controls", [])}))

left, right = st.columns([1, 3], vertical_alignment="top")
with left:
    search = st.text_input("Search AWS references")
    families = st.multiselect("Pattern family", sorted({note["aws_family"] for note in aws_references if note.get("aws_family")}))
    services = st.multiselect("AWS service", sorted({service for note in aws_references for service in note.get("aws_services", [])}))
    control_themes = st.multiselect("Control theme", sorted({control for note in aws_references for control in note.get("related_controls", [])}))

filtered = aws_references
if search:
    lowered = search.lower()
    filtered = [
        note for note in filtered
        if lowered in note["title"].lower() or lowered in note["summary"].lower() or lowered in note["file_path"].lower()
    ]
if families:
    filtered = [note for note in filtered if note.get("aws_family") in families]
if services:
    filtered = [note for note in filtered if set(note.get("aws_services", [])).intersection(set(services))]
if control_themes:
    filtered = [note for note in filtered if set(note.get("related_controls", [])).intersection(set(control_themes))]

with right:
    st.write(f"{len(filtered)} filtered AWS references")
    st.download_button(
        "Export filtered AWS references to CSV",
        data=records_to_csv(
            filtered,
            [
                ("Title", "title"),
                ("Family", "aws_family"),
                ("Services", "aws_services"),
                ("Controls", "related_controls"),
                ("Source", "file_path"),
            ],
        ),
        file_name="aws_genai_references.csv",
    )
    if filtered:
        selected_title = st.selectbox("Open AWS reference", [note["title"] for note in filtered])
        selected = next(note for note in filtered if note["title"] == selected_title)
        st.markdown(f"## {selected['title']}")
        st.caption(selected["file_path"])
        if selected.get("scenario"):
            st.markdown("**Scenario**")
            st.write(selected["scenario"])
        else:
            st.write(selected["summary"] or "No summary available.")
        st.markdown("**Common implementation patterns**")
        if selected.get("implementation_patterns"):
            for item in selected["implementation_patterns"]:
                st.write(f"- {item}")
        else:
            st.write("No implementation patterns parsed.")
        render_tag_list("AWS family", [selected["aws_family"]] if selected.get("aws_family") else [])
        render_tag_list("AWS services", selected.get("aws_services", []))
        render_tag_list("Control themes", selected.get("related_controls", []))
        if selected.get("architecture_guidance"):
            st.markdown("**Architecture guidance**")
            for item in selected["architecture_guidance"][:4]:
                st.write(f"- {item}")
        st.markdown(f"[Open full note]({selected['absolute_path']})")
    else:
        st.info("No AWS references match the current filters.")
