class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Find the shortest common supersequence of two strings.

        Args:
        str1 (str): First input string.
        str2 (str): Second input string.

        Returns:
        str: The shortest common supersequence.
        """
        m, n = len(str1), len(str2)
        
        # Create a 2D DP table to store lengths of shortest common supersequences
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Reconstruct the shortest common supersequence from the DP table
        i, j = m, n
        result = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str1[i - 1])
                i -= 1
            else:
                result.append(str2[j - 1])
                j -= 1
        
        # Append remaining characters of str1 and str2
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        
        return ''.join(result[::-1])

# Example usage:
solution = Solution()
print(solution.shortestCommonSupersequence("abac", "cab"))  # Output: "cabac"
print(solution.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))  # Output: "aaaaaaaa"