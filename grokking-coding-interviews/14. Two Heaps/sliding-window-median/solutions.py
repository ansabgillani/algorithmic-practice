from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Initialize the result list and a sorted list to keep track of window elements
        result = []
        window = SortedList()
        
        for i in range(len(nums)):
            # Add current element to the window
            window.add(nums[i])
            
            # Remove the element that is out of the sliding window
            if i >= k:
                window.remove(nums[i - k])
            
            # When the window size reaches k, calculate the median
            if len(window) == k:
                if k % 2 == 1:
                    result.append(float(window[k // 2]))
                else:
                    mid1 = window[(k // 2) - 1]
                    mid2 = window[k // 2]
                    result.append((mid1 + mid2) / 2.0)
        
        return result