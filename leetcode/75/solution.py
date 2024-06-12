from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts an array of 0's, 1's, and 2's in-place using the Dutch National Flag algorithm.
        
        :param nums: List of integers where each integer is either 0, 1, or 2.
        """
        low = mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Example usage:
# sol = Solution()
# sol.sortColors([2,0,2,1,1,0])
# print(sol.nums)  # Output: [0,0,1,1,2,2]

# Test cases
def check_solution():
    test_cases = [
        ([2,0,2,1,1,0], [0,0,1,1,2,2]),
        ([2,0,1], [0,1,2]),
        ([0,1,2], [0,1,2]),
        ([0,2,1], [0,1,2]),
        ([1,0,2], [0,1,2]),
        ([1,2,0], [0,1,2])
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        sol = Solution()
        sol.sortColors(nums)
        assert nums == expected, f"Test case {i+1} failed: expected {expected}, got {nums}"
        print(f"Test case {i+1} passed.")

check_solution()