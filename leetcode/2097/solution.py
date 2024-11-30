class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = {}
        in_degree = {}
        out_degree = {}

        # Build the graph and calculate degrees
        for u, v in pairs:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            out_degree[u] = out_degree.get(u, 0) + 1
            in_degree[v] = in_degree.get(v, 0) + 1

        start_node = list(graph.keys())[0]
        if len(out_degree) > 1:
            for u in graph:
                if out_degree[u] - in_degree[u] == 1:
                    start_node = u
                    break

        # Hierholzer's Algorithm to find Eulerian Path
        path, stack = [], [start_node]
        while stack:
            u = stack[-1]
            if graph[u]:
                v = graph[u].pop()
                stack.append(v)
            else:
                path.append(stack.pop())
        
        # Reverse the path to get the valid arrangement
        return [[path[i], path[i+1]] for i in range(len(path)-1)][::-1]