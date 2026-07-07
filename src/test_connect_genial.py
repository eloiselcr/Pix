import json
import requests
from pathlib import Path

# Désactiver les avertissements SSL pour l'intranet de ton bureau
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("Démarrage du test de connexion à Génial...")

chemin_racine = Path(__file__).parent.parent # /Pix
chemin_config = chemin_racine / "config.json"

with open(chemin_config, "r", encoding="utf-8") as fichier:
    config = json.load(fichier)

cle_genial = config.get("GENIAL_API_KEY")

if not cle_genial:
    print("Erreur : Manque clé API GENIAL")
    exit()


# Préparation appel
url_genial = "https://api-genial.artemis-ia-dr.intradef.gouv.fr/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {cle_genial}"
}
donnees_requete = {
    "model": "Générique v2", 
    "messages": [
        {
            "role": "user",
            "content": "Dis moi de quelle couleur est le soleil ?"
        }
    ]
}

# Envoie de la requête
print("Envoi de la requête à Genial...")
try:
    reponse = requests.post(url_genial, headers=headers, json=donnees_requete, verify=False)
    
    if reponse.status_code == 200:
        print("Connexion réussie !")
        # On extrait la réponse textuelle de l'IA
        texte_reponse = reponse.json()["choices"][0]["message"]["content"]
        print(f"Genial a répondu : {texte_reponse}")
    else:
        print(f"Échec (Code d'erreur : {reponse.status_code})")
        print(reponse.text)
        
except Exception as e:
    print("Erreur réseau :")
    print(e)