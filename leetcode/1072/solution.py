class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        transformed_rows = {}

        for row in matrix:
            normal, flipped = tuple(row), tuple(1-x for x in row)

            if normal not in transformed_rows: 
                transformed_rows[normal] = 0
            if flipped not in transformed_rows:
                transformed_rows[flipped] = 0

            transformed_rows[normal] += 1
            transformed_rows[flipped] += 1

        return max(transformed_rows.values())