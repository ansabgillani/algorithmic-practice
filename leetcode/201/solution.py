class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Returns the bitwise AND of all numbers in the range [left, right], inclusive.
        
        :param left: The start of the range (inclusive).
        :param right: The end of the range (inclusive).
        :return: The bitwise AND result.
        """
        shift = 0
        # Find the common prefix of left and right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift