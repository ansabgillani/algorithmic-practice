from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Finds a special number x such that there are exactly x numbers in nums greater than or equal to x.
        
        :param nums: List of non-negative integers
        :return: The value of x if the array is special, otherwise -1
        """
        nums.sort()
        n = len(nums)
        for i in range(n + 1):
            j = bisect_left(nums, i)
            if n - j == i:
                return i
        return -1