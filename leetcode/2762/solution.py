from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Initialize a deque to keep track of indices
        dq = deque()
        max_val = min_val = nums[0]
        count = 0
        
        for i, num in enumerate(nums):
            # Remove elements from the deque if they are out of the valid range
            while dq and (num - nums[dq[-1]] > 2 or nums[dq[-1]] - num > 2):
                last_index = dq.pop()
                max_val = max(max_val, nums[last_index])
                min_val = min(min_val, nums[last_index])
            
            # If the deque is not empty, calculate the number of valid subarrays ending at i
            if dq:
                count += (i - dq[0])
            else:
                count += i
            
            # Update max and min values in the deque
            while dq and num > nums[dq[0]]:
                dq.popleft()
            while dq and num < nums[dq[-1]]:
                dq.pop()
            
            # Add the current index to the deque
            dq.appendleft(i)
        
        return count