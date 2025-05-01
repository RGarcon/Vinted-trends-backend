from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/trends")
def get_trends():
    hashtags = ["vintedstyle", "haulvinted", "vintedfr", "vintedhaul"]
    return jsonify(hashtags)

@app.route("/ping")
def ping():
    return "pong"
