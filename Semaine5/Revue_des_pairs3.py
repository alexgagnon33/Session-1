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
print(minimum)

#Maximum
maximum = nombres[0]
for i in nombres:
    if i > maximum:
        maximum = i
print(maximum)

#Moyenne
def find_mean(Nombre_Math):
    total = 0
    for num in Nombre_Math:
        total += num
    return total/len(Nombre_Math)
Nombre_Math = nombres

#Médiane
def find_median(Nombre_Math):
    if len(Nombre_Math) % 2 == 0:
        middle = len(Nombre_Math) / 2
        median = (Nombre_Math[middle - 1] + Nombre_Math[middle]) / 2
    else:
        middle = len(Nombre_Math) // 2
        median = Nombre_Math[middle]
    return median

find_median(Nombre_Math)

#Mode
def find_mode(Nombre_Math):
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
