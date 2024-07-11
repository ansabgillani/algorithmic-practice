class Solution:
    def reverseParentheses(self, s):
        stack = []
        result = ''
        
        for c in s:
            if c == '(':
                stack.append(result)
                result = ''
            elif c == ')':
                prev = stack.pop()
                result = prev + result[::-1]
            else:
                result += c
                
        return result