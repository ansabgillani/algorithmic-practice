from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Build the graph where each node points to a list of tuples (neighbor, time)
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((y, t))
            graph[y].append((x, t))

        # Initialize the result set with people who know the secret
        result = {0, firstPerson}
        
        # Process meetings sorted by time
        for _, meeting_times in sorted(graph.items()):
            queue = deque()
            visited = set()
            
            # Add all meetings at this time to the queue and mark as visited
            for neighbor, _ in meeting_times:
                if neighbor in result:
                    queue.append(neighbor)
                    visited.add(neighbor)
            
            # Perform BFS to share the secret among connected people at this time
            while queue:
                current = queue.popleft()
                for neighbor, _ in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        result.add(neighbor)
                        queue.append(neighbor)
        
        return list(result)