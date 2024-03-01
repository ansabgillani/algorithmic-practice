class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        """
        Rearranges the bits in the binary string to form the maximum odd binary number.
        
        :param s: The input binary string containing at least one '1'.
        :return: A string representing the maximum odd binary number.
        """
        count_ones = s.count('1')
        return ('1' * (count_ones - 1) + '0' * (len(s) - count_ones) + '1')

# Test cases
assert Solution().maximumOddBinaryNumber("010") == "001"
assert Solution().maximumOddBinaryNumber("0101") == "1001"