class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1 = [i for i in range(n+1)]
        uf2 = [i for i in range(n+1)]

        def find(x):
            if x != uf1[x]:
                uf1[x] = find(uf1[x])
            return uf1[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    uf1[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    uf1[root_x] = root_y
                else:
                    uf1[root_y] = root_x
                    rank[root_x] += 1

        def union_bob(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                uf2[root_y] = root_x

        rank = [0] * (n+1)

        for t, x, y in edges:
            if t == 3:
                union(x, y)
                union_bob(x, y)

        count1, count2 = n, n
        for t, x, y in edges:
            if t == 1 and find(x) != find(y):
                union(x, y)
                count1 -= 1
            elif t == 2 and find_bob(x) != find_bob(y):
                union_bob(x, y)
                count2 -= 1

        return len(edges) - (n + n - 2) if count1 == 1 and count2 == 1 else -1