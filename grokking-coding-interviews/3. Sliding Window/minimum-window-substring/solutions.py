from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of 's' such that every character in 't' (including duplicates)
        is included in the window.
        
        :param s: The source string
        :param t: The target string
        :return: The minimum window substring, or an empty string if no such substring exists
        """
        # Initialize counters for characters in t and the current window
        target_count = Counter(t)
        window_count = {}
        
        left = 0
        formed = 0
        required = len(target_count)
        
        min_len = float('inf')
        min_start = 0
        
        for right, char in enumerate(s):
            # Add the character to the current window count
            if char not in window_count:
                window_count[char] = 0
            window_count[char] += 1
            
            # If the character is part of t and its count matches the target count, increment formed
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            # Try to contract the window from the left as small as possible
            while left <= right and formed == required:
                char = s[left]
                
                # Update the minimum window if the current window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # Remove the character from the window count
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                
                left += 1
        
        return s[min_start:min_start+min_len] if min_len != float('inf') else ""