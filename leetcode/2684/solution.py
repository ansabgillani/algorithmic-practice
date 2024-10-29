class Solution:
    def maxMoves(self, grid):
        m, n = len(grid), len(grid[0])
        moves = [[-1] * n for _ in range(m)]

        def dfs(x, y):
            if moves[x][y] != -1:
                return moves[x][y]
            
            res = 0
            for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                    res = max(res, dfs(nx, ny))
            
            moves[x][y] = 1 + res
            return moves[x][y]

        max_moves = 0
        for i in range(m):
            max_moves = max(max_moves, dfs(i, 0))

        return max_moves - 1