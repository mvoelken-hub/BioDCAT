import argparse
import csv
from pathlib import Path
import yaml

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def uri_details(schema: dict) -> list[dict[str, str]]:
    details = []

    def collect_entities(
        value: object,
        path: tuple[str, ...] = (),
        parent_class: str = "",
    ) -> None:
        if isinstance(value, dict):
            for name, definition in value.items():
                entity_path = path + (str(name),)
                if isinstance(definition, dict):
                    current_parent = parent_class
                    if path == ("classes",):
                        current_parent = str(name)
                    if "slot_uri" in definition or "class_uri" in definition:
                        uri_key = "slot_uri" if "slot_uri" in definition else "class_uri"
                        details.append(
                            {
                                "entity_name": ".".join(entity_path),
                                "uri": str(definition[uri_key]),
                                "parent_class": current_parent,
                                "description": str(definition.get("description", "")),
                            }
                        )
                    collect_entities(definition, entity_path, current_parent)
        elif isinstance(value, list):
            for item in value:
                collect_entities(item, path, parent_class)

    collect_entities(schema)
    return sorted(details, key=lambda detail: detail["entity_name"])

def main():
    parser = argparse.ArgumentParser(
        description="Write entities with slot_uri or class_uri from both YAML schema files"
    )
    parser.add_argument("ground_truth", type=Path, help="Ground-truth YAML schema")
    parser.add_argument("comparison", type=Path, help="YAML schema to check")
    args = parser.parse_args()

    ground_truth_entities = uri_details(load_yaml(args.ground_truth))
    comparison_entities = uri_details(load_yaml(args.comparison))
    with open("test.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, lineterminator="\n", delimiter = "|")
        writer.writerow(["file", "entity_name", "uri", "parent_class", "description"])
        for path, entities in (
            (args.ground_truth, ground_truth_entities),
            (args.comparison, comparison_entities),
        ):
            for entity in entities:
                writer.writerow(
                    [
                        path.name,
                        entity["entity_name"],
                        entity["uri"],
                        entity["parent_class"],
                        entity["description"],
                    ]
                )


if __name__ == "__main__":
    main()