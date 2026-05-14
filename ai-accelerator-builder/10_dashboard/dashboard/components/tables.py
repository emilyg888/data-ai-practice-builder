from __future__ import annotations

import streamlit as st

from services.export_service import records_to_markdown_table


def render_markdown_table(records: list[dict], columns: list[tuple[str, str]], empty_message: str) -> None:
    if not records:
        st.info(empty_message)
        return
    st.markdown(records_to_markdown_table(records, columns))
