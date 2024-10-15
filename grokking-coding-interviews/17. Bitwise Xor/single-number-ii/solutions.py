class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the element that appears exactly once in a list where all other elements appear three times.
        
        This function uses bitwise operations to achieve O(1) space complexity and linear time complexity.
        
        :param nums: List of integers where every element appears three times except for one.
        :return: The single number that appears only once.
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

# Test cases
def test_singleNumber():
    assert Solution().singleNumber([2, 2, 3, 2]) == 3
    assert Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
    print("All tests passed.")

test_singleNumber()