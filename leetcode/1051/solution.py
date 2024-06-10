class Solution:
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        return sum(1 for h, e in zip(heights, sorted_heights) if h != e)