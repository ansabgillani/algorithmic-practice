class Solution:
    def numMagicSquaresInside(self, grid):
        def is_magic(subgrid):
            # Check if the subgrid has all unique values and sum of each row, column, diagonal are equal to 15.
            return len(set(map(sum, subgrid))) == 1 and set(map(sum, zip(*subgrid))) == {15} and sum([subgrid[0][0], subgrid[0][2], subgrid[1][1], subgrid[2][0], subgrid[2][2]]) == 15

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if is_magic([grid[i+k][j:j+3] for k in range(3)]):
                    count += 1
                    
        return count