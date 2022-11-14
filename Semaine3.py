#EXERCICE 1
##RETURN EST LA DERNIÈRE *LIGNE D'UN CODE*, METTRE IF AVANT LE RETURN
#pas écrire fonction dans la définition et ne pas écrire carré, mais valeur dans le nom de la variable

from socket import J1939_MAX_UNICAST_ADDR
from statistics import NormalDist


def fonction_exercice1(carée):
    carrée = int(input('entrer un chiffre à mettre au carrée : '))
    if carrée > 0:
       return carrée ** 2, carrée ** 0,5
    else:
        return carrée ** 2
    
#meilleur
def calcul_carre():
    carre = int(input("Entrer un nombre : "))
    if carre > 0 :
        return carre * carre, carre ** 0,5
    return carre * carre 

#meilleur, meilleur?
def calcul_carre2():
    valeur = int(input("Entrer un nombre entier a mettre au valeur et en racine : "))
    resultat = valeur ** 2
    if valeur > 0:
        resultat = valeur ** 2, valeur ** 0,5
    return resultat

#EXERCICE 2
def recupereinfoanimal():
    nom_animal = int(input("Entrer un nom d'animal: "))
    couleur_animal = int(input('Enter une couleur: '))
    lieu_prefere = input("Entrer un lieu: ")
    infos_animal = nom_animal, couleur_animal, lieu_prefere
    return infos_animal
#;gt >
def formatageinfosanimal():
    nom, couleur, lieu = recupererinfosanimal()
    return f" J'ai trouvé un {nom} de couleur {couleur} dans mon lieu préféré: {lieu} "#.format()

#2.1

def user_infos_animal():
    nom_animal = input("Entrer un nom d'animal: ")
    couleur_animal = input("Entrer une couleur: ")
    lieu_prefere = input("Entrer un lieu: ")
    infos_animal = nom_animal, couleur_animal, lieu_prefere
    return infos_animal

def formatage_infos_animal(infos):
    nom, couleur, lieu = infos
    return f" J'ai trouvé un {nom} de couleur {couleur} dans mon lieu préféré: {lieu} "#.format()
    
infos = user_infos_animal()
infos_f = formatage_infos_animal(infos)
print(infos_f)

print(formatage_infos_animal(user_infos_animal()))
print(formatageinfosanimal())

#EXERCICE 3
#jamais INT quand stream

def date_de_fête():

    #Faire deux inputs (1 pour le jour, 1 pour le mois)
    date = input("Entrer votre date de fête: ")
    #31 octobre
    #09/31
    #09 - 31
    #October 31st
    if date == "31 octobre":
        return "bonne fête"
    else :
        return "ce n'est pas ta fête aujourd'hui"

print(date_de_fête())
# PLUS PLUS
def fete():
    mois = int(input("Entrer votre mois de fête en nombre(avril=4): "))
    jour = int(input("Entrer votre jours de fête: "))

    jour_a = dt.datetime.today().day
    mois_a = dt.datetime.today().month

    
    if jour == jour_a and mois == mois_a:
        print("Bonne fête!")
    else:
        print("Ce n'est pas ta fête aujourd'hui! :(")

#Exercice 4
##Créez un programme demandant à un utilisateur d'entrer sa date de fête et retournez-lui sa saison de naissance s'il est né dans 
## l'hémisphère Nord. (Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)
##### Important de décrire les inputs pour mettre plus de clarté!!!!

#70%
def saison_de_fete_detector():
    jour_user = int(input('Entrer votre jour de naissance (ex: 15): '))
    mois_user = int(input('Entrer votre mois de naissance (ex: avril = 4 ou 04): '))
    if 1 <= jour_user <= 31 and 1 <= mois_user <= 2:
        print('Vous etes née en hiver ! ')
    elif 22 <= jour_user <= 31 and mois_user == 12 :
        print('Vous etes née en hiver ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 3:
        print('Vous etes née en hiver ! ')

    elif 22 <= jour_user <= 31 and mois_user == 3 :
        print('Vous etes née au printemps ! ')
    elif 1 <= jour_user <= 31 and 4 <= mois_user <= 5:
        print('Vous etes née au printemps ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 6:
        print('Vous etes née au printemps ! ')

    elif 22 <= jour_user <= 31 and mois_user ==  6:
        print('Vous etes née en été ! ')
    elif 1 <= jour_user <= 31 and 7 <= mois_user <= 8:
        print('Vous etes née en été ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 9:
        print('Vous etes née en été ! ')
    
    elif 22 <= jour_user <= 31 and mois_user == 9 :
        print('Vous etes née en automne ! ')
    elif 1 <= jour_user <= 31 and 10 <= mois_user <= 11 :
        print('Vous etes née en automne ! ')
    elif 1 <= jour_user <= 21 and  mois_user == 12 :
        print('Vous etes née en automne ! ')
        
    else :
        print('Erreur')

saison_de_fete_detector()







def date_de_fête():
    mois = int(input("Entrer votre mois de fête en nombre: "))
    jour = int(input("Entrer votre jours de fête: "))
    hémisphère = int(input("Entrer votre lieux de naissance: "))
input()
    jour_a = dt.datetime.today().day
    mois_a = dt.datetime.today().month
    
    hémisphère == 'Hémisphère Nord':
    print(mois)

    if mois == Janvier, Février, Mars
    print(Hiver)
    else jour > 20 alors Été

    if mois == Avril, Mai, Juin

    if mois == Juillet, Aout, Septembre

    if mois == octobre novembre décembre

#Exercice 5

#Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction permettant de vérifier que les nombres ne sont 
#pas les deux pairs ou impairs, et affichez la phrase suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de leur 
#division est égal à z. Vous ne devez qu'afficher 3 chiffres après le point.

def nombre_de_utilisateur():
    nb_pair = int(input('Entrer un nombre pair: '))
    nb_impair = int(input('Entrer un nombre impaire: '))
def modulo (nombre):
    nb_pair, nb_impair = nombre
    return nb_pair % nb_impair
def division_nb (div_nb):
    nb_pair, nb_impair = div_nb
    return nb_pair/nb_impair
if nombre == 0
    print('Votre nombre impair est le x, votre nombre pair est le y et le résultat de leur division est égal à z.')
else:
    nombre == cut
    

#Exercice 6
#En partant de l'exercice du système de géolocation, modifiez votre code pour que les positions en DMS incluent la direction cardinale
#(N, S, E, W ou O) et retourne une position en DD pouvant être négative. Modifiez ensuite votre code pour permettre à un utilisateur 
#de manuellement rentrer sa position.

def dms_to_dd(dms):
    degres, minutes, secondes = dms
    return degres + minutes/60 + secondes/3600

def distance_2_point(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    
    return ((x2-x1) ** 2 + (y2-y1) ** 2) 
    #math.sqrt()
def distance_pole_nord(position):
    POLENORD_LAT = 86, 494
    POLENORD_LONG = 162,167
    POLE_NORD = POLENORD_LAT, POLENORD_LONG
    
    lat, long = position
    lat_dd = dms_to_dd(lat)
    long_dd = dms_to_dd(long)
    position_dd = lat_dd, long_dd

    return distance_2_point(position_dd, POLE_NORD)

longitude = 45, 30, 31.9968
latitude = 73, 33, 42.0048
position = longitude, latitude

dist = distance_pole_nord(position)
print(dist)

def coordonné_GPS(graphique)
    while longitude > 1 , latitude = 0: 
        print(E)
        while longitude < 1 , latitude = 0: 
        print(w)
        while longitude = 0 , latitude > 1: 
        print(N)
        while longitude = 0 , latitude < 1: 
        print(S)