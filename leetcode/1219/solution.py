class Solution:
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max_gold = 0
        
        def dfs(x, y, gold_collected):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            
            gold_collected += grid[x][y]
            self.max_gold = max(self.max_gold, gold_collected)
            
            temp, grid[x][y] = grid[x][y], 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                dfs(x + dx, y + dy, gold_collected)
            grid[x][y] = temp
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
        
        return self.max_gold