class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        stack = []
        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1

            stack.append(digit)

        final_stack = stack[:-k] if k else stack
        result = ''.join(final_stack).lstrip('0')

        return result if result else '0'