class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Helper function to evaluate two numbers using a given operator
        def eval(a, b, op):
            if op == '+': return a + b
            elif op == '-': return a - b
            else: return a * b

        # Dictionary to store results of subproblems for memoization
        memo = {}

        # Recursive function to compute all possible results
        def dp(expr):
            if expr.isdigit():
                return [int(expr)]
            if expr in memo:
                return memo[expr]

            result = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left_results = dp(expr[:i])
                    right_results = dp(expr[i+1:])
                    result.extend(eval(a, b, char) for a in left_results for b in right_results)

            memo[expr] = result
            return result

        return dp(expression)