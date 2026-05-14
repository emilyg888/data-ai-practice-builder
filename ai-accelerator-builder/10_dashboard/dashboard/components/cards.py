from __future__ import annotations

import streamlit as st


def render_record_card(title: str, subtitle: str, metadata: list[str], body: str) -> None:
    st.markdown(f"### {title}")
    if subtitle:
        st.caption(subtitle)
    if metadata:
        st.write(" | ".join(item for item in metadata if item))
    if body:
        st.write(body)


def render_tag_list(label: str, values: list[str]) -> None:
    if values:
        st.markdown(f"**{label}:** " + ", ".join(values))
