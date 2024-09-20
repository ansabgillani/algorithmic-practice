class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Returns the shortest palindrome by adding characters in front of the given string.
        
        Args:
            s (str): The input string to be transformed into a palindrome.
            
        Returns:
            str: The shortest palindrome that can be formed.
        """
        if not s:
            return ""
        
        rev_s = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s