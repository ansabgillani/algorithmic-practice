class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # Flip rows to ensure the first column is all 1s
        for row in A:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        
        # Flip columns if necessary to maximize the score
        for col in range(1, len(A[0])):
            count = sum(A[row][col] for row in range(len(A)))
            if count < len(A) / 2:
                for row in range(len(A)):
                    A[row][col] = 1 - A[row][col]
        
        # Calculate the score
        score = 0
        for row in A:
            score += int(''.join(map(str, row)), 2)
        
        return score

# Example usage:
solution = Solution()
print(solution.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))  # Output: 39