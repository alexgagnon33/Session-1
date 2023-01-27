cours = {
    "CP1": "Keven Presseau-St-Laurent",
    "CP2": "John Doe",
    "CP3": "Jane Smith"
}

print("Sélectionnez un cours:")
for i, c in enumerate(cours):
    print(f"{i + 1}. {c}")

choix = int(input())
nom_cours = list(cours.keys())[choix - 1]
nom_enseignant = cours[nom_cours]

print(f"L'enseignant pour {nom_cours} est {nom_enseignant}.")