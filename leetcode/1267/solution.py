class Solution:
    def countServers(self, grid):
        rows, cols = [0] * len(grid), [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        
        return sum((rows[i] > 1 or cols[j] > 1) and grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])))