class Solution(object):
    def canConstruct(self, s, k):
        """
        Check if all characters in s can be used to construct k palindrome strings.
        
        :type s: str
        :type k: int
        :rtype: bool
        """
        # Early return based on length and k
        if len(s) < k:
            return False
        
        # Count the frequency of each character
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        # Calculate the number of characters with odd counts
        odd_chars = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # The number of palindromes we can form is at least half the number of characters with odd counts
        return k >= odd_chars and k <= len(s)

# Example usage:
sol = Solution()
print(sol.canConstruct("annabelle", 2))  # Output: True
print(sol.canConstruct("leetcode", 3))   # Output: False
print(sol.canConstruct("true", 4))       # Output: True