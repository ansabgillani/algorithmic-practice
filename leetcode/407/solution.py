class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        
        for i in range(m):
            heappush(heap, (heightMap[i][0], i, 0))
            heightMap[i][0] -= 100001
            heappush(heap, (heightMap[i][n-1], i, n-1))
            heightMap[i][n-1] -= 100001
        
        for j in range(n):
            heappush(heap, (heightMap[0][j], 0, j))
            heightMap[0][j] -= 100001
            heappush(heap, (heightMap[m-1][j], m-1, j))
            heightMap[m-1][j] -= 100001
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_water = 0
        
        while heap:
            height, i, j = heappop(heap)
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < m and 0 <= nj < n and heightMap[ni][nj] != -100001:
                    if heightMap[ni][nj] < height:
                        total_water += height - heightMap[ni][nj]
                    
                    heappush(heap, (max(height, heightMap[ni][nj]), ni, nj))
                    heightMap[ni][nj] -= 100001
        
        return total_water