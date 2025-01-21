class Solution:
    def gridGame(self, grid):
        left = [0] * len(grid[0])
        right = [0] * len(grid[0])

        left[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            left[i] = left[i-1] + grid[0][i]

        right[-1] = grid[1][-1]
        for j in range(len(grid[0])-2, -1, -1):
            right[j] = right[j+1] + grid[1][j]

        min_points = float('inf')
        for k in range(len(grid[0])):
            current_points = max(left[k], right[k])
            min_points = min(min_points, current_points)

        return min_points