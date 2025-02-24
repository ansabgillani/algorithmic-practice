from collections import defaultdict, deque
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        tree = defaultdict(list)
        
        # Build the tree
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Find the path from Bob to root (0)
        def find_bob_path(bob):
            parent = [None] * n
            queue = deque([bob])
            visited = set([bob])
            
            while queue:
                node = queue.popleft()
                for neighbor in tree[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = node
                        if neighbor == 0:
                            return parent
            return parent
        
        parent = find_bob_path(bob)
        
        # Update the amount considering Bob's path
        time_to_root = [float('inf')] * n
        time_to_root[bob] = 0
        for u, v in edges:
            if time_to_root[u] == float('inf'):
                time_to_root[v] = time_to_root[u] + 1
            else:
                time_to_root[u] = time_to_root[v] + 1
        
        for i in range(n-1, -1, -1):
            if parent[i] is not None and time_to_root[parent[i]] == time_to_root[i] + 1:
                amount[parent[i]] //= 2
            elif parent[i] is None or time_to_root[parent[i]] < time_to_root[i]:
                amount[i] = 0
        
        # Calculate the maximum profit for Alice
        def dfs(node, parent):
            max_profit = float('-inf')
            for neighbor in tree[node]:
                if neighbor != parent:
                    current_profit = dfs(neighbor, node)
                    if current_profit > max_profit:
                        max_profit = current_profit
            
            if max_profit == float('-inf'):
                return amount[node]
            
            return amount[node] + max_profit
        
        return dfs(0, None)