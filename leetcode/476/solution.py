class Solution:
    def findComplement(self, num: int) -> int:
        """
        Find the complement of a given integer by flipping all its bits in binary representation.
        
        :param num: Integer to find the complement of.
        :return: Complement of the given integer.
        """
        # Create a mask with the same bit length as 'num' but all bits set to 1
        mask = (1 << num.bit_length()) - 1
        
        # XOR 'num' with the mask to flip its bits
        return num ^ mask