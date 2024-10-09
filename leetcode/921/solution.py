class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = close_count = 0
        
        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
                    
        return open_count + close_count