import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Priority queue to store (cost, current_node, remaining_stops)
        pq = [(0, src, k + 1)]
        visited = set()
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return cost
            
            if stops == 0 or (node, stops) in visited:
                continue
                
            visited.add((node, stops))
            
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbor, stops - 1))
        
        return -1