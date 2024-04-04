class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        current_depth = 0

        for char in s:
            if char == '(':
                current_depth += 1
                depth = max(depth, current_depth)
            elif char == ')':
                current_depth -= 1

        return depth