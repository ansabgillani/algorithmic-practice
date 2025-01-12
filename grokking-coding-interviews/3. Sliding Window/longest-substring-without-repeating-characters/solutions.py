class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        
        :param s: Input string
        :return: Length of the longest substring without repeating characters
        """
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            else:
                max_length = max(max_length, right - left + 1)
            
            char_map[s[right]] = right
        
        return max_length

# Test cases
print(Solution().lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(Solution().lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(Solution().lengthOfLongestSubstring("pwwkew"))    # Output: 3