class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        heap = [(0, 0, 0)]  # (cost, x, y)
        visited = [[False]*n for _ in range(m)]
        
        while heap:
            cost, x, y = heapq.heappop(heap)
            
            if x == m - 1 and y == n - 1:
                return cost
            
            if not visited[x][y]:
                visited[x][y] = True
                
                for i, (dx, dy) in enumerate(directions):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[x][y] == i + 1:
                            heapq.heappush(heap, (cost, nx, ny))
                        else:
                            heapq.heappush(heap, (cost + 1, nx, ny))
    
        return -1