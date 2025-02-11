class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs(node):
            if node in color:
                return True
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    if not dfs(neighbor):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True