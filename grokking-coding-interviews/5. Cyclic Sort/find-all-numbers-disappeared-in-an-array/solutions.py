class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Mark the presence of an element by negating the value at the index corresponding to that element
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Collect all indices with positive values, which correspond to missing numbers
        return [i + 1 for i, num in enumerate(nums) if num > 0]