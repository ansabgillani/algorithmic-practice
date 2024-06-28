class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        degrees = [len(neighbors) for neighbors in graph]
        
        heapq.heapify(degrees)
        max_importance = 0
        
        while degrees:
            current_node_impact = n * heapq.heappop(degrees)
            max_importance += current_node_impact
            n -= 1
        
        return max_importance