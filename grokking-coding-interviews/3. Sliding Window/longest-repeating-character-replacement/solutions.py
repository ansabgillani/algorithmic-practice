class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring containing the same letter after performing at most k replacements.
        
        Args:
        s (str): The input string.
        k (int): The maximum number of allowed replacements.
        
        Returns:
        int: The length of the longest possible substring with the same character after replacements.
        """
        # Dictionary to store frequency of characters in the current window
        char_frequency = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            char_frequency[s[end]] = char_frequency.get(s[end], 0) + 1
            
            # The length of the window is between 'start' and 'end', which is end - start + 1.
            # max_char_count gives us the count of the most frequent character in this window.
            max_char_count = max(char_frequency.values())
            
            # If the number of characters to be replaced (window_length - max_char_count)
            # is more than k, then shrink the window from the start
            if (end - start + 1 - max_char_count > k):
                char_frequency[s[start]] -= 1
                if not char_frequency[s[start]]:
                    del char_frequency[s[start]]
                start += 1
            
            # Update the maximum length found so far
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example usage:
# sol = Solution()
# print(sol.characterReplacement("AABABBA", 2))  # Output: 4