class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the given string.
        
        :param s: Input string consisting of words and spaces
        :type s: str
        :return: Length of the last word
        :rtype: int
        """
        # Strip leading and trailing spaces, then split by spaces
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1])