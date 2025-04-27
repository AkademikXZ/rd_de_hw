import requests

data = {
    "raw_dir": "file_storage/raw/sales/2022-08-09",
    "stg_dir": "file_storage/stg/sales/2022-08-09"
}

response = requests.post("http://localhost:8082/", json=data)

print("Status code:", response.status_code)
print("Response:", response.json())