class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Initialize a stack to keep track of potential 'k' values
        stack = []
        # Initialize the variable 's2' to store the maximum 'j' value found so far
        s2 = float('-inf')
        
        # Iterate over the list in reverse order
        for num in reversed(nums):
            # Check if we have found a valid 132 pattern
            if num < s2:
                return True
            # Maintain the stack to keep it sorted and update 's2' accordingly
            while stack and stack[-1] < num:
                s2 = stack.pop()
            stack.append(num)
        
        # If no valid pattern is found, return False
        return False