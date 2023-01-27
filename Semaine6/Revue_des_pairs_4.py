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


courses = {
    "Concepts de programmation 1": "Keven Presseau-St-Laurent",
    "Algorithmique avancée": "Jean-Francois Tremblay",
    "Architecture des ordinateurs": "Martin Dupont"
}

print("Sélectionnez un cours:")
for i, course in enumerate(courses):
    print(f"{i+1}. {course}")
    
selected_course = int(input())

course_name = list(courses.keys())[selected_course - 1]
teacher_name = courses[course_name]
print(f"Enseignant: {teacher_name}\nCours: {course_name}")


courses = {}
with open("bdd.txt", "r") as bdd_file:
    lines = bdd_file.readlines()
    for i in range(0, len(lines), 2):
        course_name = lines[i].strip()
        teacher_name = lines[i+1].strip()
        courses[course_name] = teacher_name
        
print("Sélectionnez un cours:")
for i, course in enumerate(courses):
    print(f"{i+1}. {course}")

selected_course = int(input())

course_name = list(courses.keys())[selected_course - 1]
teacher_name = courses[course_name]
print(f"Enseignant: {teacher_name}\nCours: {course_name}")


courses = {}
with open("bdd.txt", "r") as bdd_file:
    lines = bdd_file.readlines()
    for i in range(0, len(lines), 2):
        course_name = lines[i].strip()
        teacher_name = lines[i+1].strip()
        courses[course_name] = teacher_name
        
while True:
    print("1. Sélectionner un cours")
    print("2. Rechercher un enseignant")
    print("3. Quitter")
    choice = int(input())
    
    if choice == 1:
        print("Sélectionnez un cours:")
        for i, course in enumerate(courses):
            print(f"{i+1}. {course}")

        selected_course = int(input())

        course_name = list(courses.keys())[selected_course - 1]
        teacher_name = courses[course_name]
        print(f"Enseignant: {teacher_name}\nCours: {course_name}")
        
    elif choice == 2:
        teacher_name = input("Entrez le nom de l'enseignant à rechercher: ")
        found = False
        for course, teacher in courses.items():
            if teacher.lower() == teacher_name.lower():
                print(f"{teacher} enseigne le cours {course}")
                found = True
        if not found:
            print(f"Aucun cours enseigné par {teacher_name} n'a été trouvé.")
            
    elif choice == 3:
        break
    else:
        print("Sélection non valide. Veuillez sélectionner une option valide.")


courses = {}
with open("bdd.txt", "r") as bdd_file:
    lines = bdd_file.readlines()
    for i in range(0, len(lines), 2):
        course_name = lines[i].strip()
        teacher_name = lines[i+1].strip()
        courses[course_name] = teacher_name

while True:
    print("1. Sélectionner un cours")
    print("2. Rechercher un enseignant")
    print("3. Ajouter un cours")
    print("4. Quitter")
    choice = int(input())
    
    if choice == 1:
        print("Sélectionnez un cours:")
        for i, course in enumerate(courses):
            print(f"{i+1}. {course}")

        selected_course = int(input())

        course_name = list(courses.keys())[selected_course - 1]
        teacher_name = courses[course_name]
        print(f"Enseignant: {teacher_name}\nCours: {course_name}")
        
    elif choice == 2:
        teacher_name = input("Entrez le nom de l'enseignant à rechercher: ")
        found = False
        for course, teacher in courses.items():
            if teacher.lower() == teacher_name.lower():
                print(f"{teacher} enseigne le cours {course}")
                found = True
        if not found:
            print(f"Aucun cours enseigné par {teacher_name} n'a été trouvé.")
            
    elif choice == 3:
        course_name = input("Entrez le nom du cours: ")
        teacher_name = input("Entrez le nom de l'enseignant: ")
        courses[course_name] = teacher_name
        with open("bdd.txt", "a") as bdd_file:
            bdd_file.write(f"{course_name}\n{teacher_name}\n")
        print(f"Le cours {course_name} enseigné par {teacher_name} a été ajouté à la base de données.")
            
    elif choice == 4:
        break
    else:
        print("Sélection non valide. Veuillez sélectionner une option valide.")
