class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)
        
        # Generate candidate palindromes
        candidates = {10**length + 1, 10**(length - 1) - 1}
        half = int(n[: (length + 1) // 2])
        for x in range(half - 1, half + 2):
            y = x if length % 2 == 0 else x // 10
            candidates.add(int(str(y) + str(y)[::-1]))
        
        # Remove the original number from candidates
        candidates.discard(num)
        
        # Find the closest palindrome
        min_diff, closest = float('inf'), None
        for candidate in candidates:
            diff = abs(candidate - num)
            if diff < min_diff or (diff == min_diff and candidate < closest):
                min_diff, closest = diff, candidate
        
        return str(closest)