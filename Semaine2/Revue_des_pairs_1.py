"""­­
Créer une calculatrice pour fractions incluant les opérations suivantes: 

Addition (a/b + d/c)
Soustraction (a/b - d/c)
Multiplication (a/b * d/c)
Divisions (a/b / d/c)

Exercice 1, Partie 2:
Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).

Exercice 1, Partie 3:
Affichez vos résultats sous forme de fraction et sous forme d'un float.

Testez vos fonctions avec plusieurs fractions pour vous assurer du bon fonctionnement.
"""
def calculatrice_etape1():

    Fraction1Num = print(int(input("Entrer le numérateur de la première fraction: ")))
    Fraction1Dén = print(int(input("Entrer le dénominateur de la première fraction: ")))
    Fraction2Num = print(int(input("Entrer le numérateur de la deuxième fraction: ")))
    Fraction2Dén = print(int(input("Entrer le dénominateur de la deuxième fraction: ")))

    Addition = (Fraction1Num / Fraction1Dén) + (Fraction2Num / Fraction2Dén)
    Soustraction = (Fraction1Num / Fraction2Dén) - (Fraction2Num / Fraction2Dén)
    Multiplication = (Fraction1Num / Fraction2Dén) * (Fraction2Num / Fraction2Dén)
    Division = (Fraction1Num / Fraction2Dén) / (Fraction2Num / Fraction2Dén)
    print(Addition, Soustraction, Multiplication, Division)

calculatrice_etape1()

def calculatrice_etape2():

    from fractions import Fraction

    Fraction1Num = print(int(input("Entrer le numérateur de la première fraction: ")))
    Fraction1Dén = print(int(input("Entrer le dénominateur de la première fraction: ")))
    Fraction2Num = print(int(input("Entrer le numérateur de la deuxième fraction: ")))
    Fraction2Dén = print(int(input("Entrer le dénominateur de la deuxième fraction: ")))

    fct1 = Fraction({Fraction1Num} / {Fraction1Dén})
    fct2 = Fraction({Fraction2Num / Fraction2Dén})
    
    Addition = fct1 + fct2
    Soustraction = fct1 - fct2
    Multiplication = fct1 * fct2
    Division = fct1 / fct2 

    print(Addition, Soustraction, Multiplication, Division)

calculatrice_etape2

