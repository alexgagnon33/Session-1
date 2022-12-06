"""
Laboratoire 3:

Vous devez implémenter un simple programme implémentant un jeu de cartes et quelques algorithmes de brasssage. Vous devez vous-même implémenter les algorithmes de brassage, vous ne pouvez pas utiliser de modules pour effectuer les brassages.

Étape 1:

Créer programmatiquement un jeu de 52 cartes régulières, excluant les jokers.

Le paquet initial doit être créé selon les paramètres suivant:

Les cartes doivent initialement être dans leur ordre croissant, soit de 1 à 13 ou A, 2, 3.., V, D, R  ou A, 2, 3 ..., J, Q, K ou toutes autres variations.

Les cartes doivent initialement être dans l'ordre suivant (choisissez la représentation qui vous convient):

Carreau     -> Trèfle -> Cœur  -> Pique.
Diamonds -> Clubs -> Hearts -> Spades.
      ♦         ->    ♣    ->     ♥     ->      ♠.
Indice:

Vous ne devez pas manuellement initialiser votre paquet, vous devez implémenter un algorithme créant le jeu de cartes pour vous. Sinon, vous auriez 52 cartes à configurer à la main.
Étape 2:
Offrir un menu à l'utilisateur avec les options suivantes tant et aussi longtemps que l'utilisateur ne choisi pas l'option 4, cette dernière permet de sortir de l'exécution du programme:

Afficher l'état du jeu de carte
Effectuer un brassage inter-coupé
Effectuer un brassage par paquets
Sauvegarder l'état final dans un fichier
Indice:

S'assurer que chaque option exécute uniquement ce que l'option décrit. (ex: option 2 ne devrait que brasser les cartes, sans en afficher l'état et sans l'écrire dans un fichier.)
L'option 4 devrait terminer l'exécution de votre programme après la sauvegarde. Sinon, le menu devrait être offert après chaque brassage ou affichage de l'état du jeu de carte.
Par conséquent, l'utilisateur devrait pouvoir effectuer plusieurs brassages de suite en affichant le résultat seulement lorsque l'option 1 est choisie.
Étape 3 (afficher l'état du jeu de carte):

Vous devez afficher l'état du jeu de carte à la console sur 4 lignes. Donc, 13 cartes par lignes.



Étape 4 (effectuer une brassage inter-coupé):

Vous devez changer la position de vos cartes de la manière suivante:

Subdivisez votre jeu de cartes en deux paquet égaux (26 cartes par paquet).
Placer les cartes en suivant l'ordre suivant:
[Paquet1-Carte1, Paquet2-Carte1, Paquet1-Carte2, Paquet2-Carte2, ...]
Indice:

Pour les visuels, vous devez implémenter un algorithme brassant vos cartes comme dans ce gif: https://64.media.tumblr.com/14f6c90e564e85f53b90c37f49dc52f4/tumblr_mhagrkuZwc1rowobho1_400.gifv

Étape 5 (effectuer un brassage par paquets):

Vous devez changer la position de vos cartes de la manière suivante:

Subdivisez votre jeu de cartes en 13 paquets égaux (paquets de 4)
Réorganisez vos paquets dans l'ordre suivant:
P7, P1, P3, P13, P2, P4, P11, P6, P8, P5, P12, P10, P9
Pour les visuels, vous devez implémenter un cas particulier de ce type de brassage (en respectant l'ordre ci-haut): https://shuffletech.com/wp-content/uploads/2020/05/Overhand-Shuffle.gif

Étape 6 (Sauvegarde de l'état final):

Vous devez sauvegarder l'état final de votre jeu de carte dans le fichier cards.txt dans un format facilement lisible. Ensuite, vous devez sortir de votre menu/programme.
"""
def initialisation():
    
    symbols = ["A", "J", "Q", "R"]
    temp_1 = symbols[:1]
    temp_2 = [str(i) for i in range(2,11)]
    temp_3 = symbols[1:]

    # temp_4 = []
    # for i in range(2,11):
    #     temp_4.append(str(i))

    SYMBOLS = tuple(temp_1 + temp_2 + temp_3)
    SUITS = ("♦", "♣", "♥", "♠")

    paquet = []
    for suit in SUITS:
        for symbol in SYMBOLS:
            paquet.append(f"{symbol}{suit}")

    return paquet


def afficher(paquet : list[str]):
    offset = len(paquet)//4
    #0..12    #12%13 = 12
    #13..25   #25%13 = 12
    #26..38   #38%13 = 12
    #39..52   #52%13 = 12
    for i, carte in enumerate(paquet):
        print(f"{carte:<4}", end="")
        if i % offset == offset - 1:
            print()
    """
    #0..13    #12%13 = 12
    #13..26   #25%13 = 12
    #26..39   #38%13 = 12
    #39..52   #52%13 = 12
    #13 + 13*i = 13(1 + i)

    sous_paquets = []
    
    for i in range(4):
        sous_paquets.append(paquet[ i * offset : (i+1) * offset ])
    
    for sous_paquet in sous_paquets:
        for carte in sous_paquet:
            print(f"{carte:<4}", end="")
        print()
    """

def inter_coupe(paquet : list[str]):
    # 20 // 13= 1
    # 20 % 13 = 7
    # 20 division entiere de 13 = 1R7

    middle = len(paquet)//2
    sous_paquet_1 = paquet[:middle]
    sous_paquet_2 = paquet[middle:]
    paquet_brasse = []

    for carte1, carte2 in zip(sous_paquet_1, sous_paquet_2):    
        paquet_brasse.append(carte1)
        paquet_brasse.append(carte2)
    
    return paquet_brasse

def par_paquet(paquet : list[str]):
    #0..4      i = 0   #[ i*taille : (i+1)*taille]
    #4..8      i = 1
    #8..12     i = 2
    #12..16    i = 3
    #16..20    i = 4
    #P7, P1, P3, P13, P2, P4, P11, P6, P8, P5, P12, P10, P9
    NOMBRE_PAQUET = 13
    ORDRE = (6, 0, 2, 12, 1, 3, 10, 5, 7, 4, 11, 9, 8)
    TAILLE = len(paquet)//NOMBRE_PAQUET
    sous_paquets = []
    paquet_brasse = []

    for i in range(NOMBRE_PAQUET):
        sous_paquets.append(paquet[i*TAILLE:(i+1)*TAILLE])
    
    for indice in ORDRE:
        paquet_brasse.extend(sous_paquets[indice])
    
    return paquet_brasse

def sauvegarde(paquet : list[str]):
    with open("cards.txt", "w", encoding="UTF-8") as f:
        offset = len(paquet)//4
        for i, carte in enumerate(paquet):
            f.write(f"{carte:<4}")
            if i % offset == offset - 1:
                f.write("\n")

def menu():
    paquet = initialisation()
    sortie = False
    while not sortie:
        menu = {1: "Afficher le jeu de carte",
                2: "Brassage inter-coupé",
                3: "Brassage par paquet",
                4: "Sauvegarder l'état du jeu"}

        print()
        for num, opt in menu.items():
            print(f"{num} - {opt}")

        choix = int(input("Entrer votre choix: "))
        print() 

        if choix == 1:
            afficher(paquet)

        elif choix == 2:
            paquet = inter_coupe(paquet)

        elif choix == 3:
            paquet = par_paquet(paquet)

        elif choix == 4:
            sauvegarde(paquet)
            sortie = True
menu()
        
        


#Les étendues!!
#tuple : constante = MAJUSCULE 
#type hinting = def sauvegarde(paquet : list[str]):

ou en liste

from random import sample

class Card:


    def __init__(self, num, suite):
        self.num = num 
        self.suite = suite

    def __str__(self):

        #Formatte le chiffre/la lettre de la carte pour 
        #qu'elle prenne toujours 3 espaces et ajoutes la suite
        return f"{self.num:3}{self.suite}"


class Deck:

    def __init__(self):

        NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "  V", "  D", "  R"]
        SUITES = ["♦", "♣", "♥", "♠"]
        self.card_deck = []

        #Créé les 13 cartes de chaque suite en ordre
        for s in SUITES:
            for n in NUMBERS:
                self.card_deck.append(Card(n, s))

    #Permet de faire un brassage inter-coupé parfait
    def riffle_shuffle(self):
        #trouve le point milieu du paquet (Ex: 26 pour un paquet de 52 cartes)
        half_deck = len(self.card_deck)//2
        #Crée 2 sous paquets en coupant le paquet au milieu
        sub_decks = [self.card_deck[:half_deck], self.card_deck[half_deck:]]
        shuffled_deck = []

        #Inter-coupe les sous paquets
        #zip(list1, list2) = (list1[0], list2[0]), (list1[1], list2[1]), ...
        #zip s'arrête au dernier élément de la plus petite liste
        for c1, c2 in zip(sub_decks[0], sub_decks[1]):
            shuffled_deck.append(c1)
            shuffled_deck.append(c2)
        
        #Met à jours le paquet
        self.card_deck = shuffled_deck

    #Permet de faire un brassage par paquet de 4
    def overhand_shuffle(self):
        
        sub_decks = []
        shuffled_deck = []
        #Crée les nombres de 0 jusqu'au quart du paquet
        order = range(len(self.card_deck)//4)
        #Les placent dans un ordre aléatoire
        shuffled_order = sample(order, len(order))

        #Subdivise le paquet en sous-paquets de 4
        for i in range(0, len(self.card_deck), 4):
            sub_decks.append(self.card_deck[i:i+4])

        #Les placent dans l'ordre aléatoire généré plus haut
        for o in shuffled_order:
            shuffled_deck = shuffled_deck + sub_decks[o]
        
        #Mets à jour le paquet
        self.card_deck = shuffled_deck
    
    #Écrit un nouveau fichier deck.txt avec l'état du paquet de carte
    def save(self):
        f = open("deck.txt", "w", encoding="utf-8")
        #Utilise la fonction __str__(self) pour avoir le paquet en string
        f.write(str(self))
        
    #Formate le paquet sous un string
    def __str__(self):

        str_deck = ""
        #On utilise énumerate car on a besoin de l'index
        #pour faire un retour de ligne à chaque 13 cartes
        for i, card in enumerate(self.card_deck):
            #Utilise la méthode __str__(self) de la classe Card
            str_deck += str(card)
            if i%13 == 12:
                str_deck += " \n"
        return str_deck     
      

def menu():
    #Initialisation du paquet
    new_deck = Deck()
    exit = False
    while not exit:
        
        print("1. Afficher l'état du jeu de cartes")
        print("2. Faire un brassage inter-coupé")
        print("3. Faire un brassage par paquet aléatoire")
        print("4. Sauvegarder l'état du jeu")
        
        option = int(input("Choisir une option: "))
        
        if option == 1:
            print(new_deck)
        elif option == 2:
            new_deck.riffle_shuffle()
        elif option == 3:
            new_deck.overhand_shuffle()
        elif option == 4:
            new_deck.save()
            exit = True

menu()




        

