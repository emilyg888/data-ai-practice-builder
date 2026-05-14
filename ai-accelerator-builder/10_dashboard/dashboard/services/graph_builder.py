from __future__ import annotations

import math
import random
import re
from collections import Counter, defaultdict

from services.metadata_parser import slugify


FAMILY_LABELS = {
    "bedrock_knowledge_bases": "Bedrock Knowledge Bases",
    "bedrock_guardrails": "Bedrock Guardrails",
    "bedrock_agents": "Bedrock Agents",
    "rag": "Retrieval-Augmented Generation",
    "vector_store": "Vector Store",
    "prompt_management": "Prompt Management",
    "evaluation_monitoring": "Evaluation And Monitoring",
    "sagemaker": "Amazon SageMaker",
    "lambda_orchestration": "Serverless Orchestration",
    "private_network_security": "Private Network Security",
    "cross_region_inference": "Cross-Region Inference",
    "bedrock_data_automation": "Bedrock Data Automation",
    "audit_logging": "Audit Logging",
    "implementation_patterns": "Implementation Guidance",
}

CONTROL_LABELS = {
    "access_control": "Access Control",
    "private_networking": "Private Networking",
    "pii_protection": "PII Protection",
    "retrieval_grounding": "Retrieval Grounding",
    "prompt_policy": "Prompt Management",
    "guardrails": "Guardrails",
    "model_evaluation": "Model Evaluation",
    "audit_logging": "Audit Logging",
    "monitoring": "Monitoring",
    "evidence_retention": "Evidence Retention",
}

AI_IMPACT_LABELS = {
    "ai_as_knowledge_interface": "Knowledge Interface",
    "ai_as_reasoning_assistant": "Reasoning Assistant",
    "ai_as_decision_support": "Decision Support",
    "ai_as_agentic_executor": "Agentic Execution",
}

TYPE_COLORS = {
    "concept": "#5b8def",
    "component": "#67d26f",
    "pattern": "#f28c38",
}


def build_aws_pattern_graph(reference_notes: list[dict]) -> dict[str, object]:
    pattern_counts: Counter[str] = Counter()
    service_counts: Counter[str] = Counter()
    concept_counts: Counter[str] = Counter()
    edge_weights: Counter[tuple[str, str, str]] = Counter()
    pattern_sources: defaultdict[str, list[str]] = defaultdict(list)
    pattern_absolute_paths: defaultdict[str, list[str]] = defaultdict(list)
    concept_subtypes: defaultdict[str, set[str]] = defaultdict(set)
    service_examples: defaultdict[str, set[str]] = defaultdict(set)

    for note in reference_notes:
        pattern_label = normalize_pattern_title(note.get("title", ""))
        pattern_id = f"pattern:{slugify(pattern_label)}"
        pattern_counts[pattern_label] += 1
        pattern_sources[pattern_label].append(note.get("title", ""))
        if note.get("absolute_path"):
            pattern_absolute_paths[pattern_label].append(note["absolute_path"])

        note_concepts = extract_concepts(note)
        for concept_type, concept_label in note_concepts:
            concept_id = f"concept:{slugify(concept_label)}"
            concept_counts[concept_label] += 1
            concept_subtypes[concept_label].add(concept_type)
            edge_weights[(pattern_id, concept_id, "concept_link")] += 1

        for service in sorted(set(note.get("aws_services", []))):
            component_id = f"component:{slugify(service)}"
            service_counts[service] += 1
            service_examples[service].add(pattern_label)
            edge_weights[(pattern_id, component_id, "service_link")] += 1

    nodes: list[dict] = []
    for pattern_label, frequency in pattern_counts.items():
        nodes.append(
            {
                "id": f"pattern:{slugify(pattern_label)}",
                "label": pattern_label,
                "type": "pattern",
                "subtype": "pattern_theme",
                "frequency": frequency,
                "color": TYPE_COLORS["pattern"],
                "description": f"{frequency} AWS reference notes contribute to this pattern theme.",
                "examples": pattern_sources[pattern_label][:6],
                "paths": pattern_absolute_paths[pattern_label][:6],
            }
        )

    for service, frequency in service_counts.items():
        nodes.append(
            {
                "id": f"component:{slugify(service)}",
                "label": service,
                "type": "component",
                "subtype": "aws_service",
                "frequency": frequency,
                "color": TYPE_COLORS["component"],
                "description": f"{frequency} AWS reference notes mention this service.",
                "examples": sorted(service_examples[service])[:6],
                "paths": [],
            }
        )

    for concept_label, frequency in concept_counts.items():
        nodes.append(
            {
                "id": f"concept:{slugify(concept_label)}",
                "label": concept_label,
                "type": "concept",
                "subtype": ", ".join(sorted(concept_subtypes[concept_label])),
                "frequency": frequency,
                "color": TYPE_COLORS["concept"],
                "description": f"{frequency} AWS reference notes connect to this concept.",
                "examples": [],
                "paths": [],
            }
        )

    edges = [
        {
            "source": source,
            "target": target,
            "type": edge_type,
            "weight": weight,
        }
        for (source, target, edge_type), weight in edge_weights.items()
    ]

    positions = compute_force_layout(nodes, edges)
    for node in nodes:
        position = positions[node["id"]]
        node["x"] = round(position[0], 2)
        node["y"] = round(position[1], 2)
        node["radius"] = round(node_radius(node["frequency"], node["type"]), 2)

    adjacency = build_adjacency(nodes, edges)
    for node in nodes:
        node["neighbors"] = adjacency.get(node["id"], [])

    concept_total = sum(1 for node in nodes if node["type"] == "concept")
    component_total = sum(1 for node in nodes if node["type"] == "component")
    pattern_total = sum(1 for node in nodes if node["type"] == "pattern")
    max_frequency = max((node["frequency"] for node in nodes), default=0)

    return {
        "nodes": nodes,
        "edges": edges,
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "concepts": concept_total,
            "components": component_total,
            "patterns": pattern_total,
            "max_frequency": max_frequency,
        },
        "colors": TYPE_COLORS,
    }


def normalize_pattern_title(title: str) -> str:
    cleaned = re.sub(r"^\s*(question\s+)?\d+\s*:\s*", "", title, flags=re.IGNORECASE).strip()
    return cleaned or "Implementation Patterns"


def extract_concepts(note: dict) -> list[tuple[str, str]]:
    concepts: set[tuple[str, str]] = set()
    family = note.get("aws_family")
    if family:
        concepts.add(("family", FAMILY_LABELS.get(family, humanize_token(family))))
    for control in note.get("related_controls", []):
        concepts.add(("control", CONTROL_LABELS.get(control, humanize_token(control))))
    for impact in note.get("ai_impact", []):
        concepts.add(("impact", AI_IMPACT_LABELS.get(impact, humanize_token(impact))))
    return sorted(concepts, key=lambda item: (item[0], item[1]))


def humanize_token(value: str) -> str:
    words = re.split(r"[_\-\s]+", value.strip())
    special = {"aws": "AWS", "ai": "AI", "rag": "RAG", "pii": "PII", "api": "API", "iam": "IAM"}
    return " ".join(special.get(word.lower(), word.capitalize()) for word in words if word)


def node_radius(frequency: int, node_type: str) -> float:
    base = {"concept": 7.5, "component": 9.5, "pattern": 6.5}[node_type]
    return base + min(15.0, math.sqrt(max(frequency, 1)) * 2.4)


def compute_force_layout(
    nodes: list[dict],
    edges: list[dict],
    width: int = 1320,
    height: int = 860,
    iterations: int = 220,
) -> dict[str, tuple[float, float]]:
    if not nodes:
        return {}

    randomizer = random.Random(17)
    anchors = {
        "pattern": (width * 0.54, height * 0.53, 130.0),
        "concept": (width * 0.47, height * 0.44, 215.0),
        "component": (width * 0.58, height * 0.58, 255.0),
    }
    positions: dict[str, list[float]] = {}
    for node in nodes:
        anchor_x, anchor_y, spread = anchors[node["type"]]
        angle = randomizer.random() * math.tau
        radius = spread * (0.35 + randomizer.random() * 0.65)
        positions[node["id"]] = [
            anchor_x + math.cos(angle) * radius,
            anchor_y + math.sin(angle) * radius,
        ]

    node_index = {node["id"]: index for index, node in enumerate(nodes)}
    node_ids = [node["id"] for node in nodes]
    area = width * height
    k = math.sqrt(area / max(len(nodes), 1)) * 0.78
    temperature = width / 11

    normalized_weights = [edge["weight"] for edge in edges] or [1]
    max_weight = max(normalized_weights)

    for step in range(iterations):
        displacements = {node_id: [0.0, 0.0] for node_id in node_ids}

        for left in range(len(nodes)):
            left_id = node_ids[left]
            left_x, left_y = positions[left_id]
            for right in range(left + 1, len(nodes)):
                right_id = node_ids[right]
                right_x, right_y = positions[right_id]
                dx = left_x - right_x
                dy = left_y - right_y
                distance = math.hypot(dx, dy) or 0.01
                force = (k * k) / distance
                push_x = (dx / distance) * force
                push_y = (dy / distance) * force
                displacements[left_id][0] += push_x
                displacements[left_id][1] += push_y
                displacements[right_id][0] -= push_x
                displacements[right_id][1] -= push_y

        for edge in edges:
            source = edge["source"]
            target = edge["target"]
            source_x, source_y = positions[source]
            target_x, target_y = positions[target]
            dx = source_x - target_x
            dy = source_y - target_y
            distance = math.hypot(dx, dy) or 0.01
            weight = 0.65 + (edge["weight"] / max_weight) * 1.35
            force = ((distance * distance) / k) * 0.035 * weight
            pull_x = (dx / distance) * force
            pull_y = (dy / distance) * force
            displacements[source][0] -= pull_x
            displacements[source][1] -= pull_y
            displacements[target][0] += pull_x
            displacements[target][1] += pull_y

        for node in nodes:
            node_id = node["id"]
            node_type = node["type"]
            anchor_x, anchor_y, _ = anchors[node_type]
            position = positions[node_id]
            displacement = displacements[node_id]
            displacement[0] += (anchor_x - position[0]) * 0.028
            displacement[1] += (anchor_y - position[1]) * 0.028

            gravity_x = (width / 2 - position[0]) * 0.006
            gravity_y = (height / 2 - position[1]) * 0.006
            displacement[0] += gravity_x
            displacement[1] += gravity_y

            length = math.hypot(displacement[0], displacement[1]) or 0.01
            limited = min(length, temperature)
            position[0] += (displacement[0] / length) * limited
            position[1] += (displacement[1] / length) * limited

            margin = 30
            position[0] = min(width - margin, max(margin, position[0]))
            position[1] = min(height - margin, max(margin, position[1]))

        temperature *= 0.976 - (0.10 / max(iterations, 1))
        temperature = max(2.2, temperature)

    return {node_id: (xy[0], xy[1]) for node_id, xy in positions.items()}


def build_adjacency(nodes: list[dict], edges: list[dict]) -> dict[str, list[dict]]:
    labels = {node["id"]: node["label"] for node in nodes}
    node_types = {node["id"]: node["type"] for node in nodes}
    adjacency: defaultdict[str, list[dict]] = defaultdict(list)
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        payload = {
            "source": source,
            "target": target,
            "source_label": labels[source],
            "target_label": labels[target],
            "source_type": node_types[source],
            "target_type": node_types[target],
            "weight": edge["weight"],
            "type": edge["type"],
        }
        adjacency[source].append(payload)
        adjacency[target].append(payload)

    for node_id, neighbors in adjacency.items():
        adjacency[node_id] = sorted(neighbors, key=lambda item: (-item["weight"], item["target_label"]))
    return dict(adjacency)
