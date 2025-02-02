from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        Finds all the minimum height trees in a tree with n nodes and n-1 edges.
        
        :param n: Number of nodes
        :param edges: List of edges as pairs [a, b]
        :return: List of root labels for the MHTs
        """
        if n == 1:
            return [0]
        
        # Build adjacency list and degree map
        graph = defaultdict(list)
        degree = {i: 0 for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        # Initialize leaves (nodes with degree 1)
        leaves = [node for node in degree if degree[node] == 1]
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves

# Example usage:
solution = Solution()
print(solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))  # Output: [1]
print(solution.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))  # Output: [3, 4]