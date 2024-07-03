class Solution:
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0
        
        # Sort the array
        nums.sort()
        
        # There can be four possible scenarios to reduce the maximum difference:
        # - Remove the 3 largest elements
        # - Remove the 2 largest and 1 smallest element
        # - Remove the 1 largest and 2 smallest elements
        # - Remove the 3 smallest elements
        
        return min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1] - nums[3])