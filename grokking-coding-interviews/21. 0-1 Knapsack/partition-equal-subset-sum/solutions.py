class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # If the total sum is odd, it's not possible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        # Target sum for each subset
        target = total_sum // 2
        
        # Initialize a DP array where dp[i] will be True if a subset with sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # A subset with sum 0 is always possible: the empty subset
        
        # Iterate through each number in nums
        for num in nums:
            # Update the DP array from right to left to avoid using the same number multiple times
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]

# Test cases
solution = Solution()
print(solution.canPartition([1, 5, 11, 5]))  # True
print(solution.canPartition([1, 2, 3, 5]))   # False