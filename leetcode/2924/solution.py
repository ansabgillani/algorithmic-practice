class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Create a set of all nodes
        all_nodes = set(range(n))
        
        # Create a set of nodes that have incoming edges
        has_incoming_edge = {v for u, v in edges}
        
        # The champion is the node with no incoming edge
        champion = all_nodes - has_incoming_edge
        
        # If there is exactly one champion, return it; otherwise, return -1
        return next(iter(champion), -1) if len(champion) == 1 else -1

# Example usage:
solution = Solution()
print(solution.findChampion(3, [[0, 1], [1, 2]]))  # Output: 0
print(solution.findChampion(4, [[0, 2], [1, 3], [1, 2]]))  # Output: -1