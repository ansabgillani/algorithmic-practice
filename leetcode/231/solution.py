class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Returns true if n is a power of two, otherwise returns false.
        
        :type n: int
        :rtype: bool
        """
        # A number is a power of two if it has exactly one bit set in its binary representation.
        # We can use the property that n & (n - 1) will be 0 for powers of two.
        return n > 0 and (n & (n - 1)) == 0