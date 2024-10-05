from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1.
        
        Args:
        s1 (str): The first string.
        s2 (str): The second string.
        
        Returns:
        bool: True if s2 contains a permutation of s1, False otherwise.
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False
        
        # Initialize character count dictionaries
        s1_count = Counter(s1)
        s2_count = Counter()
        
        # Slide the window over s2
        for i in range(len_s2):
            # Add current character to s2_count
            s2_count[s2[i]] += 1
            
            # Remove character that is left out of the window
            if i >= len_s1:
                if s2_count[s2[i - len_s1]] == 1:
                    del s2_count[s2[i - len_s1]]
                else:
                    s2_count[s2[i - len_s1]] -= 1
            
            # Check if current window matches the count of s1
            if s1_count == s2_count:
                return True
        
        return False

# Example usage:
# sol = Solution()
# print(sol.checkInclusion("ab", "eidbaooo"))  # Output: True
# print(sol.checkInclusion("ab", "eidboaoo"))  # Output: False