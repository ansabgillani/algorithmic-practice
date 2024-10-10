class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        min_index = [n-1]
        for i in range(n-2, -1, -1):
            if nums[min_index[-1]] >= nums[i]:
                min_index.append(i)

        max_ramp_width = 0
        j = 0
        for i in range(n-1, -1, -1):
            while j < len(min_index) and nums[min_index[j]] <= nums[i]:
                max_ramp_width = max(max_ramp_width, i - min_index[j])
                j += 1

        return max_ramp_width