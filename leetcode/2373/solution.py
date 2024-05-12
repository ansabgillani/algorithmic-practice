class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(1, n-1): 
            for j in range(1, n-1): 
                maxLocal[i-1][j-1] = max(grid[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2))
                
        return maxLocal