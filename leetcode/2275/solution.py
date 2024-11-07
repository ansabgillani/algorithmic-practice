class Solution:
    def largestCombination(self, candidates):
        max_comb = 0
        for i in range(32):
            count = sum((c >> i) & 1 for c in candidates)
            max_comb = max(max_comb, count)
        
        return max_comb

# Example usage:
solution = Solution()
print(solution.largestCombination([16,17,71,62,12,24,14]))  # Output: 4
print(solution.largestCombination([8,8]))  # Output: 2