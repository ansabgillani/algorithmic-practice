class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums)
        
        while low <= high:
            mid = (low + high) // 2
            count = sum(1 for num in nums if num >= mid)
            
            # Check if the current mid meets the special array criteria
            if count == mid:
                return mid
            elif count < mid:
                high = mid - 1
            else:
                low = mid + 1
    
        # If no such x is found, return -1
        return -1