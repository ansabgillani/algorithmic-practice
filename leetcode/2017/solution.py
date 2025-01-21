class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Calculate prefix sums from left and right for each row
        top = [0] * len(grid[0])
        bottom = [0] * len(grid[0])
        
        for i in range(1, len(grid[0])):
            top[i] = top[i - 1] + grid[0][i - 1]
        
        for i in range(len(grid[0]) - 2, -1, -1):
            bottom[i] = bottom[i + 1] + grid[1][i + 1]
        
        # Initialize the answer with the maximum possible points
        ans = float('inf')
        
        # Iterate through each column to find the optimal split point
        for i in range(len(grid[0])):
            # The first robot's points are all from the top row up to the current split point (inclusive)
            # The second robot's points are all from the bottom row after the current split point (exclusive)
            ans = min(ans, max(top[i], bottom[i]))
        
        return ans