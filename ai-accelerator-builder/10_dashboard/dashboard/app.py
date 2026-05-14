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

DIAGRAM_PATH = (
    APP_ROOT.parent.parent
    / "01_capabilities"
    / "enterprise_ai_enablers"
    / "EnterpriseAI_Enablers.png"
)

content = load_repository_content()
render_sidebar_nav("app.py")

st.markdown(
    """
    <style>
    .ov-hero {
        padding: 1.25rem 0 0.5rem 0;
    }
    .ov-kicker {
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-size: 0.8rem;
        color: #7dd3fc;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    .ov-title {
        font-size: 3rem;
        line-height: 1.05;
        font-weight: 800;
        margin: 0;
        color: #f8fafc;
    }
    .ov-diagram-wrap {
        background: linear-gradient(180deg, rgba(11, 18, 32, 0.98) 0%, rgba(17, 24, 39, 0.98) 100%);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 20px;
        padding: 1rem;
    }
    .ov-section-intro {
        color: #cbd5e1;
        line-height: 1.7;
        margin-top: 0.35rem;
    }
    .ov-panel {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.98) 0%, rgba(17, 24, 39, 0.96) 100%);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        padding: 1.2rem 1.25rem;
        height: 100%;
    }
    .ov-panel-title {
        font-size: 0.84rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #94a3b8;
        margin-bottom: 0.8rem;
        font-weight: 700;
    }
    .ov-thesis-text {
        color: #e2e8f0;
        line-height: 1.55;
        margin: 0;
    }
    .ov-value-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.9rem;
    }
    .ov-value-card {
        background: rgba(17, 24, 39, 0.96);
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 16px;
        padding: 1rem;
    }
    .ov-value-title {
        color: #f8fafc;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }
    .ov-value-text {
        color: #cbd5e1;
        line-height: 1.6;
        margin: 0;
    }
    .ov-use-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.9rem;
    }
    .ov-use-card {
        background: rgba(17, 24, 39, 0.96);
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 16px;
        padding: 1rem;
    }
    .ov-use-title {
        color: #f8fafc;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    .ov-use-text {
        color: #cbd5e1;
        line-height: 1.6;
        margin: 0;
    }
    @media (max-width: 900px) {
        .ov-value-grid, .ov-use-grid {
            grid-template-columns: 1fr;
        }
        .ov-title {
            font-size: 2.3rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="ov-hero">', unsafe_allow_html=True)
st.markdown('<div class="ov-kicker">AI-ACCELERATOR Overview</div>', unsafe_allow_html=True)
st.markdown(
    '<h1 class="ov-title">From AI Accelerator to Repeatable Practice IP</h1>',
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("### Enterprise AI Scale Enablers")
st.markdown(
    """
    <div class="ov-section-intro">
    The diagram below is the backbone of the practice: reusable capabilities for governed AI adoption across client
    enterprises, spanning consulting assets, control layers, runtime capabilities, data foundations, and operating gates.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="ov-diagram-wrap">', unsafe_allow_html=True)
st.image(str(DIAGRAM_PATH), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

value_left, value_right = st.columns([1.15, 0.85], gap="large")
with value_left:
    st.markdown("### What This Creates")
    st.markdown(
        """
        <div class="ov-value-grid">
            <div class="ov-value-card">
                <div class="ov-value-title">GTM leverage</div>
                <p class="ov-value-text">Sharper RFP narratives, reusable solution stories, and clearer executive confidence in the delivery model.</p>
            </div>
            <div class="ov-value-card">
                <div class="ov-value-title">Delivery leverage</div>
                <p class="ov-value-text">Faster mobilisation, less reinvention, and more consistent engineering patterns across teams and accounts.</p>
            </div>
            <div class="ov-value-card">
                <div class="ov-value-title">Control leverage</div>
                <p class="ov-value-text">Governance, security, risk, and auditability get embedded from the start instead of being bolted on late.</p>
            </div>
            <div class="ov-value-card">
                <div class="ov-value-title">Commercial leverage</div>
                <p class="ov-value-text">Lower cost-to-deliver and a more scalable path from one-off AI work to cross-vertical repeatable IP.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with value_right:
    st.markdown("### Dashboard Use")
    st.markdown(
        """
        <div class="ov-panel">
            <div class="ov-panel-title">How To Work This Practice</div>
            <p class="ov-thesis-text">
                Use the dashboard to move from capability framing to governed pattern selection, then into maturity,
                controls, and engagement-ready client views.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.markdown(
        f"""
        <div class="ov-panel">
            <div class="ov-panel-title">Current Library Signal</div>
            <p class="ov-thesis-text">Capabilities: <strong>{len(content["capabilities"])}</strong></p>
            <p class="ov-thesis-text">Patterns: <strong>{len(content["patterns"])}</strong></p>
            <p class="ov-thesis-text">AWS references: <strong>{len(content["aws_references"])}</strong></p>
            <p class="ov-thesis-text">Controls: <strong>{len(content["controls"])}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("### Workbench Modules")
st.markdown(
    """
    <div class="ov-use-grid">
        <div class="ov-use-card">
            <div class="ov-use-title">Client Assessment</div>
            <p class="ov-use-text">Start from a client context, focus the target capabilities, and generate a governed engagement view.</p>
        </div>
        <div class="ov-use-card">
            <div class="ov-use-title">Capability Browser</div>
            <p class="ov-use-text">Inspect the reusable capability stack behind the enabler model and understand where each asset sits.</p>
        </div>
        <div class="ov-use-card">
            <div class="ov-use-title">Pattern Browser</div>
            <p class="ov-use-text">Shortlist reusable architecture and orchestration patterns for a given AI role, domain, and risk profile.</p>
        </div>
        <div class="ov-use-card">
            <div class="ov-use-title">Maturity Heatmap</div>
            <p class="ov-use-text">Score current versus target maturity and translate capability gaps into prioritised delivery themes.</p>
        </div>
        <div class="ov-use-card">
            <div class="ov-use-title">Control Matrix</div>
            <p class="ov-use-text">Map patterns and reference notes to evidence expectations so governed delivery stays explicit.</p>
        </div>
        <div class="ov-use-card">
            <div class="ov-use-title">AWS Reference Views</div>
            <p class="ov-use-text">Use the browser and graph to inspect implementation notes, service families, and technical theme connections.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
