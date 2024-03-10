class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Returns the unique intersection of two arrays.
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert both lists to sets to remove duplicates and allow for efficient intersection
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of both sets
        intersection_set = set1 & set2
        
        # Convert the result back to a list
        return list(intersection_set)

# Example usage:
# solution = Solution()
# print(solution.intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
# print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4]