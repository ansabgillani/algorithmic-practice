class Solution:
    def mincostTickets(self, days, costs):
        max_day = days[-1]
        dp = [0] * (max_day + 1)
        
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(i-1, 0)] + costs[0],
                             dp[max(i-7, 0)] + costs[1],
                             dp[max(i-30, 0)] + costs[2])
        
        return dp[-1]