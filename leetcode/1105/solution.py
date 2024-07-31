def minHeightShelves(books, shelfWidth):
    """
    :type books: List[List[int]]
    :type shelfWidth: int
    :rtype: int
    """
    n = len(books)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        height = 0
        width = 0
        for j in range(i - 1, -1, -1):
            width += books[j][0]
            if width > shelfWidth:
                break
            height = max(height, books[j][1])
            dp[i] = min(dp[i], dp[j] + height)

    return dp[n]

# Example usage:
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
print(minHeightShelves(books, shelfWidth))  # Output: 6

books = [[1,3],[2,4],[3,2]]
shelfWidth = 6
print(minHeightShelves(books, shelfWidth))  # Output: 4