#créer un fichier/le nommer
#nb rdm dans le fichier seulement positif
#puis suivre les règles

def document_nb():
    nom_fichier = int(input('Écriver le nom du document'))
    nb_choisi = int(input('Écriver des nombres a inclure dans le document'))
    nb_croissant = sorted(nb_choisi) 
    nb_decroissant = nb_choisi.sort (Fasle=True)
    nb_max = max(nb_choisi)
    nb_min = min(nb_choisi)
    nb_moy = sum(nb_choisi)/len(nb_choisi)
    nb_med = dsdsds
    nb_mode = 
if nb_choisi >= 0:



def doc_nb():
    nom_fichier = int(input('Écriver le nom du document'))
    nb_choisi = int(input('Écriver des nombres a inclure dans le document'))
    document = {
    'nb_croissant' : nb_choisi.sort() 
    'nb_decroissant' : nb_choisi.sort (Fasle=True)
}






def doc_nb():
    nom_fichier = int(input('Écriver le nom du document'))
    nb_choisi = int(input('Écriver des nombres a inclure dans le document'))
    nb_croissant = nb_choisi.sort() 
    nb_decroissant = nb_choisi.sort (Fasle=True)
    nb_max = max(nb_choisi)
    nb_min = min(nb_choisi)
    nb_moy = sum(nb_choisi)/len(nb_choisi)
def median(l):
    half = len(l) // 2
    l.sort()
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]
if nb_choisi >= 0:
    with open('{nom_fichier}.txt', 'x') as f:
        f.write{nb_croissant}
else:
    print('Vos nombres choisi sont négatif')




def document():
    nb_document = int(input('Écriver les nombre que vous voulez écrire dans le document avec un espace'))
    print("\n")
    user_list = nb_document.split()
    print('list: ', user_list)
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])

#Donc doit définir et faire des boucles pour trouver tous les éléments de la liste
#puis return à la fin de la boucle

def plus_petit(données )

def ordre_croissant(données):
    triés = [données]
    while len (données) > 0:
    min = plus_petit(données)
    données.remove(min)
    données.append(min)

    for in 
    
"""
Exercice 5 Revue des pairs:
Offrir à l'utilisateur d'entrer un nom de fichier et un nombre illimité de nombres positifs, tant et aussi longtemps qu'il ne rentre 
pas un nombre négatif. Ajouter les nombres entrés par l'utilisateur à une liste en excluant le nombre négatif. Ensuite, écrire les résultats
suivants dans le fichier nommé par l'utilisateur:

La liste en ordre croissant
La liste en ordre décroissant
Le maximum
Le minimum
La moyenne de la liste
La médiane (la valeur à la position centrale si la longueur de la liste est impaire et la moyenne des deux valeurs centrales si paire)
Ex: 1, 2, 3, 5, 4. Médiane = 3.
Ex: 1, 2, 3, 4, 5, 6. Médiane = 3.5
Le mode (l'occurrence la plus fréquente s'il y a lieu. Si chaque entrée est unique, inscrire que le mode = none)
Ex: 1, 2, 2, 2, 3, 4, 3, 4. La mode = 2

Vous ne pouvez pas utiliser de module, vous devez donc vous-même implémenter l'algorithme pour trier une liste en ordre croissant, trier une 
liste en ordre décroissant, trouver le maximum, trouver le minimum, calculer la moyenne, trouver la médiane, et trouver le mode
(utilisez un dictionnaire pour chaque donnée en tant que clef, affectez 0 comme valeur initiale et incrémentez de 1 à chaque répétition).
"""