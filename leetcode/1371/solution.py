from collections import defaultdict

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Dictionary to store the first occurrence of each state
        char_state_map = {0: -1}
        current_state = 0
        max_length = 0
        
        for i, c in enumerate(s):
            if c in "aeiou":
                # Toggle the bit corresponding to the vowel
                current_state ^= 1 << (ord(c) - ord('a'))
            
            if current_state in char_state_map:
                # Calculate the length of substring from the first occurrence of this state
                max_length = max(max_length, i - char_state_map[current_state])
            else:
                # Store the first occurrence of this state
                char_state_map[current_state] = i
        
        return max_length

# Example usage:
sol = Solution()
print(sol.findTheLongestSubstring("eleetminicoworoep"))  # Output: 13
print(sol.findTheLongestSubstring("leetcodeisgreat"))     # Output: 5
print(sol.findTheLongestSubstring("bcbcbc"))              # Output: 6