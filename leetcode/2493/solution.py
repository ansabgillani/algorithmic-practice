from collections import defaultdict, deque
import math

class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to find the longest path in each connected component
        def bfs(start):
            queue = deque([start])
            visited = set([start])
            distance = [0] * (n + 1)
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        distance[neighbor] = distance[node] + 1
            return max(distance)
        
        # Check if the graph can be divided into valid groups
        def can_divide():
            color = [-1] * (n + 1)
            for i in range(1, n + 1):
                if color[i] == -1:
                    if not dfs(i, 0):
                        return False
            return True
        
        # DFS to check bipartiteness
        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == -1 and not dfs(neighbor, c ^ 1):
                    return False
                elif color[neighbor] == c:
                    return False
            return True
        
        # Main logic
        if not can_divide():
            return -1
        
        max_groups = 0
        for i in range(1, n + 1):
            if color[i] != -1:
                continue
            max_groups += bfs(i)
        
        return max_groups