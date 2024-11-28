import heapq

class Solution:
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(grid[0][0], 0, 0)]  # (obstacles, x, y)
        visited = set()
        
        while heap:
            obstacles, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            if x == m - 1 and y == n - 1:
                return obstacles
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(heap, (obstacles + grid[nx][ny], nx, ny))
        
        return -1

# Example usage:
sol = Solution()
print(sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))  # Output: 2
print(sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))  # Output: 0