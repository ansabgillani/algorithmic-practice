class Solution:
    def canPartition(self, nums: List[int], target_sum: int) -> bool:
        """
        Determines if there is a subset of the given array whose sum equals the target sum.
        
        :param nums: List of non-negative integers
        :param target_sum: Target sum to find in any subset
        :return: True if such a subset exists, False otherwise
        """
        n = len(nums)
        dp = [False] * (target_sum + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target_sum]

# Test cases
solution = Solution()
print(solution.canPartition([3, 34, 4, 12, 5, 2], 9))  # Output: True
print(solution.canPartition([3, 34, 4, 12, 5, 2], 30))  # Output: False