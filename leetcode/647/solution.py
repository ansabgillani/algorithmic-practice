class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts all palindromic substrings in the given string.
        
        :param s: The input string to search for palindromic substrings.
        :return: The number of palindromic substrings.
        """
        n = len(s)
        count = 0
        
        # Helper function to expand around the center
        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                nonlocal count
                count += 1
                left -= 1
                right += 1
        
        # Check for odd length palindromes
        for i in range(n):
            expand_around_center(i, i)
        
        # Check for even length palindromes
        for i in range(n - 1):
            expand_around_center(i, i + 1)
        
        return count

# Example usage:
sol = Solution()
print(sol.countSubstrings("abc"))  # Output: 3
print(sol.countSubstrings("aaa"))  # Output: 6