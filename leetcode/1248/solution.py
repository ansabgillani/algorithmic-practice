class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            count = left = 0
            result = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                count = right - left + 1
                result += count
            return result
        
        return atMostK(k) - atMostK(k - 1)