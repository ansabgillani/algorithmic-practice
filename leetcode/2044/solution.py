from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        Given an integer array `nums`, find the maximum possible bitwise OR of a subset of `nums` 
        and return the number of different non-empty subsets with the maximum bitwise OR.
        """
        total_max_or = 0
        count_max_or_subsets = 0
        
        # Calculate the total number of subsets
        n = len(nums)
        total_subsets = 1 << n
        
        for i in range(total_subsets):
            current_or = 0
            for j in range(n):
                if i & (1 << j):
                    current_or |= nums[j]
            
            if current_or == total_max_or:
                count_max_or_subsets += 1
            elif current_or > total_max_or:
                total_max_or = current_or
                count_max_or_subsets = 1
        
        return count_max_or_subsets

# Example usage:
sol = Solution()
print(sol.countMaxOrSubsets([3,1]))  # Output: 2
print(sol.countMaxOrSubsets([2,2,2]))  # Output: 7
print(sol.countMaxOrSubsets([3,2,1,5]))  # Output: 6