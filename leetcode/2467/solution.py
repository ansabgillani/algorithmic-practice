from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(list)

        # Build the graph from edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def find_bob_path(node=0, parent=-1):
            if node == bob:
                return 0

            min_cost = float('inf')

            # Explore all children
            for neighbor in graph[node]:
                if neighbor != parent:
                    cost = find_bob_path(neighbor, node)
                    if cost < min_cost:
                        min_cost = cost

            # If Bob is on a leaf node, return 1 (path length)
            if min_cost == float('inf'):
                return 1

            return min_cost + 1

        def dfs(node=0, parent=-1, path_length=0):
            nonlocal max_income
            income = amount[node]

            # If Bob has passed this node already, reduce the income accordingly
            if path_length > bob_path[node]:
                income /= 2
            elif path_length == bob_path[node]:
                income = 0

            # Update maximum income
            if node != 0 and not graph[node]:  # Only update for leaf nodes except root
                max_income = max(max_income, income)

            # Explore all children
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, path_length + 1)

        bob_path = [float('inf')] * n
        find_bob_path()  # Find the path length from root to Bob

        max_income = float('-inf')
        dfs()  # Calculate maximum income for Alice

        return max_income