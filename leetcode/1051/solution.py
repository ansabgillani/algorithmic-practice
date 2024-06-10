class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Return the number of indices where heights[i] != expected[i].
        
        :param heights: List of student heights in current order.
        :return: Number of mismatched indices.
        """
        # Sort a copy of the heights list to get the expected order
        expected = sorted(heights)
        
        # Count the number of positions where heights[i] != expected[i]
        return sum(h != e for h, e in zip(heights, expected))