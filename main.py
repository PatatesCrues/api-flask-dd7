from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/extraire', methods=['POST'])
def extraire_dd7():
    data = request.json
    urls = data.get("urls", [])
    resultats = []

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            html = response.text
            matches = re.findall(r'<dd[^>]*>(.*?)<\/dd>', html, re.DOTALL | re.IGNORECASE)
            valeur = matches[6] if len(matches) > 6 else "Non trouvé"
            valeur = re.sub(r'<[^>]+>', '', valeur).strip()
        except Exception as e:
            valeur = "Erreur"

        resultats.append(valeur)

    return jsonify({"resultats": resultats})
