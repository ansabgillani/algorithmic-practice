class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        from collections import defaultdict
        import heapq
        
        # Build the graph with all possible transformations and their costs
        n = len(original)
        graph = defaultdict(dict)
        for i in range(n):
            x, y, c = original[i], changed[i], cost[i]
            if c < graph[x].get(y, float('inf')):
                graph[x][y] = c
        
        # Floyd-Warshall algorithm to find the minimum cost of transforming any character to another
        for k in graph:
            for i in graph:
                for j in graph:
                    if graph[i].get(k, float('inf')) + graph[k].get(j, float('inf')) < graph[i].get(j, float('inf')):
                        graph[i][j] = graph[i][k] + graph[k][j]
        
        # Calculate the total cost to convert source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s != t and graph[s].get(t, float('inf')) == float('inf'):
                return -1
            total_cost += graph[s][t]
        
        return total_cost