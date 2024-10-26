class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Removes all adjacent duplicate letters from a string.
        
        Parameters:
            s (str): Input string consisting of lowercase English letters.
            
        Returns:
            str: Final string after removing all adjacent duplicates.
        """
        stack = []
        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
            elif stack and stack[-1] == char:
                stack.pop()
        return ''.join(stack)

# Test cases
print(Solution().removeDuplicates("abbaca"))  # Output: "ca"
print(Solution().removeDuplicates("azxxzy"))  # Output: "ay"