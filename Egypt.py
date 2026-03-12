import math

def egyptian_fraction(numerator, denominator):
    result = []

    while numerator != 0:
        # Find the ceiling of denominator / numerator
        unitDen = math.ceil(denominator / numerator)

        # add faction to linst
        result.append(unitDen)

        # subtract the fraction
        numerator = numerator * unitDen - denominator
        denominator = denominator * unitDen

        # simplify the fraction
        g = math.gcd(numerator, denominator)
        numerator //= g
        denominator //= g

    return result



num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

fractions = egyptian_fraction(num, den)

print("\nEgyptian Fraction Decomposition:")
for d in fractions:
    print(f"1/{d}")
