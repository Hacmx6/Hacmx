from flask import Flask, render_template
import json
import os

app = Flask(__name__)
output_dir = "/data/data/com.termux/files/home/storage/downloads/Hacmx"
json_path = os.path.join(output_dir, "scans.json")

@app.route("/")
def home():
    if os.path.exists(json_path):
        with open(json_path) as f:
            scans = json.load(f)
    else:
        scans = []
    return render_template("dashboard.html", scans=scans)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
