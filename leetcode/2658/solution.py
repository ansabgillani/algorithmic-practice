class Solution:
    def maxFish(self, grid):
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            fish = grid[i][j]
            grid[i][j] = 0  # Mark as visited by setting to 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                fish += dfs(i + dx, j + dy)
            return fish
        
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, dfs(i, j))
        
        return max_fish

# Example usage:
solution = Solution()
grid1 = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
print(solution.maxFish(grid1))  # Output: 7

grid2 = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
print(solution.maxFish(grid2))  # Output: 1