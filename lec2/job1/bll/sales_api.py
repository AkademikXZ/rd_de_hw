import os
import shutil
import requests
import json
from pathlib import Path

AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")
print(AUTH_TOKEN)
def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    raw_path = Path(raw_dir)

    if raw_path.exists():
        shutil.rmtree(raw_path)
    raw_path.mkdir(parents=True, exist_ok=True)

    page = 1
    while True:
        url = f"https://fake-api-vycpfa6oca-uc.a.run.app/sales?date={date}&page={page}"
        headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code} {response.text}")

        sales_data = response.json()
        if not sales_data:
            break

        out_file = raw_path / f"sales_{date}_{page}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(sales_data, f, ensure_ascii=False, indent=2)

        page += 1
