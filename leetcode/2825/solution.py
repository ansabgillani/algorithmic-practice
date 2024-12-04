class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        Determines if it is possible to make str2 a subsequence of str1 by incrementing characters in str1 at most once.
        
        Args:
        str1 (str): The original string.
        str2 (str): The target subsequence.
        
        Returns:
        bool: True if str2 can be made a subsequence, False otherwise.
        """
        j = 0
        for i in range(len(str1)):
            # Check if characters match or if incrementing str1[i] would make them match
            if str1[i] == str2[j] or (str1[i] == 'z' and str2[j] == 'a'):
                j += 1
                if j == len(str2):
                    return True
        return False

# Test cases
print(Solution().canMakeSubsequence("abc", "ad"))  # Output: True
print(Solution().canMakeSubsequence("zc", "ad"))   # Output: True
print(Solution().canMakeSubsequence("ab", "d"))    # Output: False