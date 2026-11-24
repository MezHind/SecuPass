# generator.py
import secrets
import string

# Mots faibles à éviter (à compléter)
weak_words = ["azerty", "password", "123456", "qwerty", "admin", "letmein", "motdepasse"]
# Patterns simples à éviter
simple_patterns = ["123", "abc", "2024", "000", "111", "987"]

def generate_password(length=12):
    if length < 8:
        raise ValueError("La longueur minimale recommandée est de 12 caractères.")

    # Caractères à inclure
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    while True:
        # Génère un mot de passe aléatoire
        pwd = ''.join(secrets.choice(all_chars) for _ in range(length))

        # Vérifie la présence obligatoire de chaque type
        if (any(c in lower for c in pwd)
            and any(c in upper for c in pwd)
            and any(c in digits for c in pwd)
            and any(c in symbols for c in pwd)):

            pwd_lower = pwd.lower()

            # Vérifie qu'aucun mot faible ou motif simple n'est présent
            if not any(word in pwd_lower for word in weak_words) and not any(pattern in pwd_lower for pattern in simple_patterns):
                return pwd
