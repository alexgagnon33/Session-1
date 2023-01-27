courses = {"Concepts de programmation 1": "Keven Presseau-St-Laurent",
"Systèmes d'exploitation": "Keven Presseau-St-Laurent",
"Logique mathématique pour les professionnelles": "Nicolas Thavonekham Robidoux"}

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
            print(f"{course_name} - {teacher_name}")
        else:
            print("Sélection non valide. Veuillez sélectionner une option valide.")