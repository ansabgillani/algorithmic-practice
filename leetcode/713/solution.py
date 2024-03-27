class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        left = ans = product = 0
        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product /= nums[left]
                left += 1
            
            ans += right - left + 1

        return int(ans)