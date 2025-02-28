from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Returns the length of the longest subarray such that the absolute difference between any two elements is <= limit.
        
        Args:
        nums (List[int]): The input array of integers.
        limit (int): The maximum allowed absolute difference between any two elements in the subarray.

        Returns:
        int: The size of the longest valid subarray.
        """
        if not nums:
            return 0
        
        min_deque = []
        max_deque = []
        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            # Maintain min deque
            while min_deque and nums[min_deque[-1]] > num:
                min_deque.pop()
            min_deque.append(right)

            # Maintain max deque
            while max_deque and nums[max_deque[-1]] < num:
                max_deque.pop()
            max_deque.append(right)

            # Ensure the difference between max and min is <= limit
            while max_deque[0] - min_deque[0] > limit:
                if min_deque[0] == left:
                    min_deque.pop(0)
                if max_deque[0] == left:
                    max_deque.pop(0)
                left += 1

            # Update the maximum length of the valid subarray
            max_length = max(max_length, right - left + 1)

        return max_length