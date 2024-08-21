class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j] + 1
                if s[i] == s[j]:
                    dp[i][j] -= 1

                for k in range(i + 1, j + 1):
                    dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k][j])

        return dp[0][n - 1]

# Example usage:
# sol = Solution()
# print(sol.strangePrinter("aaabbb"))  # Output: 2
# print(sol.strangePrinter("aba"))     # Output: 2