class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        graph = [[float('inf')]*n for _ in range(n)]
        for i, j, w in edges:
            graph[i][j] = graph[j][i] = w
        for i in range(n):
            graph[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

        min_neighbors, city_id = n+1, -1
        for i in range(n):
            count = sum(1 for dist in graph[i] if dist <= distanceThreshold)
            if count < min_neighbors:
                min_neighbors, city_id = count, i
            elif count == min_neighbors and i > city_id:
                city_id = i

        return city_id