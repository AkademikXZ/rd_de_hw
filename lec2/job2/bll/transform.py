import os
import shutil
import json
from pathlib import Path
from fastavro import writer, parse_schema

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def convert_raw_to_avro(raw_dir: str, stg_dir: str) -> None:
    raw_path = BASE_DIR / raw_dir
    stg_path = BASE_DIR / stg_dir

    if stg_path.exists():
        shutil.rmtree(stg_path)
    stg_path.mkdir(parents=True, exist_ok=True)

    json_files = sorted(raw_path.glob("*.json"))

    for idx, file in enumerate(json_files, start=1):
        with open(file, "r", encoding="utf-8") as f:
            records = json.load(f)

        if not records:
            continue

        example = records[0]
        schema = {
            "name": "SalesRecord",
            "type": "record",
            "fields": [{"name": k, "type": ["null", "string", "int", "float"]} for k in example]
        }
        parsed_schema = parse_schema(schema)

        avro_filename = f"{file.stem}.avro"
        avro_path = stg_path / avro_filename
        with open(avro_path, "wb") as out:
            writer(out, parsed_schema, records)