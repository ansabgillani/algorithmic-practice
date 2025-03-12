class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find the first non-negative number using binary search
        first_non_negative = self.find_first(nums, 0)
        
        # The number of negative integers is the index of the first non-negative number
        neg_count = first_non_negative
        
        # The number of positive integers is the total length minus the first non-negative index
        pos_count = len(nums) - first_non_negative
        
        # Return the maximum of the two counts
        return max(neg_count, pos_count)
    
    def find_first(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left