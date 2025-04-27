import requests

data = {
    "date": "2022-08-09",
    "raw_dir": "file_storage/raw/sales/2022-08-09"
}

response = requests.post("http://localhost:8081/", json=data)

print("Status code:", response.status_code)
print("Response:", response.json())