class Solution:
    def longestSubarray(self, nums):
        max_val = max(nums)
        max_len, current_len = 0, 0
        
        for num in nums:
            if num == max_val:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
                
        return max_len