class Solution:
    def findDuplicate(self, nums):
        slow = fast = nums[0]  # Initialize two pointers
        
        # Phase 1: Finding the intersection point of the two runners
        while True:
            slow = nums[slow]       # Move slow pointer by one step
            fast = nums[nums[fast]] # Move fast pointer by two steps
            if slow == fast:
                break
        
        # Phase 2: Finding the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]       # Move both pointers by one step
            fast = nums[fast]
        
        return slow                # The duplicate number is found