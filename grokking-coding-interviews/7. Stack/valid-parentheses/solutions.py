class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold matching pairs of brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []
        
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in bracket_map:
                # If the stack is empty or the top of the stack doesn't match the corresponding opening bracket, return False
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                # If the character is not a valid bracket, return False
                return False
        
        # If the stack is empty, all brackets were matched; otherwise, return False
        return not stack

# Example usage
solution = Solution()
print(solution.isValid("()"))       # Output: True
print(solution.isValid("()[]{}"))   # Output: True
print(solution.isValid("(]"))       # Output: False
print(solution.isValid("([)]"))     # Output: False