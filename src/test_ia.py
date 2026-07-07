import json
from pathlib import Path
from google import genai


print("Démarrage test_ia")

# Path pour gérer transition "/" (Mac) et "\" (Win)
chemin_racine = Path(__file__).parent.parent #/Users/eloiselcr/Pix
chemin_config = chemin_racine / "config.json" 

print("Lecture du fichier config : {chemin_config}")
with open(chemin_config, "r", encoding="utf-8") as fichier:
    config = json.load(fichier)

cle_api = config.get("GEMINI_API_KEY")

if not cle_api:
    print("Erreur : aucune clé API trouvée dans config.json")
    exit()


# Initialisation du client en lui donnant clé api
client = genai.Client(api_key=cle_api)

print("Envoi de la question à l'IA...")

# Query 
reponse = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="Quelle est la couleur du soleil ?"
)

# Reponse
print("Gemini répond : ", reponse.text)