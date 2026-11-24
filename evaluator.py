import string
import re

# Patterns faibles fréquents
WEAK_PATTERNS = ['123', 'abc', 'password', 'azerty', 'qwerty', '2024']

# Caractères de contrôle ou invisibles
CONTROL_CHARS = [chr(c) for c in range(0, 32)] + [chr(127)]


def evaluate_password(password):
    """
    Évalue la robustesse d'un mot de passe sur une échelle de 0 à 6.
    Retourne le score, une appréciation et des recommandations personnalisées.
    """
    score = 0
    feedback = []

    length = len(password)

    # Longueur du mot de passe
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
        feedback.append("👍 Bon début, mais 12 caractères ou plus, ce serait encore mieux !")
    else:
        feedback.append("❌ Mot de passe trop court.")

    # Diversité de caractères
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("❌ Pas de lettres minuscules.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Pas de lettres majuscules.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Pas de chiffres.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("❌ Pas de symboles spéciaux.")

    # Motifs faibles
    pwd_lower = password.lower()
    for pattern in WEAK_PATTERNS:
        if pattern in pwd_lower:
            score -= 1
            feedback.append(f"⚠️ Contient un motif faible : '{pattern}'")
            break

    # Caractères indésirables
    if any(c in password for c in CONTROL_CHARS):
        score -= 1
        feedback.append("⚠️ Contient des caractères invisibles ou de contrôle (ex: retour à la ligne, tabulation).")

    if ' ' in password:
        score -= 1
        feedback.append("⚠️ Contient un espace. Ce caractère est souvent accidentel ou problématique.")

    
    # Limite du score entre 0 et 6
    score = max(0, min(score, 6))

    # Appréciation globale
    if score >= 6:
        strength = "Très fort"
    elif score >= 4:
        strength = "Correct"
    elif score >= 2:
        strength = "Faible"
    else:
        strength = "Très faible"

    return {
        'score': score,
        'strength': strength,
        'feedback': feedback
    }
