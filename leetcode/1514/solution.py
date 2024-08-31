import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Build the graph with weighted probabilities
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))
        
        # Priority queue to store nodes by their probability of being reached
        pq = [(-1.0, start)]
        visited = set()
        
        while pq:
            prob, node = heapq.heappop(pq)
            if node in visited: continue
            visited.add(node)
            
            if node == end:
                return -prob
            
            for neighbor, next_prob in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (prob * next_prob, neighbor))
        
        return 0.0