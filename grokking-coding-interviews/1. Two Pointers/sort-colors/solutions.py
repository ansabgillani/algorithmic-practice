class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the input list in-place using the Dutch National Flag algorithm.
        
        The algorithm uses three pointers to partition the array into three segments:
        0s, 1s, and 2s. It ensures that all 0s are on the left, all 2s are on the right,
        and all 1s are in between.
        
        Args:
        nums (List[int]): The list of integers to sort in-place.

        Returns:
        None: The function sorts the array in-place.
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
sol = Solution()
nums_example_1 = [2,0,2,1,1,0]
sol.sortColors(nums_example_1)
print(nums_example_1)  # Output: [0, 0, 1, 1, 2, 2]

nums_example_2 = [2,0,1]
sol.sortColors(nums_example_2)
print(nums_example_2)  # Output: [0, 1, 2]