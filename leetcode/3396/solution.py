class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # If the array is already empty or has distinct elements, no operations are needed.
        if not nums or len(set(nums)) == len(nums):
            return 0
        
        count = 0
        while True:
            # Remove the first 3 elements or all remaining elements if fewer than 3
            if len(nums) >= 3:
                nums = nums[3:]
            else:
                nums = []
            
            # Increment the operation count
            count += 1
            
            # If the array is now empty or has distinct elements, break the loop
            if not nums or len(set(nums)) == len(nums):
                break
        
        return count