class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_ones = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            max_ones = max(max_ones, right - left + 1)
        
        return max_ones