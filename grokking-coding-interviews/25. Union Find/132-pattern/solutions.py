class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Finds if there exists a 132 pattern in the given array of integers.
        
        A 132 pattern is defined as three indices i, j, k such that i < j < k and
        nums[i] < nums[k] < nums[j].
        
        Args:
            nums: List[int] - The input list of integers.
            
        Returns:
            bool - True if a 132 pattern exists, False otherwise.
        """
        stack = []  # Stack to keep track of potential 'k' values
        third = float('-inf')  # Initialize the 'third' element
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:
                return True  # Found the pattern
            while stack and stack[-1] < nums[i]:
                third = stack.pop()  # Update 'third' to be the largest value smaller than nums[i]
            stack.append(nums[i])
        
        return False  # No pattern found

# Example usage
solution = Solution()
print(solution.find132pattern([1,2,3,4]))  # Output: False
print(solution.find132pattern([3,1,4,2]))  # Output: True
print(solution.find132pattern([-1,3,2,0]))  # Output: True