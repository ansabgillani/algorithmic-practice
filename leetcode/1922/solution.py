class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # There are 5 choices (0, 2, 4, 6, 8) for even indices and 4 choices (2, 3, 5, 7) for odd indices
        even_count = n // 2 + n % 2
        odd_count = n // 2
        
        # Calculate the number of good digit strings using modular exponentiation
        result = pow(5, even_count, MOD) * pow(4, odd_count, MOD)
        
        return result % MOD