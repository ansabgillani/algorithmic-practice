class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Squares each element in the sorted array and returns a new sorted array.
        
        This solution uses a two-pointer approach to achieve O(n) time complexity.
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        
        return result

# Example usage:
# solution = Solution()
# print(solution.sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]