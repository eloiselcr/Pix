# 📝 Documentation du Projet Pix

Ce projet a pour but de lire automatiquement un fichier devis au format PDF, d'en extraire les informations clés à l'aide de l'IA (Gemini) et de remplir automatiquement une Fiche d'Expression de Besoin (FEB) au format Excel.

---

## 📁 Structure du Projet

Voici l'organisation des dossiers et fichiers du projet :

```text
Pix/
├── .gitignore          # Fichiers et dossiers à exclure de Git (ex: venv, config.json)
├── config.json         # Configuration locale contenant les clés API (secret, non partagé)
├── requirements.txt    # Liste des bibliothèques Python indispensables au projet
├── src/                # Dossier contenant tous les scripts de programmation Python
│   ├── test_ia.py       # Script de test de communication avec Gemini
│   ├── test_pdf.py      # Script de test de lecture et extraction de PDF
│   ├── scan_tags.py     # Script utilitaire pour lister les balises du modèle Excel
│   └── analyse_devis.py # Script d'analyse de devis par l'IA
├── templates/          # Dossier contenant les modèles de fichiers
│   └── FEB_modele.xlsx  # Modèle de la FEB Excel contenant les balises {{ }}
└── libs/               # Dossier destiné à contenir les paquets .whl pour l'installation hors-ligne
```

---

## 📚 Bibliothèques Installées

Toutes les bibliothèques choisies sont en **"Pure Python"** (sans compilation C/C++ nécessaire lors de l'installation), ce qui garantit une installation fluide sur le PC Windows cible hors-ligne.

| Bibliothèque | Rôle | Pourquoi ce choix ? |
| :--- | :--- | :--- |
| **`google-genai`** | SDK Google pour Gemini | Permet de communiquer proprement avec l'IA de Google en mode développement. |
| **`pypdf`** | Extraction de texte PDF | Bibliothèque légère et pure Python, très stable pour lire les fichiers PDF. |
| **`openpyxl`** | Modification de fichiers Excel | Indispensable pour ouvrir un `.xlsx` existant, y chercher des balises et les remplacer. |

---

## 💻 Instructions pour l'installation hors-ligne (PC Cible)

Puisque le PC cible n'a pas accès à internet, nous utiliserons la méthode des paquets locaux `.whl` (wheels).

### Étape A : Télécharger les paquets sur la machine connectée (Mac)
Depuis le dossier du projet sur ton Mac connecté à internet, lance la commande suivante pour télécharger les installateurs Windows dans le dossier `libs/` :
```bash
pip download -r requirements.txt --dest libs --platform win_amd64 --python-version 3.12 --only-binary=:all:
```

### Étape B : Installer sur la machine déconnectée (Windows)
Une fois le dossier du projet copié sur le PC cible (via USB ou réseau interne), ouvre un terminal dans le dossier et lance :
```bash
pip install --no-index --find-links=libs -r requirements.txt
```
Cette commande installera toutes les bibliothèques listées dans `requirements.txt` en allant piocher directement dans le dossier `libs/`, sans jamais interroger internet !
