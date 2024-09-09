class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directionIndex = 0
        
        row, col = 0, 0
        
        while head:
            result[row][col] = head.val
            head = head.next

            newRow, newCol = row + directions[directionIndex][0], col + directions[directionIndex][1]
            
            if not (0 <= newRow < m and 0 <= newCol < n) or result[newRow][newCol] != -1:
                directionIndex = (directionIndex + 1) % 4
                newRow, newCol = row + directions[directionIndex][0], col + directions[directionIndex][1]
            
            row, col = newRow, newCol
        
        return result