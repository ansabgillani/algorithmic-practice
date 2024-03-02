class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        output = [0] * (right + 1)
        position = right
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                output[position] = nums[left] ** 2
                left += 1
            else:
                output[position] = nums[right] ** 2
                right -= 1
            
            position -= 1
        
        return output