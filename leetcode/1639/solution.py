class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words[0]), len(target)
        
        # Count the frequency of each character at each position in words
        count = [[0] * 26 for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                count[i][ord(char) - ord('a')] += 1
        
        # Initialize DP array where dp[j] is the number of ways to form target[:j+1]
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to form an empty string: by choosing nothing
        
        # Fill the DP array
        for i in range(m):
            for j in range(n - 1, -1, -1):
                char = target[j]
                index = ord(char) - ord('a')
                dp[j + 1] += dp[j] * count[i][index]
                dp[j + 1] %= MOD
        
        return dp[n]