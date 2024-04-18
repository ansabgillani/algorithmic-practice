class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Calculate the perimeter of the island in a given 2D grid.
        
        :param grid: A list of lists representing the grid where 1 is land and 0 is water.
        :return: The perimeter of the island.
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Each land cell contributes 4 to the perimeter
                    perimeter += 4
                    
                    # Subtract 1 for each adjacent land cell (up, down, left, right)
                    if r > 0 and grid[r-1][c] == 1: perimeter -= 1
                    if r < rows - 1 and grid[r+1][c] == 1: perimeter -= 1
                    if c > 0 and grid[r][c-1] == 1: perimeter -= 1
                    if c < cols - 1 and grid[r][c+1] == 1: perimeter -= 1
        
        return perimeter