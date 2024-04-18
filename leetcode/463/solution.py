class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        result = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    result += 4
                    
                    if col > 0 and grid[row][col-1] == 1:
                        result -= 2

                    if row > 0 and grid[row-1][col] == 1:
                        result -= 2
                        
        return result