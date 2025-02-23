class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent array to keep track of each node's parent
        parent = list(range(len(edges) + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return True  # Cycle detected
            parent[rootX] = rootY  # Union by rank is not needed here due to path compression
            return False
        
        for edge in edges:
            if union(edge[0], edge[1]):
                return edge

# Example usage:
solution = Solution()
print(solution.findRedundantConnection([[1,2],[1,3],[2,3]]))  # Output: [2,3]
print(solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # Output: [1,4]