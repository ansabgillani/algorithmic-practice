class Solution:
    def maximumOddBinaryNumber(self, s):
        ones_count = s.count('1')
        if ones_count == 1:
            return '0' * (len(s) - 1) + '1'
        return '1' * (ones_count - 1) + '0' * (len(s) - ones_count) + '1'