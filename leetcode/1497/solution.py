from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Compute remainders when each element is divided by k
        remainders = [a % k for a in arr]
        
        # Count occurrences of each remainder
        remainder_count = Counter(remainders)
        
        # Check pairs of remainders (i, k-i)
        for i in range(k):
            if i == 0:
                # For remainder 0, count must be even
                if remainder_count[i] % 2 != 0:
                    return False
            else:
                # Remainder i and k-i must have the same count
                if remainder_count[i] != remainder_count[k - i]:
                    return False
        
        return True

# Test cases
print(Solution().canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))  # Output: true
print(Solution().canArrange([1, 2, 3, 4, 5, 6], 7))              # Output: true
print(Solution().canArrange([1, 2, 3, 4, 5, 6], 10))             # Output: false