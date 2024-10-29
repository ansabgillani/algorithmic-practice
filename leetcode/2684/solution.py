class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(x, y):
            if x < 0 or x >= m or y >= n:
                return -float('inf')
            if dp[x][y] != -1:
                return dp[x][y]
            moves = [
                dfs(x-1, y+1),
                dfs(x, y+1),
                dfs(x+1, y+1)
            ]
            dp[x][y] = 1 + max(moves) if any(moves) else 0
            return dp[x][y]
        
        max_moves = 0
        for i in range(m):
            max_moves = max(max_moves, dfs(i, 0))
        
        return max_moves