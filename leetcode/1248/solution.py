class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMostK(nums, k):
            result = left = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                result += right - left + 1
            return result
        
        return atMostK(nums, k) - atMostK(nums, k - 1)