class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for neighbor in adj[node]:
                        stack.append(neighbor)
        
        for i in range(n):
            dfs(i)
        
        return [visited[b] for a, b in queries]