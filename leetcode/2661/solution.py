class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Create a dictionary to store the position of each element in the matrix
        pos = {}
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)
        
        # Initialize counters for rows and columns
        row_count = [0] * m
        col_count = [0] * n
        
        # Iterate through the array to paint cells
        for i, num in enumerate(arr):
            x, y = pos[num]
            row_count[x] += 1
            col_count[y] += 1
            
            # Check if any row or column is completely painted
            if row_count[x] == n or col_count[y] == m:
                return i
        
        return -1  # This line should never be reached due to problem constraints