class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Finds all start indices of `p`'s anagrams in `s`.
        
        Args:
        s (str): The main string to search within.
        p (str): The pattern to find anagrams of.
        
        Returns:
        List[int]: A list of starting indices where an anagram of `p` is found in `s`.
        """
        from collections import Counter
        
        # Initialize the result list and counters
        res = []
        p_count = Counter(p)
        s_count = Counter()
        
        # Slide the window over the string `s`
        for i in range(len(s)):
            s_count[s[i]] += 1
            
            # Remove the leftmost character if window size exceeds pattern length
            if i >= len(p):
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    s_count[s[i - len(p)]] -= 1
            
            # Compare current window counter with the pattern counter
            if s_count == p_count:
                res.append(i - len(p) + 1)
        
        return res

# Test cases
solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))  # Output: [0,6]
print(solution.findAnagrams("abab", "ab"))        # Output: [0,1,2]