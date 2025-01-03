class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Returns the number of valid splits in the array nums.
        
        A split at index i is valid if the sum of the first i+1 elements 
        is greater than or equal to the sum of the last n-i-1 elements.
        There must be at least one element on the right side of the split.
        
        :param nums: List[int] - The input array
        :return: int - The number of valid splits
        """
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_splits += 1
                
        return valid_splits