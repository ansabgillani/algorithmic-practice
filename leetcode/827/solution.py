class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Union-Find data structure to manage connected components
        parent = list(range(n * n))
        size = [1] * (n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
                size[rootX] += size[rootY]

        # Union connected components
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            union(i * n + j, ni * n + nj)

        # Calculate the size of the largest island without any change
        max_island_size = max(size)
        
        # Try changing each 0 to 1 and calculate the new island size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    visited = set()
                    current_size = 1
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            root = find(ni * n + nj)
                            if root not in visited:
                                current_size += size[root]
                                visited.add(root)
                    max_island_size = max(max_island_size, current_size)

        return max_island_size