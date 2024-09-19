class Solution:
    def diffWaysToCompute(self, expression):
        # Helper function to evaluate expression parts
        def evaluate(left, right, operator):
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            else:
                return left * right
        
        # Base case: single number
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for i in range(len(expression)):
            # Check for operators
            if expression[i] in "+-*":
                # Recursively compute results for the left and right parts of the expression
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Evaluate all combinations of results from left and right parts
                for left in left_results:
                    for right in right_results:
                        results.append(evaluate(left, right, expression[i]))
        
        return results