class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n):
            primes = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n + 1, p):
                        primes[i] = False
                p += 1
            return [p for p in range(2, n) if primes[p]]
        
        # Generate all prime numbers up to right
        primes = sieve_of_eratosthenes(right)
        
        # Filter primes that are within the given range
        filtered_primes = [p for p in primes if p >= left]
        
        # Handle cases with less than 2 primes
        if len(filtered_primes) < 2:
            return [-1, -1]
        
        # Find the two closest prime numbers
        min_diff = float('inf')
        result = []
        for i in range(1, len(filtered_primes)):
            diff = filtered_primes[i] - filtered_primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [filtered_primes[i - 1], filtered_primes[i]]
        
        return result