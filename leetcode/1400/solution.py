from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        Determines if all characters in 's' can be used to construct 'k' non-empty palindrome strings.
        
        :param s: Input string consisting of lowercase English letters.
        :param k: Number of palindrome strings to construct.
        :return: True if it's possible, False otherwise.
        """
        if len(s) < k:
            return False
        
        char_count = Counter(s)
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        return odd_count <= k