class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(lambda: defaultdict(int))
        for o, c, p in zip(original, changed, cost):
            if adj[o][c] > 0:
                adj[o][c] = min(adj[o][c], p)
            else:
                adj[o][c] = p
        
        def dijkstra():
            dist = defaultdict(lambda: float('inf'))
            pq = [(0, o) for o in adj]
            
            while pq:
                d, o = heapq.heappop(pq)
                if dist[o] < d:
                    continue
                for c, p in adj[o].items():
                    new_d = d + p
                    if new_d < dist[c]:
                        dist[c] = new_d
                        heapq.heappush(pq, (new_d, c))
        
            return dict(dist)
        
        shortest_paths = dijkstra()
        
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                c = shortest_paths.get((s, t), float('inf'))
                if c == float('inf'):
                    return -1
                total_cost += c
        
        return total_cost