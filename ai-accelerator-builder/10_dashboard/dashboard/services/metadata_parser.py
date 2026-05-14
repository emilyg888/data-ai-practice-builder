from __future__ import annotations

import re
from pathlib import Path


FRONT_MATTER_BOUNDARY = "---"
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
KEY_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*)$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_front_matter(text: str) -> tuple[dict, str]:
    stripped_text = text.lstrip()
    if not stripped_text.startswith(FRONT_MATTER_BOUNDARY):
        return {}, text
    parts = stripped_text.split(FRONT_MATTER_BOUNDARY, 2)
    if len(parts) < 3:
        return {}, text
    raw = parts[1].strip("\n")
    body = parts[2].lstrip("\n")
    return parse_simple_yaml(raw), body


def parse_simple_yaml(raw: str) -> dict:
    data: dict[str, object] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        key_match = KEY_RE.match(stripped)
        if key_match:
            key, remainder = key_match.groups()
            if remainder == "":
                data[key] = []
                current_key = key
            else:
                data[key] = parse_inline_value(remainder)
                current_key = key if isinstance(data[key], list) else None
            continue
        if current_key and stripped[:2] in {"- ", "* "}:
            values = data.setdefault(current_key, [])
            if isinstance(values, list):
                values.append(parse_inline_value(stripped[2:].strip()))
            continue
        if current_key and isinstance(data.get(current_key), list):
            data[current_key].append(parse_inline_value(stripped))
    return data


def parse_inline_value(value: str) -> object:
    value = value.strip()
    if value in {"[]", ""}:
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_inline_value(part) for part in inner.split(",")]
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    if lowered in {"null", "none"}:
        return ""
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        return value[1:-1]
    return value


def first_heading(body: str) -> str:
    for line in body.splitlines():
        match = HEADING_RE.match(line.strip())
        if match:
            return match.group(2).strip()
    return ""


def extract_sections(body: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = "_root"
    sections[current] = []
    for line in body.splitlines():
        match = HEADING_RE.match(line.strip())
        if match:
            current = normalize_section_name(match.group(2))
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line)
    return {key: "\n".join(lines).strip() for key, lines in sections.items()}


def normalize_section_name(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^[0-9.]+\s*", "", value)
    return re.sub(r"[^a-z0-9]+", "_", value).strip("_")


def extract_bullets(text: str) -> list[str]:
    bullets: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped[:2] in {"- ", "* "}:
            bullets.append(clean_bullet(stripped[2:]))
        elif re.match(r"^\d+\.\s+", stripped):
            bullets.append(clean_bullet(re.sub(r"^\d+\.\s+", "", stripped)))
    return [bullet for bullet in bullets if bullet]


def clean_bullet(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^\*\*(.*?)\*\*\s*", r"\1 ", value)
    return re.sub(r"\s+", " ", value).strip()


def parse_markdown_tables(text: str) -> list[list[dict[str, str]]]:
    tables: list[list[dict[str, str]]] = []
    lines = [line.rstrip() for line in text.splitlines()]
    index = 0
    while index < len(lines) - 1:
        header = lines[index].strip()
        divider = lines[index + 1].strip()
        if header.startswith("|") and divider.startswith("|") and "---" in divider:
            headers = [cell.strip() for cell in header.strip("|").split("|")]
            index += 2
            rows: list[dict[str, str]] = []
            while index < len(lines):
                row_line = lines[index].strip()
                if not row_line.startswith("|"):
                    break
                cells = [cell.strip() for cell in row_line.strip("|").split("|")]
                if len(cells) != len(headers):
                    break
                rows.append({headers[i]: cells[i] for i in range(len(headers))})
                index += 1
            if rows:
                tables.append(rows)
            continue
        index += 1
    return tables


def first_paragraph(text: str) -> str:
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    for chunk in chunks:
        if not chunk.startswith("|"):
            return re.sub(r"\s+", " ", chunk)
    return ""


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def title_from_path(path: Path) -> str:
    stem = path.stem if path.stem != "pattern" else path.parent.name
    stem = stem.replace("_", " ").replace("-", " ")
    return " ".join(part.capitalize() for part in stem.split())


def relative_display_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def ensure_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [normalize_scalar(item) for item in value if normalize_scalar(item)]
    normalized = normalize_scalar(value)
    if not normalized:
        return []
    if "," in normalized:
        return [part.strip() for part in normalized.split(",") if part.strip()]
    return [normalized]


def normalize_scalar(value: object) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return "" if text.lower() in {"", "tbd", "none", "null", "n/a"} else text
