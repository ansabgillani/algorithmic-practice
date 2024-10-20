class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        current = ""
        
        for char in expression:
            if char == "," or char == ")":
                if current != "":
                    stack.append(current)
                    current = ""
            elif char != "(":
                current += char
            
            # Evaluate when closing parenthesis is found
            if char == ")":
                subexpressions = []
                while stack[-1] != "(":
                    subexpressions.append(stack.pop())
                stack.pop()  # Remove the opening '(' from the stack
                
                operation = stack.pop()
                result = None
                
                if operation == "!":
                    result = not self.parseBoolExpr(subexpressions[0])
                elif operation == "&":
                    result = all(self.parseBoolExpr(expr) for expr in subexpressions)
                elif operation == "|":
                    result = any(self.parseBoolExpr(expr) for expr in subexpressions)
                
                stack.append(str(result))
        
        return bool(int(stack.pop()))