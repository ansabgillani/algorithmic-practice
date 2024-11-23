class Solution:
    def rotateTheBox(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Apply gravity to each row before rotation
        for i in range(m):
            last_j = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '#':
                    boxGrid[i][j], boxGrid[i][last_j] = boxGrid[i][last_j], boxGrid[i][j]
                    last_j -= 1
                elif boxGrid[i][j] == '*':
                    last_j = j - 1
                    
        # Rotate the box 90 degrees clockwise
        rotated_grid = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_grid[j][m-1-i] = boxGrid[i][j]
        
        return rotated_grid