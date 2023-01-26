#Partie 1
def calculatrice_etape1():

    Fraction1Num = int(input("Entrer le numérateur de la première fraction: "))
    Fraction1Dén = int(input("Entrer le dénominateur de la première fraction: "))
    Fraction2Num = int(input("Entrer le numérateur de la deuxième fraction: "))
    Fraction2Dén = int(input("Entrer le dénominateur de la deuxième fraction: "))

    Num_Addition = (Fraction1Num * Fraction2Dén) + (Fraction1Dén * Fraction2Num)
    Dén_Addition = (Fraction1Dén * Fraction2Dén)

    Num_Soustraction = (Fraction1Num * Fraction2Dén) - (Fraction1Dén * Fraction2Num)
    Dén_Soustraction = (Fraction1Dén * Fraction2Dén)

    Num_Multiplication = (Fraction1Num * Fraction2Num) 
    Dén_Multiplication = (Fraction1Dén * Fraction2Dén)

    Num_Division = (Fraction1Num * Fraction2Dén) 
    Dén_Division = (Fraction1Dén * Fraction2Num)
    
    print("Addition: ", Num_Addition, "/", Dén_Addition)
    print("Soustraction: ", Num_Soustraction, "/", Dén_Soustraction)
    print("Multiplication: ", Num_Multiplication, "/", Dén_Multiplication)
    print("Division: ", Num_Division, "/", Dén_Division)


#Partie 2
def addition(fraction1, fraction2):
    a, b = fraction1
    c, d = fraction2
    numerateur = (a * d) + (b * c)
    denominateur = b * d
    return (numerateur, denominateur)

def soustraction(fraction1, fraction2):
    a, b = fraction1
    c, d = fraction2
    numerateur = (a * d) - (b * c)
    denominateur = b * d
    return (numerateur, denominateur)

def multiplication(fraction1, fraction2):
    a, b = fraction1
    c, d = fraction2
    numerateur = a * c
    denominateur = b * d
    return (numerateur, denominateur)

def division(fraction1, fraction2):
    a, b = fraction1
    c, d = fraction2
    numerateur = a * d
    denominateur = b * c
    return (numerateur, denominateur)

#Partie3
