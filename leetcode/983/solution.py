from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a list to store minimum cost up to each day of the year
        dp = [0] * (days[-1] + 1)
        
        # Index of next travel day
        i = 0
        
        for d in range(1, len(dp)):
            if d == days[i]:
                # Minimum cost on travel days
                dp[d] = min(
                    dp[d - 1] + costs[0],   # 1-day pass
                    dp[max(0, d - 7)] + costs[1],  # 7-day pass
                    dp[max(0, d - 30)] + costs[2]  # 30-day pass
                )
                i += 1
            else:
                # No travel on this day, carry forward the previous cost
                dp[d] = dp[d - 1]
        
        return dp[-1]

# Example usage
solution = Solution()
print(solution.mincostTickets([1,4,6,7,8,20], [2,7,15]))  # Output: 11
print(solution.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))  # Output: 17