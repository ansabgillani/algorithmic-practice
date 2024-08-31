class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        # Create adjacency list
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        # Priority queue: (-probability, node)
        pq = [(-1.0, start)]
        visited = set()

        while pq:
            prob, node = heapq.heappop(pq)
            
            if node in visited:
                continue
            visited.add(node)

            if node == end:
                return -prob

            for neighbor, edge_prob in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (prob * edge_prob, neighbor))

        return 0.0