class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # If the target is not achievable return 0
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        subset_sum = (total_sum + target) // 2
        n = len(nums)
        
        # Create a DP array with (n+1)x(subset_sum+1) dimensions initialized to 0
        dp = [[0] * (subset_sum + 1) for _ in range(n + 1)]
        
        # Base case: There's always one way to achieve sum 0 (with an empty subset)
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(subset_sum + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        
        return dp[n][subset_sum]

# Example usage:
sol = Solution()
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
print(sol.findTargetSumWays([1], 1))  # Output: 1