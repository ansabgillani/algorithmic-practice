class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        Returns the maximum number of stones Alice can get when playing optimally.
        
        :param piles: A list of integers representing the piles of stones.
        :return: An integer representing the maximum number of stones Alice can get.
        """
        n = len(piles)
        prefix_sum = [0] * (n + 1)
        
        # Calculate prefix sums from right to left
        for i in range(n - 1, -1, -1):
            prefix_sum[i] = prefix_sum[i + 1] + piles[i]
            
        dp = [[0] * (n + 1) for _ in range(n)]
        
        # Fill the DP table
        for i in range(n):
            dp[i][i] = piles[i]
            for j in range(i - 1, -1, -1):
                for x in range(1, min((i - j + 1) // 2 + 1, 2)):
                    dp[j][i] = max(dp[j][i], prefix_sum[j] - dp[j + x][i])
                    
        return dp[0][n - 1]