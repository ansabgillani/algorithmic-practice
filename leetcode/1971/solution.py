class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        # Create adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Initialize visited array and queue for BFS
        visited = [False] * n
        queue = [start]
        
        while queue:
            current = queue.pop(0)
            
            if current == end:
                return True
        
            if not visited[current]:
                visited[current] = True
                for neighbor in adj_list[current]:
                    if not visited[neighbor]:
                        queue.append(neighbor)

        return False