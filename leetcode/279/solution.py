class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize a list to store the minimum number of squares needed for each value up to n
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Iterate through each number from 1 to n
        for i in range(1, n + 1):
            j = 1
            # Check all perfect squares less than or equal to i
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]