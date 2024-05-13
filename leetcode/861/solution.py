class Solution:
    def matrixScore(self, A):
        # Flip rows to ensure all rows start with 1
        for row in A:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        
        # Flip columns if the number of zeros is greater than ones in a column
        for col in range(1, len(A[0])):
            num_zeros = sum(1 for row in A if row[col] == 0)
            if num_zeros > len(A) / 2:
                for row in A:
                    row[col] = 1 - row[col]
        
        # Calculate the score
        score = 0
        for i in range(len(A)):
            score += int(''.join(map(str, A[i])), 2)
        
        return score