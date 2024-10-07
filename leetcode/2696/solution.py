class Solution:
    def minLength(self, s: str) -> int:
        """
        Removes all occurrences of "AB" and "CD" from the string until no more such substrings exist.
        
        Parameters:
        s (str): The input string consisting only of uppercase English letters.
        
        Returns:
        int: The minimum possible length of the resulting string after removing all "AB" and "CD" substrings.
        """
        stack = []
        for char in s:
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)

# Example usage:
# solution = Solution()
# print(solution.minLength("ABFCACDB"))  # Output: 2
# print(solution.minLength("ACBBD"))    # Output: 5