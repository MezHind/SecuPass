# main.py
from generator import generate_password
from evaluator import evaluate_password
import time

def show_intro():
    print("=" * 60)
    print(" BIENVENUE DANS SECUPASS ".center(60))
    print("=" * 60)
    print("Un outil éducatif pour :")
    print("- Générer des mots de passe sécurisés")
    print("- Évaluer leur robustesse")
    print("- Comprendre les critères de sécurité")
    print("=" * 60)
    print()

def menu():
    print("\n MENU PRINCIPAL")
    print("1. Générer un mot de passe sécurisé")
    print("2. Évaluer un mot de passe")
    print("3. Quitter")
    return input("\n => Que souhaitez-vous faire ? (1/2/3) : ")

def handle_generation():
    print("\n Génération d’un mot de passe sécurisé (12 caractères obligatoires)...\n")
    pwd = generate_password()
    print(f" => Mot de passe généré : \033[92m{pwd}\033[0m\n")
    input(" Appuyez sur Entrée pour revenir au menu...")

def handle_evaluation():
    while True:
        pas = input("Entrez un mot de passe à évaluer : ")

        if pas.lower() == 'exit':
            print("Fermeture du programme.")
            break

        result = evaluate_password(pas)

        print(f"\n => Score : {result['score']}/7")
        print(f"=> Niveau : {result['strength']}")
        if result['feedback']:
            print(" Suggestions :")
            for fb in result['feedback']:
                print(f"   - {fb}")

        # Si mot de passe très fort, sortir
        if result['strength'] == "Très fort":
            print("\n✅ Bon mot de passe ! Vous pouvez l'utiliser.")
            break
        else:
            print("\n❌ Mot de passe à améliorer. Essayez encore ou tapez 'exit' pour quitter.\n")
def main():
    show_intro()
    while True:
        choice = menu()
        if choice == '1':
            handle_generation()
        elif choice == '2':
            handle_evaluation()
        elif choice == '3':
            print("\n Merci d’avoir utilisé SecuPass. Restez en sécurité !\n")
            break
        else:
            print(" Choix invalide. Veuillez entrer 1, 2 ou 3.")

if __name__ == "__main__":
    main()
