class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store character counts
        char_count = {}
        
        # First pass to count characters
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Second pass to find the first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character is found
        return -1

# Test cases
solution = Solution()
print(solution.firstUniqChar("leetcode"))  # Output: 0
print(solution.firstUniqChar("loveleetcode"))  # Output: 2
print(solution.firstUniqChar("aabbcc"))  # Output: -1