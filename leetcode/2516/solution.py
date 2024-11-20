class Solution:
    def takeKOfEachCharacter(self, s: str, k: int) -> int:
        count = [s.count('a'), s.count('b'), s.count('c')]
        
        if min(count) < k:
            return -1
        
        n = len(s)
        ans = float('inf')
        
        for mid_length in range(3 * k + 1):
            left = right = mid_length // 3
            remaining = mid_length % 3
            
            if left <= count[0] and right <= count[1] and remaining <= count[2]:
                ans = min(ans, n - (mid_length + mid_length))
    
        return ans if ans != float('inf') else -1