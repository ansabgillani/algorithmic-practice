class Solution:
    def longestPalindrome(self, s):
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        length = 0
        odd_found = False
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length

# Test the method
solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Output: 7
print(solution.longestPalindrome("a"))         # Output: 1