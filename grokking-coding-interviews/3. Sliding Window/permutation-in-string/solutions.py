from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1.
        
        :param s1: The string containing characters to be permuted.
        :param s2: The string in which to search for permutations of s1.
        :return: True if any permutation of s1 is a substring of s2, False otherwise.
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False
        
        # Count characters in the first window of s2
        s2_count = Counter(s2[:len_s1])
        s1_count = Counter(s1)
        
        # Check if the count matches for the initial window
        if s2_count == s1_count:
            return True
        
        # Slide the window across s2 and compare counts
        for i in range(len_s1, len_s2):
            s2_count[s2[i]] += 1
            s2_count[s2[i - len_s1]] -= 1
            
            # Remove characters that have a count of zero
            if s2_count[s2[i - len_s1]] == 0:
                del s2_count[s2[i - len_s1]]
            
            # Check if the current window matches the count of s1
            if s2_count == s1_count:
                return True
        
        return False