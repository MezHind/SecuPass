from evaluator import evaluate_password

def main():
    print("🔐 Vérification de mot de passe sécurisé")
    print("Tapez 'exit' pour quitter.\n")

    while True:
        pas = input("Entrez un mot de passe à évaluer : ")

        if pas.lower() == 'exit':
            print("Fermeture du programme.")
            break

        result = evaluate_password(pas)

        print(f"\n➡️ Score : {result['score']}/6")  
        print(f"➡️ Niveau : {result['strength']}")
        if result['feedback']:
            print("⚠️ Suggestions :")
            for fb in result['feedback']:
                print(f"   - {fb}")

        # Si mot de passe très fort, sortir
        if result['strength']== "Très fort":
            print("\n✅ Bon mot de passe ! Vous pouvez l'utiliser.")
            break
        else:
            print("\n❌ Mot de passe à améliorer. Essayez encore ou tapez 'exit' pour quitter.\n")

if __name__ == "__main__":
    main()
   