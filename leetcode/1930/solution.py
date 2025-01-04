class Solution:
    def countPalindromicSubsequence(self, s):
        char_positions = {char: [] for char in set(s)}
        
        for i, char in enumerate(s):
            char_positions[char].append(i)
        
        unique_count = 0
        
        for char in char_positions:
            if len(char_positions[char]) > 1:
                first, last = char_positions[char][0], char_positions[char][-1]
                unique_count += len(set(s[first+1:last]))
        
        return unique_count