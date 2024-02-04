class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        # Initialize character counts
        target_count = Counter(t)
        window_count = Counter()
        
        left, right = 0, 0
        formed = 0
        required = len(target_count)
        
        min_len = float('inf')
        min_left = min_right = -1
        
        while right < len(s):
            character = s[right]
            window_count[character] += 1
            
            if character in target_count and window_count[character] == target_count[character]:
                formed += 1
            
            while left <= right and formed == required:
                character = s[left]
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left, min_right = left, right
                
                window_count[character] -= 1
                if character in target_count and window_count[character] < target_count[character]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return s[min_left:min_right + 1] if min_len != float('inf') else ""