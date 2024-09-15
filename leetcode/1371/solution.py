class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        count = {char: 0 for char in 'aeiou'}
        start_index = {tuple(count.values()): -1}
        max_length = 0

        for i, char in enumerate(s):
            if char in 'aeiou':
                count[char] ^= 1
            
            current_state = tuple(count.values())
            
            if current_state in start_index:
                max_length = max(max_length, i - start_index[current_state])
            else:
                start_index[current_state] = i
        
        return max_length