class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""
        
        for char in s:
            if char == '(':
                stack.append(current)
                current = ""
            elif char == ')':
                reversed_current = current[::-1]
                current = stack.pop() + reversed_current
            else:
                current += char
        
        return current

# Example usage:
# solution = Solution()
# print(solution.reverseParentheses("(abcd)"))  # Output: "dcba"
# print(solution.reverseParentheses("(u(love)i)"))  # Output: "iloveu"
# print(solution.reverseParentheses("(ed(et(oc))el)"))  # Output: "leetcode"