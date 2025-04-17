from collections import defaultdict

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        # Dictionary to store indices of each number
        num_indices = defaultdict(list)
        
        # Populate the dictionary with indices
        for i, num in enumerate(nums):
            num_indices[num].append(i)
        
        # Count pairs
        count = 0
        for indices in num_indices.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        
        return count