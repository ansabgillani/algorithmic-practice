class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Initialize an array to store the length of the longest ideal subsequence ending at each character
        dp = [0] * 26
        
        # Iterate through each character in the string
        for char in s:
            index = ord(char) - ord('a')
            # Update the DP value for the current character
            dp[index] += 1
            # Check the characters within the allowed difference and update if a longer subsequence is found
            for j in range(max(0, index - k), min(26, index + k + 1)):
                if j != index:
                    dp[index] = max(dp[index], dp[j])
        
        # Return the maximum value from the DP array which represents the length of the longest ideal subsequence
        return max(dp)