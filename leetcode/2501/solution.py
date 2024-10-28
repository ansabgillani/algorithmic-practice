class Solution:
    def longestSquareStreak(self, nums):
        nums = set(nums)
        max_streak = 0
        
        for num in sorted(nums):
            if (num**0.5).is_integer():
                continue
            current_num, streak = num, 1
            
            while current_num * current_num in nums:
                current_num *= current_num
                streak += 1
            
            max_streak = max(max_streak, streak)
        
        return -1 if max_streak == 1 else max_streak