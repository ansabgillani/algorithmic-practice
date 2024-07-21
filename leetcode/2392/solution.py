from typing import List, Dict, Set, Tuple
import collections

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologicalSort(conditions: List[List[int]]) -> Tuple[bool, List[int], Dict[int, int]]:
            graph = {i: [] for i in range(1, k + 1)}
            indegree = [0] * (k + 1)
            
            for above, below in conditions:
                graph[above].append(below)
                indegree[below] += 1
            
            queue = collections.deque([i for i in range(1, k + 1) if indegree[i] == 0])
            sorted_order = []
            
            while queue:
                if len(queue) > 1:
                    return False, [], {}
                current = queue.popleft()
                sorted_order.append(current)
                for neighbor in graph[current]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(sorted_order) != k:
                return False, [], {}
            
            node_to_index = {node: idx for idx, node in enumerate(sorted_order)}
            return True, sorted_order, node_to_index
        
        row_valid, row_order, row_map = topologicalSort(rowConditions)
        col_valid, col_order, col_map = topologicalSort(colConditions)
        
        if not row_valid or not col_valid:
            return []
        
        matrix = [[0] * k for _ in range(k)]
        
        for i in range(k):
            matrix[row_map[i + 1]][col_map[i + 1]] = i + 1
        
        return matrix