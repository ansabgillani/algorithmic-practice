from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        """
        Find the minimum number of deletions to remove both the minimum and maximum elements from the array.
        
        :param nums: List of distinct integers.
        :return: Minimum number of deletions.
        """
        if not nums or len(nums) == 1:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        min_index, max_index = nums.index(min_val), nums.index(max_val)
        
        # Ensure min_index is less than max_index for simplicity
        if min_index > max_index:
            min_index, max_index = max_index, min_index
        
        # Calculate deletions from both ends and the middle
        delete_from_front = max_index + 1
        delete_from_back = len(nums) - min_index
        delete_from_middle = min_index + 1 + (len(nums) - max_index)
        
        # Return the minimum of the three cases
        return min(delete_from_front, delete_from_back, delete_from_middle)