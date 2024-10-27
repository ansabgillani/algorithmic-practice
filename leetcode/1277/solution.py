class Solution:
    def countSquares(self, matrix):
        # Initialize result counter to 0
        result = 0
        
        # Get the number of rows and columns in the matrix
        row, column = len(matrix), len(matrix[0])
        
        # Iterate over each cell in the matrix
        for i in range(row):
            for j in range(column):
                # If the current cell is 1, check possible squares starting from this cell
                if matrix[i][j]:
                    # Calculate the size of the square with all ones ending at the current cell
                    size = min([row - i, column - j])
                    
                    # Check each possible size of the square
                    for k in range(1, size + 1):
                        flag = True
                        # If any cell in this square is zero, then it's not a square with all ones
                        for x in range(i, i + k):
                            for y in range(j, j + k):
                                if matrix[x][y] == 0:
                                    flag = False
                                    break
                            if not flag: 
                                break
                        # If the current configuration is a valid square, increment the result
                        if flag: 
                            result += 1
        
        return result