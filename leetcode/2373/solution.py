class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        
        # Iterate over the grid to find the maximum value in each 3x3 submatrix
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                maxLocal[i-1][j-1] = max(grid[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2))
        
        return maxLocal