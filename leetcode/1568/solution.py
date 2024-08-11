class Solution:
    def minDays(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)

        island_count = sum(dfs(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1)
        
        if island_count < 2:
            return 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    new_island_count = sum(dfs(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1)
                    if new_island_count < 2:
                        return 1
                    grid[i][j] = 1
        
        return 2

# Example usage:
sol = Solution()
grid1 = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
print(sol.minDays(grid1))  # Output: 2

grid2 = [[1,1]]
print(sol.minDays(grid2))  # Output: 2