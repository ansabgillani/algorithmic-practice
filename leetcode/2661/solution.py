class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        num_to_pos = {}
        
        for i in range(m):
            for j in range(n):
                num_to_pos[mat[i][j]] = (i, j)

        rows_painted = [0] * m
        cols_painted = [0] * n

        for i, num in enumerate(arr):
            x, y = num_to_pos[num]
            rows_painted[x] += 1
            cols_painted[y] += 1
            
            if rows_painted[x] == n or cols_painted[y] == m:
                return i

        return -1