class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        # Build in-degrees and out-degrees
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Find the starting node
        start_node = None
        for node in graph:
            if out_degree[node] == in_degree[node] + 1:
                start_node = node
                break
        
        if not start_node:
            start_node = next(iter(graph))
        
        # Hierholzer's algorithm to find Eulerian path
        def eulerian_path(node):
            while graph[node]:
                next_node = graph[node].pop()
                yield from eulerian_path(next_node)
                yield [node, next_node]
        
        return list(eulerian_path(start_node))