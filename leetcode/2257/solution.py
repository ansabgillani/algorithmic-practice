class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize grid with 0s (unguarded), 1s (walls), and 2s (guards)
        grid = [[0] * n for _ in range(m)]
        
        for x, y in walls:
            grid[x][y] = 1
        for x, y in guards:
            grid[x][y] = 2
        
        # Directions for north, east, south, west
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Mark cells guarded by each guard
        for x, y in guards:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1:  # Stop if encountering a wall or guard
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = -1  # Mark as guarded
                    nx, ny = nx + dx, ny + dy
        
        # Count unguarded cells (cells with value 0)
        return sum(row.count(0) for row in grid)