import heapq
from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # Initialize adjacency matrix
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        
        # Function to perform Dijkstra's algorithm and find the shortest paths from a given source
        def dijkstra(start):
            distances = [float('inf')] * n
            distances[start] = 0
            pq = [(0, start)]
            
            while pq:
                current_dist, u = heapq.heappop(pq)
                if current_dist > distances[u]:
                    continue
                for v in graph[u]:
                    distance = current_dist + graph[u][v]
                    if distance < distances[v]:
                        distances[v] = distance
                        heapq.heappush(pq, (distance, v))
            
            return distances
        
        # Find the number of reachable cities within the threshold distance for each city
        min_reachable = n
        best_city = -1
        
        for i in range(n):
            distances = dijkstra(i)
            reachable_count = sum(1 for d in distances if 0 < d <= distanceThreshold)
            if reachable_count <= min_reachable:
                min_reachable = reachable_count
                best_city = i
        
        return best_city

# Example usage:
solution = Solution()
print(solution.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)) # Output: 3
print(solution.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2)) # Output: 0