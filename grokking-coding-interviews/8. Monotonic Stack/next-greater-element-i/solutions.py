class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds the next greater element for each element in nums1 based on their positions in nums2.
        
        Args:
        nums1 (List[int]): The subset of numbers to find next greater elements for.
        nums2 (List[int]): The array in which to search for next greater elements.

        Returns:
        List[int]: A list containing the next greater element for each number in nums1, or -1 if not found.
        """
        stack = []
        num_to_next_greater = {}
        
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                num_to_next_greater[num] = stack[-1]
            else:
                num_to_next_greater[num] = -1
            stack.append(num)
        
        return [num_to_next_greater[num] for num in nums1]