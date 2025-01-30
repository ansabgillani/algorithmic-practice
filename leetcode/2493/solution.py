class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (n + 1)
        
        def bfs(node):
            queue = deque([node])
            level = 0
            levels = defaultdict(set)
            while queue:
                level += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if visited[node]:
                        continue
                    visited[node] = True
                    for neighbor in adj[node]:
                        if not visited[neighbor] and abs(node - neighbor) != 1:
                            return -1
                        levels[level].add(neighbor)
                        queue.append(neighbor)
            return len(levels)

        result = 0
        for i in range(1, n + 1):
            if not visited[i]:
                groups = bfs(i)
                if groups == -1:
                    return -1
                result += groups

        return result