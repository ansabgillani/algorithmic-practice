class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Removes k digits from a non-negative integer represented as a string to form the smallest possible number.
        
        :param num: String representing a non-negative integer
        :param k: Integer indicating the number of digits to remove
        :return: Smallest possible number after removing k digits, as a string
        """
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If there are still digits to remove, remove them from the end
        final_stack = stack[:-k] if k else stack
        
        # Remove leading zeros
        result = ''.join(final_stack).lstrip('0')
        
        # Return '0' if result is empty after removing zeros
        return result if result else '0'