from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        Returns the number of non-empty beautiful subsets of the array nums.
        
        A subset is beautiful if it does not contain two integers with an absolute difference equal to k.
        
        :param nums: List of positive integers
        :param k: Positive integer
        :return: Number of non-empty beautiful subsets
        """
        def backtrack(start, current):
            if start == len(nums):
                return 1 if current else 0
            count = backtrack(start + 1, current)
            if current and abs(current[-1] - nums[start]) != k:
                count += backtrack(start + 1, current + [nums[start]])
            return count
        
        return backtrack(0, [])

# Example usage:
sol = Solution()
print(sol.beautifulSubsets([2, 4, 6], 2))  # Output: 4
print(sol.beautifulSubsets([1], 1))      # Output: 1