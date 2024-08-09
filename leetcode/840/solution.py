from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Function to check if a 3x3 grid is a magic square
        def is_magic_square(square):
            target_sum = sum(square[0])
            for i in range(1, 3):
                if sum(square[i]) != target_sum or sum(square[j][i] for j in range(3)) != target_sum:
                    return False
            if square[0][0] + square[1][1] + square[2][2] != target_sum or square[0][2] + square[1][1] + square[2][0] != target_sum:
                return False
            # Check distinct numbers from 1 to 9
            if sorted([square[i][j] for i in range(3) for j in range(3)]) != list(range(1, 10)):
                return False
            return True
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        # Iterate over all possible 3x3 subgrids
        for i in range(rows - 2):
            for j in range(cols - 2):
                square = [grid[i+k][j:j+3] for k in range(3)]
                if is_magic_square(square):
                    count += 1
        
        return count