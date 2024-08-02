class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        total_ones = sum(nums)
        
        if total_ones == 0:
            return 0
        
        current_zeros = nums[:total_ones].count(0)
        min_swaps_needed = current_zeros
        
        for i in range(total_ones, n):
            if nums[i] == 0:
                current_zeros += 1
            if nums[i - total_ones] == 0:
                current_zeros -= 1
            min_swaps_needed = min(min_swaps_needed, current_zeros)
        
        for i in range(total_ones):
            if nums[-i-1] == 0:
                current_zeros += 1
            if nums[n - total_ones + i] == 0:
                current_zeros -= 1
            min_swaps_needed = min(min_swaps_needed, current_zeros)
        
        return min_swaps_needed