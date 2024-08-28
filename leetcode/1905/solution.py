class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0:
                return True
            if grid2[r][c] == 1 and grid1[r][c] == 0:
                return False
            grid2[r][c] = 0  # Mark as visited
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            return up and down and left and right
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        count += 1
        
        return count

# Example usage:
sol = Solution()
print(sol.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))  # Output: 3
print(sol.countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))  # Output: 2