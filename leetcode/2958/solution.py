class Solution:
    def longestSubarray(self, nums, k):
        freq = {}
        
        left, right = 0, 0
        max_length = 0
        
        while right < len(nums):
            if nums[right] not in freq:
                freq[nums[right]] = 0
            freq[nums[right]] += 1
            
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            
            max_length = max(max_length, right - left + 1)
            
            right += 1
        
        return max_length