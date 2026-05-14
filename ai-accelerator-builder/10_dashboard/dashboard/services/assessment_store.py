from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ASSESSMENT_DIR = Path(__file__).resolve().parents[1] / "data" / "assessments"


def list_assessments() -> list[dict]:
    records: list[dict] = []
    for path in sorted(ASSESSMENT_DIR.glob("*.json")):
        try:
            records.append(json.loads(path.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            continue
    return sorted(records, key=lambda item: item.get("created_date", ""), reverse=True)


def load_assessment(assessment_id: str) -> dict | None:
    path = ASSESSMENT_DIR / f"{assessment_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_assessment(record: dict) -> Path:
    ASSESSMENT_DIR.mkdir(parents=True, exist_ok=True)
    record = dict(record)
    record.setdefault("created_date", datetime.utcnow().date().isoformat())
    path = ASSESSMENT_DIR / f"{record['assessment_id']}.json"
    path.write_text(json.dumps(record, indent=2), encoding="utf-8")
    return path


def default_assessment() -> dict:
    return {
        "assessment_id": "",
        "client_name": "",
        "business_domain": "",
        "use_case": "",
        "ai_role": "",
        "risk_level": "high",
        "current_scores": {},
        "target_scores": {},
        "selected_patterns": [],
        "required_controls": [],
        "roadmap": [],
        "created_date": datetime.utcnow().date().isoformat(),
    }
