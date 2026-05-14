from __future__ import annotations


RISK_WEIGHTS = {"low": 0, "medium": 1, "high": 2, "very_high": 3}


def build_maturity_rows(capabilities: list[dict], current_scores: dict, target_scores: dict) -> list[dict]:
    rows: list[dict] = []
    for capability in capabilities:
        current = int(current_scores.get(capability["capability_id"], 0))
        target = int(target_scores.get(capability["capability_id"], max(current, 3)))
        gap = max(target - current, 0)
        risk_weight = RISK_WEIGHTS.get(normalize_risk(capability.get("risk_level", "")), 1)
        dependency_weight = 1 if capability.get("related_patterns") else 0
        priority_score = gap + risk_weight + dependency_weight
        rows.append(
            {
                "capability": capability["capability_name"],
                "capability_id": capability["capability_id"],
                "current": current,
                "target": target,
                "gap": gap,
                "risk": capability.get("risk_level", "unknown"),
                "priority_score": priority_score,
                "priority": classify_priority(priority_score),
            }
        )
    return rows


def classify_priority(score: int) -> str:
    if score >= 4:
        return "High"
    if score >= 2:
        return "Medium"
    return "Low"


def normalize_risk(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def render_heatmap_html(rows: list[dict]) -> str:
    head = (
        "<table style='width:100%; border-collapse:collapse;'>"
        "<thead><tr>"
        "<th style='text-align:left; padding:8px; border-bottom:1px solid #ddd;'>Capability</th>"
        "<th style='padding:8px; border-bottom:1px solid #ddd;'>Current</th>"
        "<th style='padding:8px; border-bottom:1px solid #ddd;'>Target</th>"
        "<th style='padding:8px; border-bottom:1px solid #ddd;'>Gap</th>"
        "<th style='padding:8px; border-bottom:1px solid #ddd;'>Risk</th>"
        "<th style='padding:8px; border-bottom:1px solid #ddd;'>Priority</th>"
        "</tr></thead><tbody>"
    )
    body = []
    for row in rows:
        body.append(
            "<tr>"
            f"<td style='padding:8px; border-bottom:1px solid #f0f0f0;'>{row['capability']}</td>"
            f"<td style='padding:8px; text-align:center; background:{score_color(row['current'])};'>{row['current']}</td>"
            f"<td style='padding:8px; text-align:center; background:{score_color(row['target'])};'>{row['target']}</td>"
            f"<td style='padding:8px; text-align:center; background:{gap_color(row['gap'])};'>{row['gap']}</td>"
            f"<td style='padding:8px; text-align:center;'>{row['risk']}</td>"
            f"<td style='padding:8px; text-align:center;'>{row['priority']}</td>"
            "</tr>"
        )
    return head + "".join(body) + "</tbody></table>"


def score_color(score: int) -> str:
    palette = {
        0: "#f7e8d8",
        1: "#f3d4b0",
        2: "#efbf88",
        3: "#b9d6c2",
        4: "#8fbd9f",
        5: "#6aa37d",
    }
    return palette.get(score, "#ffffff")


def gap_color(score: int) -> str:
    palette = {
        0: "#dff0e3",
        1: "#fff3cd",
        2: "#ffd6a5",
        3: "#f7b267",
        4: "#f4845f",
        5: "#d95d39",
    }
    return palette.get(score, "#ffffff")
