from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from services.metadata_parser import (
    ensure_list,
    extract_bullets,
    extract_front_matter,
    extract_sections,
    first_heading,
    first_paragraph,
    normalize_scalar,
    parse_markdown_tables,
    read_text,
    relative_display_path,
    slugify,
    title_from_path,
)


KNOWLEDGE_ROOT = Path(__file__).resolve().parents[3]
TARGET_FOLDERS = [
    "00_overview",
    "01_capabilities",
    "02_patterns",
    "03_playbooks",
    "04_templates",
    "05_reference_architectures",
    "07_controls",
]


@lru_cache(maxsize=1)
def load_repository_content() -> dict[str, object]:
    capabilities: list[dict] = []
    patterns: list[dict] = []
    reference_notes: list[dict] = []
    controls: list[dict] = []
    playbooks: list[dict] = []
    templates: list[dict] = []
    validation_errors: list[str] = []
    maturity_levels: list[dict] = []

    for path in iter_markdown_files():
        record = parse_markdown_record(path)
        record_type = record["type"]
        if record_type == "capability":
            capabilities.append(build_capability_record(record))
        elif record_type == "pattern":
            patterns.append(build_pattern_record(record))
        elif record_type == "reference_note":
            reference_notes.append(build_reference_note_record(record))
        elif record_type == "playbook":
            playbooks.append(build_generic_record(record, "playbook"))
        elif record_type == "template":
            templates.append(build_generic_record(record, "template"))
        elif record_type == "overview":
            if path.name in {"maturity_model.md", "bfsi_data_ai_maturity_model.md"}:
                maturity_levels = extract_maturity_levels(record)
        elif record_type in {"control_library", "control"}:
            controls.extend(build_control_records(record))

    patterns = dedupe_patterns(patterns)
    synthesize_relationships(capabilities, patterns)
    controls = synthesize_controls(controls, capabilities, patterns, reference_notes)

    for capability in capabilities:
        if not capability["capability_name"]:
            validation_errors.append(f"Missing capability_name: {capability['file_path']}")
        if not capability["capability_layer"]:
            validation_errors.append(f"Missing capability_layer: {capability['file_path']}")
    for pattern in patterns:
        if not pattern["pattern_name"]:
            validation_errors.append(f"Missing pattern_name: {pattern['file_path']}")

    return {
        "capabilities": sorted(capabilities, key=lambda item: item["capability_name"]),
        "patterns": sorted(patterns, key=lambda item: item["pattern_name"]),
        "reference_notes": sorted(reference_notes, key=lambda item: item["title"]),
        "aws_references": sorted(
            [item for item in reference_notes if item.get("platform") == "aws"],
            key=lambda item: item["title"],
        ),
        "controls": sorted(controls, key=lambda item: item["control_name"]),
        "playbooks": sorted(playbooks, key=lambda item: item["name"]),
        "templates": sorted(templates, key=lambda item: item["name"]),
        "maturity_levels": maturity_levels or default_maturity_levels(),
        "validation_errors": validation_errors,
        "knowledge_root": KNOWLEDGE_ROOT,
    }


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for folder in TARGET_FOLDERS:
        base = KNOWLEDGE_ROOT / folder
        files.extend(
            path
            for path in base.rglob("*.md")
            if ".git" not in path.parts
            and "/dashboard/" not in path.as_posix()
            and path.name != "issue_pending_review.md"
        )
    return sorted(files)


def parse_markdown_record(path: Path) -> dict:
    text = read_text(path)
    metadata, body = extract_front_matter(text)
    sections = extract_sections(body)
    record_type = infer_type(path, metadata)
    return {
        "path": path,
        "file_path": relative_display_path(path, KNOWLEDGE_ROOT),
        "metadata": metadata,
        "body": body,
        "sections": sections,
        "title": first_heading(body) or title_from_path(path),
        "type": record_type,
    }


def infer_type(path: Path, metadata: dict) -> str:
    declared = normalize_scalar(metadata.get("type"))
    if declared:
        return declared
    if "01_capabilities" in path.parts:
        return "capability"
    if "02_patterns" in path.parts:
        return "pattern"
    if "03_playbooks" in path.parts:
        return "playbook"
    if "04_templates" in path.parts:
        return "template"
    if "05_reference_architectures" in path.parts:
        return "reference_note"
    if "07_controls" in path.parts:
        return "control_library"
    return "document"


def build_capability_record(record: dict) -> dict:
    metadata = record["metadata"]
    sections = record["sections"]
    capability_name = normalize_scalar(metadata.get("capability_name")) or record["title"]
    summary = first_paragraph(sections.get("definition", "")) or first_paragraph(sections.get("_root", ""))
    return {
        "capability_id": normalize_scalar(metadata.get("capability_id")) or slugify(capability_name),
        "capability_name": capability_name,
        "capability_layer": normalize_scalar(metadata.get("capability_layer")) or record["path"].parent.name,
        "architecture_layer": ensure_list(metadata.get("architecture_layer")),
        "bfsi_domains": ensure_list(metadata.get("bfsi_domains")),
        "ai_impact": ensure_list(metadata.get("ai_impact")) or ensure_list(metadata.get("ai_relevance")),
        "risk_level": normalize_scalar(metadata.get("risk_level")) or "unknown",
        "related_patterns": ensure_list(metadata.get("related_patterns")),
        "related_controls": ensure_list(metadata.get("related_controls")),
        "maturity_applicability": ensure_list(metadata.get("maturity_applicability")),
        "status": normalize_scalar(metadata.get("status")) or "draft",
        "summary": summary,
        "file_path": record["file_path"],
    }


def build_pattern_record(record: dict) -> dict:
    metadata = record["metadata"]
    sections = record["sections"]
    pattern_name = normalize_scalar(metadata.get("pattern_name")) or record["title"]
    problem_solved = first_paragraph(sections.get("problem_solved", "")) or first_paragraph(sections.get("_root", ""))
    required_capabilities = (
        ensure_list(metadata.get("related_capabilities"))
        or ensure_list(metadata.get("capability_layers"))
        or extract_bullets(sections.get("required_capabilities", ""))
    )
    related_controls = ensure_list(metadata.get("related_controls")) or extract_bullets(sections.get("control_gates", ""))
    business_domains = ensure_list(metadata.get("business_domains"))
    ai_impact = ensure_list(metadata.get("ai_impact"))
    artefacts = extract_bullets(sections.get("artefacts_produced", ""))
    return {
        "pattern_id": normalize_scalar(metadata.get("pattern_id"))
        or slugify(record["path"].parent.name if record["path"].stem == "pattern" else pattern_name),
        "pattern_name": pattern_name,
        "business_domains": business_domains,
        "capability_layers": ensure_list(metadata.get("capability_layers")),
        "ai_impact": ai_impact,
        "risk_level": normalize_scalar(metadata.get("risk_level")) or "unknown",
        "related_controls": related_controls,
        "related_capabilities": required_capabilities,
        "reference_architectures": ensure_list(metadata.get("reference_architectures")),
        "status": normalize_scalar(metadata.get("status")) or "draft",
        "problem_solved": problem_solved,
        "when_to_use": sections.get("when_to_use", ""),
        "common_risks": extract_bullets(sections.get("common_risks_and_failure_modes", ""))
        or extract_bullets(sections.get("common_risks", "")),
        "artefacts": artefacts,
        "file_path": record["file_path"],
    }


def dedupe_patterns(patterns: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = {}
    for pattern in patterns:
        key = slugify(pattern["pattern_name"])
        grouped.setdefault(key, []).append(pattern)

    deduped: list[dict] = []
    for key in sorted(grouped):
        candidates = grouped[key]
        chosen = sorted(candidates, key=pattern_preference_key)[0]
        deduped.append(chosen)
    return deduped


def pattern_preference_key(pattern: dict) -> tuple[int, int, str]:
    file_path = pattern.get("file_path", "")
    return (
        0 if file_path.endswith("/pattern.md") else 1,
        len(file_path),
        file_path,
    )


def build_generic_record(record: dict, kind: str) -> dict:
    metadata = record["metadata"]
    return {
        "id": normalize_scalar(metadata.get(f"{kind}_id")) or slugify(record["title"]),
        "name": normalize_scalar(metadata.get(f"{kind}_name")) or record["title"],
        "status": normalize_scalar(metadata.get("status")) or "draft",
        "file_path": record["file_path"],
    }


def build_reference_note_record(record: dict) -> dict:
    metadata = record["metadata"]
    sections = record["sections"]
    title = normalize_scalar(metadata.get("title")) or record["title"]
    pattern_summary = first_paragraph(sections.get("pattern_summary", ""))
    summary = pattern_summary or first_paragraph(sections.get("scenario", "")) or first_paragraph(sections.get("_root", ""))
    platform = normalize_scalar(metadata.get("platform")) or infer_platform(record["path"])
    related_controls = ensure_list(metadata.get("related_controls")) or infer_controls_from_text(record["body"])
    implementation_patterns = extract_bullets(sections.get("common_implementation_patterns", ""))
    anti_patterns = extract_bullets(sections.get("common_anti_patterns", ""))
    architecture_guidance = extract_bullets(sections.get("architecture_guidance", ""))
    aws_family = (
        normalize_scalar(metadata.get("pattern_family"))
        or normalize_scalar(metadata.get("aws_family"))
        or (infer_aws_family(record["file_path"], title, record["body"]) if platform == "aws" else "")
    )
    aws_services = ensure_list(metadata.get("aws_services")) or (
        infer_services(record["body"], record["file_path"]) if platform == "aws" else []
    )
    return {
        "reference_id": normalize_scalar(metadata.get("reference_id"))
        or normalize_scalar(metadata.get("source"))
        or slugify(title),
        "title": title,
        "summary": summary,
        "pattern_summary": pattern_summary,
        "scenario": sections.get("scenario", ""),
        "implementation_patterns": implementation_patterns,
        "anti_patterns": anti_patterns,
        "architecture_guidance": architecture_guidance,
        "platform": platform,
        "source": normalize_scalar(metadata.get("source")),
        "status": normalize_scalar(metadata.get("status")) or "draft",
        "risk_level": normalize_scalar(metadata.get("risk_level")) or "medium_to_high",
        "ai_impact": ensure_list(metadata.get("ai_impact")) or infer_ai_impact(record["body"]),
        "related_controls": related_controls,
        "aws_family": aws_family,
        "aws_services": aws_services,
        "topics": ensure_list(metadata.get("topics")),
        "use_cases": ensure_list(metadata.get("use_cases")),
        "file_path": record["file_path"],
        "absolute_path": str(record["path"]),
    }


def build_control_records(record: dict) -> list[dict]:
    if record["type"] == "control":
        metadata = record["metadata"]
        return [
            {
                "control_id": normalize_scalar(metadata.get("control_id")) or slugify(record["title"]),
                "control_name": normalize_scalar(metadata.get("control_name")) or record["title"],
                "control_type": normalize_scalar(metadata.get("control_type")) or record["path"].parent.name.replace("_controls", ""),
                "risk_area": normalize_scalar(metadata.get("risk_area")),
                "evidence_required": ensure_list(metadata.get("evidence_required")),
                "related_patterns": ensure_list(metadata.get("related_patterns")),
                "related_capabilities": ensure_list(metadata.get("related_capabilities")),
                "owner": normalize_scalar(metadata.get("owner")),
                "file_path": record["file_path"],
            }
        ]

    control_type = record["path"].parent.name.replace("_controls", "")
    records: list[dict] = []
    for table in parse_markdown_tables(record["body"]):
        if not table or "Control" not in table[0]:
            continue
        for row in table:
            control_name = row.get("Control", "").strip()
            if not control_name:
                continue
            records.append(
                {
                    "control_id": slugify(control_name),
                    "control_name": control_name,
                    "control_type": control_type,
                    "risk_area": row.get("Purpose", "").strip(),
                    "evidence_required": split_delimited_values(row.get("Evidence", "")),
                    "related_patterns": [],
                    "related_capabilities": [],
                    "owner": row.get("Owner", "").strip(),
                    "file_path": record["file_path"],
                }
            )
    return records


def split_delimited_values(value: str) -> list[str]:
    if not value:
        return []
    parts = [part.strip() for part in value.replace(";", ",").split(",")]
    return [part for part in parts if part]


def synthesize_relationships(capabilities: list[dict], patterns: list[dict]) -> None:
    capabilities_by_id = {item["capability_id"]: item for item in capabilities}
    capabilities_by_name = {slugify(item["capability_name"]): item for item in capabilities}
    for pattern in patterns:
        linked_ids: list[str] = []
        for capability in pattern["related_capabilities"]:
            capability_key = slugify(capability)
            match = capabilities_by_id.get(capability_key) or capabilities_by_name.get(capability_key)
            if match:
                linked_ids.append(match["capability_id"])
                if pattern["pattern_id"] not in match["related_patterns"]:
                    match["related_patterns"].append(pattern["pattern_id"])
        if linked_ids:
            pattern["related_capabilities"] = linked_ids


def synthesize_controls(
    controls: list[dict],
    capabilities: list[dict],
    patterns: list[dict],
    reference_notes: list[dict],
) -> list[dict]:
    indexed = {item["control_id"]: item for item in controls}
    for capability in capabilities:
        for control_name in capability["related_controls"]:
            add_control_reference(indexed, control_name, capability_id=capability["capability_id"])
    for pattern in patterns:
        for control_name in pattern["related_controls"]:
            add_control_reference(indexed, control_name, pattern_id=pattern["pattern_id"])
    for note in reference_notes:
        for control_name in note["related_controls"]:
            add_control_reference(indexed, control_name, reference_id=note["reference_id"])
    return list(indexed.values())


def add_control_reference(
    indexed: dict[str, dict],
    control_name: str,
    capability_id: str | None = None,
    pattern_id: str | None = None,
    reference_id: str | None = None,
) -> None:
    control_key = slugify(control_name)
    if not control_key:
        return
    record = indexed.setdefault(
        control_key,
        {
            "control_id": control_key,
            "control_name": control_name,
            "control_type": infer_control_type(control_name),
            "risk_area": "",
            "evidence_required": [],
            "related_patterns": [],
            "related_reference_notes": [],
            "related_capabilities": [],
            "owner": "",
            "file_path": "",
        },
    )
    if capability_id and capability_id not in record["related_capabilities"]:
        record["related_capabilities"].append(capability_id)
    if pattern_id and pattern_id not in record["related_patterns"]:
        record["related_patterns"].append(pattern_id)
    if reference_id and reference_id not in record["related_reference_notes"]:
        record["related_reference_notes"].append(reference_id)


def infer_control_type(control_name: str) -> str:
    lowered = control_name.lower()
    if any(token in lowered for token in ["access", "privacy", "security"]):
        return "security"
    if any(token in lowered for token in ["human", "evaluation", "prompt", "retrieval", "explainability"]):
        return "ai"
    if any(token in lowered for token in ["regulatory", "compliance", "policy"]):
        return "regulatory"
    if any(token in lowered for token in ["quality", "lineage", "data"]):
        return "data"
    return "operational"


def infer_platform(path: Path) -> str:
    if "05_reference_architectures" not in path.parts:
        return ""
    folder = path.parts[path.parts.index("05_reference_architectures") + 1]
    return folder.lower()


def infer_aws_family(path: str, title: str, body: str) -> str:
    text = f"{path} {title} {body[:800]}".lower()
    families = [
        ("bedrock_knowledge_bases", ["knowledge-base", "knowledge base", "bedrock knowledge"]),
        ("bedrock_guardrails", ["guardrail", "pii", "masking"]),
        ("bedrock_agents", ["agent", "orchestration"]),
        ("rag", ["rag", "retrieval"]),
        ("vector_store", ["vector", "opensearch", "embedding"]),
        ("prompt_management", ["prompt"]),
        ("evaluation_monitoring", ["evaluation", "regression", "monitoring", "judge"]),
        ("sagemaker", ["sagemaker", "model registry", "model monitor"]),
        ("lambda_orchestration", ["lambda", "api gateway", "step functions"]),
        ("private_network_security", ["vpc", "privatelink", "private subnets", "lake formation"]),
        ("cross_region_inference", ["cross-region"]),
        ("bedrock_data_automation", ["bda", "bedrock data automation", "multimodal"]),
        ("audit_logging", ["audit", "cloudtrail", "logging"]),
    ]
    matches = [name for name, keys in families if any(key in text for key in keys)]
    return matches[0] if matches else "implementation_patterns"


def infer_services(body: str, path: str = "") -> list[str]:
    services = [
        "Amazon Bedrock",
        "Bedrock Knowledge Bases",
        "Bedrock Guardrails",
        "Bedrock Agents",
        "Amazon SageMaker",
        "AWS Lambda",
        "Amazon API Gateway",
        "AWS Step Functions",
        "Amazon S3",
        "Amazon OpenSearch Service",
        "Amazon Athena",
        "AWS Glue",
        "Amazon CloudWatch",
        "AWS CloudTrail",
        "AWS IAM",
        "AWS Lake Formation",
        "AWS PrivateLink",
        "Amazon Kendra",
        "Amazon DynamoDB",
        "Amazon EventBridge",
        "Amazon Bedrock Data Automation",
        "Amazon Bedrock AgentCore Runtime",
        "Amazon Comprehend",
        "Amazon Q Developer",
        "AWS Outposts",
        "AWS Well-Architected Tool",
    ]
    text = f"{body} {path}".lower()
    found: list[str] = []
    for service in services:
        keys = [service.lower()]
        if service.startswith("Amazon "):
            keys.append(service.replace("Amazon ", "").lower())
        if service.startswith("AWS "):
            keys.append(service.replace("AWS ", "").lower())
        if any(key in text for key in keys):
            found.append(service)
    return sorted(set(found))


def infer_controls_from_text(body: str) -> list[str]:
    controls: set[str] = set()
    text = body.lower()
    mapping = {
        "access_control": ["access", "iam", "rbac", "abac", "least-privilege", "lake formation"],
        "private_networking": ["vpc", "privatelink", "private subnet", "no internet"],
        "pii_protection": ["pii", "phi", "mask", "sensitive"],
        "retrieval_grounding": ["retrieval", "ground", "citation", "rag"],
        "prompt_policy": ["prompt"],
        "guardrails": ["guardrail", "refusal"],
        "model_evaluation": ["evaluation", "judge", "correctness", "relevance"],
        "audit_logging": ["audit", "cloudtrail", "log"],
        "monitoring": ["cloudwatch", "monitoring", "metrics"],
        "evidence_retention": ["evidence", "retention"],
    }
    for control, keys in mapping.items():
        if any(key in text for key in keys):
            controls.add(control)
    return sorted(controls)


def infer_ai_impact(body: str) -> list[str]:
    text = body.lower()
    impacts: list[str] = []
    if "rag" in text or "knowledge" in text or "retrieval" in text:
        impacts.append("ai_as_knowledge_interface")
    if "summar" in text or "explain" in text or "reason" in text:
        impacts.append("ai_as_reasoning_assistant")
    if "recommend" in text or "decision" in text:
        impacts.append("ai_as_decision_support")
    if "agent" in text or "tool" in text or "api" in text:
        impacts.append("ai_as_agentic_executor")
    return impacts or ["ai_as_reasoning_assistant"]


def extract_maturity_levels(record: dict) -> list[dict]:
    levels: list[dict] = []
    for table in parse_markdown_tables(record["body"]):
        if table and {"Level", "Name", "Description"}.issubset(table[0].keys()):
            for row in table:
                levels.append(
                    {
                        "level": row["Level"],
                        "name": row["Name"],
                        "description": row["Description"],
                    }
                )
            break
    return levels


def default_maturity_levels() -> list[dict]:
    return [
        {"level": "0", "name": "Not Present", "description": "Capability does not exist"},
        {"level": "1", "name": "Ad Hoc", "description": "Informal, fragmented, inconsistent"},
        {"level": "2", "name": "Repeatable", "description": "Some repeatable practices exist"},
        {"level": "3", "name": "Governed", "description": "Ownership, standards and controls exist"},
        {"level": "4", "name": "Industrialised", "description": "Automated, reusable, monitored"},
        {"level": "5", "name": "Adaptive", "description": "Continuously optimised and self-improving"},
    ]
