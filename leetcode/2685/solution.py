from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        complete_components_count = 0
        
        def is_complete_component(component_nodes):
            size = len(component_nodes)
            # A component is complete if it has size * (size - 1) / 2 edges
            actual_edges = sum(len(graph[node]) for node in component_nodes) // 2
            return actual_edges == size * (size - 1) // 2
        
        for node in range(n):
            if node not in visited:
                # Perform BFS to find all nodes in the current connected component
                component_nodes = set()
                queue = deque([node])
                
                while queue:
                    current_node = queue.popleft()
                    if current_node in visited:
                        continue
                    visited.add(current_node)
                    component_nodes.add(current_node)
                    for neighbor in graph[current_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                
                # Check if the found component is complete
                if is_complete_component(component_nodes):
                    complete_components_count += 1
        
        return complete_components_count