from collections import deque
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # If the cell in the same row or column is less than 2, it's impossible to move diagonally
        if grid[1][0] < 2 and grid[0][1] < 2:
            return -1
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        pq = [(0, 0, 0)]  # (time, x, y)
        
        while pq:
            time, x, y = heapq.heappop(pq)
            
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if x == m - 1 and y == n - 1:
                return time
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                
                wait_time = max(0, grid[nx][ny] - time - 1)
                next_time = time + wait_time + 1
                heapq.heappush(pq, (next_time, nx, ny))
                
        return -1

# Example usage:
solution = Solution()
grid1 = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
print(solution.minimumTime(grid1))  # Output: 7

grid2 = [[0,2,4],[3,2,1],[1,0,4]]
print(solution.minimumTime(grid2))  # Output: -1