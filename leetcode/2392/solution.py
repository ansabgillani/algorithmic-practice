class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        def topological_sort(conditions):
            graph = [[] for _ in range(k+1)]
            indegree = [0]*(k+1)
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            queue = [i for i in range(1, k+1) if indegree[i] == 0]
            topo_order = []
            
            while queue:
                node = queue.pop(0)
                topo_order.append(node)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                    
            return topo_order if len(topo_order) == k else []
        
        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
    
        if not row_order or not col_order:
            return []
    
        matrix = [[0]*k for _ in range(k)]
    
        for i, num in enumerate(row_order):
            matrix[i][col_order.index(num)] = num
    
        return matrix