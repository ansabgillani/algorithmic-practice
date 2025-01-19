import heapq

def trapRainWater(heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    if not heightMap:
        return 0
    
    m, n = len(heightMap), len(heightMap[0])
    heap = []
    visited = [[False] * n for _ in range(m)]
    
    # Initialize heap with the boundary cells and mark them as visited
    for i in range(m):
        heapq.heappush(heap, (heightMap[i][0], i, 0))
        heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
        visited[i][0] = True
        visited[i][n-1] = True
    
    for j in range(1, n-1):
        heapq.heappush(heap, (heightMap[0][j], 0, j))
        heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
        visited[0][j] = True
        visited[m-1][j] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = 0
    
    while heap:
        h, x, y = heapq.heappop(heap)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                result += max(0, h - heightMap[nx][ny])
                heapq.heappush(heap, (max(h, heightMap[nx][ny]), nx, ny))
                visited[nx][ny] = True
    
    return result