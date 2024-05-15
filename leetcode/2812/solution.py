import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # BFS to calculate the minimum distance from each cell to any thief
        def bfs():
            queue = []
            visited = set()
            
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        heapq.heappush(queue, (0, i, j))
                        visited.add((i, j))
            
            while queue:
                dist, x, y = heapq.heappop(queue)
                grid[x][y] = dist
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        heapq.heappush(queue, (dist + 1, nx, ny))
                        visited.add((nx, ny))
        
        bfs()
        
        # Dijkstra's algorithm to find the path with maximum safeness factor
        def dijkstra():
            heap = [(-grid[0][0], 0, 0)]
            visited = set()
            
            while heap:
                min_dist, x, y = heapq.heappop(heap)
                
                if (x, y) in visited:
                    continue
                
                if x == n - 1 and y == n - 1:
                    return -min_dist
                
                visited.add((x, y))
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        heapq.heappush(heap, (-min(grid[nx][ny], -min_dist), nx, ny))
        
        return dijkstra()

# Example usage:
solution = Solution()
grid1 = [[1,0,0],[0,0,0],[0,0,1]]
print(solution.maximumSafenessFactor(grid1))  # Output: 0

grid2 = [[0,0,1],[0,0,0],[0,0,0]]
print(solution.maximumSafenessFactor(grid2))  # Output: 2

grid3 = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
print(solution.maximumSafenessFactor(grid3))  # Output: 2