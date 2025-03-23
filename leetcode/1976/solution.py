import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        # Define the modulo constant
        MOD = 10**9 + 7
        
        # Create a graph from the roads
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Initialize distances and ways to reach each node
        distances = [float('inf')] * n
        ways = [0] * n
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0)]  # (current_time, current_node)
        
        # Set the distance and number of ways to reach the start node
        distances[0] = 0
        ways[0] = 1
        
        while pq:
            current_time, current_node = heapq.heappop(pq)
            
            if current_time > distances[current_node]:
                continue
            
            for neighbor, travel_time in graph[current_node]:
                new_time = current_time + travel_time
                
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    ways[neighbor] = ways[current_node]
                    heapq.heappush(pq, (new_time, neighbor))
                elif new_time == distances[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[current_node]) % MOD
        
        return ways[n - 1]