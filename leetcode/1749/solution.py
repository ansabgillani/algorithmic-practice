class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Finds the maximum absolute sum of any subarray in the given list of integers.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The maximum absolute sum of any subarray.
        """
        max_sum = 0
        current_max = 0
        current_min = 0
        
        for num in nums:
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)
            max_sum = max(max_sum, abs(current_max), abs(current_min))
        
        return max_sum

# Test cases
print(Solution().maxAbsoluteSum([1,-3,2,3,-4]))  # Output: 5
print(Solution().maxAbsoluteSum([2,-5,1,-4,3,-2]))  # Output: 8