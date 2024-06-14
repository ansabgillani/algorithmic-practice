class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        Sorts the array and uses a greedy approach to ensure all elements are unique.
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) as we are modifying the input in place
        """
        if not nums:
            return 0
        
        nums.sort()
        moves = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment
        
        return moves

# Example usage:
# solution = Solution()
# print(solution.minIncrementForUnique([1,2,2]))  # Output: 1
# print(solution.minIncrementForUnique([3,2,1,2,1,7]))  # Output: 6