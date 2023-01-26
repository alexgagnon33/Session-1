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
    
calculatrice_etape1()

#Partie 2
def addition(fraction1, fraction2):
        a, b = fraction1
        c, d = fraction2
        Num = (a * d) + (b * c)
        Dén = b * d
        return (Num, Dén)

def soustraction(fraction1, fraction2):
        a, b = fraction1
        c, d = fraction2
        Num = (a * d) - (b * c)
        Dén = b * d
        return (Num, Dén)

def multiplication(fraction1, fraction2):
        a, b = fraction1
        c, d = fraction2
        Num = a * c
        Dén = b * d
        return (Num, Dén)

def division(fraction1, fraction2):
        a, b = fraction1
        c, d = fraction2
        Num = a * d
        Dén = b * c
        return (Num, Dén)

fraction1 = (1, 2)
fraction2 = (3, 4)

addition(fraction1, fraction2)
soustraction(fraction1, fraction2)
multiplication(fraction1, fraction2)
division(fraction1, fraction2)

#Partie3

def float(fraction):
    numerateur, denominateur = fraction
    return numerateur / denominateur

fraction1 = (1, 2)
fraction2 = (3, 4)
result = addition(fraction1, fraction2)
print(float(result))

float()