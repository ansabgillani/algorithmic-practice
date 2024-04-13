class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for row in range(rows):
            for col in range(cols):
                heights[col] = heights[col] + 1 if matrix[row][col] == '1' else 0
            stack = [-1]
            
            for i, height in enumerate(heights):
                while stack and height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area