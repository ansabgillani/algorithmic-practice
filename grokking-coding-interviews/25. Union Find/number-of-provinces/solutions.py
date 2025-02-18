class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for other_city in range(n):
                if isConnected[city][other_city] == 1 and not visited[other_city]:
                    visited[other_city] = True
                    dfs(other_city)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)
        
        return provinces