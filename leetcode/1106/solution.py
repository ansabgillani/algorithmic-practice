class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        def eval_expr(expr):
            if expr == 't':
                return True
            elif expr == 'f':
                return False
        
        for char in expression:
            if char == '(' or char == ',':
                continue
            elif char == 't' or char == 'f':
                stack.append(eval_expr(char))
            elif char == '!':
                result = not stack.pop()
                stack.append(result)
            else:  # AND, OR operators
                right = stack.pop()
                left = stack.pop()
                if char == '&':
                    result = left and right
                elif char == '|':
                    result = left or right
                stack.append(result)
        
        return stack[0]

# Example usage:
sol = Solution()
print(sol.parseBoolExpr("&(|(f))"))  # Output: False
print(sol.parseBoolExpr("|(f,f,f,t)"))  # Output: True
print(sol.parseBoolExpr("!(&&(f,t))"))  # Output: True