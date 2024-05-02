class Solution:
    def findMaxK(self, nums):
        seen = set()
        max_k = -1
        
        for num in nums:
            if -num in seen:
                max_k = max(max_k, abs(num))
            seen.add(num)
        
        return max_k