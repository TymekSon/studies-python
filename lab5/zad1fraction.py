class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self, other):
        if type(other) == type(self):
            return Fraction(other.numerator*self.numerator, other.denominator*self.denominator)
        if type(other) == int or type(other) == float:
            return Fraction(other*self.numerator, self.denominator)

    def __add__(self, other):
        if type(other) == type(self):
            return Fraction(other.numerator*self.denominator+self.numerator*other.denominator, other.denominator*self.denominator)
        if type(other) == int or type(other) == float:
            return Fraction(self.numerator+other*self.denominator, self.denominator)

    def __sub__(self, other):
        if type(other) == type(self):
            return Fraction(other.numerator*self.denominator-self.numerator*other.denominator, other.denominator*self.denominator)
        if type(other) == int or type(other) == float:
            return Fraction(self.numerator-other*self.denominator, self.denominator)

    def __truediv__(self, other):
        if type(other) == type(self):
            return Fraction(other.denominator*self.numerator, other.numerator*self.denominator)
        if type(other) == int or type(other) == float:
            return Fraction(self.numerator, self.denominator*other)

    def __str__( self ):
        return str(self.numerator ) + "/" + str (self .denominator)


newFraction = Fraction(2,3)
newFraction2 = Fraction(3,5)
print(newFraction*newFraction2)
print(newFraction*7)

print(newFraction/newFraction2)
print(newFraction2/2)

print(newFraction+newFraction2)
print(newFraction2+4)

print(newFraction-newFraction2)
print(newFraction2-6)