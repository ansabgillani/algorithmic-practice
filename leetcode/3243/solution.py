class Solution:
    def __init__(self, n):
        self.adj_list = defaultdict(list)
        for i in range(n - 1):
            self.adj_list[i].append(i + 1)

    def add_road(self, u, v):
        self.adj_list[u].append(v)

    def bfs_shortest_path(self, start, end):
        dist = [float('inf')] * len(self.adj_list)
        dist[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in self.adj_list[node]:
                if dist[neighbor] == float('inf'):
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        return dist[end]

    def shortest_path_after_queries(self, queries):
        result = []
        for u, v in queries:
            self.add_road(u, v)
            result.append(self.bfs_shortest_path(0, len(self.adj_list) - 1))
        return result