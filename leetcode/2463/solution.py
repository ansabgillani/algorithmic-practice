class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort both arrays to facilitate the assignment of robots to factories
        robot.sort()
        factory.sort()
        
        # Create a 2D DP array where dp[i][j] represents the minimum distance to assign the first i robots to the first j factories
        n, m = len(robot), len(factory)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        # Fill the DP array
        for i in range(1, n + 1):
            for j in range(1, min(i + 1, m + 1)):
                for k in range(factory[j - 1][1] + 1):
                    if k > 0:
                        dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + sum(abs(robot[i - 1 - p] - factory[j - 1][0]) for p in range(k)))
        
        return dp[n][m]