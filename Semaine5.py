#Exercice 1 :
#À partir de votre exercice sur les données DMS, créez un programme permettant de recevoir une liste de données(en DMS) dans un 
#fichier data.txt d'une taille indéterminée et trouvez la position la plus proche du Pôle-Nord.
#Pour tester l'exécution de votre programme vous devez créer une liste ayant les positions en DMS d'au moins 10 villes 
#et les placer dans le fichier data.txt.

Recevoir liste
puis faire code avec numéro


f = open(Desktop, mode)
with open('Montréal.txt', 'w') as f:
    f.write(1)
f = open("Montréal.txt")

if f < 1:
    print('La ville est la plus proche du Pôle-Nord')
elif f



#Exercice 2:
#À partir de votre programme de calcul de l'effet de l'inflation, implémentez un programme prenant une fichier intitulé ipc.txt où 
#vous aurez les IPCs des années 1960 à 2021 et permettant à l'utilisateur d'entrer une année de son choix pour effectuer le calcul. 
#Vous devez aussi permettre à l'utilisateur d'entrer le prix de l'article en 1970 et son coût en 2021 pour connaitre le nom d'heures 
#de travail nécessaire.
# créer un fichier avec toutes les données, lire le fichier, mettre user_input pour choisir l'année et montrer l'année
# mettre un user_input en 1970 et 2021, mettre if $1970 et 2021 > 50 = 5h ...
f = open("myfile.txt", "x")
f.write("Woops! I have deleted the content!")
f.close()


#Exercice 3:
#Créer une fonction prenant une liste de nombres, d'une taille indéterminée, et permettant de les trier en ordre croissant. 
#(Vous ne pouvez pas utiliser sort() ou sorted(), vous devez vous-même implémenter l'algorithme)

import math

def trier(donnees: list[int]):

    donnees_triees = []

    while len(donnees) > 0:

        min = math.inf
        donnees_temp = []

        for donnee in donnees:
            if donnee < min:
                min = donnee

        for donnee in donnees:
            if donnee != min:
                donnees_temp.append(donnee)

        donnees = donnees_temp
        donnees_temp = []

        donnees_triees.append(min)
    return donnees_triees

données = [1, 8, 3, 11, 2, 5, 6, -4]
print(trier(données))

#OM Exploitation
def deplacer_a_droite_le_plus_grand(suite: list[int], n):
    permuter = False
    for i in range(n):
        if(suite[i] > suite [i+1]):
            permuter = True
            suite[i] , suite[i+1] = suite[i+1] , suite[i]
    return permuter

def trier_suite_ascendant(suite):
    continuer = True
    n = len(suite) - 1
    i = 0
    while i < n and continuer:
        continuer = deplacer_a_droite_le_plus_grand(suite, n - i)
        i = i+1
       
données = [1, 8, 3, 11, 2, 5, 6, -4]
trier_suite_ascendant(données)
print(données)

#Exercice 4:
#Créer un menu demandant à un utilisateur d'entrer un nombre pair, divisible par 3 et entre 10 et 29. Si l'utilisateur entre 
#un nombre ne correspondant pas à ces conditions, offrez-lui l'opportunité de faire un nouvel essai, tant et aussi longtemps 
#qu'il n'entre pas un bon nombre.

def menu_special():

    condition = False
    while not condition:

        user_input = int(input("Entrer un nombre entre 10 et 29, pair et divisible par 3: "))

        if 10 <= user_input <= 29 and user_input % 3 == 0 and user_input % 2 == 0:
            condition = True
            print("Votre nombre est valide.")
        else:
            print("Votre nombre n'est pas valide.")
menu_special()