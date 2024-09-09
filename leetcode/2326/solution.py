class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the matrix with -1
        result = [[-1] * n for _ in range(m)]
        
        # Directions for right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c, dir_idx = 0, 0, 0
        
        while head:
            result[r][c] = head.val
            
            # Calculate the next position
            nr, nc = r + directions[dir_idx][0], c + directions[dir_idx][1]
            
            # Check if the next position is out of bounds or already filled
            if nr < 0 or nr >= m or nc < 0 or nc >= n or result[nr][nc] != -1:
                dir_idx = (dir_idx + 1) % 4  # Change direction
            
            # Move to the next position
            r, c = r + directions[dir_idx][0], c + directions[dir_idx][1]
            
            head = head.next
        
        return result