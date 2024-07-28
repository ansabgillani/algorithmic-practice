import heapq
from collections import defaultdict, deque

def secondMinimum(n: int, edges: list[list[int]], time: int, change: int) -> int:
    # Build graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize distances and visit counts
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = 0

    # Min-heap for Dijkstra's algorithm
    pq = [(0, 1)]

    while pq:
        d, node = heapq.heappop(pq)
        
        # Check if we have already found the second minimum distance to this node
        if dist[node][1] != float('inf'):
            continue
        
        # Update second minimum distance
        for neighbor in graph[node]:
            new_d = d + time
            if new_d >= dist[neighbor][0]:
                heapq.heappush(pq, (new_d, neighbor))
                continue
            
            if new_d < dist[neighbor][0]:
                dist[neighbor][1] = dist[neighbor][0]
                dist[neighbor][0] = new_d
                heapq.heappush(pq, (dist[neighbor][0], neighbor))
            else:
                dist[neighbor][1] = min(dist[neighbor][1], new_d)
    
    return dist[n][1]

# Example usage:
# print(secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))  # Output: 13
# print(secondMinimum(2, [[1,2]], 3, 2))  # Output: 11