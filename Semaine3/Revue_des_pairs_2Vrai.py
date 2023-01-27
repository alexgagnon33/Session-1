def calcul_imc(taille, poids):
    imc = poids / (taille ** 2)
    if imc < 18.5:
        return "Sous-poids", imc
    elif 18.5 <= imc < 25:
        return "Poids normal", imc
    elif 25 <= imc < 30:
        return "Surpoids", imc
    else:
        return "Obésité", imc

taille = input("Entrez votre grandeur en mètres: ")
poids = input("Entrez votre poids en kg: ")

categorie, imc = calcul_imc(float(taille), float(poids))
print("Votre IMC est de {:.2f}. Vous êtes dans la catégorie: {}.".format(imc, categorie))