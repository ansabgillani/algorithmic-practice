import heapq
from collections import defaultdict

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        # Build the graph with negative weights
        graph = defaultdict(list)
        for a, b, w in edges:
            if w == -1:
                graph[a].append((b, 2 * 10**9))
                graph[b].append((a, 2 * 10**9))
            else:
                graph[a].append((b, w))
                graph[b].append((a, w))
        
        # Function to perform Dijkstra's algorithm
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    new_d = d + w
                    if new_d < dist[v]:
                        dist[v] = new_d
                        heapq.heappush(pq, (new_d, v))
            return dist
        
        # Perform Dijkstra's algorithm from the source
        distances = dijkstra(source)
        
        # If the distance is already less than target, return the original edges
        if distances[destination] < target:
            return edges
        
        # Adjust negative weights to make the path exactly target length
        for u, v, w in edges:
            if w == -1 and distances[u] + 1 + distances[v] <= target:
                distances[v] = min(distances[v], distances[u] + 1)
        
        # Re-run Dijkstra's algorithm after adjusting weights
        new_distances = dijkstra(source)
        
        # If the distance is exactly target, return the edges with adjusted weights
        if new_distances[destination] == target:
            for i in range(len(edges)):
                if edges[i][2] == -1 and distances[edges[i][0]] + 1 + distances[edges[i][1]] <= target:
                    edges[i][2] = distances[edges[i][0]] + 1
            return edges
        
        # If no valid modification is possible, return an empty array
        return []