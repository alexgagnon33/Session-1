def func1(valeur = 4):
    return valeur * valeur
variable = func1()
variable2 = func1(5)


def mult(valeur, mult = 2):
    return valeur * mult
m1 = mult(2, 4)
m2 = mult(3)

def showEmployee(nom, salaire = 9000):
    print(f'Name: {nom} salary: {salaire}')
showEmployee("Ben", 12000)
showEmployee("Jessa")
showEmployee("Victor", 12000000)

    # Create an outer function that will accept two parameters, a and b
    # Create an inner function inside an outer function that will calculate the addition of a and b
    # At last, an outer function will add 5 into addition and return it

#Créer une fonction externe qui accepte 2 paramètres a et b
#Créer une fonction interne à l'intérieur de la fonction externe qui permet de calculer l'Addition de a et b
#finalement, la fonction externe ajoute 5 au résultat de l'addition

def fonctionExterne(a, b):
    def fonctionInterne(a, b):
        return a + b
    resultat = fonctionInterne(a, b)
    return resultat + 5
print(fonctionExterne(3, 4))

def fct2():
    a = 2
    b = 3
    return a, b 
resultats = fct2()
c, d = resultats
print(print(c))

def fct4(a, b):
    somme = a + b
    return somme
fct4(5, 6)
#Créer une fonction qui prend un ou deux paramètre (si un seul paramètre est entré, assumer que le deuxieme est 10) 
# et retourne la somme et multiplication
def operation(a, b = 10):
    somme = a + b
    produit = a * b
    return somme, produit
    #return a+b, a*b

a = 2
a = a + 2
print(a)

####Exercices !!!

# Exercices 1:

# Créer une fonction prenant en paramètre l'année de naissance d'une personne 
# et lui retournant son l'âge qu'elle aura à sa fête en 2022

from __future__ import division
from doctest import OutputChecker
from termios import NL1
from tkinter import N


def age_donnee(annee_naissance):
    ANNEE_ACTUELLE = 2022
    age = ANNEE_ACTUELLE - annee_naissance
    return age
print(age_donnee(1980))

# Exercices 2:

# Créer une fonction prenant 2 nombres en paramètre et retournant leur addition et soustraction.
## Bien de pacter les informations (deux dièses = mes commentaires)
def somme_soustraction(nombre_1, nombre_2):
    somme = nombre_1 + nombre_2
    soustraction = nombre_1 - nombre_2 
    return somme, soustraction
print(somme_soustraction(2,3))

def somme_soustraction(nombre_1, nombre_2):
    somme  = nombre_1 + nombre_2
    soustraction = nombre_1 - nombre_2
    print(somme, soustraction)
    return somme, soustraction
somme_soustraction(2, 3)

def exemple():
    phrase = 'test'
    phrase.replace

    # Exercices 3:

# Créer une fonction prenant 1 ou 2 nombres et effectuer l'addition de leur carré. 
# Si un seul nombre est passé en paramètre, assumez que la valeur par défaut est 1. (donc celle qui est la plus à droite)

def somme_carres(nombre_1, valeur_2 = 1):
    carres_1, carres_2 = nombre_1**2, valeur_2**2
    somme = carres_1 + carres_2
    return somme

def somme_carres_2 (nombre_1, nombre_2 = 1):
             return nombre_1 ** 2 + nombre_2 ** 2

def somme_carres_3(nombre_1, nombre_2 = 1):
    def carre(nombre):
        return nombre * nombre
    somme = carre(nombre_1) + carre(nombre_2)
    return somme

# Exercice 4:
# Créer une fonction prenant trois nombres et retournant la moyenne de leur carré + 1.
# Ensuite, ecrire une nouvelle fonction pour retourner la moyenne de leur cube + 2.
# Finalement retournant la moyenne de la fonction suivante: x^x + x + 3, pour les 3 nombres.

def moyenne_carres (nombre_1, nombre_2, nombre_3):
    moyenne = (nombre_1 **2 + nombre_2 **2 + nombre_3 **2) / 3
    return moyenne + 1

def moy_carres(n1, n2, n3):
    def carre(n):
        return n**2
    return (carre(n1) + carre(n2) + carre(n3))/3 + 1

def moy_cube(n1, n2, n3):
    def cube(n):
        return n**3
    return (cube(n1) + cube(n2) + cube(n3))/3 + 2

def puissance(n1, n2, n3 ):
    def operation(n):
        return n^n + n + 3
    return (operation(n1) + operation(n2) + operation(n3)) / 3

def resultats(n1, n2, n3):
    def carre(n):
        return n ** 2
    def cube(n):
        return n ** 3
    def fct(n):
        return n ** n + n + 3
    def moy(n1, n2, n3):
        return (n1 + n2 + n3) / 3
    moy_carre = moy(carre(n1), carre(n2), carre(n3)) + 1
    moy_cube = moy(cube(n1), cube(n2), cube(n3)) + 2
    moy_fct = moy(fct(n1), fct(n2), fct(n3))
    return moy_carre, moy_cube, moy_fct 

# print(age_donnee(1980))
# print(somme_soustraction(2,3))
# print(somme_carres(1))

if __name__ == '__main__':
    res = resultats(1, 2, 3)
    print(res)

#Exercice 5:
#Créer une fonction prenant 4 paramètres et retournant la somme des deux premiers multipliés par le 3ième et divisé par le 4ème.
#Moi
def fonction(par_1, par_2, par_3, par_4):
    somme = par_1 + par_2
    multiplication = somme * par_3
    division = multiplication / par_4
    return somme, multiplication, division 
#Réponse
def exercice_5(n1, n2, n3, n4):
    return (n1 + n2) * n3 / n4

#Exercice 6:
#Créer une fonction qui calcule la moyenne de 4 paramètre et qui retourne aussi la somme de ces 4 paramètres.
###N1,N2,N3,N4 BONNE VARIABLE QUAND ON NE CONNAIT PAS LES VARIABLES
#moi
def fonction (par_1, par_2, par_3, par_4):
    moyen = (par_1 + par_2 + par_3 + par_4) / 4
    somme = par_1 + par_2 + par_3 + par_4
    return somme, moyen
#réponse
def moyenne_somme(n1, n2, n3, n4):
    somme = n1 + n2 + n3 + n4
    moyenne = somme / 4
    return somme, moyenne
resultat = moyenne_somme(1,2,3,4)
somme, moyenne = moyenne_somme(1,2,3,4)
print(somme, moyenne)
print(resultat)
print(moyenne_somme(1, 2, 3, 4))
    
#Exercice 7:
#Créer une fonction qui permet de calculer la fonction suivante: (x + y) / z.
#Essayer avec z = 0.
#moi
def fonction(nb1, nb2, nb3 = 0):
    calcul = (nb1 + nb2) / nb3   
    return calcul
print(fonction(1,2))
#réponse
def fonction_r(x, y, z):
    return (x + y) / z
print(f"{fonction_r(1, 3, 0)}")

def fonction_r(x, y, z):
    if z == 0:
        return
    elif z == 1:
        return x + y
    #return (x + y) / z
print(f"{fonction_r(1, 3, 0)}")

def fonction_r(x, y, z):
    if z == 0:
        return 
    elif z == 1:
        return x + y
#or
    else:
        return (x + y) / z
print(f"{fonction_r(1, 3, 0)}")

#Exercice 8:
#Créer une fonction prenant un seul paramètre retournant le modulo de deux nombres(a modulo b).
#me
def par_modulo(nb1, nb2):
    def modulo(nb):
        return nb % nb
    resultat_1 = modulo(nb1, nb2)
#you
def modulo(tuple_deux_nombres):
    nombre_1, nombre_2 = tuple_deux_nombres
    return nombre_1 % nombre_2

def modulo(nombres):
    
    nombre_1, nombre_2 = nombres
    return nombre_1 % nombre_2

nombres = 10, 3
print(modulo(nombres))

#ma_strucutre = (1992, nom)
#def ma_fonction(mes_infos)`:
#    annee, nom = mes_infos
#    print(annnee, nom)
#    print(mes_infos[0], mes_infos[1]) à éviter
#ma_fonction(ma_structure)
   
#Exercice 9: (IF à apprendre)
#Créer une fonction permettant de faire la puissance d'un nombre pour ensuite en faire la division. Votre fonction doit prendre de 1 à 3 paramètres, le premier paramètre étant la base, le deuxième paramètre étant l'exposant et le troisième paramètre étant la division. Si aucun exposant n'est donné, faites le carré. Si aucun diviseur n'est donné, n'effectuez pas de division.

def fonction_x(base, exposant=2, diviseur=1):
    return base ** exposant / diviseur
print(fonction_x(2))
print(fonction_x(2,4))    
print(fonction_x(3,4,6)) 