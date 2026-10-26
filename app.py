from flask import Flask, render_template, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path(__file__).parent / "sample_data" / "tasks.json"

def load_tasks():
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html", tasks=load_tasks())

@app.route("/api/tasks")
def api_tasks():
    return jsonify(load_tasks())

@app.route("/health")
def health():
    return jsonify({"status": "ok", "project": "Beyond the Screen"})

if __name__ == "__main__":
    app.run(debug=True)
