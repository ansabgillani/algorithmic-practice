class Solution:
    def beautifulSubsets(self, nums, k):
        def is_beautiful(subset):
            return all(abs(a - b) != k for a, b in combinations(subset, 2))

        count = sum(1 for subset in range(1, len(nums)+1) if is_beautiful(combinations(nums, subset)))
        
        return count