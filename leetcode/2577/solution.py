class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Priority queue to hold cells to be processed
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))
        
        # Distance array to store the minimum time required to reach each cell
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        
        while pq:
            t, x, y = heapq.heappop(pq)
            
            # If we have reached the bottom-right cell, return the time
            if (x, y) == (m-1, n-1):
                return t
        
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is within bounds
                if 0 <= nx < m and 0 <= ny < n:
                    nt = max(t+1, grid[nx][ny]) + (nx - x + ny - y) % 2
                    
                    # If a shorter path to this cell has been found, update the distance array and priority queue
                    if dist[nx][ny] > nt:
                        dist[nx][ny] = nt
                        heapq.heappush(pq, (nt, nx, ny))
                    
        return -1