from collections import defaultdict, deque

class Solution:
    def modifyGraphEdges(self, n, edges, source, destination, target):
        graph = defaultdict(list)
        weights = {}

        for a, b, w in edges:
            graph[a].append(b)
            graph[b].append(a)
            weights[(a, b)] = -1 if w == -1 else w

        def bfs(start):
            dist = [-1] * n
            queue = deque([start])
            dist[start] = 0
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + weights[(u, v)]
                        queue.append(v)
            return dist

        src_dist = bfs(source)
        dst_dist = bfs(destination)

        if src_dist[destination] <= target:
            return edges

        for u, v in edges:
            if weights[(u, v)] == -1:
                if (src_dist[u] + 1 + dst_dist[v]) <= target:
                    weights[(u, v)] = max(1, target - (src_dist[u] + dst_dist[v]))
                    src_dist = bfs(source)
                    if src_dist[destination] == target:
                        return [(u, v, weights[(u, v)]) for u, v in edges]

        return []