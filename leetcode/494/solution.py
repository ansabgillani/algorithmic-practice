class Solution:
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        
        n = len(nums)
        dp = [[0 for _ in range(total_sum + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(total_sum + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][abs(target)]