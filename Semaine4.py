# Exercice 1:
# Créer une fonction prenant 4 paramètres et les retournant en ordre croissant en utilisant que des conditions(en n’utilisant pas de loops).

def triage(n1, n2, n3, n4):

    def triage_simplifie(n1, n2, n3, n4):
        if n1<n2 and n1<n3 and n1<n4:
            if n2<n3 and n2<n4 :
                if n3<n4:
                    return n1, n2, n3, n4
                elif n4 < n3 :
                    return n1, n2, n4, n3

            elif n3<n2 and n3<n4 :
                if n2<n4:
                    return n1, n3, n2, n4
                elif n4 < n2 :
                    return n1, n3, n4, n2

            elif n4<n2 and n4<n3 :
                if n3<n2:
                    return n1, n4, n3, n2
                elif n2 < n3 :
                    return n1, n4, n2, n3
        else:
            return None


    if triage_simplifie(n1, n2, n3, n4) is not None:
        return triage_simplifie(n1, n2, n3, n4)
    
    elif triage_simplifie(n2, n1, n3, n4) is not None:
        return triage_simplifie(n2, n1, n3, n4)

    elif triage_simplifie(n3, n2, n1, n4) is not None:
        return triage_simplifie(n3, n2, n1, n4)

    elif triage_simplifie(n4, n2, n3, n1) is not None:
        return triage_simplifie(n4, n2, n3, n1)
        
    else:
        return None

#1.1

def nombres_croissant(nb1, nb2, nb3, nb4) :

    def compare_swap(nombre1, nombre2) :
        if nombre2 <= nombre1 :
            return nombre2, nombre1
        else : 
            return nombre1, nombre2
    
    nb1, nb2 = compare_swap(nb1, nb2)
    nb1, nb3 = compare_swap(nb1, nb3)
    nb1, nb4 = compare_swap(nb1, nb4)
    nb2, nb3 = compare_swap(nb2, nb3)
    nb2, nb4 = compare_swap(nb2, nb4)
    nb3, nb4 = compare_swap(nb3, nb4)

    croissant_list = nb1, nb2, nb3, nb4
    return croissant_list

#1.2 

def max_4(a1, a2, a3, a4):
    if a1 > a2:
        a1, a2 = a2, a1
    if a2 > a3:
        a2, a3 = a3, a2
    if a3 > a4:
        a3, a4 = a4, a3
    return a1, a2, a3, a4

def max_3(a1, a2, a3): 
    if a1 > a2:
        a1, a2 = a2, a1
    if a2 > a3:
        a2, a3 = a3, a2
    return a1, a2, a3
     
def max_2(a1, a2) :
    if a1 > a2:
      a1, a2 = a2, a1
    return a1, a2

def triage(a1, a2, a3, a4):
    
    a1, a2, a3, a4 = max_4(a1, a2, a3, a4)
    a1, a2, a3 = max_3(a1, a2,a3)
    a1, a2 = max_2(a1,a2)
    print(f"{a1}, {a2}, {a3}, {a4}")

a1, a2, a3, a4 = 5, 7, 1, 6
triage(a1, a2, a3, a4)

# Exercice 2:

# Créer un programme prenant en paramètre les conditions météorologiques suivantes:

# L'état du ciel(Ensoleillé, nuageux ou éclaircies), les précipitations (aucune, pluie, neige ou verglas), la vitesse des vents en km/h et la température en C.

# Ensuite, affichez à l'écran un message d'alerte météorologique si les conditions suivantes sont respectées:

#     Il y a des précipitations et les vents sont supérieurs à 30 km/h
#     Il y a du verglas
#     Il fait soleil, mais les vents sont supérieurs à 70km/h ou les températures sont supérieures à 30C ou inférieures à -25C.
#     Il fait nuageux et les vents sont supérieurs à 50km/h.
#     Il fait nuageux et les vents sont supérieurs à 30km/h, mais la température est supérieure à 25C ou inférieure à -20C
#     Il neige et la température est inférieure à -25C.
#     Il fait ensoleillé, il n'y a pas de vent et la température est supérieure à 25C.

# Permettez à un utilisateur de rentrer les conditions météorologiques à l'aide d'un menu et assurez-vous qu'il soit impossible de rentrer des conditions météorologiques qui ne font pas de sens.

# !commencer par les menus (recueille les informations)

def cueillette_meteo():
    
    def menu():
        def input_ciel():
            print("Menu ciel: ")
            print("1 - Ensoleille")
            print("2 - Nuageux")
            print("3 - Eclaircies")
            user_ciel = int(input("SVP enter l'etat du ciel: "))
            if user_ciel == 1:
                return "Ensoleille"
            elif user_ciel == 2:
                return "Nuageux"
            elif user_ciel == 3:
                return "Eclaircies"

        def input_precip():
            print("Menu Precipitation: ")
            print("1 - Aucune")
            print("2 - Pluie")
            print("3 - Neige")
            print("4 - Verglas")
            user_ciel = int(input("SVP enter la precipitation: "))
            if user_ciel == 1:
                return "Aucune"
            elif user_ciel == 2:
                return "Pluie"
            elif user_ciel == 3:
                return "Neige"
            elif user_ciel == 4:
                return "Verglas"

        def vitesse_vent():
            print("Menu vitesse des vents: ")
            user_vent = int(input("SVP entrer la vitesse des vents en km/h (nombres entiers): "))
            return user_vent
        
        def input_temp():
            print("Menu Temperature: ")
            user_temp = int(input("SVP entrer la temperature en C (nombres entiers): "))
            return user_temp
        
        utilisateur_ciel = input_ciel()
        utilisateur_precip = input_precip()
        utilisateur_vent = vitesse_vent()
        utilisateur_temp = input_temp()
        return utilisateur_ciel, utilisateur_precip, utilisateur_vent, utilisateur_temp
    
    return menu()
    #print(f"Journée: {etat_ciel}  {precip}   {vit_vent}   {temp_c}")

# Ensuite, affichez à l'écran un message d'alerte météorologique si les conditions suivantes sont respectées:

#     x Il y a des précipitations et les vents sont supérieurs à 30 km/h
#     x Il y a du verglas
#     x Il fait soleil, mais les vents sont supérieurs à 70km/h ou les températures sont supérieures à 30C ou inférieures à -25C.
#     x Il fait nuageux et les vents sont supérieurs à 50km/h.
#     x Il fait nuageux et les vents sont supérieurs à 30km/h, mais la température est supérieure à 25C ou inférieure à -20C
#     x Il neige et la température est inférieure à -25C.
#     x Il fait ensoleillé, il n'y a pas de vent et la température est supérieure à 25C.

def alerte_meteo(etat_ciel, precip, vit_vent, temp):
    if vit_vent > 30:
        if precip != "Aucune":
            print("Alerte")
            return
            # return "Alerte"

    if precip == "Verglas":
        print("Alerte")
        return
        
    if etat_ciel == "Nuageux":
        if vit_vent > 50:
            print("Alerte")
            return
        elif vit_vent > 30:
            if temp < -20 and temp > 25:
                print("Alerte")
                return

    if etat_ciel == "Ensoleille":
        if vit_vent > 70:
            if temp < -25 or temp > 20:
                print("Alerte")
                return

        if vit_vent == 0:
            if temp > 25:
                print("Alerte")
                return

    if precip == "Neige":
        if temp < -25:
            print("Alerte")
            return
    



        
ciel, precip, vent, temp = cueillette_meteo()
alerte_meteo(ciel, precip, vent, temp)
#print(alerte_meteo(ciel, precip, vent, temp))



# Exercices similaires au laboratoire:

# Exercice 3:
# Écrire un programme offrant un menu à un utilisateur avec les 3 choix suivant et 
# lui affichant que la phrase sélectionnée une fois sélectionnée :
# 1. Bonjour
# 2. Au revoir
# 3. À plus tard

def afficher_phrase():
    print('Voice les phrases disponibles: ')
    print('1 - Bonjour  ')
    print('2 - Au revoir ')
    print('3 - À plus tard')
    choix_user = int(input('Choisir un phrase a recevoir (ex: 1 , 2  ou 3 ): '))
    if choix_user == 1:
        print('Bonjour')
    elif choix_user == 2:
        print('Au revoir')
    elif choix_user == 3:
        print('À plus tard')
    else:
        print('Erreur')

#afficher_phrase()  
#boucle, dictionnaire

def afficher_phrase_2():
    print('Voice les phrases disponibles: ')
    menu = {"1" : "Bonjour", "2" : "Au Revoir", "3" : "À plus tard"}
    
    for key, value in menu.items():
        print(f"{key} - {value}")

    choix_user = input('Choisir un phrase a recevoir (ex: 1 , 2  ou 3 ): ')
     
    if choix_user in menu:
        print(menu[choix_user])
    else:
        print("Je ne sais pas")

afficher_phrase_2()

#ou

def afficher_phrase_2():

    print('Voice les phrases disponibles: ')

    menu = {1 : "Bonjour", 2 : "Au Revoir", 3 : "À plus tard"}

    for key, value in menu.items():
        print(f"{key} - {value}")

    choix_user = int(input('Choisir un phrase a recevoir (ex: 1 , 2  ou 3 ): '))
     
    if choix_user in menu:
        print(menu[choix_user])
    else:
        print("Je ne sais pas")


## pas d'utilisateur, pas d'input 
  
# Exercice 4:
# Écrire un programme avec une fonction prenant 2 floats et retournant leur 
# addition soustraction et division. Les résultats des additions doivent avoir au plus 
# 1 chiffre après la virgule, la soustraction 2 chiffres après la virgule et la division 3 chiffres après la virgule.

def add_sub_div(reel_1, reel_2):

    def add(reel_1, reel_2):
        return "addition", f"{reel_1 + reel_2:.1f}"
    def sub(reel_1, reel_2):
        return "soustraction", f"{reel_1 - reel_2:.2f}"
    def div(reel_1, reel_2):
        return "division", f"{reel_1 / reel_2:.3f}"

    add_sub_div = add(reel_1, reel_2), sub(reel_1, reel_2), div(reel_1, reel_2)
    return add_sub_div
print(add_sub_div(8.4, 6.33))

#meilleur

def add_sub_div_2(reel_1, reel_2):

    def add(reel_1, reel_2):
        return reel_1 + reel_2
    def sub(reel_1, reel_2):
        return reel_1 - reel_2
    def div(reel_1, reel_2):
        return reel_1 / reel_2

    return f"Addition: {add(reel_1, reel_2):.1f} Soustraction: {sub(reel_1, reel_2):.2f} Div: {div(reel_1, reel_2):.3f}"
    
print(add_sub_div_2(8.4, 6.33))

#À NE PAS FAIRE
num1 = 6.987
num2 = 3.867
#À NE PAS FAIRE
def calcul():
    add = num1 + num2
    sous = num1 = num2
    div = num1 / num2
    print(f"addition: {add:.1f}, Soustraction: {sous:.2f}, Division: {div:.3f}")

calcul()

#MAIS

def calcul(num1, num2):
    add = num1 + num2
    sous = num1 = num2
    div = num1 / num2
    print(f"addition: {add:.1f}, Soustraction: {sous:.2f}, Division: {div:.3f}")
    
num1 = 6.987
num2 = 3.867

#print(calculatrice(3.5, 4.6))

# Exercice 5:
# Écrire un programme prenant l'année de naissance de l'utilisateur 
# et lui retournant sa génération. 
# Vous pouvez utiliser la source suivante: https://www.eurecia.com/blog/generations-x-y-z-sont-elles/

def generation():
    anne_naissance = int(input ("Quelle est votre année de naissance? ex. 1994: "))
    if 1946 <= anne_naissance < 1965:
        return "Vous etes un baby-boomer"
    elif 1965 <= anne_naissance < 1980:
        return "Vous faites partis de la generation X"
    elif 1980 <= anne_naissance < 2000:
        return "Vous faites partis des milleniaux"
    elif anne_naissance >= 2000:
        return "Vous faites partis de la generation Z"
    else:
        return "Desole je ne sais pas"
#print(generation())

# Exercice 6:
# Écrire un programme demandant un entier à un utilisateur 
# et lui retournant sa parité. Ex.: Le nombre «4» est pair.

def parite():
    entier_user = int(input("Entrer un entier: "))
    if entier_user % 2 == 0:
        return f"L'entier {entier_user} est pair."
    else:
        return f"L'entier {entier_user} est impair."

print(parite())

# Exercice 7:
# Écrire un programme demandant à l'utilisateur de rentrer un nombre entre 2 et 20, 
# vérifier si ce dernier est bel et bien entre 2 et 20, et indiquez-lui si son nombre 
# est un nombre premier (ayant aucun autre facteur entier que 1 et lui-même)
## PAS BESOIN DE RUTURN CAR CE N'EST PAS SPÉCIFIÉ DANS L'ÉNONCÉ

def est_premier():
    entier = int(input("Entrer un nombre entre 2 et 20: "))
    if 2 <= entier <= 20:
        if entier == 2 or entier == 3 or entier == 5 or entier == 7 or entier == 11: 
            print("Le nombre est entre 2 et 20 et il est premier")
        elif  entier == 13 or entier == 17 or entier == 19 :
            print("Le nombre est entre 2 et 20 et il est premier")
        else:
            print("Le nombre est entre 2 et 20 mais il n'est pas premier")

    else:
        print("Le nombre n'est pas entre 2 et 20")
        
#est_premier()

#OU

def premier_entre_2_20( n ):
    if (n % 2  == 0 and n!= 2) or n == 9 or n == 15:
        print (f"Le nombre {n} n'est pas premier")
    else:
        print (f"Le nombre {n} est premier")
    
def saisie_nombre():
    n = int(input("Entre un entier entre 2 et 20: "))
    if not 2 <= n <= 20:
        print("Valeur en dehors de 2 et 20 - programme s'arrete")
        return False, -1
    else:
        return True, n

def go():
    ok, n = saisie_nombre()
    if ok:
        premier_entre_2_20(n)

go()

#boucle

def premier():
    entier = int(input("Entrer un nombre entre 2 et 20: "))
    if 2 <= entier <= 20:
        PREMIER = [2, 3, 5, 7, 11, 13, 17, 19]
        if entier in PREMIER:
            print("Le nombre est premier")
    else:
        print("Le nombre n'est pas entre 2 et 20")

# Exercice 8:
# Écrire une fonction prenant deux nombres et vérifiant si le premier nombre est plus petit que le deuxième, 
# si ce n'est pas le cas, les retourner dans l'ordre inverse. Ex.: fonction(4, 3) retournerait 3 et, ensuite, 4.

def plus_petit(nb_1, nb_2):
    if nb_1 < nb_2:
        return nb_1, nb_2
    else:
        return nb_2, nb_1

print(plus_petit(4,3))