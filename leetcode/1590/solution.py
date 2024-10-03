class Solution:
    def minSubarray(self, nums, p):
        target = sum(nums) % p
        if target == 0:
            return 0
        
        prefix_sum_mod = {}
        current_sum_mod = 0
        result = float('inf')
        
        for i, num in enumerate(nums):
            current_sum_mod = (current_sum_mod + num) % p
            
            required_mod = (current_sum_mod - target + p) % p
            
            if required_mod in prefix_sum_mod:
                result = min(result, i - prefix_sum_mod[required_mod])
            
            if current_sum_mod not in prefix_sum_mod:
                prefix_sum_mod[current_sum_mod] = i
        
        return result if result < len(nums) else -1