class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # Create a graph and in-degree dictionary
        graph = defaultdict(set)
        indegree = {x: 0 for seq in seqs for x in seq}
        
        # Build the graph and calculate in-degrees
        for seq in seqs:
            for i in range(len(seq) - 1):
                if seq[i + 1] not in graph[seq[i]]:
                    graph[seq[i]].add(seq[i + 1])
                    indegree[seq[i + 1]] += 1
        
        # Check if there is a unique topological order
        queue = deque([node for node in indegree if indegree[node] == 0])
        result = []
        
        while queue:
            if len(queue) > 1:
                return False
            current = queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(result) == len(indegree) and result == org