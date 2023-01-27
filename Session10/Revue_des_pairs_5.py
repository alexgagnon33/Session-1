class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        numer = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denom = self.denominator * other.denominator
        return Fraction(numer, denom)

    def __sub__(self, other):
        numer = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denom = self.denominator * other.denominator
        return Fraction(numer, denom)
    
    def __eq__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator
        return first_num == second_num

    def __mul__(self, other):
        numer = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(numer, denom)

    def __truediv__(self, other):
        numer = self.numerator * other.denominator
        denom = self.denominator * other.numerator
        return Fraction(numer, denom)

    def __pow__(self, power):
        return (self.numerator/self.denominator) ** power

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Compare")
    print("4. Multiply")
    print("5. Divide")
    print("6. Raise to a power")
    choice = input("Enter choice (1/2/3/4/5/6):")

    if choice == '1':
        num1 = Fraction(int(input("Enter numerator for first fraction: ")), int(input("Enter denominator for first fraction: ")))
        num2 = Fraction(int(input("Enter numerator for second fraction: ")), int(input("Enter denominator for second fraction: ")))
        print(num1 + num2)
    elif choice == '2':
        num1 = Fraction(int(input("Enter numerator for first fraction: ")), int(input("Enter denominator for first fraction: ")))
        num2 = Fraction(int(input("Enter numerator for second fraction: ")), int(input("Enter denominator for second fraction: ")))
        print(num1 - num2)
    elif choice == '3':
        num1 = Fraction(int(input("Enter numerator for first fraction: ")), int(input("Enter denominator for first fraction: ")))
        num2 = Fraction(int(input("Enter numerator for second fraction: ")), int(input("Enter denominator for second fraction: ")))
        if num1 == num2:
            print("The fractions are equal")
        else:
            print("The fractions are not equal")
    elif choice == '4':
        num1 = Fraction(int(input("Enter numerator for first fraction: ")), int(input("Enter denominator for first fraction: ")))
        num2 = Fraction(int(input("Enter numerator for second fraction: ")), int(input("Enter denominator for second fraction: ")))
        print(num1 * num2)
    elif choice == '5':
        num1 = Fraction(int(input("Enter numerator for first fraction: ")), int(input("Enter denominator for first fraction: ")))
        num2 = Fraction(int(input("Enter numerator for second fraction: ")), int(input("Enter denominator for second fraction: ")))
        print(num1 / num2)
    elif choice == '6':
        num1 = Fraction(int(input("Enter numerator for fraction: ")), int(input("Enter denominator for fraction: ")))
        power = int(input("Enter power to raise the fraction to: "))
        print(num1 ** power)
    else:
        print("Invalid input")

menu()