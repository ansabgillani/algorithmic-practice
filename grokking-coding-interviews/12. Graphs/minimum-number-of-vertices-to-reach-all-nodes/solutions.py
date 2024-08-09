from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a set to track vertices with incoming edges
        in_degree = set(range(n))
        
        # Remove vertices that have incoming edges from the set
        for _, to in edges:
            if to in in_degree:
                in_degree.remove(to)
        
        # The remaining vertices are those with zero in-degree, which means they are reachable from all other nodes
        return list(in_degree)