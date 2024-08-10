class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4 * n * n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                parent[rootA] = rootB

        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                char = grid[i][j]

                # Union the top and right segments of the current cell
                if char == '/':
                    union(index, index + 3)
                    union(index + 1, index + 2)
                elif char == '\\':
                    union(index, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)

                # Union the current cell with the cell below it
                if i < n - 1:
                    union(index + 2, index + 4 * n)

                # Union the current cell with the cell to the right of it
                if j < n - 1:
                    union(index + 3, index + 4)

        return len(set(find(i) for i in range(4 * n * n)))