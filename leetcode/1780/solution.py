class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Determines if a given integer can be represented as the sum of distinct powers of three.
        
        :param n: Integer to be checked
        :return: True if n can be represented as the sum of distinct powers of three, False otherwise
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkPowersOfThree(12))  # Output: True
    print(sol.checkPowersOfThree(91))  # Output: True
    print(sol.checkPowersOfThree(21))  # Output: False