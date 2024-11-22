class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Normalize each row to have a leading '0'
        normalized_rows = set()
        for row in matrix:
            if row[0] == 1:
                row = [1 - x for x in row]
            normalized_rows.add(tuple(row))
        
        # Count the frequency of each normalized row
        from collections import Counter
        count = Counter(normalized_rows)
        
        # Return the maximum count
        return max(count.values())