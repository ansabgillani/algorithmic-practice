class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Merge two 2D integer arrays by summing values and return the resulting array sorted in ascending order by id.
        """
        from collections import defaultdict
        
        # Create a dictionary to store the sum of values for each id
        merged = defaultdict(int)
        
        # Add values from nums1 to the dictionary
        for id, val in nums1:
            merged[id] += val
        
        # Add values from nums2 to the dictionary, summing with existing values
        for id, val in nums2:
            merged[id] += val
        
        # Convert the dictionary back to a sorted list of [id, value]
        result = sorted([[id, val] for id, val in merged.items()])
        
        return result