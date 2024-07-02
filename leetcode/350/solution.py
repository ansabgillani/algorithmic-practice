from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds the intersection of two arrays where each element appears as many times as it shows in both arrays.
        
        Args:
        nums1 (List[int]): The first list of integers.
        nums2 (List[int]): The second list of integers.
        
        Returns:
        List[int]: A list containing the intersection of the two input lists.
        """
        # Create a dictionary to store counts of elements in the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count_map = {}
        for num in nums1:
            count_map[num] = count_map.get(num, 0) + 1
        
        # Find the intersection by checking the larger array against the dictionary
        result = []
        for num in nums2:
            if num in count_map and count_map[num] > 0:
                result.append(num)
                count_map[num] -= 1
        
        return result

# Example usage:
# solution = Solution()
# print(solution.intersect([1,2,2,1], [2,2]))  # Output: [2, 2]
# print(solution.intersect([4,9,5], [9,4,9,8,4]))  # Output: [4, 9]