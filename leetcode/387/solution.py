class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Finds the index of the first unique character in a string.
        
        Args:
        s (str): The input string consisting of lowercase English letters.
        
        Returns:
        int: The index of the first non-repeating character, or -1 if no such character exists.
        """
        # Dictionary to store the frequency of each character
        char_count = {}
        
        # First pass to count the occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Second pass to find the first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character is found, return -1
        return -1