class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        
        # Initialize the heights matrix
        heights = [[-1] * n for _ in range(m)]

        # Enqueue all water cells with height 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j))
                    heights[i][j] = 0

        while queue:
            x, y = queue.pop(0)
        
            # Explore all four directions from the current cell
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
            
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    queue.append((nx, ny))

        return heights