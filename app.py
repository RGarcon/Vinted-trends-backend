from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/trends")
def trends():
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.tiktok.com/tag/vinted"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    tags = set()
    for tag in soup.find_all("a", href=True):
        if "/tag/" in tag["href"]:
            tag_name = tag["href"].split("/tag/")[1].split("?")[0]
            tags.add(tag_name.lower())

    return jsonify(sorted(list(tags))[:15])
