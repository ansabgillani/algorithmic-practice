class Solution:
    def countBadPairs(self, nums):
        return len(nums) * (len(nums) - 1) // 2 - sum((i - num) for i, num in enumerate(nums)) // 2