class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Calculate the score of a string based on the sum of absolute differences 
        between ASCII values of adjacent characters.
        
        :param s: Input string consisting only of lowercase English letters.
        :return: The calculated score of the string.
        """
        return sum(abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s)))