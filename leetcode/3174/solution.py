class Solution:
    def clearDigits(self, s: str) -> str:
        # Initialize a stack to keep track of non-digit characters
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if not char.isdigit():
                # If the character is not a digit, push it onto the stack
                stack.append(char)
            elif stack:
                # If the character is a digit and there's a non-digit on the stack, pop the non-digit
                stack.pop()
        
        # Join the characters in the stack to form the resulting string
        return ''.join(stack)