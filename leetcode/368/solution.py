from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Sort the numbers to facilitate the subset construction
        nums.sort()

        # Initialize the dp array where dp[i] is the size of the largest divisible subset ending with nums[i]
        dp = [1] * len(nums)
        # prev array to reconstruct the actual subset
        prev = [-1] * len(nums)

        max_size, max_index = 1, 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_size:
                max_size, max_index = dp[i], i

        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        return result[::-1]