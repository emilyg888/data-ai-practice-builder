from __future__ import annotations

import csv
import io


def records_to_csv(records: list[dict], columns: list[tuple[str, str]]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([heading for heading, _ in columns])
    for record in records:
        writer.writerow([stringify(record.get(key, "")) for _, key in columns])
    return buffer.getvalue()


def records_to_markdown_table(records: list[dict], columns: list[tuple[str, str]]) -> str:
    headers = [heading for heading, _ in columns]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for record in records:
        row = [escape_pipes(stringify(record.get(key, ""))) for _, key in columns]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def build_assessment_summary(
    assessment: dict,
    maturity_rows: list[dict],
    patterns: list[dict],
    controls: list[dict],
    aws_references: list[dict] | None = None,
) -> str:
    aws_references = aws_references or []
    current_average = average([row["current"] for row in maturity_rows])
    target_average = average([row["target"] for row in maturity_rows])
    top_gaps = sorted(maturity_rows, key=lambda row: (-row["gap"], row["capability"]))[:5]
    top_gap_text = ", ".join(row["capability"] for row in top_gaps if row["gap"] > 0) or "no material gaps"

    lines = [
        f"# Client Assessment Summary: {assessment.get('client_name') or 'Unnamed Assessment'}",
        "",
        f"- Domain: {assessment.get('business_domain', '')}",
        f"- Use case: {assessment.get('use_case', '')}",
        f"- AI role: {assessment.get('ai_role', '')}",
        f"- Risk level: {assessment.get('risk_level', '')}",
        f"- Average current maturity: {current_average:.1f}",
        f"- Average target maturity: {target_average:.1f}",
        "",
        "## Executive Summary",
        "",
        (
            f"The client is seeking to improve {assessment.get('use_case', 'a priority process')} "
            f"across the {assessment.get('business_domain', 'selected')} domain. "
            f"The largest maturity gaps are in {top_gap_text}. "
            f"Because the AI role is classified as {assessment.get('ai_role', 'not specified')} "
            f"with {assessment.get('risk_level', 'unspecified')} risk, the recommended solution requires "
            "governed patterns, explicit controls, and a phased delivery roadmap."
        ),
        "",
        "## Recommended Patterns",
        "",
    ]
    for pattern in patterns:
        lines.append(f"- {pattern['pattern_name']}")
    if aws_references:
        lines.extend(["", "## AWS GenAI Reference Notes", ""])
        for note in aws_references:
            lines.append(f"- {note['title']} ({note.get('aws_family') or note.get('platform', '')})")
    lines.extend(["", "## Roadmap", ""])
    for step in assessment.get("roadmap", []):
        lines.append(f"1. {step}")
    return "\n".join(lines)


def stringify(value: object) -> str:
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def escape_pipes(value: str) -> str:
    return value.replace("|", "\\|")


def average(values: list[int]) -> float:
    return sum(values) / len(values) if values else 0.0
