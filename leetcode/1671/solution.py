class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper function to find the length of Longest Increasing Subsequence (LIS) ending at index i
        def lis(i):
            dp = [1] * (i + 1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            return dp[i]
        
        # Helper function to find the length of Longest Decreasing Subsequence (LDS) starting at index i
        def lds(i):
            dp = [1] * (n - i)
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j - i] + 1)
            return dp[i]
        
        # Find the minimum removals to make the array a mountain array
        ans = float('inf')
        for i in range(1, n - 1):
            if lis(i) > 1 and lds(i) > 1:
                ans = min(ans, n - (lis(i) + lds(i) - 1))
        
        return ans