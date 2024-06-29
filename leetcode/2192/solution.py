from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Build the graph and compute in-degrees
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Initialize the result list and queue for topological sorting
        ancestors = [set() for _ in range(n)]
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Convert sets to sorted lists
        return [sorted(list(anscestors[i])) for i in range(n)]