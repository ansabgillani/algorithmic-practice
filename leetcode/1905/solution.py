class Solution:
    def countSubIslands(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])

        def dfs(r, c):
            nonlocal valid
            if not (0 <= r < m and 0 <= c < n) or grid2[r][c] == 0:
                return
            if grid1[r][c] == 0:
                valid = False
                return
            grid2[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0

        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1:
                    valid = True
                    dfs(r, c)
                    if valid:
                        count += 1

        return count