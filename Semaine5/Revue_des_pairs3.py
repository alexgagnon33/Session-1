nom_fichier = input("Écrivez le nom du fichier: ")
fichier = open(nom_fichier, "w")

nombres = []

while True:
    n = float(input("Entrez un nombre positif (entrer un nombre négatif pour arrêter): "))
    if n < 0:
        break
    nombres.append(n)

nombres.sort()

#Décroissant
for i in range(len(nombres)):
    max_index = i
    for j in range(i + 1, len(nombres)):
        if nombres[j] > nombres[max_index]:
            max_index = j
    nombres[i], nombres[max_index] = nombres[max_index], nombres[i]

print(nombres)

#Croissant
for i in range(len(nombres)):
    min_index = i
    for j in range(i + 1, len(nombres)):
        if nombres[j] < nombres[min_index]:
            min_index = j
    nombres[i], nombres[min_index] = nombres[min_index], nombres[i]

print(nombres)

#Minimum
minimum = nombres[0]
for i in nombres:
    if i < minimum:
        minimum = i
print("Voici le minimum : ", (minimum))

#Maximum
maximum = nombres[0]
for i in nombres:
    if i > maximum:
        maximum = i
print("Voici le maximum : ", (maximum))

#Moyenne
def moyenne(Nombre_Math):
    total = 0
    for num in Nombre_Math:
        total += num
    return total/len(Nombre_Math)
Nombre_Math = nombres
print("Voici la moyenne : ", (moyenne))
#Médiane
def mediane(Nombre_Math):
    if len(Nombre_Math) % 2 == 0:
        middle = len(Nombre_Math) / 2
        median = (Nombre_Math[middle - 1] + Nombre_Math[middle]) / 2
    else:
        middle = len(Nombre_Math) // 2
        median = Nombre_Math[middle]
    return median

mediane(Nombre_Math)
print("Voici la mediane : ", (mediane))
#Mode
def mode(Nombre_Math):
    counts = {}
    for num in Nombre_Math:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = max(counts.values())
    if max_count == 1:
        return None
    else:
        mode = [k for k, v in counts.items() if v == max_count]
        return mode

print("Voici le mode : ", (mode))