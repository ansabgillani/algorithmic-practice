class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Counts the number of unique length-3 palindromic subsequences in a given string.
        
        :param s: Input string
        :return: Number of unique length-3 palindromic subsequences
        
        Algorithm:
        1. Track the first and last occurrence of each character.
        2. For each character, find all unique characters between its first and last occurrence.
        3. Count these unique characters as they form potential palindromes with the current character at both ends.
        """
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26
        
        # Track first and last occurrence of each character
        for i, char in enumerate(s):
            if first[ord(char) - ord('a')] == -1:
                first[ord(char) - ord('a')] = i
            last[ord(char) - ord('a')] = i
        
        count = 0
        
        # Check each character to see if it can form a palindrome with unique characters in between
        for i in range(26):
            if first[i] != -1 and last[i] != -1 and first[i] < last[i]:
                unique_chars = set(s[first[i]+1:last[i]])
                count += len(unique_chars)
        
        return count

# Example usage:
sol = Solution()
print(sol.countPalindromicSubsequence("aabca"))  # Output: 3
print(sol.countPalindromicSubsequence("adc"))    # Output: 0
print(sol.countPalindromicSubsequence("bbcbaba"))# Output: 4