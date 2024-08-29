class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Initialize Union-Find data structure
        parent = {}
        
        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Union all stones that share the same row or column
        for x, y in stones:
            union(x, ~y)  # Using negative y to distinguish between rows and columns
        
        # Count unique roots which represent connected components
        return len(stones) - len(set(find(x) for x, _ in stones))

# Example usage:
# sol = Solution()
# print(sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))  # Output: 5