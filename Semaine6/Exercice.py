def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False

print(is_prime(4))

#Exercice 1:
#Créer une liste contenant tous les nombres premiers entre 2 et 20. Ensuite, demander à l'utilisateur d'écrire un nombre entre 2 et 20 
#(bien vérifier si c'est le cas) et vérifier si ce nombre est premier à l'aide de votre liste en affichant le résultat à la console.

def nb_liste():

    nb_premier_min = 2
    nb_premier_max = 20

    choix_utilisateur = int(input("Ecriver un nombre premier entre 2 et 20: "))

    if choix_utilisateur > 1:
        for i in range(2, choix_utilisateur//2):
            if (choix_utilisateur % i) == 0:
                        print(choix_utilisateur, "est un nombre premier")
            else:
                print(choix_utilisateur, "n'est pas un nombre premier")

nb_liste


#and choix_utilisateur > nb_premier_min and choix_utilisateur < nb_premier_max:


#Exercice 2:
#Créer une liste de 5 éléments : [1, 2, 5, 3, 4]. Ensuite, créer deux copies de cette liste, une copie en surface et une copie profonde 
#intitulée respectivement surface et profonde. Finalement, demander à l'utilisateur d'entrer un mot, modifier le 2e élément de la liste 
#«surface» et le 3e élément de la liste «profonde» et imprimer les trois listes à la console.
import copy

def liste_element():

    nb_liste = [[1, 2, 5, 3, 4]]
    nb_liste_surface = copy.copy(nb_liste)
    nb_liste_profonde = copy.deepcopy(nb_liste)

    mot_utilisateur = input("Entrer un mot a integrer dans la liste: ")
    nb_liste.append({mot_utilisateur})
    
    nb_mod_2 = int(input("Entrer un nombre qui remplacera le 2e element: "))
    nb_liste_surface.insert(1, {nb_mod_2})

    nb_mod_3 = int(input("Entrer un nombre qui remplacera le 3e element: "))
    nb_liste_profonde.insert(1, {nb_mod_3})

    print(nb_liste)
    print(nb_liste_surface)
    print(nb_liste_profonde)




def suite_feb():
    num = int(input("Entrer un numero"))
    n1, n2 = 0, 1
    sum = 0
    for i in range (0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
suite_feb()

