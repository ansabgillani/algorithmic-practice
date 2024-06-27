class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns indices of the two numbers such that they add up to the target.
        
        Args:
            nums (List[int]): The list of integers.
            target (int): The target sum.
            
        Returns:
            List[int]: Indices of the two numbers that add up to the target.
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        raise ValueError("No two sum solution")

# Test cases to verify the solution
def test_two_sum():
    assert Solution().twoSum([2,7,11,15], 9) == [0, 1], "Test case 1 failed"
    assert Solution().twoSum([3,2,4], 6) == [1, 2], "Test case 2 failed"
    assert Solution().twoSum([3,3], 6) == [0, 1], "Test case 3 failed"

test_two_sum()