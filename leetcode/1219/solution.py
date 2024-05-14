class Solution:
    def getMaximumGold(self, grid):
        def backtrack(i, j, current_gold):
            nonlocal max_gold
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return

            # Collect gold from the current cell
            current_gold += grid[i][j]
            max_gold = max(max_gold, current_gold)

            # Temporarily set the cell to 0 to mark it as visited
            temp = grid[i][j]
            grid[i][j] = 0
            
            # Explore all four possible directions
            backtrack(i + 1, j, current_gold)
            backtrack(i - 1, j, current_gold)
            backtrack(i, j + 1, current_gold)
            backtrack(i, j - 1, current_gold)

            # Backtrack: restore the original value of the cell
            grid[i][j] = temp

        m, n = len(grid), len(grid[0])
        max_gold = 0
    
        # Iterate over every cell as starting point
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    backtrack(i, j, 0)

        return max_gold