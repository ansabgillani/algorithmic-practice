class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Finds the minimum common value between two sorted arrays.
        
        Args:
        nums1 (List[int]): The first sorted array.
        nums2 (List[int]): The second sorted array.
        
        Returns:
        int: The smallest common value, or -1 if no common value exists.
        """
        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                return num
        return -1