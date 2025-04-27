import os
from flask import Flask, request
from flask import typing as flask_typing
from dotenv import load_dotenv
import sys
from bll.transform import convert_raw_to_avro

load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.append(BASE_DIR)
os.chdir(BASE_DIR)
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    input_data = request.json
    raw_dir = input_data.get("raw_dir")
    stg_dir = input_data.get("stg_dir")

    if not raw_dir or not stg_dir:
        return {"message": "raw_dir or stg_dir missing"}, 400

    convert_raw_to_avro(raw_dir=raw_dir, stg_dir=stg_dir)

    return {"message": "Data successfully converted to Avro"}, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)