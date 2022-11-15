####Géo 1

# Vous travaillez sur un système de géolocation s'intitulant à la recherche du pôle Nord utilisant des coordonnées 
# sous la forme degrés minutes secondes (DMS).

# Pour faciliter l'utilisation du système, on vous demande de créer un court 
# programme permettant de convertir ces données sous la forme de degrés décimaux (DD).

# De plus, considérant que le but de l'application est d'indiquer la distance des usagers 
# du pôle Nord magnétique en plus d'indiquer leur position, on vous demande d'ajouter à votre programme 
# une fonction permettant de calculer cette distance.

# Versionner votre travail avec GitHub desktop et publié le sur votre profil GitHub Web une fois terminé.

from multiprocessing.reduction import DupFd
from turtle import fd

#import math

def dms_to_dd(dms):
    degres, minutes, secondes = dms
    return degres + minutes/60 + secondes/3600

#Variable qui ne change pas dans la fonction = écrire en majuscule

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