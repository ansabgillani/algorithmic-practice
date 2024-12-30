class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)

        def dfs(n):
            if n > high:
                return 0
            if dp[n]:
                return dp[n]
            dp[n] = (dfs(n + zero) + dfs(n + one)) % 1000000007
            return dp[n]

        total_good_strings = sum(dfs(i) for i in range(low, high + 1))
        return total_good_strings % 1000000007