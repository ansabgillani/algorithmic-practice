class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Step 1: Create the graph
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Find connected components and calculate their bitwise AND cost
        def bfs(start):
            visited = [False] * n
            queue = deque([start])
            min_and_cost = (1 << 31) - 1  # Initialize to maximum value
            
            while queue:
                node = queue.popleft()
                if not visited[node]:
                    visited[node] = True
                    for neighbor, weight in graph[node]:
                        min_and_cost &= weight
                        if not visited[neighbor]:
                            queue.append(neighbor)
            
            return min_and_cost, visited
        
        # Step 3: Process each query
        answers = [-1] * len(query)
        component_costs = {}
        
        for i, (s, t) in enumerate(query):
            if s == t:
                answers[i] = 0
                continue
            
            if (s, t) not in component_costs:
                cost_s, visited_s = bfs(s)
                cost_t, _ = bfs(t)
                
                # If both nodes are in the same connected component
                if visited_s[t]:
                    component_costs[(s, t)] = component_costs.get((t, s), cost_s & cost_t)
                else:
                    component_costs[(s, t)] = -1
            
            answers[i] = component_costs[(s, t)]
        
        return answers