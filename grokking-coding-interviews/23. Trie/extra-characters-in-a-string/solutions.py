from typing import List
import collections

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # Create a set of words in the dictionary for quick lookup
        word_set = set(dictionary)
        
        # Initialize the DP array to store minimum extra characters up to each index
        dp = [0] * (len(s) + 1)
        
        # Iterate over each character in the string
        for i in range(1, len(s) + 1):
            # Assume the worst case: no word matches at this position
            dp[i] = dp[i - 1] + 1
            
            # Check all possible substrings ending at the current index
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[len(s)]