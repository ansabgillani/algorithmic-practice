class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        degree = [0] * n
        graph = [[] for _ in range(n)]
        
        # Build the graph and calculate degrees
        for i in range(n):
            graph[favorite[i]].append(i)
            degree[i] += 1
        
        # Step 1: Remove leaves (employees with no favorite or only one favorite)
        queue = deque([i for i in range(n) if degree[i] == 1])
        while queue:
            node = queue.popleft()
            neighbor = graph[node][0]
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
                queue.append(neighbor)
        
        # Step 2: Calculate the size of each cycle
        def get_cycle_length(node):
            length = 0
            while node != -1:
                next_node = graph[node][0]
                length += 1
                degree[next_node] -= 1
                if degree[next_node] == 1:
                    break
                node = next_node
            return length
        
        max_cycle_length = 0
        for i in range(n):
            if degree[i] == 2:
                cycle_length = get_cycle_length(i)
                max_cycle_length += cycle_length
        
        # Step 3: Calculate the maximum number of employees that can be invited
        def dfs(node):
            visited.add(node)
            nonlocal count
            for neighbor in graph[node]:
                if neighbor not in visited and degree[neighbor] == 1:
                    count += 1
                    dfs(neighbor)
        
        max_invitations = 0
        for i in range(n):
            if degree[i] == 2:
                count = 0
                visited = set()
                dfs(i)
                max_invitations += count + 2
        
        return max(max_cycle_length, max_invitations)