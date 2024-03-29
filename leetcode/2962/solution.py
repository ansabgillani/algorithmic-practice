class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find the maximum element in the array
        max_val = max(nums)
        
        # Initialize variables
        count = 0
        left = 0
        max_count = 0
        
        # Iterate through the array with a sliding window approach
        for right, num in enumerate(nums):
            if num == max_val:
                max_count += 1
            
            # When there are at least k occurrences of the max element
            while max_count >= k:
                count += len(nums) - right  # All subarrays ending at 'right' and starting from [left, right]
                if nums[left] == max_val:
                    max_count -= 1
                left += 1
        
        return count