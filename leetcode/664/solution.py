class Solution:
    def strangePrinter(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Iterate over the length of substrings from 1 to n
        for length in range(1, n + 1):
            # Iterate over starting index of substring from 0 to n-length+1
            for start in range(n - length + 1):
                end = start + length - 1
                dp[start][end] = length
                # Iterate over the substring to find if there is a character that can be used to merge
                for k in range(start, end):
                    if s[k] == s[end]:
                        dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end-1])
        
        # Return the minimum number of turns needed to print the string from index 0 to n-1
        return dp[0][n-1]