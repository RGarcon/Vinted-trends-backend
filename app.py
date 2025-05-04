from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Hashtags en dur pour Vinted
VINTED_HASHTAGS = [
    "vintedstyle", "haulvinted", "vintedfr", "vintedhaul",
    "vintedlook", "vintedtrouve", "vintedfashion", "vintedfinds"
]

@app.route("/trends")
def trends():
    return jsonify(VINTED_HASHTAGS)

@app.route("/keywords/<tag>")
def keywords(tag):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.tiktok.com/tag/{tag}"
    
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        
        texts = soup.stripped_strings
        all_text = " ".join(texts)

        words = re.findall(r'\b\w{4,15}\b', all_text.lower())  # Mots de 4 à 15 lettres
        ignore = {"https", "tiktok", "video", "vinted", "watch", "share", "more"}
        freq = {}

        for word in words:
            if word not in ignore:
                freq[word] = freq.get(word, 0) + 1

        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:15]
        return jsonify([w[0] for w in top_words])
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
