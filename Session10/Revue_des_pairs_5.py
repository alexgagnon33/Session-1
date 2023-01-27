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

fraction1 = Fraction(1, 2)
fraction2 = Fraction(2, 3)
print(fraction1 + fraction2) # 3/6
print(fraction1 - fraction2) # -1/6
print(fraction1 == fraction2) # False
print(fraction1 * fraction2) # 2/6
print(fraction1 / fraction2) # 3/4
print(fraction1 ** 0.5) #0.7071067811865475
