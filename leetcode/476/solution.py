class Solution:
    def findComplement(self, num):
        """
        Finds the bitwise complement of given number.
        
        Args:
        num (int): The integer to find complement for.
        
        Returns:
        int: Complement of the given integer.
        """
        # Initialize mask with 0 and shift it to the left by the number of bits in num
        mask = 0
        while num > 0:
            # Shift 1 to the left by 1 bit and OR it with mask
            mask = (mask << 1) | 1
            num >>= 1
        
        # Perform bitwise XOR between original num and mask to get complement
        return num ^ mask