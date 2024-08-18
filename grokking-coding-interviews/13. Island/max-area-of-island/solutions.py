from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
                return 0
            visited[i][j] = True
            area = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                area += dfs(i + dx, j + dy)
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area