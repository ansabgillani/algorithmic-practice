class Solution:
    def luckyNumbers(self, matrix):
        min_in_rows = {min(row) for row in matrix}
        max_in_cols = {max(col) for col in zip(*matrix)}
        return list(min_in_rows & max_in_cols)