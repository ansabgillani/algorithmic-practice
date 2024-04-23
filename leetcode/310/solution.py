class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # If there's only one node, it is the MHT itself
        if n == 1:
            return [0]
        
        # Build the graph using adjacency list
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Initialize leaves (nodes with only one connection)
        leaves = [node for node, neighbors in adj_list.items() if len(neighbors) == 1]
        
        # Reduce the graph layer by layer from the leaves
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        # The remaining nodes are the roots of MHTs
        return leaves