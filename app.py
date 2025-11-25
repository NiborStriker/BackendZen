from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Active CORS pour permettre les requêtes depuis ton frontend

# Liste de citations inspirantes en français
citations = [
    {
        "texte": "La vie est un défi à relever, un bonheur à mériter, une aventure à tenter.",
        "auteur": "Mère Teresa"
    },
    {
        "texte": "Le succès c'est d'aller d'échec en échec sans perdre son enthousiasme.",
        "auteur": "Winston Churchill"
    },
    {
        "texte": "Ce n'est pas parce que les choses sont difficiles que nous n'osons pas, c'est parce que nous n'osons pas qu'elles sont difficiles.",
        "auteur": "Sénèque"
    },
    {
        "texte": "La seule façon de faire du bon travail est d'aimer ce que vous faites.",
        "auteur": "Steve Jobs"
    },
    {
        "texte": "Croyez en vos rêves et ils se réaliseront peut-être. Croyez en vous et ils se réaliseront sûrement.",
        "auteur": "Martin Luther King Jr."
    }
]

@app.route('/api/citation', methods=['GET'])
def obtenir_citation():
    """Renvoie une citation aléatoire en JSON"""
    citation_aleatoire = random.choice(citations)
    return jsonify(citation_aleatoire)

@app.route('/', methods=['GET'])
def accueil():
    """Page d'accueil de l'API"""
    return jsonify({
        "message": "Bienvenue sur l'API des citations inspirantes !",
        "endpoint": "/api/citation",
        "methode": "GET"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)