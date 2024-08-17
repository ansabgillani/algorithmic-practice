class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [0] * n

        for r in range(m):
            max_left = 0
            for c1 in range(n):
                max_left = max(max_left - 1, dp[c1])
                dp[c1] = max(dp[c1], max_left + points[r][c1])

            max_right = 0
            for c2 in range(n-1, -1, -1):
                max_right = max(max_right - 1, dp[c2])
                dp[c2] = max(dp[c2], max_right + points[r][c2])
    
        return max(dp)