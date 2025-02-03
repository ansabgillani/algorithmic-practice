class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Returns the length of the longest strictly increasing or decreasing subarray in nums.
        
        :param nums: List[int] - The input array of integers.
        :return: int - The length of the longest monotonic subarray.
        """
        if not nums:
            return 0

        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
                max_length = max(max_length, current_length)
            elif nums[i] < nums[i - 1]:
                current_length = 1
                while i + 1 < len(nums) and nums[i + 1] < nums[i]:
                    i += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        
        return max_length