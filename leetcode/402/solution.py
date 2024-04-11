class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Removes k digits from a non-negative integer represented as a string to form the smallest possible number.
        
        Args:
        num (str): The input string representing a non-negative integer.
        k (int): The number of digits to remove.
        
        Returns:
        str: The smallest possible integer after removing k digits.
        """
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove the remaining k digits if any
        final_stack = stack[:-k] if k else stack
        
        # Convert list to string, remove leading zeros, and return
        result = ''.join(final_stack).lstrip('0')
        return result if result else '0'