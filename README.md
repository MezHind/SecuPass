# 🔐 SecuPass

> Outil éducatif en Python pour **générer**, **évaluer** et **comprendre** la robustesse des mots de passe, avec en bonus un mini-scanner de fichiers suspects.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/UI-CLI%20%2B%20CustomTkinter-informational)
![Domaine](https://img.shields.io/badge/Domaine-Cybers%C3%A9curit%C3%A9-red)
![Statut](https://img.shields.io/badge/Statut-Projet%20p%C3%A9dagogique-green)

---

## 📌 Contexte

Projet réalisé dans le cadre de ma formation d'**ingénieur en cybersécurité**. Il a pour objectifs de :

- mettre en pratique les bonnes pratiques de **génération cryptographiquement sûre** de secrets ;
- implémenter un **évaluateur heuristique** de robustesse de mots de passe ;
- fournir un **retour pédagogique** à l'utilisateur sur les critères de sécurité ;
- explorer les bases de la **détection statique** de fichiers suspects (module bonus).

> ⚠️ **Projet pédagogique** : il ne remplace ni un gestionnaire de mots de passe, ni un antivirus, ni un audit de sécurité.

---

## ✨ Fonctionnalités

### 1. Générateur de mots de passe (`generator.py`)
- Utilise le module [`secrets`](https://docs.python.org/3/library/secrets.html) (CSPRNG) et **non** `random`, qui n'est pas adapté à un usage cryptographique.
- Alphabet de 94 caractères : minuscules, majuscules, chiffres, symboles.
- Garantit la présence d'**au moins un caractère de chaque catégorie**.
- Rejette les mots de passe contenant des **mots faibles** (`password`, `azerty`, `qwerty`, `admin`…) ou des **motifs simples** (`123`, `abc`, `2024`, `000`…).
- Longueur par défaut : **12 caractères** (≈ 78 bits d'entropie théorique : 12 × log₂(94)).

### 2. Évaluateur de robustesse (`evaluator.py`)
Score de **0 à 6** calculé selon les critères suivants :

| Critère | Points |
|---|---|
| Longueur ≥ 12 | +2 |
| Longueur entre 8 et 11 | +1 |
| Présence de minuscules | +1 |
| Présence de majuscules | +1 |
| Présence de chiffres | +1 |
| Présence de symboles | +1 |
| Motif faible détecté (`123`, `abc`, `password`, `azerty`, `qwerty`, `2024`) | −1 |
| Caractères de contrôle / invisibles | −1 |
| Présence d'un espace | −1 |

| Score | Niveau |
|---|---|
| 0 – 1 | Très faible |
| 2 – 3 | Faible |
| 4 – 5 | Correct |
| 6 | Très fort |

Chaque faiblesse détectée produit une **recommandation personnalisée**.

### 3. Interfaces
| Fichier | Description |
|---|---|
| `main.py` | Interface en ligne de commande (menu interactif) |
| `main_modern.py` | Interface graphique moderne (mode sombre) avec [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) |
| `test.py` | Boucle de test rapide de l'évaluateur en console |

### 4. Module bonus : scanner de fichiers suspects (`proget2/main.py`)
Mini-outil de détection **statique** qui parcourt un répertoire selon trois méthodes :

1. **Nom de fichier** : comparaison avec une liste de noms connus comme suspects ;
2. **Empreinte (hash)** : calcul du MD5 de chaque fichier et comparaison avec une liste de hash malveillants ;
3. **Chaînes de caractères** : recherche de mots-clés suspects (`steal`, `keylogger`…) dans le contenu binaire.

> Les listes fournies sont des **exemples fictifs** destinés à illustrer les principes de détection par signature.

---

## 🗂️ Structure du projet

```
SecuPass/
├── generator.py        # Génération sécurisée de mots de passe
├── evaluator.py        # Évaluation de la robustesse
├── main.py             # Interface CLI
├── main_modern.py      # Interface graphique (CustomTkinter)
├── test.py             # Test interactif de l'évaluateur
├── proget2/
│   └── main.py         # Scanner de fichiers suspects (bonus)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

**Prérequis** : Python 3.10 ou supérieur.

```bash
# 1. Cloner le dépôt
git clone https://github.com/<votre-utilisateur>/<nom-du-depot>.git
cd <nom-du-depot>

# 2. (Recommandé) Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate

# 3. Installer les dépendances (uniquement pour l'interface graphique)
pip install -r requirements.txt
```

La version console et le scanner n'utilisent que la **bibliothèque standard** de Python.

---

## 💻 Utilisation

### Interface console
```bash
python main.py
```
```
============================================================
                   BIENVENUE DANS SECUPASS
============================================================
 MENU PRINCIPAL
1. Générer un mot de passe sécurisé
2. Évaluer un mot de passe
3. Quitter
```

### Interface graphique
```bash
python main_modern.py
```

### Scanner de fichiers suspects
```bash
cd proget2
python main.py        # analyse le répertoire courant
```

### Utilisation en tant que bibliothèque
```python
from generator import generate_password
from evaluator import evaluate_password

pwd = generate_password(16)
print(evaluate_password(pwd))
# {'score': 6, 'strength': 'Très fort', 'feedback': []}
```

### Créer un exécutable Windows (optionnel)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main_modern.py
```

---

## 🛡️ Notions de sécurité abordées

- **CSPRNG vs PRNG** : choix de `secrets` plutôt que `random`.
- **Entropie** : taille de l'alphabet et longueur comme facteurs de résistance au brute-force.
- **Politiques de complexité** et leurs limites.
- **Détection par signature** : nom, hash, chaînes de caractères.
- **Hygiène de saisie** : détection des caractères de contrôle et espaces accidentels.

---

## ⚠️ Limites connues

L'évaluateur est **heuristique** et volontairement simple :

- ne mesure pas l'entropie réelle (un mot de passe peut satisfaire tous les critères et rester prévisible, ex. `Azerty!2024x` est pénalisé, mais `Soleil#Paris9` passe malgré une structure courante) ;
- n'utilise **pas de dictionnaire** étendu (type RockYou) ni de détection de séquences clavier avancée ;
- ne vérifie pas si le mot de passe a fuité (ex. API [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) en *k-anonymity*) ;
- le scanner utilise **MD5**, algorithme obsolète pour la sécurité (SHA-256 recommandé), et lit les fichiers en mémoire en une seule fois ;
- la détection par chaînes de caractères génère de nombreux **faux positifs** (le mot « password » est très courant).

---

## 🔭 Pistes d'amélioration

- [ ] Calcul d'entropie (formule de Shannon / bibliothèque `zxcvbn`)
- [ ] Vérification des fuites via HIBP (k-anonymity)
- [ ] Dictionnaire de mots de passe courants en fichier externe
- [ ] Options de génération (longueur, jeux de caractères, passphrases)
- [ ] Migration du scanner vers SHA-256 et lecture par blocs
- [ ] Tests unitaires (`pytest`) et intégration continue (GitHub Actions)
- [ ] Journalisation et export des résultats du scanner

---

## 🧰 Technologies

- **Python 3** : `secrets`, `string`, `hashlib`, `os`
- **CustomTkinter** : interface graphique
- **PyInstaller** : packaging en exécutable

---

## 📄 Licence

Distribué sous licence **MIT** (à adapter selon votre choix).

---

## 👤 Auteur

**<Votre Nom>** : étudiant ingénieur en cybersécurité
[LinkedIn](https://linkedin.com/in/<votre-profil>) · [GitHub](https://github.com/<votre-utilisateur>)

> *Ne saisissez jamais vos vrais mots de passe dans un outil dont vous ne maîtrisez pas le code.*
