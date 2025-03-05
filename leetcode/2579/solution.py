class Solution:
    def coloredCells(self, n: int) -> int:
        """
        Returns the total number of colored cells after n minutes.
        
        The pattern observed is that at each minute m, the number of new cells added is 4*(m-1).
        Therefore, the total number of cells after n minutes can be derived from a series sum formula.
        """
        return n * n + (n - 1) * (n - 1)

# Test cases
print(Solution().coloredCells(1))  # Output: 1
print(Solution().coloredCells(2))  # Output: 5
print(Solution().coloredCells(3))  # Output: 13