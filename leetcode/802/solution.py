class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        safe = [False] * n

        def dfs(node):
            if safe[node]:
                return True
            if not graph[node]:  
                safe[node] = True
                return True
            
            safe[node] = False
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            safe[node] = True
            return True

        for i in range(n):
            if not safe[i]:
                dfs(i)

        return [i for i in range(n) if safe[i]]