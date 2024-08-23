class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a: int, b: int) -> int:  # Greatest common divisor function
            while b:
                a, b = b, a % b
            return abs(a)
        
        def simplify(numerator: int, denominator: int) -> tuple:  # Simplify the fraction to irreducible form
            div = gcd(numerator, denominator)
            return numerator // div, denominator // div
        
        num = 0
        den = 1
        i = 0
        while i < len(expression):
            sign = 1 if expression[i] != '-' else -1  # Determine the sign of the current fraction
            i += 1 if expression[i] == '+' or expression[i] == '-' else 0  # Move past the sign character
            
            numer = ''
            while i < len(expression) and expression[i].isdigit():
                numer += expression[i]
                i += 1
            
            denom = ''
            while i < len(expression) and not expression[i].isdigit() and expression[i] != '/':
                i += 1
            while i < len(expression) and expression[i].isdigit():
                denom += expression[i]
                i += 1
        
            numer, denom = int(numer), int(denom)
        
            num = num * denom + sign * numer * den
            den *= denom
    
        return '{}/{}'.format(*simplify(num, den))