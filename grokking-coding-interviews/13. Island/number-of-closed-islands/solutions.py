class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            isClosed = True
            for dr, dc in directions:
                isClosed &= dfs(r + dr, c + dc)
            return isClosed
        
        closedIslandsCount = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        closedIslandsCount += 1
        return closedIslandsCount

# Example usage:
# solution = Solution()
# print(solution.closedIsland([[0,0,1,0],[0,1,0,0],[0,1,1,0],[0,0,0,0]]))  # Output: 2