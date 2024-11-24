class Solution:
    def maxMatrixSum(self, matrix):
        min_val = float('inf')
        negatives = 0
        
        for row in matrix:
            for val in row:
                if val < 0:
                    negatives += 1
                min_val = min(abs(val), min_val)
            
        return (2 * sum(abs(num) for row in matrix for num in row)) if negatives % 2 == 0 else \
               (2 * sum(abs(num) for row in matrix for num in row) - 2 * min_val)