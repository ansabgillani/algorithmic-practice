class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMostKDistinct(k):
            left = 0
            count = {}
            result = 0
            
            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1
                
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
            
                result += right - left + 1
        
            return result
        
        return atMostKDistinct(k) - atMostKDistinct(k-1)