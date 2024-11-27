class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Returns an array where each element is the length of the shortest path 
        from city 0 to city n - 1 after processing the first i + 1 queries.
        """
        
        # Initialize the answer array with the initial path length
        answer = [n-1] * len(queries)
        
        # Create a adjacency list for the graph
        adj_list = defaultdict(list)
        for u in range(n-1):
            adj_list[u].append(u+1)

        # Process each query
        for i, (u, v) in enumerate(queries):
            if u not in adj_list:
                adj_list[u] = []
            adj_list[u].append(v)
            
            # Use BFS to find the shortest path from 0 to n-1 after adding the road
            queue = deque([0])
            visited = set([0])
            distance = 0
            
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node == n-1:
                        answer[i] = distance
                        break
                    for neighbor in adj_list[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                else:
                    distance += 1

        return answer