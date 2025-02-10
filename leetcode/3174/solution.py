class Solution:
    def clear_digits(self, s):
        stack = []
        
        for char in s:
            if not char.isdigit():
                stack.append(char)
            elif stack and not stack[-1].isdigit():
                stack.pop()
        
        return ''.join(stack)