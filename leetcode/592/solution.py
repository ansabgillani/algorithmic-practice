from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        Given a string representing an expression of fraction addition and subtraction,
        return the calculation result in string format as an irreducible fraction.
        
        :param expression: String representing the fraction expression
        :return: String representing the result fraction in the form 'numerator/denominator'
        """
        # Split the expression by '+' and '-' to handle multiple fractions
        parts = expression.replace('-', '+-').split('+')
        
        # Sum up all fractions using Python's built-in Fraction class for automatic reduction
        result = sum(Fraction(part) for part in parts if part)
        
        # Convert the result back to a string in the required format
        return str(result)

# Example usage:
solution = Solution()
print(solution.fractionAddition("-1/2+1/2"))  # Output: "0/1"
print(solution.fractionAddition("-1/2+1/2+1/3"))  # Output: "1/3"
print(solution.fractionAddition("1/3-1/2"))  # Output: "-1/6"