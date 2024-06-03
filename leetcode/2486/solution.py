class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Initialize pointers for both strings
        i, j = 0, 0
        
        # Iterate through the string s
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1  # Move to the next character in t
            i += 1  # Always move to the next character in s
        
        # The number of characters needed is the remaining length of t
        return len(t) - j

# Test cases
print(Solution().appendCharacters("coaching", "coding"))  # Output: 4
print(Solution().appendCharacters("abcde", "a"))          # Output: 0
print(Solution().appendCharacters("z", "abcde"))        # Output: 5