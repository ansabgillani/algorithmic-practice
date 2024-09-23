class Solution:
    def minExtraChar(self, s, dictionary):
        dp = [len(s)] * (len(s) + 1)
        dp[0] = 0
        word_set = set(dictionary)
        
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i, -1, -1):
                prefix = s[j:i]
                if prefix in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[-1]