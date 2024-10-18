from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the next greater element of each element in nums1 based on their order in nums2.
        
        :param nums1: List of integers for which to find the next greater elements.
        :param nums2: List of integers where the search for next greater elements is performed.
        :return: A list of integers representing the next greater element of each element in nums1.
        """
        stack = []
        next_greater_map = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater_map[stack.pop()] = num
            stack.append(num)
        
        return [next_greater_map.get(x, -1) for x in nums1]