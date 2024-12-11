class Solution:
    def maximumBeauty(self, nums, k):
        nums.sort()
        i = 0
        ans = 0
        for j, num in enumerate(nums):
            while nums[i] + k < num - k:
                i += 1
            ans = max(ans, j - i + 1)
        return ans