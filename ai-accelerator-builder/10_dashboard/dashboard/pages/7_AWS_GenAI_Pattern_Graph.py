from __future__ import annotations

import json
import sys
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

APP_ROOT = Path(__file__).resolve().parents[1]
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from services.content_loader import load_repository_content
from services.graph_builder import build_aws_pattern_graph


st.set_page_config(page_title="AWS GenAI Pattern Graph", page_icon=":material/hub:", layout="wide")

content = load_repository_content()
graph = build_aws_pattern_graph(content["aws_references"])

st.title("AWS GenAI Pattern Graph")
st.caption("Interactive knowledge graph over the AWS GenAI pattern corpus, styled after the Obsidian dashboard graph view.")

metric_columns = st.columns(4)
metric_columns[0].metric("Nodes", graph["stats"]["nodes"])
metric_columns[1].metric("Edges", graph["stats"]["edges"])
metric_columns[2].metric("AWS pattern themes", graph["stats"]["patterns"])
metric_columns[3].metric("AWS services", graph["stats"]["components"])

st.markdown(
    """
    This view aggregates the AWS reference notes into three node types:

    - `Concepts`: control themes, AWS families, and AI impact lenses
    - `Components`: AWS services and managed building blocks
    - `Patterns`: reusable technical GenAI pattern themes derived from the note corpus
    """
)


def build_graph_html(data: dict[str, object]) -> str:
    graph_json = json.dumps(data)
    return f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      :root {{
        --bg: #0f172a;
        --panel: #111827;
        --panel-2: #1e293b;
        --border: #334155;
        --text: #e5eefc;
        --muted: #94a3b8;
        --concept: #5b8def;
        --component: #67d26f;
        --pattern: #f28c38;
      }}

      * {{
        box-sizing: border-box;
      }}

      body {{
        margin: 0;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: var(--bg);
        color: var(--text);
      }}

      .layout {{
        display: grid;
        grid-template-columns: 320px 1fr;
        min-height: 920px;
        border: 1px solid var(--border);
        border-radius: 18px;
        overflow: hidden;
        background: var(--bg);
      }}

      .sidebar {{
        background: linear-gradient(180deg, #0f172a 0%, #0b1325 100%);
        border-right: 1px solid var(--border);
        display: flex;
        flex-direction: column;
      }}

      .section {{
        padding: 18px 18px 16px;
        border-bottom: 1px solid var(--border);
      }}

      .title {{
        font-size: 18px;
        font-weight: 800;
        margin: 0;
      }}

      .muted {{
        color: var(--muted);
        font-size: 13px;
        margin-top: 6px;
      }}

      .search {{
        width: 100%;
        border: 1px solid #41536a;
        background: #1e293b;
        color: var(--text);
        border-radius: 12px;
        padding: 12px 14px;
        font-size: 14px;
        outline: none;
      }}

      .tab {{
        width: 100%;
        border: none;
        border-radius: 12px;
        background: rgba(91, 141, 239, 0.22);
        color: #8cb2ff;
        text-align: left;
        padding: 14px 14px;
        font-size: 15px;
        font-weight: 700;
      }}

      .list {{
        display: grid;
        gap: 10px;
      }}

      .stat-row, .check-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        font-size: 14px;
      }}

      .check-row {{
        justify-content: flex-start;
      }}

      .check-row input {{
        transform: scale(1.1);
        accent-color: #7aa2ff;
      }}

      .dot {{
        width: 12px;
        height: 12px;
        border-radius: 999px;
        display: inline-block;
      }}

      .label-strong {{
        font-size: 12px;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--muted);
        margin-bottom: 10px;
      }}

      .range-wrap {{
        display: grid;
        gap: 10px;
      }}

      .range {{
        width: 100%;
        accent-color: #7aa2ff;
      }}

      .graph-wrap {{
        position: relative;
        min-width: 0;
        background:
          radial-gradient(circle at 30% 20%, rgba(91, 141, 239, 0.08), transparent 34%),
          radial-gradient(circle at 72% 62%, rgba(103, 210, 111, 0.08), transparent 38%),
          #0f172a;
      }}

      svg {{
        width: 100%;
        height: 920px;
        display: block;
      }}

      .tooltip {{
        position: absolute;
        pointer-events: none;
        background: rgba(15, 23, 42, 0.96);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 10px 12px;
        font-size: 13px;
        color: var(--text);
        max-width: 280px;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
        display: none;
        z-index: 4;
      }}

      .detail {{
        position: absolute;
        top: 18px;
        right: 18px;
        width: 320px;
        max-height: calc(100% - 36px);
        overflow: auto;
        background: rgba(15, 23, 42, 0.94);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 18px 48px rgba(0, 0, 0, 0.32);
        backdrop-filter: blur(10px);
      }}

      .detail h3 {{
        margin: 0;
        font-size: 19px;
        line-height: 1.2;
      }}

      .detail .badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 5px 10px;
        border-radius: 999px;
        border: 1px solid var(--border);
        background: rgba(30, 41, 59, 0.9);
        color: var(--muted);
        font-size: 12px;
        margin-top: 10px;
      }}

      .detail p {{
        color: var(--muted);
        font-size: 13px;
        line-height: 1.5;
      }}

      .chips {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
      }}

      .chip {{
        border-radius: 999px;
        border: 1px solid var(--border);
        padding: 6px 10px;
        font-size: 12px;
        color: var(--text);
        background: rgba(30, 41, 59, 0.78);
      }}

      .empty {{
        color: var(--muted);
        font-size: 13px;
      }}

      @media (max-width: 1200px) {{
        .layout {{
          grid-template-columns: 280px 1fr;
        }}

        .detail {{
          width: 280px;
        }}
      }}
    </style>
  </head>
  <body>
    <div class="layout">
      <aside class="sidebar">
        <div class="section">
          <h1 class="title">Knowledge Dashboard</h1>
          <div id="stats" class="muted"></div>
        </div>
        <div class="section">
          <input id="search" class="search" type="text" placeholder="Search..." />
        </div>
        <div class="section">
          <button class="tab">🔗 Graph</button>
          <div class="list" style="margin-top: 16px;">
            <div class="stat-row"><span>💡 Concepts</span><span id="conceptCount">0</span></div>
            <div class="stat-row"><span>🧩 Components</span><span id="componentCount">0</span></div>
            <div class="stat-row"><span>🟠 Patterns</span><span id="patternCount">0</span></div>
          </div>
        </div>
        <div class="section">
          <div class="label-strong">Filters</div>
          <div class="list">
            <label class="check-row">
              <input id="showConcepts" type="checkbox" checked />
              <span class="dot" style="background: var(--concept);"></span>
              <span>Concepts</span>
            </label>
            <label class="check-row">
              <input id="showComponents" type="checkbox" checked />
              <span class="dot" style="background: var(--component);"></span>
              <span>Components</span>
            </label>
            <label class="check-row">
              <input id="showPatterns" type="checkbox" checked />
              <span class="dot" style="background: var(--pattern);"></span>
              <span>Patterns</span>
            </label>
          </div>
          <div class="range-wrap" style="margin-top: 18px;">
            <div class="muted" id="frequencyLabel">Min frequency: 0</div>
            <input id="frequency" class="range" type="range" min="0" max="{data['stats']['max_frequency']}" value="0" />
          </div>
        </div>
        <div class="section" style="margin-top: auto;">
          <div class="muted">Node size = note frequency</div>
          <div class="muted">Edge opacity = relationship weight</div>
        </div>
      </aside>
      <main class="graph-wrap">
        <svg id="graph" viewBox="0 0 1320 920" preserveAspectRatio="xMidYMid meet"></svg>
        <div id="tooltip" class="tooltip"></div>
        <div id="detail" class="detail">
          <h3>AWS Pattern Graph</h3>
          <p>Select a node to inspect what it connects to across the AWS GenAI reference corpus.</p>
          <div class="chips">
            <span class="chip">Concepts = control and architecture ideas</span>
            <span class="chip">Components = AWS services</span>
            <span class="chip">Patterns = reusable technical themes</span>
          </div>
        </div>
      </main>
    </div>

    <script>
      const graphData = {graph_json};
      const state = {{
        search: "",
        showConcepts: true,
        showComponents: true,
        showPatterns: true,
        minFrequency: 0,
        selectedId: null,
      }};

      const svg = document.getElementById("graph");
      const tooltip = document.getElementById("tooltip");
      const detail = document.getElementById("detail");
      const controls = {{
        search: document.getElementById("search"),
        showConcepts: document.getElementById("showConcepts"),
        showComponents: document.getElementById("showComponents"),
        showPatterns: document.getElementById("showPatterns"),
        frequency: document.getElementById("frequency"),
        frequencyLabel: document.getElementById("frequencyLabel"),
        stats: document.getElementById("stats"),
        conceptCount: document.getElementById("conceptCount"),
        componentCount: document.getElementById("componentCount"),
        patternCount: document.getElementById("patternCount"),
      }};

      const byId = new Map(graphData.nodes.map((node) => [node.id, node]));

      function escapeHtml(value) {{
        return String(value)
          .replaceAll("&", "&amp;")
          .replaceAll("<", "&lt;")
          .replaceAll(">", "&gt;")
          .replaceAll('"', "&quot;");
      }}

      function passesFilters(node) {{
        const search = state.search.trim().toLowerCase();
        if (node.type === "concept" && !state.showConcepts) return false;
        if (node.type === "component" && !state.showComponents) return false;
        if (node.type === "pattern" && !state.showPatterns) return false;
        if (node.frequency < state.minFrequency) return false;
        if (!search) return true;
        return node.label.toLowerCase().includes(search) || String(node.subtype || "").toLowerCase().includes(search);
      }}

      function visibleGraph() {{
        const nodes = graphData.nodes.filter(passesFilters);
        const visibleIds = new Set(nodes.map((node) => node.id));
        const edges = graphData.edges.filter(
          (edge) => visibleIds.has(edge.source) && visibleIds.has(edge.target)
        );
        return {{ nodes, edges }};
      }}

      function renderDetail(node, edges) {{
        if (!node) {{
          detail.innerHTML = `
            <h3>AWS Pattern Graph</h3>
            <p>Select a node to inspect what it connects to across the AWS GenAI reference corpus.</p>
            <div class="chips">
              <span class="chip">Concepts = control and architecture ideas</span>
              <span class="chip">Components = AWS services</span>
              <span class="chip">Patterns = reusable technical themes</span>
            </div>
          `;
          return;
        }}

        const related = edges
          .filter((edge) => edge.source === node.id || edge.target === node.id)
          .map((edge) => {{
            const other = edge.source === node.id ? byId.get(edge.target) : byId.get(edge.source);
            return {{
              label: other ? other.label : "Unknown",
              type: other ? other.type : "unknown",
              weight: edge.weight,
            }};
          }})
          .sort((left, right) => right.weight - left.weight || left.label.localeCompare(right.label))
          .slice(0, 10);

        const badges = (node.examples || []).slice(0, 6).map((example) => `<span class="chip">${{escapeHtml(example)}}</span>`).join("");
        const neighbors = related.length
          ? related.map((item) => `<span class="chip">${{escapeHtml(item.label)}} · ${{item.weight}}</span>`).join("")
          : `<span class="empty">No visible relationships under the current filters.</span>`;
        const paths = (node.paths || []).slice(0, 3).map((path) => `<span class="chip">${{escapeHtml(path.split("/").slice(-3).join("/"))}}</span>`).join("");

        detail.innerHTML = `
          <h3>${{escapeHtml(node.label)}}</h3>
          <div class="badge">
            <span class="dot" style="background:${{node.color}};"></span>
            <span>${{escapeHtml(node.type)}}${{node.subtype ? " · " + escapeHtml(node.subtype) : ""}}</span>
          </div>
          <p>${{escapeHtml(node.description || "")}}</p>
          <p><strong style="color:#e5eefc;">Frequency:</strong> ${{node.frequency}}</p>
          <div class="label-strong" style="margin-top: 16px;">Connected nodes</div>
          <div class="chips">${{neighbors}}</div>
          ${{
            badges
              ? `<div class="label-strong" style="margin-top: 16px;">Example notes</div><div class="chips">${{badges}}</div>`
              : ""
          }}
          ${{
            paths
              ? `<div class="label-strong" style="margin-top: 16px;">Example files</div><div class="chips">${{paths}}</div>`
              : ""
          }}
        `;
      }}

      function render() {{
        const {{ nodes, edges }} = visibleGraph();
        const counts = {{
          concept: nodes.filter((node) => node.type === "concept").length,
          component: nodes.filter((node) => node.type === "component").length,
          pattern: nodes.filter((node) => node.type === "pattern").length,
        }};

        controls.stats.textContent = `${{nodes.length}} nodes · ${{edges.length}} edges`;
        controls.conceptCount.textContent = counts.concept;
        controls.componentCount.textContent = counts.component;
        controls.patternCount.textContent = counts.pattern;
        controls.frequencyLabel.textContent = `Min frequency: ${{state.minFrequency}}`;

        const visibleIds = new Set(nodes.map((node) => node.id));
        if (state.selectedId && !visibleIds.has(state.selectedId)) {{
          state.selectedId = null;
        }}

        svg.innerHTML = "";

        const edgeLayer = document.createElementNS("http://www.w3.org/2000/svg", "g");
        const nodeLayer = document.createElementNS("http://www.w3.org/2000/svg", "g");
        const labelLayer = document.createElementNS("http://www.w3.org/2000/svg", "g");

        const maxWeight = Math.max(...edges.map((edge) => edge.weight), 1);
        for (const edge of edges) {{
          const source = byId.get(edge.source);
          const target = byId.get(edge.target);
          if (!source || !target) continue;
          const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
          line.setAttribute("x1", source.x);
          line.setAttribute("y1", source.y);
          line.setAttribute("x2", target.x);
          line.setAttribute("y2", target.y);
          line.setAttribute("stroke", "#314158");
          line.setAttribute("stroke-width", String(0.9 + (edge.weight / maxWeight) * 1.4));
          line.setAttribute("stroke-opacity", String(0.10 + (edge.weight / maxWeight) * 0.38));
          edgeLayer.appendChild(line);
        }}

        for (const node of nodes) {{
          const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          circle.setAttribute("cx", node.x);
          circle.setAttribute("cy", node.y);
          circle.setAttribute("r", node.radius);
          circle.setAttribute("fill", node.color);
          circle.setAttribute("fill-opacity", node.id === state.selectedId ? "1" : "0.95");
          circle.setAttribute("stroke", node.id === state.selectedId ? "#ffffff" : "rgba(255,255,255,0.15)");
          circle.setAttribute("stroke-width", node.id === state.selectedId ? "2.3" : "1.1");
          circle.style.cursor = "pointer";

          circle.addEventListener("mouseenter", (event) => {{
            tooltip.style.display = "block";
            tooltip.innerHTML = `
              <strong>${{escapeHtml(node.label)}}</strong><br/>
              <span style="color:${{node.color}}">${{escapeHtml(node.type)}}</span>
              &nbsp;·&nbsp; freq: ${{node.frequency}}
            `;
          }});
          circle.addEventListener("mousemove", (event) => {{
            tooltip.style.left = `${{event.clientX - svg.getBoundingClientRect().left + 16}}px`;
            tooltip.style.top = `${{event.clientY - svg.getBoundingClientRect().top + 16}}px`;
          }});
          circle.addEventListener("mouseleave", () => {{
            tooltip.style.display = "none";
          }});
          circle.addEventListener("click", () => {{
            state.selectedId = node.id === state.selectedId ? null : node.id;
            render();
          }});

          nodeLayer.appendChild(circle);
        }}

        for (const node of nodes) {{
          const alwaysLabel = node.type === "concept" && node.frequency >= 4;
          const selectedLabel = node.id === state.selectedId;
          const frequentLabel = node.type !== "pattern" ? node.frequency >= 7 : node.frequency >= 4;
          const searchMatch = state.search && node.label.toLowerCase().includes(state.search.trim().toLowerCase());
          if (!(alwaysLabel || selectedLabel || frequentLabel || searchMatch)) continue;

          const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
          label.setAttribute("x", node.x);
          label.setAttribute("y", String(node.y + node.radius + 14));
          label.setAttribute("text-anchor", "middle");
          label.setAttribute("font-size", node.id === state.selectedId ? "14" : "12");
          label.setAttribute("font-weight", node.id === state.selectedId ? "700" : "500");
          label.setAttribute("fill", node.id === state.selectedId ? "#f8fafc" : "#a7b7cc");
          label.textContent = node.label.length > 28 ? node.label.slice(0, 26) + "…" : node.label;
          labelLayer.appendChild(label);
        }}

        svg.appendChild(edgeLayer);
        svg.appendChild(nodeLayer);
        svg.appendChild(labelLayer);
        renderDetail(state.selectedId ? byId.get(state.selectedId) : null, edges);
      }}

      controls.search.addEventListener("input", (event) => {{
        state.search = event.target.value || "";
        render();
      }});
      controls.showConcepts.addEventListener("change", (event) => {{
        state.showConcepts = event.target.checked;
        render();
      }});
      controls.showComponents.addEventListener("change", (event) => {{
        state.showComponents = event.target.checked;
        render();
      }});
      controls.showPatterns.addEventListener("change", (event) => {{
        state.showPatterns = event.target.checked;
        render();
      }});
      controls.frequency.addEventListener("input", (event) => {{
        state.minFrequency = parseInt(event.target.value || "0", 10);
        render();
      }});

      render();
    </script>
  </body>
</html>
"""


components.html(build_graph_html(graph), height=960, scrolling=False)
