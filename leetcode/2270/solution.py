class Solution:
    def waysToSplitArray(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        result = 0
        
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            
            if left_sum >= right_sum:
                result += 1
        
        return result