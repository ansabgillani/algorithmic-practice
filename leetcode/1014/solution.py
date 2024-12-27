class Solution:
    def maxSightseeingPair(self, values):
        max_score, max_i = 0, 0
        for j in range(1, len(values)):
            max_score = max(max_score, values[max_i] + values[j] - j + i)
            if values[i] + i > values[max_i] + max_i:
                max_i = i
        return max_score

# Example usage:
sol = Solution()
print(sol.maxSightseeingPair([8,1,5,2,6]))  # Output: 11
print(sol.maxSightseeingPair([1,2]))        # Output: 2