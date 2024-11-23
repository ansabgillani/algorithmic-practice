class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Step 1: Apply gravity to each row in the original grid
        for row in boxGrid:
            i = len(row) - 1
            j = len(row) - 1
            while j >= 0:
                if row[j] == '#':
                    row[i], row[j] = row[j], row[i]
                    i -= 1
                elif row[j] == '*':
                    i = j - 1
                j -= 1
        
        # Step 2: Rotate the grid 90 degrees clockwise
        rotated = []
        for col in range(len(boxGrid[0])):
            new_row = []
            for row in reversed(boxGrid):
                new_row.append(row[col])
            rotated.append(new_row)
        
        return rotated