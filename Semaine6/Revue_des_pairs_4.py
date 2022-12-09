"""
Partie 1:
Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant respectif. Par exemple:
Keven Presseau-St-Laurent - Concepts de programmation 1

Ensuite, afficher un menu à la console présentant les 3 cours et offrant à l'utilisateur d'en sélectionner 1. 
Lorsque l'utilisateur à fait sa sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

Partie 2:
En se basant sur la partie 1, créer un fichier bdd.txt fonctionnant comme une base de données et remplir le dictionnaire à partir 
de ce fichier. Pour vous faciliter la tâche, vous pouvez écrire les informations de la manière suivante:
Nom de cours 1
Nom de prof 1
Nom de cours 2

Partie 3:
En se basant sur la partie 2, modifier le menu utilisateur en y ajoutant une option lui permettant de faire une recherche d'enseignant. 
Vérifier si l'enseignant entré par l'utilisateur est présent dans votre liste de cours et indiquer le résultat à la console.

Partie 4:
Offrir à l'utilisateur une nouvelle option au menu lui permettant d'ajouter un cours et un nom d'enseignant à la base de données de 
la partie 2. Une fois les données utilisateurs entrées, ajouter les informations à la fin du document bdd.txt
"""

def dictionnaire():
    cours = {'Keven Presseau-St-Laurent' : 'Concepts de programmation',
             'Keven Presseau-St-Laurent'  : 'Système exploitation',
              'Prof Math' : 'Logique Mathématique'}

def doc(menu):
    with open('bdd.txt', 'w', encoding='UTF-8') as f:
        f.write(f'{menu} \n')

def menuoui():
    sortie = False
    while not sortie:
        menu={1 : 'Concepts de programmation', 
              2 : 'Logique Mathématique',
              3 : 'Système exploitation',
              4 : 'Sortie'}
        print(menu)
        for num, option in menu.items():
            print(f'{num}-{option}')
        choix = int(input("Option choisie: "))
        print(choix)
        match choix:
            case 1:
                print('Keven Presseau-St-Laurent' : 'Concepts de programmation')
                doc(menu)
            case 2:
                print('Keven Presseau-St-Laurent'  : 'Système exploitation')
                doc(menu)
            case 3:
                print('Prof Math' : 'Logique Mathématique')
                doc(menu)
            case 4:
                sortie = True
            case 5:
                #Permettre utilisateur d'écrire le om d'un prof et montrer lees cours qu'ils enseignent


