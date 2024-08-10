class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                idx = 4 * (i * n + j)
                if grid[i][j] != '\\':
                    union(idx + 0, idx + 1)
                    union(idx + 2, idx + 3)
                if grid[i][j] != '/':
                    union(idx + 0, idx + 2)
                    union(idx + 1, idx + 3)
                if i > 0:
                    union(idx + 0, (idx - 4 * n) + 2)
                if j > 0:
                    union(idx + 3, (idx - 4) + 1)

        return sum(find(i) == i for i in range(4 * n * n))