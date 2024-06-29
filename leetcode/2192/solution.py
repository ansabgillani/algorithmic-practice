class Solution:
    def getAncestors(self, n, edges):
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        ancestors = [set() for _ in range(n)]
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                ancestors[v].update(ancestors[u])
                ancestors[v].add(u)
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        return [sorted(list(a)) for a in ancestors]