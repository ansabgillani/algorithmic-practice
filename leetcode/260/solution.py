class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Finds two unique numbers in a list where every other number appears twice.
        
        Args:
        nums (List[int]): The input list of integers.
        
        Returns:
        List[int]: A list containing the two unique numbers.
        """
        # XOR all numbers to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Find a set bit in xor_all (this will be different between the two unique numbers)
        set_bit = xor_all & -xor_all
        
        # Divide numbers into two groups based on the set bit and XOR each group to find the unique numbers
        unique1, unique2 = 0, 0
        for num in nums:
            if num & set_bit:
                unique1 ^= num
            else:
                unique2 ^= num
        
        return [unique1, unique2]