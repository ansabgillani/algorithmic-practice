from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Initialize dp array where dp[i][j] represents the minimum falling path sum to reach cell (i, j)
        dp = [[0] * n for _ in range(n)]
        
        # Base case: first row remains the same as grid
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        # Fill the dp array
        for i in range(1, n):
            min_val_1st, min_val_2nd = float('inf'), float('inf')
            min_idx_1st = -1
            
            # Find the two smallest values and their indices in the previous row
            for j in range(n):
                if grid[i-1][j] < min_val_1st:
                    min_val_2nd = min_val_1st
                    min_val_1st = grid[i-1][j]
                    min_idx_1st = j
                elif grid[i-1][j] < min_val_2nd:
                    min_val_2nd = grid[i-1][j]
            
            # Fill the current row of dp array with the minimum sum excluding the same column as the smallest value in the previous row
            for j in range(n):
                if j == min_idx_1st:
                    dp[i][j] = dp[i-1][min_idx_2nd] + grid[i][j]
                else:
                    dp[i][j] = dp[i-1][min_idx_1st] + grid[i][j]
        
        # The minimum falling path sum is the minimum value in the last row of dp array
        return min(dp[-1])