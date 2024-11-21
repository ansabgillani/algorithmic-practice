class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize grid
        grid = [[0] * n for _ in range(m)]
        
        # Mark walls and guards on the grid
        for x, y in walls:
            grid[x][y] = -1  # Wall
        for x, y in guards:
            grid[x][y] = 1  # Guard
        
        # Directions: North, East, South, West
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        # Mark all cells guarded by each guard
        for x, y in guards:
            for dx, dy in directions:
                i, j = x + dx, y + dy
                while 0 <= i < m and 0 <= j < n and grid[i][j] != -1:  # Stop at wall or another guard
                    if grid[i][j] == 0:
                        grid[i][j] = 2  # Mark as guarded
                    i += dx
                    j += dy
        
        # Count unguarded cells
        return sum(cell == 0 for row in grid for cell in row)