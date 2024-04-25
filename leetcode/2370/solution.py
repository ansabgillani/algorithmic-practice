class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            max_length = 1
            
            for j in range(max(0, index - k), min(26, index + k + 1)):
                if abs(j - index) <= k:
                    max_length = max(max_length, dp[j] + 1)
        
            dp[index] = max_length
        
        return max(dp)