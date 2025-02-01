class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        Check if the given array is a special array.
        
        A special array has adjacent elements with different parity (one even, one odd).
        
        :param nums: List of integers
        :return: True if the array is special, False otherwise
        """
        for i in range(1, len(nums)):
            if (nums[i] % 2) == (nums[i - 1] % 2):
                return False
        return True

# Test cases to verify the solution
assert Solution().isArraySpecial([1]) == True
assert Solution().isArraySpecial([2, 1, 4]) == True
assert Solution().isArraySpecial([4, 3, 1, 6]) == False