class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number in an array containing n distinct numbers 
        in the range [0, n].
        
        Parameters:
        nums (List[int]): The input list of integers.
        
        Returns:
        int: The missing number in the range.
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Example usage:
solution = Solution()
print(solution.missingNumber([3,0,1]))  # Output: 2
print(solution.missingNumber([0,1]))    # Output: 2
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8