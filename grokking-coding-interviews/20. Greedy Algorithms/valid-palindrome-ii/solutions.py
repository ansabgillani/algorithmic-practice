class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Determines if a string can be a palindrome after deleting at most one character from it.
        
        Args:
        s (str): The input string to check.
        
        Returns:
        bool: True if the string can be a palindrome with at most one deletion, False otherwise.
        """
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try deleting either the character at 'left' or 'right'
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        
        return True

# Test cases
print(Solution().validPalindrome("aba"))  # True
print(Solution().validPalindrome("abca"))  # True
print(Solution().validPalindrome("abc"))  # False