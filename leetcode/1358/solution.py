class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Initialize pointers and count
        left = 0
        right = 0
        count = 0
        
        # Dictionary to track the last occurrence of 'a', 'b', and 'c'
        char_map = {'a': -1, 'b': -1, 'c': -1}
        
        # Iterate over the string with the right pointer
        while right < len(s):
            # Update the last occurrence of the current character
            char_map[s[right]] = right
            
            # Check if all three characters have been seen at least once
            if min(char_map.values()) != -1:
                # Calculate the number of valid substrings ending at 'right'
                count += min(char_map.values()) + 1
                
                # Move the left pointer to find the smallest window containing all three characters
                left += 1
            
            # Move the right pointer
            right += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.numberOfSubstrings("abcabc"))  # Output: 10