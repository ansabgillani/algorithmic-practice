class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # Create adjacency list representation of the graph
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Use BFS to check if there is a valid path from start to end
        queue = deque([start])
        visited = set([start])
        
        while queue:
            node = queue.popleft()
            if node == end:
                return True
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False

# Example usage
sol = Solution()
print(sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))  # Output: True
print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))  # Output: False