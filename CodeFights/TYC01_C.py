from fractions import Fraction

def fractionDivision(a, b):
    ans = Fraction(*a) / Fraction(*b)
    return [ans.numerator, ans.denominator]
