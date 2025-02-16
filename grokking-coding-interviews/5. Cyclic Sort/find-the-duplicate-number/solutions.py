class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in the given array using Floyd's Tortoise and Hare (Cycle Detection) algorithm.
        
        Time complexity: O(n)
        Space complexity: O(1)
        
        :param nums: List of integers with one duplicate
        :return: The duplicate integer
        """
        # Phase 1: Finding the intersection point of the two runners
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Finding the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

# Test cases
test_cases = [
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([1, 1], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 9)
]

# Check function
def check_solution():
    solution = Solution()
    for nums, expected in test_cases:
        assert solution.findDuplicate(nums) == expected, f"Failed for input: {nums}"
    print("All test cases passed!")

check_solution()