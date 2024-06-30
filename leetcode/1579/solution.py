class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Sort edges by type in descending order to prioritize type 3 edges first
        edges.sort(key=lambda x: -x[0])
        
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        alice_edges_used = bob_edges_used = 0
        
        for edge_type, u, v in edges:
            if edge_type == 3:
                if uf_alice.union(u, v):
                    alice_edges_used += 1
                    bob_edges_used += 1
            elif edge_type == 2:
                if uf_bob.union(u, v):
                    bob_edges_used += 1
            else:
                if uf_alice.union(u, v):
                    alice_edges_used += 1
        
        # Check if both Alice and Bob can traverse the graph
        if uf_alice.find(1) != uf_alice.find(n) or uf_bob.find(1) != uf_bob.find(n):
            return -1
        
        # Calculate the maximum number of edges that can be removed
        return len(edges) - (alice_edges_used + bob_edges_used)