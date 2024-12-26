class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Dictionary to store character frequencies
        char_count = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            # Shrink the window if there are more than k distinct characters
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            # Update the maximum length of substring found
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example usage
sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))  # Output: 3
print(sol.lengthOfLongestSubstringKDistinct("aa", 1))     # Output: 2