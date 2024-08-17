class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # Initialize left and right arrays to keep track of the maximum points from the left and right
        left = [0] * n
        right = [0] * n
        
        for i in range(m):
            # Calculate maximum points moving left to right
            max_point = 0
            for j in range(n):
                max_point = max(max_point - 1, left[j])
                left[j] = max_point + points[i][j]
            
            # Calculate maximum points moving right to left
            max_point = 0
            for j in reversed(range(n)):
                max_point = max(max_point - 1, right[j])
                right[j] = max_point + points[i][j]
            
            # Update the current row with the maximum points considering both directions
            for j in range(n):
                points[i][j] += max(left[j], right[j]) - points[i][j]
        
        # The result is the maximum points in the last row
        return max(points[-1])