class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        
        # Precompute factorials and their modular inverses up to n
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
            inv_fact[i] = pow(fact[i], MOD - 2, MOD)

        # Function to compute binomial coefficient C(n, k) % MOD
        def comb(n, k):
            if k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        # Function to find the number of ways to form an ideal array starting with a given value
        def count_ways(start):
            total = 1
            while start <= maxValue:
                exponent = 0
                num = start
                while num > 0 and num % start == 0:
                    num //= start
                    exponent += 1
                total = total * comb(n + exponent - 1, exponent) % MOD
                start *= start
            return total

        # Sum up the number of ideal arrays starting with each possible value
        result = 0
        for start in range(1, maxValue + 1):
            result = (result + count_ways(start)) % MOD

        return result