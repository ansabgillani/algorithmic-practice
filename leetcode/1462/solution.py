from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build the graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for u, v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1

        # Initialize the queue with all nodes that have zero in-degree
        queue = deque([node for node in range(numCourses) if in_degree[node] == 0])
        
        # Initialize the result matrix to store prerequisite relationships
        prerequisites_of = [[False] * numCourses for _ in range(numCourses)]
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                prerequisites_of[node][neighbor] = True
                for i in range(numCourses):
                    prerequisites_of[i][neighbor] |= prerequisites_of[i][node]
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Answer the queries based on the result matrix
        return [prerequisites_of[u][v] for u, v in queries]