from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # Create a graph using adjacency list representation
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Depth-First Search (DFS) to check if there is a path from start to end
        visited = set()
        
        def dfs(node):
            if node == end:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited and dfs(neighbor):
                    return True
            return False
        
        # Start DFS from the start node
        return dfs(start)