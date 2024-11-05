from flask import Flask
from flask import jsonify
from lib.processor import Processor


processor = Processor(data_format_path="./data_format.json", words_path="./random.txt")

app = Flask(__name__)

@app.route("/", defaults={"path" : ""})
@app.route("/<path:path>")
def catch_all(path):
    print(path)
    response = processor.process(route=path)
    return jsonify(response)

