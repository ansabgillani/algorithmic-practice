class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Finds the largest rectangle containing only 1's in a binary matrix.

        :param matrix: A list of lists representing the binary matrix.
        :return: The area of the largest rectangle containing only 1's.
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * (cols + 2)
        
        for r in range(rows):
            stack = []
            for c in range(cols + 2):
                if c < cols and matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    while stack and heights[stack[-1]] > heights[c]:
                        h = heights[stack.pop()]
                        w = c - stack[-1] - 1
                        max_area = max(max_area, h * w)
                    stack.append(c)
        
        return max_area

# Example usage:
# sol = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# print(sol.maximalRectangle(matrix))  # Output: 6