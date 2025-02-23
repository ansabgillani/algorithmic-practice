class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number in an array containing n distinct numbers in the range [0, n].
        
        This implementation uses the mathematical property of the sum of the first n natural numbers.
        The time complexity is O(n) and space complexity is O(1).
        
        :param nums: List[int] - A list of integers from 0 to n with one number missing
        :return: int - The missing number
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Test cases
solution = Solution()

assert solution.missingNumber([3, 0, 1]) == 2, "Test case 1 failed"
assert solution.missingNumber([0, 1]) == 2, "Test case 2 failed"
assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8, "Test case 3 failed"