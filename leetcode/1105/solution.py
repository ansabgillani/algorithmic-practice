class Solution:
    def minHeightShelves(self, books, shelf_width):
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            width, height = 0, 0
            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelf_width:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)

        return dp[-1]

# Test cases
sol = Solution()
print(sol.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))  # Output: 6
print(sol.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6))  # Output: 4