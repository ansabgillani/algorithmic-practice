from collections import deque

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Calculate the total number of 1's in the array
        ones_count = sum(nums)
        
        # If there are no 1's or only one 1, no swaps are needed
        if ones_count == 0 or ones_count == 1:
            return 0
        
        min_swaps = float('inf')
        window_sum = 0
        window_size = len(nums)
        
        # Use a deque to keep track of the current window
        window = deque()
        
        # Initialize the first window
        for i in range(window_size):
            if nums[i] == 1:
                window.append(i)
                window_sum += 1
        
        min_swaps = min(min_swaps, ones_count - window_sum)
        
        # Slide the window across the array
        for i in range(window_size, len(nums) * 2):
            new_index = i % window_size
            if nums[new_index] == 1:
                window.append(new_index)
                window_sum += 1
            
            old_index = (i - ones_count) % window_size
            if nums[old_index] == 1:
                window.popleft()
                window_sum -= 1
            
            min_swaps = min(min_swaps, ones_count - window_sum)
        
        return min_swaps