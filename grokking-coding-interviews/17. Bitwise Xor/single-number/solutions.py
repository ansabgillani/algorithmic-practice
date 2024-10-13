class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the element that appears only once in a list where every other element appears twice.
        
        Args:
        nums (List[int]): A non-empty list of integers where every element except one appears twice.
        
        Returns:
        int: The single number that appears only once.
        """
        # Using XOR to find the single number
        return reduce(lambda x, y: x ^ y, nums)