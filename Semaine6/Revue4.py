#Partie1

courses = {}

with open("Prof.txt", "r", encoding="UTF-8") as prof_file:
    lines = prof_file.readlines()
    for i in range(0, len(lines), 2):
        course_name = lines[i].strip()
        teacher_name = lines[i+1].strip()
        courses[course_name] = teacher_name

#Partie 3

while True:
    print("1. Sélectionner un cours")
    print("2. Rechercher un enseignant")
    print("3. Ajouter un cours")
    print("4. Quitter")
    choice = int(input())

    if choice == 1:
        print("Sélectionnez un cours:")
        for i, course in enumerate(courses.keys()):
            print(f"{i+1}. {course}")

        selected_course = int(input())
        if selected_course > 0 and selected_course <= len(courses.keys()):
            course_name = list(courses.keys())[selected_course - 1]
            teacher_name = courses[course_name]
            print(f"Enseignant: {teacher_name}\nCours: {course_name}")
        else:
            print("Sélection non valide. Veuillez sélectionner une option valide.")

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
        course_name = input("Entrez le nom du cours à ajouter: ")
        teacher_name = input("Entrez le nom de l'enseignant: ")
        courses[course_name] = teacher_name

    elif choice == 4:
        break
    else:
        print("Sélection non valide. Veuillez sélectionner une option valide.")
