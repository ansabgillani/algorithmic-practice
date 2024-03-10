class Solution:
    def intersect(self, nums1, nums2):
        """
        Returns the intersection of two integer arrays, containing unique elements.
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert both lists to sets to remove duplicates and allow for efficient lookups
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Use the intersection method of sets to find common elements
        intersection_set = set1.intersection(set2)
        
        # Return the result as a list
        return list(intersection_set)