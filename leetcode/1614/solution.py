class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Returns the maximum nesting depth of a valid parentheses string.
        
        :param s: A valid parentheses string consisting of digits and +,-,*,/,(,), and VPS is guaranteed.
        :return: The maximum nesting depth of the parentheses in the string.
        """
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth

# Example usage:
solution = Solution()
print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3
print(solution.maxDepth("((()))"))  # Output: 3