from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Returns the number of subarrays with exactly k distinct integers.
        
        :param nums: List[int] - The input array of integers.
        :param k: int - The exact number of distinct integers required in a subarray.
        :return: int - The count of good subarrays.
        """
        def atMostKDistinct(k):
            count = Counter()
            left = 0
            result = 0
            for right, num in enumerate(nums):
                if count[num] == 0:
                    k -= 1
                count[num] += 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                result += right - left + 1
            return result
        
        return atMostKDistinct(k) - atMostKDistinct(k-1)