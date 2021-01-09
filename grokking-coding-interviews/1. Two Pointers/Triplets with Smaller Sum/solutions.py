class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Finds the number of index triplets (i, j, k) with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
        
        Parameters:
        - nums (List[int]): The list of integers.
        - target (int): The target sum for the triplets.
        
        Returns:
        - int: The number of valid triplets.
        """
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    # All pairs (left, left+1), ..., (right-1) are valid with nums[i]
                    count += right - left
                    left += 1
                else:
                    right -= 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.threeSumSmaller([-2,0,1,3], 2))  # Output: 2
# print(sol.threeSumSmaller([], 0))          # Output: 0
# print(sol.threeSumSmaller([0], 0))         # Output: 0