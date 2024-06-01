class Solution:
    def calculate_score(self, s):
        score = 0
        for i in range(len(s) - 1):
            diff = abs(ord(s[i]) - ord(s[i+1]))
            score += diff
        return score

# Example usage:
solution = Solution()
print(solution.calculate_score("hello"))  # Output: 13
print(solution.calculate_score("zaz"))  # Output: 50