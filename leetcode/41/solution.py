class Solution:
    def firstMissingPositive(self, nums):
        """
        Finds the smallest missing positive integer from an unsorted array of integers.
        
        The function runs in O(n) time and uses O(1) auxiliary space.

        :param nums: List[int] - Unsorted array of integers.
        :return: int - Smallest missing positive integer.
        """
        n = len(nums)
        if 1 not in nums:
            return 1
        
        # Replace negative numbers, zeros and numbers larger than n with 1s
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Use index as a hash key and number sign as a presence detector
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # The first positive index+1 is the missing number
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1