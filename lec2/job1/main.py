import os
from flask import Flask, request
from flask import typing as flask_typing
from dotenv import load_dotenv
import sys
from bll.sales_api import save_sales_to_local_disk

load_dotenv()
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.append(BASE_DIR)
os.chdir(BASE_DIR)

if not AUTH_TOKEN:
    print("API_AUTH_TOKEN environment variable must be set")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    input_data: dict = request.json
    date = input_data.get('date')
    raw_dir = input_data.get('raw_dir')

    if not date:
        return {"message": "date parameter missed"}, 400

    save_sales_to_local_disk(date=date, raw_dir=raw_dir)

    return {"message": "Data retrieved successfully from API"}, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)