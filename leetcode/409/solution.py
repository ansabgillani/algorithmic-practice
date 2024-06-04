class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Calculate the length of the longest palindrome that can be built with the given letters.
        
        :param s: String consisting of lowercase or uppercase letters
        :return: Length of the longest possible palindrome
        
        This solution uses a hash map to count the frequency of each character. 
        For each character, if its frequency is even, it can be fully used in the palindrome.
        If odd, we use (frequency - 1) which is even, and add one to the result if there's at least one odd frequency char.
        
        Time complexity: O(n), where n is the length of the string
        Space complexity: O(1), since the hash map will contain at most 52 entries (all letters)
        """
        from collections import Counter
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        
        length = 0
        odd_found = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        # If there's at least one character with an odd frequency, we can add one more to the result
        return length + (1 if odd_found else 0)