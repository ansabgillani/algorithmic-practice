class Solution:
    def largestIsland(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Union-Find data structure
        parent = list(range(m * n))
        size = [1] * (m * n)
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                size[rootY] += size[rootX]

        # Union all connected 1's
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            union(i * n + j, ni * n + nj)

        # Find the size of each island
        islands = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unique_roots = set()
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            root = find(ni * n + nj)
                            unique_roots.add(root)
                    islands[(i, j)] = sum(size[root] for root in unique_roots) + 1
                elif (i, j) not in islands:
                    islands[(i, j)] = size[find(i * n + j)]

        return max(islands.values()) if islands else m * n