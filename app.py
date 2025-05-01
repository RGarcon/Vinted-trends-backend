from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/trends")
def get_trends():
    hashtags = ["vintedstyle", "haulvinted", "vintedfr", "vintedhaul"]
    return jsonify(hashtags)

@app.route("/ping")
def ping():
    return "pong"
