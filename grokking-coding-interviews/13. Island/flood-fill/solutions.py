from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and image[nx][ny] == original_color:
                    queue.append((nx, ny))
                    image[nx][ny] = color
        
        return image

# Example usage:
solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))  # Output: [[2,2,2],[2,2,0],[2,0,1]]
print(solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))      # Output: [[0,0,0],[0,0,0]]