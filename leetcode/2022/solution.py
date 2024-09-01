class Solution:
    def construct2DArray(self, original, m, n):
        if m * n != len(original):
            return []

        result = []
        for i in range(m):
            row = original[i*n : (i+1)*n]
            result.append(row)

        return result