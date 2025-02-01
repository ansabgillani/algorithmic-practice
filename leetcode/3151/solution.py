class Solution:
    def is_special_array(self, nums):
        if len(nums) == 1:
            return True
        
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == nums[i+1] % 2):
                return False
                
        return True