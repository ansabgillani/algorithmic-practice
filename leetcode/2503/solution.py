import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Min-heap to store the cells to be processed
        min_heap = [(grid[0][0], 0, 0)]
        grid[0][0] = -1  # Mark as visited by setting it to a negative value
        
        points_count = [0] * len(queries)
        
        # Sort queries and process them in increasing order
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        for query, original_index in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                value, x, y = heapq.heappop(min_heap)
                
                # Increment the point count for this query
                points_count[original_index] += 1
                
                # Explore all 4 directions
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                        heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
                        grid[nx][ny] = -1  # Mark as visited
        
        return points_count