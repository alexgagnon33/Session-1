

nom_fichier = input("Écrivez le nom du fichier: ")
fichier = open(nom_fichier, "w")



nombres = []



while True:
    n = float(input("Entrez un nombre positif puis un nombre négatif pour break la liste): "))
    if n < 0:
        break
    nombres.append(n)



nombres.sort()



for i in range(len(nombres)):
    max_index = i
    for j in range(i + 1, len(nombres)):
        if nombres[j] > nombres[max_index]:
            max_index = j
    nombres[i], nombres[max_index] = nombres[max_index], nombres[i]

print(nombres)



for i in range(len(nombres)):
    min_index = i
    for j in range(i + 1, len(nombres)):
        if nombres[j] < nombres[min_index]:
            min_index = j
    nombres[i], nombres[min_index] = nombres[min_index], nombres[i]

print(nombres)



minimum1 = nombres[0]
for i in nombres:
    if i < minimum1:
        minimum1 = i
print(minimum1)



maximum1 = nombres[0]
for i in nombres:
    if i > maximum1:
        maximum1 = i
print(maximum1)

nombres_intégré = nombres

def moyenne(nombres_intégré):
    total = 0
    for num in nombres_intégré:
        total += num
    return total/len(nombres_intégré)

result_moyenne = moyenne(nombres_intégré)
print("Voici la moyenne : " , result_moyenne)

def mediane(nombres_intégré):
    if len(nombres_intégré) % 2 == 0:
        middle = len(nombres_intégré) // 2
        median = (nombres_intégré[middle - 1] + nombres_intégré[middle]) / 2
    else:
        middle = len(nombres_intégré) // 2
        median = nombres_intégré[middle]
    return median

resultat_mediane = mediane(nombres_intégré)
print("Voici la moyenne : " , resultat_mediane)

def mode(nombres_intégré):
    counts = {}
    for num in nombres_intégré:
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

result_mode = mode(nombres_intégré)
print("Voici la moyenne : " , result_mode)


