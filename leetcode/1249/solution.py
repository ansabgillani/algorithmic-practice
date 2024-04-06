class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        s = list(s)
        
        # First pass: find and mark invalid ')'
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    s[i] = ''  # Mark for deletion
                else:
                    stack.pop()
                    
        # Second pass: remove unmatched '(' using the indices stored in stack
        while stack:
            del s[stack.pop()]
    
        return ''.join(s)