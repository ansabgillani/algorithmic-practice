class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        result = 0
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            if nums[left] + nums[right] >= lower:
                if nums[left] + nums[right] <= upper:
                    result += right - left
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return result