import os
from flask import Flask, render_template, request, jsonify
# Initialisation de l'application Flask avec des chemins relatifs
app = Flask(__name__, template_folder="templates", static_folder="static")

# Route principale
@app.route('/')
def home():
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    # Vérifie si Flask trouve les fichiers correctement
    print("Dossier de travail actuel :", os.getcwd())
    print("Templates trouvés ici :", os.path.join(os.getcwd(), "templates"))
    print("Static trouvé ici :", os.path.join(os.getcwd(), "static"))
# Données pour stocker les signatures et les dons
signatures = []
donations = []

# Articles de la rubrique Revue de presse
articles = [
    
    {
        "title": "En Côte d’Ivoire, asphyxiée par le plastique, la « perle des lagunes » d’Abidjan se meurt",
        "source": "Le Monde",
        "link": "https://www.lemonde.fr/afrique/article/2022/08/23/en-cote-d-ivoire-asphyxiee-par-le-plastique-la-perle-des-lagunes-d-abidjan-se-meure_6138746_3212.html",
        "summary": "Un article poignant sur les défis environnementaux que rencontre Abidjan face à la pollution plastique."
    },
    {
        "title": "Bernard Derrien dénonce : « Ce qui se passe actuellement à Abidjan est scandaleux »",
        "source": "Linfodrome",
        "link": "https://www.linfodrome.com/societe/65206-bernard-derien-president-du-collectif-des-riverains-de-la-lagune-ebrie-denonce-ce-qui-se-passe-actuellement-a-abidjan-est-scandaleux",
        "summary": "Le président du collectif des riverains de la lagune Ébrié appelle à une action urgente contre la dégradation environnementale."
    }
]

# Route principale
@app.route('/')
def home():
    """Affiche la page principale avec les articles."""
    return render_template('index.html', articles=articles)

# Route pour la pétition
@app.route('/sign', methods=['POST'])
def sign_petition():
    """Route pour enregistrer les signatures de la pétition."""
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        signatures.append({'name': name, 'email': email})
        return jsonify({'message': 'Signature enregistrée avec succès !'}), 200
    return jsonify({'message': 'Veuillez remplir tous les champs.'}), 400

# Route pour les dons
@app.route('/donate', methods=['POST'])
def make_donation():
    """Route pour enregistrer les dons."""
    amount = request.form.get('amount')
    if amount:
        donations.append({'amount': amount})
        return jsonify({'message': 'Merci pour votre don !'}), 200
    return jsonify({'message': 'Montant invalide.'}), 400

if __name__ == '__main__':
    # Impressions pour diagnostic
    print("Dossier de travail actuel :", os.getcwd())
    print("Chemin absolu pour templates :", os.path.abspath('templates'))
    print("Chemin absolu pour static :", os.path.abspath('static'))
    
    # Lancement de l'application Flask
    
    app.run(debug=True, host='0.0.0.0')

