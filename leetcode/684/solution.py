class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False
        self.parent[rootP] = rootQ
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Finds the redundant connection in a graph represented as an array of edges.
        Returns an edge that can be removed to make the graph a tree.
        If there are multiple answers, returns the one that occurs last in the input.
        
        :param edges: List of edges where each edge is a list of two integers
        :return: Redundant edge as a list of two integers
        """
        n = len(edges)
        uf = UnionFind(n + 1)
        
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]