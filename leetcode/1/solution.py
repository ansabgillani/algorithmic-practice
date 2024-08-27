class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns indices of the two numbers such that they add up to the target.
        
        Args:
        nums (List[int]): The list of integers to search through.
        target (int): The target sum.
        
        Returns:
        List[int]: A list containing the indices of the two numbers that add up to the target.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i