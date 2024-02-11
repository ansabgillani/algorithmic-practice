class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if (r1 == rows or r2 == rows or c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols):
                return float('-inf')
            if (c1 == c2 and grid[r1][c1] != 0):
                total = grid[r1][c1]
            else:
                total = grid[r1][c1] + grid[r2][c2]
            if r1 == rows - 1:
                return total
            max_cherries = float('-inf')
            for dr1 in [-1, 0, 1]:
                for dr2 in [-1, 0, 1]:
                    max_cherries = max(max_cherries, dp(r1 + 1, c1 + dr1, r2 + 1))
            return total + max_cherries
        
        result = dp(0, 0, 0)
        if result == float('-inf'):
            return 0
        else:
            return result

# Example usage:
sol = Solution()
print(sol.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))  # Output: 24
print(sol.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))  # Output: 28