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
        enseignant_choix = input()
        for c, e in cours.items():
            if e == enseignant_choix:
                nom_cours = c
                nom_enseignant = e
                break
        print(f"L'enseignant {nom_enseignant} enseigne le cours {nom_cours}.")
    elif choix == 3:
        nom_cours = input("Entrez le nom du cours: ")
        nom_enseignant = input("Entrez le nom de l'enseignant: ")
        cours[nom_cours] = nom_enseignant
        print("Cours et enseignant ajoutés.")
        with open("Revue4\pomme.txt", "w", encoding="UTF-8") as file:
            file.write(str(cours))
    elif choix == 4:
        break
    else:
        print("Choix non valide, veuillez réessayer.")