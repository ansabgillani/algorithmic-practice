from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        
        # Helper function to determine if a node is safe
        def dfs(node):
            if safe[node]:
                return True
            if not graph[node]:
                safe[node] = True
                return True
            if safe[node] == False:
                safe[node] = None  # Mark as being visited but not yet determined
                for neighbor in graph[node]:
                    if not dfs(neighbor):
                        return False
                safe[node] = True
            return safe[node]
        
        # Perform DFS for each node to determine safety
        for i in range(n):
            dfs(i)
        
        # Collect all safe nodes
        return [i for i in range(n) if safe[i]]