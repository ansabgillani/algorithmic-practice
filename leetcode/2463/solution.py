class Solution:
    def minimumTotalDistanceTraveled(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = 0
        
        for i in range(1, m + 1):
            for j in range(n + 1):
                total_distance = float('inf')
                
                for k in range(min(j, factory[i-1][1]) + 1):
                    total_distance = min(total_distance, (dp[i-1][j-k] if j-k >= 0 else float('inf')) + sum(abs(factory[i-1][0] - robot[m-j+k+l]) for l in range(k)))
                
                dp[i][j] = total_distance
    
        return dp[-1][-1]