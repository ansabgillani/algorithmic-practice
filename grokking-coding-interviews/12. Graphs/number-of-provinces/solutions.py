class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        This function calculates the number of provinces in a given network.
        
        :param isConnected: n x n matrix representing the connections between cities
        :return: The total number of provinces
        """
        if not isConnected or len(isConnected) == 0:
            return 0
        
        n = len(isConnected)
        visited = [False] * n
        count = 0
        
        def dfs(city):
            stack = [city]
            while stack:
                current_city = stack.pop()
                for neighbor in range(n):
                    if isConnected[current_city][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        
        return count