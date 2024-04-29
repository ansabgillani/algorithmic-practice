class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Returns the minimum number of operations required to make the bitwise XOR 
        of all elements of the array equal to k.
        
        Args:
        nums (List[int]): The input list of integers.
        k (int): The target XOR value.
        
        Returns:
        int: The minimum number of operations required.
        """
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        return bin(xor_result ^ k).count('1')