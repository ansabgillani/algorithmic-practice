class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Initialize a list to store the number of good strings of each length
        dp = [0] * (high + 1)
        
        MOD = 1_000_000_007
        
        # Fill the DP table from bottom up
        for length in range(high, -1, -1):
            if length + zero <= high:
                dp[length] += dp[length + zero]
            if length + one <= high:
                dp[length] += dp[length + one]
            dp[length] %= MOD
        
        # Sum up the number of good strings from length 'low' to 'high'
        return sum(dp[low:high+1]) % MOD