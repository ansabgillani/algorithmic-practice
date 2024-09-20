class Solution:
    def shortestPalindrome(self, s):
        rev_s = s[::-1]
        for i in range(len(s)):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s
        return ""