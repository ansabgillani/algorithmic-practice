class Solution:
    def removeStones(self, stones):
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
            
            def find(self, u):
                if u != self.parent[u]:
                    self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
            
            def union(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu == pv: 
                    return 0
                self.parent[pu] = pv
                return 1
        
        n = len(stones)
        uf = UnionFind(2 * 10**4 + 1)
        
        for x, y in stones:
            uf.union(x, y + 10**4 + 1)  # +10^4 to ensure unique values for columns
        
        return n - sum(uf.find(i) == i for i in range(n))