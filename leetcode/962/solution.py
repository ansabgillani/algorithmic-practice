class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        Finds the maximum width ramp in the given array.
        
        Args:
        nums (List[int]): The input integer array
        
        Returns:
        int: The maximum width of a ramp
        """
        min_stack = []  # Stack to keep track of indices with minimum values
        max_width = 0   # Variable to store the maximum width of the ramp found
        
        for i, num in enumerate(nums):
            if not min_stack or nums[min_stack[-1]] > num:
                min_stack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while min_stack and nums[j] >= nums[min_stack[-1]]:
                max_width = max(max_width, j - min_stack.pop())
            if not min_stack:
                break
        
        return max_width