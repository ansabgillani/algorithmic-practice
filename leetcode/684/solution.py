class Solution(object):
    def __init__(self):
        self.parent = {}
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
    
    def find(self, x):
        if x not in self.parent:
            return x
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        for u, v in edges:
            if self.find(u) == self.find(v):
                return [u, v]
            self.union(u, v)