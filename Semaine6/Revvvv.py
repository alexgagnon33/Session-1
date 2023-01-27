cours = {
    "CP1": "Keven Presseau-St-Laurent",
    "CP2": "John Doe",
    "CP3": "Jane Smith"
}

while True:
    print("Sélectionnez une option:")
    print("1. Sélectionnez un cours")
    print("2. Recherchez un enseignant")
    print("3. Quitter")
    choix = int(input())
    if choix == 1:
        print("Sélectionnez un cours:")
        for i, c in enumerate(cours):
            print(f"{i + 1}. {c}")
            cours_choix = int(input())
            nom_cours = list(cours.keys())[cours_choix - 1]
            nom_enseignant = cours[nom_cours]
            print(f"L'enseignant pour {nom_cours} est {nom_enseignant}.")
    elif choix == 2:
        print("Sélectionnez un enseignant:")
        for i, e in enumerate(cours.values()):
            print(f"{i + 1}. {e}")
            enseignant_choix = int(input())
            nom_enseignant = list(cours.values())[enseignant_choix - 1]
            for c, e in cours.items():
                if e == nom_enseignant:
                    nom_cours = c
                    break
        print(f"L'enseignant {nom_enseignant} enseigne le cours {nom_cours}.")
    elif choix == 3:
        break
    else:
        print("Choix non valide, veuillez réessayer.")