class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def get_next_pos(x, y):
            return x + directions[grid[x][y] - 1][0], y + directions[grid[x][y] - 1][1]
        
        from collections import deque
        queue = deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0))
        
        while queue:
            x, y, cost = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return cost
            
            for i in range(4):
                nx, ny = get_next_pos(x, y)
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, cost + (i != grid[x][y] - 1)))
        
        return -1