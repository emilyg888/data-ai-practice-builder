from __future__ import annotations

import streamlit as st


NAV_ITEMS = [
    ("app.py", "AI-ACCELERATOR", ":material/space_dashboard:"),
    ("pages/5_Client_Assessment.py", "Client Assessment", ":material/assignment:"),
    ("pages/1_Capability_Browser.py", "Capability Browser", ":material/view_list:"),
    ("pages/2_Pattern_Browser.py", "Pattern Browser", ":material/schema:"),
    ("pages/3_Maturity_Heatmap.py", "Maturity Heatmap", ":material/heat_pump:"),
    ("pages/4_Control_Matrix.py", "Control Matrix", ":material/gpp_good:"),
    ("pages/6_AWS_GenAI_Reference_Browser.py", "AWS GenAI Reference Browser", ":material/cloud:"),
    ("pages/7_AWS_GenAI_Pattern_Graph.py", "AWS GenAI Pattern Graph", ":material/hub:"),
]


def render_sidebar_nav(current_page: str) -> None:
    st.sidebar.markdown("### Navigation")
    for page, label, icon in NAV_ITEMS:
        st.sidebar.page_link(
            page,
            label=label,
            icon=icon,
            disabled=page == current_page,
            use_container_width=True,
        )
