from __future__ import annotations


def unique_values(records: list[dict], key: str) -> list[str]:
    values: set[str] = set()
    for record in records:
        current = record.get(key, [])
        if isinstance(current, list):
            values.update(value for value in current if value)
        elif current:
            values.add(str(current))
    return sorted(values)


def filter_records(
    records: list[dict],
    search: str = "",
    equals_filters: dict[str, list[str]] | None = None,
) -> list[dict]:
    equals_filters = equals_filters or {}
    search = search.strip().lower()
    filtered: list[dict] = []
    for record in records:
        if search and search not in searchable_text(record):
            continue
        matched = True
        for key, selections in equals_filters.items():
            if not selections:
                continue
            value = record.get(key, [])
            if isinstance(value, list):
                if not any(selection in value for selection in selections):
                    matched = False
                    break
            elif value not in selections:
                matched = False
                break
        if matched:
            filtered.append(record)
    return filtered


def searchable_text(record: dict) -> str:
    parts: list[str] = []
    for value in record.values():
        if isinstance(value, list):
            parts.extend(str(item) for item in value)
        else:
            parts.append(str(value))
    return " ".join(parts).lower()
