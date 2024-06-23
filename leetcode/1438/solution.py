class Solution:
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # Deque to store indices of elements in decreasing order
        max_dq = []

        # Deque to store indices of elements in increasing order
        min_dq = []

        start = 0
        max_length = 0

        for end, num in enumerate(nums):
            while max_dq and nums[max_dq[-1]] < num:
                max_dq.pop()
            
            while min_dq and nums[min_dq[-1]] > num:
                min_dq.pop()

            max_dq.append(end)
            min_dq.append(end)

            # If the difference between the max and min is greater than limit, shrink from left
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                start += 1
                if start > max_dq[0]:
                    max_dq.pop(0)
                if start > min_dq[0]:
                    min_dq.pop(0)

            # Update the maximum length found
            max_length = max(max_length, end - start + 1)
        
        return max_length