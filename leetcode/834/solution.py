class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        # Build adjacency list representation of the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Helper function to perform DFS and calculate initial distances
        def dfs(node, parent):
            count[node] = 1
            sum[node] = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    count[node] += count[neighbor]
                    sum[node] += sum[neighbor] + count[neighbor]
        
        # Helper function to update distances after root change
        def reroot(old_root, new_root):
            sum[new_root] = sum[old_root] - count[new_root] + (n - count[new_root])
            result[new_root] = result[old_root] - count[new_root] + (n - count[new_root])
            for neighbor in graph[new_root]:
                if neighbor != old_root:
                    reroot(new_root, neighbor)
        
        # Initialize counts and sums arrays
        count = [0] * n
        sum = [0] * n
        result = [0] * n
        
        # Perform DFS to calculate initial distances from node 0
        dfs(0, -1)
        
        # Reroot the tree starting from node 0
        reroot(-1, 0)
        
        return result