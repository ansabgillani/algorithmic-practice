class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize variables
        left = 0
        current_sum = 0
        result = 0
        
        # Iterate over the array with a right pointer
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left if the score is not less than k
            while left <= right and (current_sum * (right - left + 1)) >= k:
                current_sum -= nums[left]
                left += 1
            
            # All subarrays ending at 'right' and starting from any index between 'left' and 'right'
            # will have a score less than k
            result += right - left + 1
        
        return result