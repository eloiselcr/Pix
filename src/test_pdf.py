from pathlib import Path
from pypdf import PdfReader #pypdf pour lire pdf

print("Démarrage du test PDF...")

# 1. On trouve le chemin du fichier devis_test.pdf à la racine du projet
chemin_racine = Path(__file__).parent.parent
chemin_pdf = chemin_racine / "devis_test.pdf"

# sécurité
if not chemin_pdf.exists():
    print(f"Erreur : Le fichier {chemin_pdf.name} n'existe pas à la racine du projet !")
    exit()

print(f"Ouverture du fichier : {chemin_pdf.name}")

# classe PdfReader -> lit devis_pdf
devis_pdf = PdfReader(chemin_pdf)


# string pdf extract pour stocker texte extrait
pdf_extract = ""

# boucle pour parcourir devis_pdf et extraire
for index, page in enumerate(devis_pdf.pages): # on parcourt toutes les pages
    print(f"Lecture de la page {index + 1}...")
    texte_page = page.extract_text() # fonction extract 
    if texte_page: # si la page n'est pas vide
        pdf_extract = pdf_extract + texte_page + "\n" # on ajoute les nouvelles pages au fur et à mesure

print("\n--- Début du texte extrait du PDF : ---")
print(pdf_extract)
print("--- Fin du texte extrait ---")
