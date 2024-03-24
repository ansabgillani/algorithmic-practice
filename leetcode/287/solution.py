class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in the array without modifying the array and using constant extra space.
        
        The approach uses Floyd's Tortoise and Hare (Cycle Detection) algorithm which has O(n) time complexity
        and O(1) space complexity.
        
        :param nums: List of integers containing n+1 integers where each integer is in the range [1, n]
        :return: The repeated number in the array
        """
        # Initialize two pointers slow and fast
        slow = nums[0]
        fast = nums[0]
        
        # Phase 1: Finding the intersection point of the two runners
        while True:
            slow = nums[slow]  # Move one step at a time
            fast = nums[nums[fast]]  # Move two steps at a time
            if slow == fast:
                break
        
        # Phase 2: Finding the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]  # Move one step at a time
            fast = nums[fast]  # Move one step at a time
        
        return slow

# Example usage:
# sol = Solution()
# print(sol.findDuplicate([1,3,4,2,2]))  # Output: 2
# print(sol.findDuplicate([3,1,3,4,2]))  # Output: 3
# print(sol.findDuplicate([3,3,3,3,3]))  # Output: 3