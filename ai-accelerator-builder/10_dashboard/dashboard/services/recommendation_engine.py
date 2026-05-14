from __future__ import annotations


RISK_WEIGHTS = {"low": 0, "medium": 1, "medium_to_high": 2, "high": 2, "very_high": 3}


def recommend_patterns(
    patterns: list[dict],
    domain: str = "",
    ai_role: str = "",
    risk_level: str = "",
    selected_capabilities: list[str] | None = None,
    selected_controls: list[str] | None = None,
) -> list[dict]:
    selected_capabilities = selected_capabilities or []
    selected_controls = selected_controls or []
    results: list[dict] = []
    for pattern in patterns:
        score, reasons = score_pattern(
            pattern,
            domain=domain,
            ai_role=ai_role,
            risk_level=risk_level,
            selected_capabilities=selected_capabilities,
            selected_controls=selected_controls,
        )
        result = dict(pattern)
        result["recommendation_score"] = score
        result["match_band"] = classify_score(score)
        result["match_reasons"] = reasons
        results.append(result)
    return sorted(results, key=lambda item: (-item["recommendation_score"], item["pattern_name"]))


def score_pattern(
    pattern: dict,
    domain: str = "",
    ai_role: str = "",
    risk_level: str = "",
    selected_capabilities: list[str] | None = None,
    selected_controls: list[str] | None = None,
) -> tuple[int, list[str]]:
    selected_capabilities = selected_capabilities or []
    selected_controls = selected_controls or []
    score = 0
    reasons: list[str] = []

    if domain and any(match_token(domain, candidate) for candidate in pattern.get("business_domains", [])):
        score += 2
        reasons.append("domain match")
    if ai_role and any(match_token(ai_role, candidate) for candidate in pattern.get("ai_impact", [])):
        score += 2
        reasons.append("AI role match")
    capability_matches = [
        capability
        for capability in selected_capabilities
        if any(match_token(capability, candidate) for candidate in pattern.get("related_capabilities", []))
    ]
    if capability_matches:
        score += len(capability_matches)
        reasons.append(f"{len(capability_matches)} capability matches")
    control_matches = [
        control
        for control in selected_controls
        if any(match_token(control, candidate) for candidate in pattern.get("related_controls", []))
    ]
    if control_matches:
        score += len(control_matches)
        reasons.append(f"{len(control_matches)} control matches")
    if risk_level:
        if normalize_token(pattern.get("risk_level", "")) == normalize_token(risk_level):
            score += 1
            reasons.append("risk alignment")
        elif risk_distance(pattern.get("risk_level", ""), risk_level) <= 1:
            score += 0
    return score, reasons


def classify_score(score: int) -> str:
    if score >= 5:
        return "Recommended"
    if score >= 3:
        return "Relevant"
    if score >= 1:
        return "Possible"
    return "Low match"


def match_token(left: str, right: str) -> bool:
    left_token = normalize_token(left)
    right_token = normalize_token(right)
    return bool(left_token and right_token and (left_token in right_token or right_token in left_token))


def normalize_token(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def risk_distance(left: str, right: str) -> int:
    left_weight = RISK_WEIGHTS.get(normalize_token(left), 0)
    right_weight = RISK_WEIGHTS.get(normalize_token(right), 0)
    return abs(left_weight - right_weight)
