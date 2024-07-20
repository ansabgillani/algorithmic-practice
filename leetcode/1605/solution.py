class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                value = min(rowSum[i], colSum[j])
                result[i][j] = value
                rowSum[i] -= value
                colSum[j] -= value
        
        return result

# Example usage:
# sol = Solution()
# print(sol.restoreMatrix([3, 8], [4, 7]))  # Output: [[3, 0], [1, 7]]
# print(sol.restoreMatrix([5, 7, 10], [8, 6, 8]))  # Output: [[0, 5, 0], [6, 1, 0], [2, 0, 8]]