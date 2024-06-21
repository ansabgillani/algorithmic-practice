class Solution:
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
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

# Test cases to verify the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    print(solution.sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
    
    # Example 2
    print(solution.sortedSquares([-7, -3, 2, 3, 11]))  # Output: [4, 9, 9, 49, 121]