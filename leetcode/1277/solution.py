class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Counts all square submatrices with all ones in a given binary matrix.
        
        Args:
            matrix (List[List[int]]): A 2D list representing the binary matrix.
            
        Returns:
            int: The total number of square submatrices with all ones.
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]
                    
        return count

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    matrix1 = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    print(solution.countSquares(matrix1))  # Output: 15
    
    # Example 2
    matrix2 = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(solution.countSquares(matrix2))  # Output: 7