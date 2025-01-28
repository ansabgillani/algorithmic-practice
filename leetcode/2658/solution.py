class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            fish_count = grid[r][c]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                fish_count += dfs(r + dr, c + dc)
            return fish_count
        
        max_fish = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visited:
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish

# Example usage:
solution = Solution()
grid1 = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
print(solution.findMaxFish(grid1))  # Output: 7

grid2 = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
print(solution.findMaxFish(grid2))  # Output: 1