class Solution:
    def nearestPalindromic(self, n):
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        
        length = len(n)
        lower, higher = 10 ** (length - 1) - 1, 10 ** length + 1
        
        num = int(n)
        
        candidate = lower
        while candidate > 1:
            if is_palindrome(candidate) and abs(candidate - num) < abs(lower - num):
                lower = candidate
            candidate -= 1
        
        candidate = higher
        while candidate < 10 ** (length + 1):
            if is_palindrome(candidate) and abs(candidate - num) < abs(higher - num):
                higher = candidate
            candidate += 1
        
        return str(lower) if num - lower < higher - num else str(higher)